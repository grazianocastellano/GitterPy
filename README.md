# GitterPy

Python 3 interface for the [Gitter API](https://github.com/gitterHQ/docs/blob/master/09.Third-party-API-wrappers.md)

[![Build Status](https://travis-ci.org/MichaelYusko/GitterPy.svg?branch=master)](https://travis-ci.org/MichaelYusko/GitterPy) [![PyPI version](https://badge.fury.io/py/gitterpy.svg)](https://badge.fury.io/py/gitterpy)


Releases
=================================
* 0.1.6 - PyPi


Installation
=================================
```
pip install gitterpy
```

Usage
=================================

### Auth
```python
from gitterpy.client import GitterClient

# Once create instance
gitter = GitterClient('YOUR_TOKEN')

# Check_my id
gitter.auth.get_my_id # return {'name': 'Freshjelly', 'user_id': '5332131921'}
```

### Rooms
```python
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
gitter.rooms.delete_room('test-gitter/test1') #  {'success': True}
```
### Messages
```python
# Send a message to #gitterHQ/sandbox room
gitter.messages.send('gitterHQ/sandbox', 'Hello everyone')

# Message list
gitter.messages.list('gitterHQ/sandbox')

# Get single message by id
gitter.messages.get_message('gitterHQ/sandbox', '5903a16d6a471')
```


### Groups
```python
# List of groups
gitter.groups.groups_list
```

### User
```python
# Current user
gitter.user.current_user #  [{'displayName': 'freshjelly', 'id': '3131', ...}]

# User sub-resource
gitter.user.sub_resource # [{'noindex': True, 'id': '3131', ...}]

# User unread-items
gitter.user.unread_items('gitterHQ/sandbox') # {'mention': [], 'chat': []}

# Mark all messages in the room as read
gitter.user.mark_as_read('test-gitter/Lobby') # {'success': True}

# User orgs
gitter.user.orgs # [{'name': 'bla bla', 'description': 'blabla', ...}]

# User repos
gitter.user.repos # [{'name': 'MichaelYusko/GitterPy', 'description': 'Python for the Gitter API', ...}]

# User channels
gitter.user.channels
```

### Stream
```python
# Chat messages

response = gitter.stream.chat_messages('gitterHQ/sandbox')

for stream_messages in response.iter_lines():
    if stream_messages:
        print(stream_messages)

# Events
gitter.stream.events('gitterHQ/sandbox')
```


Contribution
=================================
1. `git clone git@github.com:MichaelYusko/GitterPy.git`
2. Feel free to make a PR;)
