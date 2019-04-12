# taskathon
A simple python3 wrapper for [Taskwarrior](http://taskwarrior.org/) interactions.
Needs Taskwarrior installed and available in the PATHS.
It doesn't do much fancy, other than giving a simple clean layer of interaction between python3 and Taskwarrior.

```py
from taskathon import Tasks

t = Tasks()

t.add("This adds a new task")
#Returns a confirmation message, including it's ID, useful for later.

t.done(1)
#Marks task 1 as done, returns a confirmation message

t.delete(1)
#Same as done, but deletes permenantly. Usually taskwarrior asks for confirmation, but this does not.

t.export()
#returns a list of all tasks, each task is represented by a dict;
#{"id":25,"description":"this is a task","entry":"20190406T162600Z","modified":"20190406T162600Z","project":"","status":"pending","uuid":"78706bb5-6867-4e10-aa8e-d568812fbce3","urgency":1.0274}

t.export(1)
#Same as above, but only returns the specific task

t.get('1.description')
#Returns the DOM element, for more information on that, see taskwarriors docs.
#This example gets the description of task 1
```

I'm not affiliated with Taskwarrior at all, I merely wanted a way to integrate it with my own projects and figured I'd shae incase it's ever useful to anyone else. (I doubt it, but who knows eh)
