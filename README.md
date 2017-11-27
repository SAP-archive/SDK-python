[logo]: https://cdn.recast.ai/brand/recast-ai-logo-inline.png "Recast.AI"

![alt text][logo]

# Recast.AI - SDK Python

Recast.AI official SDK in Python

## Overview

This module is a wrapper around the [Recast.AI](https://recast.ai) API, and allows you to:
* [Analyse your text](https://github.com/RecastAI/SDK-python/wiki/01-Analyse-Text)
* [Manage a conversation](https://github.com/RecastAI/SDK-python/wiki/02-Manage-conversation)
* [Receive and send messages](https://github.com/RecastAI/SDK-python/wiki/03-Receive-and-send-messages)
* [Message Payload](https://github.com/RecastAI/SDK-python/wiki/04-Message-payload)

## Installation

  #### Using pip

Install from PyPi using [pip](http://www.pip-installer.org/en/latest/), a
package manager for Python.

    pip install recastai

Don't have pip installed? Try installing it, by running this from the command
line:

    $ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

  #### With the source code

You can [download the source code
(ZIP)](https://github.com/recastAI/SDK-python/zipball/master "Recast.AI-python
source code") for `RecastAI-python`, and then run:

    python setup.py install

You may need to run the above commands with `sudo`.

This library supports both `python 2.7+` and `python 3.5+`.

You can now use the sdk in your code.

## Usage

Using the entire SDK:
```python
import recastai

client = recastai.Client('YOUR_TOKEN')

client.request.analyse_text('Hi')
client.connect.broadcast_message('Hi')
```

Extracting one single API:
```python
from recastai import Request, Connect

request = Request('YOUR_TOKEN')
request.analyse_text('Hi')

connect = Connect('YOUR_TOKEN')
connect.broadcast_message('Hi')
```

## More

You can view the whole API reference at [man.recast.ai](https://man.recast.ai).


## Author

Paul Renvoisé, paul.renvoise@recast.ai, [@paulrenvoise](https://twitter.com/paulrenvoise)

You can follow us on Twitter at [@recastai](https://twitter.com/recastai) for updates and releases.


## License

Copyright (c) [2017] [Recast.AI](https://recast.ai)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
