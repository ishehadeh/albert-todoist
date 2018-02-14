"""Quickly add todos to Todoist."""

from albertv0 import *
from shutil import which
import os
from urllib.parse import urlencode
from urllib.request import Request, urlopen

HAVE_TODOIST_LIBRARY = False
try:
    import todoist
    HAVE_TODOIST_LIBRARY = True
except ImportError:
    warning("todoist-python library not found")

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Todoist"
__version__ = "1.0"
__trigger__ = "todo: "
__author__ = "Ian Shehadeh"
__dependencies__ = []

ICON_PATH = iconLookup('todoist')
if not ICON_PATH:
    ICON_PATH = os.path.dirname(__file__)+"/todoist.svg"

# for debugging, force the plugin to use "lib", "cli" or "api"
FORCE_METHOD = None

CLI_PATH = which("todoist")
API = None
try:
    with open(os.path.dirname(__file__)+"/todoist-key.api") as f:
        if HAVE_TODOIST_LIBRARY:
            API = todoist.TodoistAPI(f.read())
        else:
            API = f.read()
    if API == "":
        API = None
except FileNotFoundError:
    warning("todoist api key not found")

def update_todoist_api(key):
    """updated the todoist api key"""
    global API

    with open(os.path.dirname(__file__)+"/todoist-key.api", "w+") as f:
        f.truncate(0)
        f.write(key)
    if HAVE_TODOIST_LIBRARY:
        API = todoist.TodoistAPI(key)
    else:
        API = key

def handleQuery(query):
    """Albert event handle for user input"""
    if query.isTriggered:
        todo_str = query.string.strip()
        item = Item(id=__prettyname__,
                    icon=ICON_PATH,
                    text=__prettyname__,
                    subtext="add todo: %s" % todo_str,
                    completion=query.rawString
                   )

        if CLI_PATH is None and API is None:
            item.text = "Todoist: Please enter your api key"
            item.subtext = "set api key"
            item.addAction(FuncAction("update api key", lambda: update_todoist_api(todo_str)))
        elif CLI_PATH is not None or FORCE_METHOD == "cli":
            item.addAction(ProcAction("add a todo (cli)", [CLI_PATH, "quick", todo_str]))
        elif API is not None:
            if HAVE_TODOIST_LIBRARY or FORCE_METHOD == "lib":
                item.addAction(FuncAction("add a todo (lib)", 
                                          lambda: API.quick.add(todo_str)))
            else:
                item.addAction(FuncAction("add a todo (api)",
                                          lambda: urlopen(Request("https://todoist.com/api/v7/quick/add",
                                                                  urlencode({'text': todo_str, 'token': API})
                                                                  .encode())).read()))
        return item
