# Albert Todoist

[Albert](https://github.com/albertlauncher/albert) plugin to quickly add items to todoist.

Use the prefix "todo: " in albert to add a todo.

# Optional Dependancies

If `todoist` is found in your `$PATH` the plugin will just use the `todoist quick <TODO>` 
to add a todo. Otherwise if the `todoist-python` python library was installed (`pip install todoist-python`)
then the plugin will make API requests through the library, if neither the cli or the library is installed
then the plugin will just make a direct request to the todoist API.