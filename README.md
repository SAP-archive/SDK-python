# Recast.AI - Python SDK

![logo](https://raw.githubusercontent.com/RecastAI/SDK-python/master/misc/logo-inline.png "Recast.AI")

Recast.AI official SDK for Python.


## Synospis

This library is a pure Python interface to the [Recast.AI](https://recast.ai) API. It allows you to make requests to your bots.


## Requirements

* python 2.7+


## Installation

### Via requirements.txt

From [pypi](https://pypi.python.org/pypi/pip)

```bash
recastai
```

From [github](https://github.com)

```bash
git+https://github.com/RecastAI/sdk-python.git#egg=recastai
```

### Via Terminal

From [pypi](https://pypi.python.org/pypi/pip):

```bash
pip install recastai
```

From [github](https://github.com)

```bash
pip install git+https://github.com/RecastAI/sdk-python.git
```


## Usage

### Package

```python
import recastai

client = recastai.Client(YOUR_TOKEN, YOUR_LANGUAGE)
response = client.text_request(YOUR_TEXT)
"""response = client.file_request(open(YOUR_FILE, 'rb'))"""

if response.intent().slug == YOUR_EXPECTED_INTENT:
  """Do your code..."""
```

## Specs

### Classes

This library contains 5 main classes, as follows:

* recastai.Client is the client allowing you to make requests.
* recastai.Response contains the response from [Recast.AI](https://recast.ai).
* recastai.Intent represents an intent of the response.
* recastai.Entity represents an entity found by Recast.AI in your user's input.
* recastai.RecastError is the error thrown by the library.

Don't hesitate to dive into the code, it's commented :)

## recastai.Client

The Client can be instanciated with a token and a language (both optional)

```python
client = recastai.Client(YOUR_TOKEN, YOUR_LANGUAGE)
```

__Your tokens__

[token]: https://github.com/RecastAI/SDK-Python/blob/master/misc/recast-ai-tokens.png "Tokens"

![alt text][token]

*Copy paste your request access token from your bot's settings*

__Your language__

```python
client = recastai.Client(YOUR_TOKEN, 'en')
```

*The language is a lowercase 639-1 isocode.*

If you pass a token or a language in the options parameter, it will override your default client language or token

```python
response = client.text_request(YOUR_TEXT)

if response.intent().slug == YOUR_EXPECTED_INTENT
  # Do your code...
end
```

```python
# With optional parameters
response = client.text_request(YOUR_TEXT, token=YOUR_TOKEN, language=YOUR_LANGUAGE)
```

__If a language is provided:__ the language you've given is used for processing if your bot has expressions for it, else your bot's primary language is used.

__If no language is provided:__ the language of the text is detected and is used for processing if your bot has expressions for it, else your bot's primary language is used for processing.

## File request

file_request(file, options = {})

If you pass a token or a language in the option parameter, it will override your default client language or token.

__file format: .wav__
```python
response = client.file_request(open(YOUR_FILE, 'rb'))

if response.intent.slug == YOUR_EXPECTED_INTENT
  # Do your code...
end
```

```python
# with optional parameters
response = client.file_request(open(YOUR_FILE, 'rb'), token=YOUR_TOKEN, language=YOUR_LANGUAGE)
```

__If a language is provided:__ the language you've given is used for processing if your bot has expressions for it, else your bot's primary language is used

__If no language is provided:__ your bot's primary language is used for processing as we do not provide language detection for speech.

## recastai.Response

The Response is generated after a call to either file\_request or text\_request.

### Get the first detected intent

| Method        | Params | Return                    |
| ------------- |:------:| :-------------------------|
| intent()      |        | the first detected intent |

```python
response = client.text_request(YOUR_TEXT)

if response.intent().slug == YOUR_EXPECTED_INTENT
  # Do your code...
end
```

### Get the first entity matching name

| Method     | Params        | Return                   |
| ---------- |:-------------:| :------------------------|
| get(name)  | name: String  | the first Entity matched |

```python
response = client.text_request(YOUR_TEXT)

location = response.get('location')
```

### Get all entities matching name

| Method     | Params        | Return                   |
| ---------- |:-------------:| :------------------------|
| all(name)  | name: String  | all the Entities matched |

```python
response = client.text_request(YOUR_TEXT)

locations = response.all('location')
```

### Act helpers

| Method          | Params | Return                                                 |
| --------------- |:------:| :----------------------------------------------------- |
| is\_assert      |        | Bool: whether or not the sentence is an assertion      |
| is\_command     |        | Bool: whether or not the sentence is a command         |
| is\_wh\_query   |        | Bool: whether or not the sentence is a question        |
| is\_yn\_query   |        | Bool: whether or not the sentence is a query           |

### Type helpers

| Method           | Params | Return                                                 |
| ---------------- |:------:| :----------------------------------------------------- |
| is\_abbreviation |        | Bool: is the answer of the sentence an abbreviation?   |
| is\_entity       |        | Bool: is the answer of the sentence an entity?         |
| is\_description  |        | Bool: is the answer of the sentence an description?    |
| is\_human        |        | Bool: is the answer of the sentence an human?          |
| is\_location     |        | Bool: is the answer of the sentence a location?        |
| is\_number       |        | Bool: is the answer of the sentence an number?         |

### Sentiment helpers

| Method        | Params | Return                                                 |
| ------------- |:------:| :----------------------------------------------------- |
| is\_vpositive |        | Bool: is the sentence very positive?                   |
| is\_positive  |        | Bool: is the sentence positive?                        |
| is\_neutral   |        | Bool: is the sentence neutral?                         |
| is\_negative  |        | Bool: is the sentence negative?                        |
| is\_vnegative |        | Bool: is the sentence very negative?                   |

### Getters

Each of the following methods corresponds to a Response attribute

| Method        | Params | Return                                              |
| ------------- |:------:| :---------------------------------------------------|
| raw()         |        | String: the raw unparsed json response              |
| uuid()        |        | String: the universal unique id of the request      |
| source()      |        | String: the user input                              |
| intents()     |        | Array[Intent]: all the matched intents              |
| act()         |        | String: the act of the sentence                     |
| type()        |        | String: the type of the sentence                    |
| sentiment()   |        | String: the sentiment of the sentence               |
| entities()    |        | Array[Entity]: all the detected entities            |
| language()    |        | String: the language of the sentence                |
| version()     |        | String: the version of the json                     |
| timestamp()   |        | String: the timestamp at the end of the processing  |
| status()      |        | String: the status of the response                  |

## recastai.Intent

Each of the following methods corresponds to an Intent attribute

| Attributes   | Description                                                   |
| ------------ |:--------------------------------------------------------------|
| slug()       | String: the slug of the intent                                |
| confidence() | Float: the unparsed json value of the intent                  |

## recastai.Entity

Each of the following methods corresponds to an Entity attribute

| Attributes   | Description                                                   |
| ------------ |:--------------------------------------------------------------|
| name()       | String: the name of the entity                                |
| raw()        | String: the raw value extracted from the sentence             |
| confidence() | Float: the detection score between 0 and 1 excluded           |

In addition to those methods, more attributes are generated depending of the nature of the entity.
The full list can be found there: [man.recast.ai](https://man.recast.ai/#list-of-entities)

```python
response = client.text_request(YOUR_TEXT)

location = response.get('location')

print(location.raw())
print(location.name())
```

### recastai.RecastError

The Recast.AI Error is thrown when receiving an non-200 response from Recast.AI.

As it inherits from Exception, it implements the default exception methods.

## More

You can view the whole API reference at [man.recast.ai](https://man.recast.ai).


## Author

Paul Renvoisé, paul.renvoise@recast.ai, [@paulrenvoise](https://twitter.com/paulrenvoise)

You can follow us on Twitter at [@recastai](https://twitter.com/recastai) for updates and releases.


## License

Copyright (c) [2016] [Recast.AI](https://recast.ai)

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
