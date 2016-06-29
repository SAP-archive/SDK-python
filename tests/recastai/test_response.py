# -*- coding: utf-8 -*-

import json
from recastai import Response
from recastai import Sentence


class TestResponse(object):
  def test_instanciable(self):
    Response(json.dumps({'results': {'source': "What's the weather in London?", 'intents': ['test'], 'sentences': [{'source': "What's the weather in London?", 'type': 'what', 'action': 'be', 'agent': 'the weather in london', 'polarity': 'positive', 'entities': {'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London'}]}}], 'language': 'en', 'version': '1.3.0', 'timestamp': '2016-05--1T17:33:00+02:00', 'status': 200}, 'message': 'Requests rendered with success.'}))

  def test_attributes(self):
    response = Response(json.dumps({'results': {'source': "What's the weather in London?", 'intents': ['test'], 'sentences': [{'source': "What's the weather in London?", 'type': 'what', 'action': 'be', 'agent': 'the weather in london', 'polarity': 'positive', 'entities': {'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London'}]}}], 'language': 'en', 'version': '1.3.0', 'timestamp': '2016-05--1T17:33:00+02:00', 'status': 200}, 'message': 'Requests rendered with success.'}))

    assert(response.raw == json.dumps({'results': {'source': "What's the weather in London?", 'intents': ['test'], 'sentences': [{'source': "What's the weather in London?", 'type': 'what', 'action': 'be', 'agent': 'the weather in london', 'polarity': 'positive', 'entities': {'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London'}]}}], 'language': 'en', 'version': '1.3.0', 'timestamp': '2016-05--1T17:33:00+02:00', 'status': 200}, 'message': 'Requests rendered with success.'}))
    assert(response.source == "What's the weather in London?")
    assert(type(response.intents) is list)
    assert(response.intents == ['test'])
    assert(type(response.sentences) is list)
    assert(type(response.sentences[0]) is Sentence)
    assert(response.language == 'en')
    assert(response.version == '1.3.0')
    assert(response.timestamp == '2016-05--1T17:33:00+02:00')
    assert(response.status == 200)

  def test_helpers(self):
    response = Response(json.dumps({'results': {'source': "What's the weather in London?", 'intents': ['test'], 'sentences': [{'source': "What's the weather in London?", 'type': 'what', 'action': 'be', 'agent': 'the weather in london', 'polarity': 'positive', 'entities': {'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London'}]}}], 'language': 'en', 'version': '1.3.0', 'timestamp': '2016-05--1T17:33:00+02:00', 'status': 200}, 'message': 'Requests rendered with success.'}))

    assert(response.intent() == response.intents[0])
    assert(response.sentence() == response.sentences[0])
    entity = None
    for s in response.sentences:
      for e in s.entities:
        if e.name.lower() == 'location':
          entity = e
          break
    assert(response.get('location') == entity)
    entities = []
    for s in response.sentences:
      for e in s.entities:
        if e.name.lower() == 'location':
          entities.append(e)
    assert(response.all('location') == entities)
    entities = []
    for s in response.sentences:
      for e in s.entities:
          entities.append(e)
    assert(response.entities() == entities)

  def test_missing_array(self):
    response = Response(json.dumps({'results': {'source': "What's the weather in London?", 'intents': [], 'sentences': [], 'language': 'en', 'version': '1.3.0', 'timestamp': '2016-05--1T17:33:00+02:00', 'status': 200}, 'message': 'Requests rendered with success.'}))

    assert(response.intent() is None)
    assert(response.sentence() is None)
