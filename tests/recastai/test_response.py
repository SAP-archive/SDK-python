# coding: utf-8

import json
from recastai import Response
from recastai import Intent
from recastai import Entity


class TestResponse(object):
  def test_instanciable(self):
    Response(json.dumps({'results': {'uuid': 'db4837b0-8359-4505-9678-c4081a6f2ad8', 'source': 'What is the weather in London tomorrow? And in Paris?', 'intents': [{'slug': 'weather', 'confidence': 0.67}], 'act': 'wh-query', 'type': 'desc:desc', 'sentiment': 'neutral', 'entities': {'action': [{'agent': 'the weather in London', 'tense': 'present', 'raw': 'is', 'confidence': 0.89}], 'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London', 'confidence': 0.97}, {'formated': 'Paris, Paris, Île-de-France, France', 'lat': 48.856614, 'lng': 2.3522219, 'raw': 'Paris', 'confidence': 0.83}], 'datetime': [{'iso': '2016-07-11T10:00:00+00:00', 'raw': 'tomorrow', 'confidence': 0.95}]}, 'language': 'en', 'version': '2.0.0', 'timestamp': '2016-07-10T23:17:59+02:00', 'status': 200}, 'message': 'Requests rendered with success'}))

  def test_attributes(self):
    response = Response(json.dumps({'results': {'uuid': 'db4837b0-8359-4505-9678-c4081a6f2ad8', 'source': 'What is the weather in London tomorrow? And in Paris?', 'intents': [{'slug': 'weather', 'confidence': 0.67}], 'act': 'wh-query', 'type': 'desc:desc', 'sentiment': 'neutral', 'entities': {'action': [{'agent': 'the weather in London', 'tense': 'present', 'raw': 'is', 'confidence': 0.89}], 'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London', 'confidence': 0.97}, {'formated': 'Paris, Paris, Île-de-France, France', 'lat': 48.856614, 'lng': 2.3522219, 'raw': 'Paris', 'confidence': 0.83}], 'datetime': [{'iso': '2016-07-11T10:00:00+00:00', 'raw': 'tomorrow', 'confidence': 0.95}]}, 'language': 'en', 'version': '2.0.0', 'timestamp': '2016-07-10T23:17:59+02:00', 'status': 200}, 'message': 'Requests rendered with success'}))

    assert(response.raw == json.dumps({'results': {'uuid': 'db4837b0-8359-4505-9678-c4081a6f2ad8', 'source': 'What is the weather in London tomorrow? And in Paris?', 'intents': [{'slug': 'weather', 'confidence': 0.67}], 'act': 'wh-query', 'type': 'desc:desc', 'sentiment': 'neutral', 'entities': {'action': [{'agent': 'the weather in London', 'tense': 'present', 'raw': 'is', 'confidence': 0.89}], 'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London', 'confidence': 0.97}, {'formated': 'Paris, Paris, Île-de-France, France', 'lat': 48.856614, 'lng': 2.3522219, 'raw': 'Paris', 'confidence': 0.83}], 'datetime': [{'iso': '2016-07-11T10:00:00+00:00', 'raw': 'tomorrow', 'confidence': 0.95}]}, 'language': 'en', 'version': '2.0.0', 'timestamp': '2016-07-10T23:17:59+02:00', 'status': 200}, 'message': 'Requests rendered with success'}))
    assert(response.source == 'What is the weather in London tomorrow? And in Paris?')
    assert(type(response.intents) is list)
    assert(type(response.intents[0]) is Intent)
    assert(response.act == 'wh-query')
    assert(response.type == 'desc:desc')
    assert(response.sentiment == 'neutral')
    assert(type(response.entities) is list)
    assert(type(response.entities[0]) is Entity)
    assert(response.language == 'en')
    assert(response.version == '2.0.0')
    assert(response.timestamp == '2016-07-10T23:17:59+02:00')
    assert(response.status == 200)

  def test_helpers(self):
    response = Response(json.dumps({'results': {'uuid': 'db4837b0-8359-4505-9678-c4081a6f2ad8', 'source': 'What is the weather in London tomorrow? And in Paris?', 'intents': [{'slug': 'weather', 'confidence': 0.67}], 'act': 'wh-query', 'type': 'desc:desc', 'sentiment': 'neutral', 'entities': {'action': [{'agent': 'the weather in London', 'tense': 'present', 'raw': 'is', 'confidence': 0.89}], 'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London', 'confidence': 0.97}, {'formated': 'Paris, Paris, Île-de-France, France', 'lat': 48.856614, 'lng': 2.3522219, 'raw': 'Paris', 'confidence': 0.83}], 'datetime': [{'iso': '2016-07-11T10:00:00+00:00', 'raw': 'tomorrow', 'confidence': 0.95}]}, 'language': 'en', 'version': '2.0.0', 'timestamp': '2016-07-10T23:17:59+02:00', 'status': 200}, 'message': 'Requests rendered with success'}))

    assert(response.intent() == response.intents[0])
    entity = None
    for e in response.entities:
      if e.name.lower() == 'location':
        entity = e
        break
    assert(response.get('location') == entity)
    entities = []
    for e in response.entities:
      if e.name.lower() == 'location':
        entities.append(e)
    assert(response.all('location') == entities)
    assert(response.is_assert() == False)
    assert(response.is_command() == False)
    assert(response.is_wh_query() == True)
    assert(response.is_yn_query() == False)
    assert(response.is_abbreviation() == False)
    assert(response.is_entity() == False)
    assert(response.is_description() == True)
    assert(response.is_human() == False)
    assert(response.is_location() == False)
    assert(response.is_number() == False)
    assert(response.is_vpositive() == False)
    assert(response.is_positive() == False)
    assert(response.is_neutral() == True)
    assert(response.is_negative() == False)
    assert(response.is_vnegative() == False)

  def test_missing_array(self):
    response = Response(json.dumps({'results': {'uuid': 'db4837b0-8359-4505-9678-c4081a6f2ad8', 'source': 'What is the weather in London tomorrow? And in Paris?', 'intents': [], 'act': 'wh-query', 'type': 'desc:desc', 'sentiment': 'neutral', 'entities': {'action': [{'agent': 'the weather in London', 'tense': 'present', 'raw': 'is', 'confidence': 0.89}], 'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London', 'confidence': 0.97}, {'formated': 'Paris, Paris, Île-de-France, France', 'lat': 48.856614, 'lng': 2.3522219, 'raw': 'Paris', 'confidence': 0.83}], 'datetime': [{'iso': '2016-07-11T10:00:00+00:00', 'raw': 'tomorrow', 'confidence': 0.95}]}, 'language': 'en', 'version': '2.0.0', 'timestamp': '2016-07-10T23:17:59+02:00', 'status': 200}, 'message': 'Requests rendered with success'}))
    assert(response.intent() is None)
