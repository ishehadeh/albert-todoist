# Albert Todoist

[Albert](https://github.com/albertlauncher/albert) plugin to quickly add items to todoist.

Use the prefix "todo: " in albert to add a todo.

# Optional Dependancies

If `todoist` is found in your `$PATH` the plugin will just use that.
Otherwise if the `todoist` python library was installed (`pip install todoist`)
then the plugin will use that to make requests, or if neither of these installed
then the  plugin will just make a raw request to the todoist API.