[logo]: https://cdn.cai.tools.sap/brand/sapcai/sap-cai-black.svg "SAP Conversational AI"

![alt text][logo]

# SAP Conversational AI - SDK Python

SAP Conversational AI official SDK in Python

## Overview

This module is a wrapper around the [SAP Conversational AI](https://cai.tools.sap) API, and allows you to:
* [Analyse your text](https://github.com/SAPConversationalAI/SDK-python/wiki/01-Analyse-Text)
* [Manage a conversation](https://github.com/SAPConversationalAI/SDK-python/wiki/02-Manage-conversation)
* [Receive and send messages](https://github.com/SAPConversationalAI/SDK-python/wiki/03-Receive-and-send-messages)

## Installation

  #### Using pip

Install from PyPi using [pip](http://www.pip-installer.org/en/latest/), a
package manager for Python.

    pip install sapcai

Don't have pip installed? Try installing it, by running this from the command
line:

    $ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

  #### With the source code

You can [download the source code
(ZIP)](https://github.com/SAPConversationalAI/SDK-python/zipball/master "SAP Conversational AI-python
source code") for `SAPConversationalAI-python`, and then run:

    python setup.py install

You may need to run the above commands with `sudo`.

This library supports both `python 2.7+` and `python 3.5+`.

You can now use the SDK in your code. All you need is your bot's token. In case you have enabled our versioning feature in the settings of your bot, you can refer to our [versioning documentation](https://cai.tools.sap/docs/concepts/versioning) to learn how to select the appropriate token for you versions and environments.

## Usage

Using the entire SDK:
```python
import sapcai

client = sapcai.Client('YOUR_TOKEN')

client.request.analyse_text('Hi')
client.connect.broadcast_message('Hi')
```

Extracting one single API:
```python
from sapcai import Request, Connect

request = Request('YOUR_TOKEN')
request.analyse_text('Hi')

connect = Connect('YOUR_TOKEN')
connect.broadcast_message('Hi')
```

## More

You can view the whole API reference at [cai.tools.sap/docs/api-reference](https://cai.tools.sap/docs/api-reference).

You can follow us on Twitter at [@sapcai](https://twitter.com/sapcai) for updates and releases.


## License

Copyright (c) [2019] [SAP Conversational AI](https://cai.tools.sap)

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
