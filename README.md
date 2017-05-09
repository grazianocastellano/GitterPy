# GitterPy

Python interface for the Gitter API

[![Build Status](https://travis-ci.org/MichaelYusko/GitterPy.svg?branch=master)](https://travis-ci.org/MichaelYusko/GitterPy)


Releases
=================================
* 0.0.1 - planning(PyPi)
* 0.0.1 - planning(PyPi test)


Installation
=================================
coming soon



Usage
=================================
```python
from gitterpy import GitterClient

# Create instance
gitter = GitterClient('YOUR_TOKEN')


# Join into the room
gitter.rooms.join('gitterHQ/sandbox')


# Leave from the room
gitter.rooms.leave('gitterHQ/sandbox')


# List of rooms
gitter.rooms.rooms_list


# Grab room
gitter.rooms.grab_room('gitterHQ/sandbox')


# Send a message to #gitterHQ/sandbox room
print(gitter.messages.send('gitterHQ/sandbox', 'Hello everyone'))


# Message list
gitter.messages.list('gitterHQ/sandbox')
```


TODO
=================================
coming soon