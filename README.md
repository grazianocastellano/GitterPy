# GitterPy

Python interface for the Gitter API

[![Build Status](https://travis-ci.org/MichaelYusko/GitterPy.svg?branch=master)](https://travis-ci.org/MichaelYusko/GitterPy)


Releases
=================================
* 0.0.2 - planning(PyPi)
* 0.0.1 - planning(PyPi test)


Installation
=================================
```
# Test PyPi
pip install --extra-index-url https://testpypi.python.org/pypi gitterpy

# PyPi
not uploaded yet

```

Usage
=================================
```python
from gitterpy import GitterClient

# Create instance
gitter = GitterClient('YOUR_TOKEN')

####### Auth
# Check_my id
gitter.auth.get_my_id # return {'name': 'Freshjelly', 'user_id': '5332131921'}



####### Rooms
# Join into the room
gitter.rooms.join('gitterHQ/sandbox')

# Leave from the room
gitter.rooms.leave('gitterHQ/sandbox')

# List of rooms
gitter.rooms.rooms_list

# Grab room
gitter.rooms.grab_room('gitterHQ/sandbox')

# Room sub-resource
gitter.rooms.sub_resource('gitterHQ/sandbox')

# Update room topic
gitter.rooms.update('test-gitter/test1', 'My updated topic')

# Delete the room
gitter.rooms.delete_room('test-gitter/test1') # return {'success': True}


####### Messages
# Send a message to #gitterHQ/sandbox room
gitter.messages.send('gitterHQ/sandbox', 'Hello everyone')

# Message list
gitter.messages.list('gitterHQ/sandbox')


####### Groups
# List of groups
gitter.groups.groups_list

####### User
# Current user
gitter.user.current_user #  [{'displayName': 'freshjelly', 'id': '3131', ...}]

# User sub-resource
gitter.user.sub_resource # [{'noindex': True, 'id': '3131', ...}]

# User unread-items
gitter.user.unread_items('gitterHQ/sandbox') # {'mention': [], 'chat': []}

# User orgs
gitter.user.orgs # [{'name': 'bla bla', 'description': 'blabla', ...}]

# User repos
gitter.user.repos # [{'name': 'MichaelYusko/GitterPy', 'description': 'Python for the Gitter API', ...}]

# User channels
gitter.user.channels


##### Stream
# Chat messages
gitter.stream.chat_messages('gitterHQ/sandbox')

# Events
gitter.stream.events('gitterHQ/sandbox')
```


Pull Requests
=================================
1. `git clone git@github.com:MichaelYusko/GitterPy.git`
2. Feel free to make a PR;)