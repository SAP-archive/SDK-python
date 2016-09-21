# coding: utf-8

import pytest
import sys
import os
import json
import responses
from recastai import Client
from recastai import Response
from recastai import RecastError


class TestClient(object):
  def test_instanciable(self):
    Client()

  def test_attributes(self):
    client = Client()

    client.token
    client.language

  def test_missing(self):
    client = Client()

    with pytest.raises(RecastError):
      client.text_request('This is my text')

    with pytest.raises(RecastError):
      client.file_request(os.path.dirname(os.path.realpath(__file__)) + '/../utils/test.wav')

  @responses.activate
  def test_bad_request(self):
    client = Client('testtoken')

    body = json.dumps({'results': {'source': 'What is the weather in London tomorrow? And in Paris?', 'intents': [{'slug': 'weather', 'confidence': 0.67}], 'act': 'wh-query', 'type': 'desc:desc', 'sentiment': 'neutral', 'entities': {'action': [{'agent': 'the weather in London', 'tense': 'present', 'raw': 'is', 'confidence': 0.89}], 'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London', 'confidence': 0.97}, {'formated': 'Paris, Paris, Île-de-France, France', 'lat': 48.856614, 'lng': 2.3522219, 'raw': 'Paris', 'confidence': 0.83}], 'datetime': [{'value': '2016-07-11T10:00:00+00:00', 'raw': 'tomorrow', 'confidence': 0.95}]}, 'language': 'en', 'version': '2.0.0', 'timestamp': '2016-07-10T23:17:59+02:00', 'status': 200}, 'message': 'Requests rendered with success'})
    responses.add(responses.POST, 'https://api.recast.ai/v2/request', body=body, status=400)

    with pytest.raises(RecastError):
      client.text_request('This is my text')

    with pytest.raises(RecastError):
      client.file_request(os.path.dirname(os.path.realpath(__file__)) + '/../utils/test.wav')

  @responses.activate
  def test_text_request(self):
    client = Client('testtoken')

    body = json.dumps({'results': {'source': 'What is the weather in London tomorrow? And in Paris?', 'intents': [{'slug': 'weather', 'confidence': 0.67}], 'act': 'wh-query', 'type': 'desc:desc', 'sentiment': 'neutral', 'entities': {'action': [{'agent': 'the weather in London', 'tense': 'present', 'raw': 'is', 'confidence': 0.89}], 'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London', 'confidence': 0.97}, {'formated': 'Paris, Paris, Île-de-France, France', 'lat': 48.856614, 'lng': 2.3522219, 'raw': 'Paris', 'confidence': 0.83}], 'datetime': [{'value': '2016-07-11T10:00:00+00:00', 'raw': 'tomorrow', 'confidence': 0.95}]}, 'language': 'en', 'version': '2.0.0', 'timestamp': '2016-07-10T23:17:59+02:00', 'status': 200}, 'message': 'Requests rendered with success'})
    responses.add(responses.POST, 'https://api.recast.ai/v2/request', body=body, status=200)

    response = client.text_request('This is my text')

    assert(type(response) == Response)

  @responses.activate
  def test_file_request(self):
    client = Client('testtoken')

    body = json.dumps({'results': {'source': 'What is the weather in London tomorrow? And in Paris?', 'intents': [{'slug': 'weather', 'confidence': 0.67}], 'act': 'wh-query', 'type': 'desc:desc', 'sentiment': 'neutral', 'entities': {'action': [{'agent': 'the weather in London', 'tense': 'present', 'raw': 'is', 'confidence': 0.89}], 'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London', 'confidence': 0.97}, {'formated': 'Paris, Paris, Île-de-France, France', 'lat': 48.856614, 'lng': 2.3522219, 'raw': 'Paris', 'confidence': 0.83}], 'datetime': [{'value': '2016-07-11T10:00:00+00:00', 'raw': 'tomorrow', 'confidence': 0.95}]}, 'language': 'en', 'version': '2.0.0', 'timestamp': '2016-07-10T23:17:59+02:00', 'status': 200}, 'message': 'Requests rendered with success'})
    responses.add(responses.POST, 'https://api.recast.ai/v2/request', body=body, status=200)

    response = client.file_request(os.path.dirname(os.path.realpath(__file__)) + '/../utils/test.wav')

    assert(type(response) == Response)

  @responses.activate
  def test_overrides(self):
    client = Client('testtoken')

    body = json.dumps({'results': {'source': 'What is the weather in London tomorrow? And in Paris?', 'intents': [{'slug': 'weather', 'confidence': 0.67}], 'act': 'wh-query', 'type': 'desc:desc', 'sentiment': 'neutral', 'entities': {'action': [{'agent': 'the weather in London', 'tense': 'present', 'raw': 'is', 'confidence': 0.89}], 'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London', 'confidence': 0.97}, {'formated': 'Paris, Paris, Île-de-France, France', 'lat': 48.856614, 'lng': 2.3522219, 'raw': 'Paris', 'confidence': 0.83}], 'datetime': [{'value': '2016-07-11T10:00:00+00:00', 'raw': 'tomorrow', 'confidence': 0.95}]}, 'language': 'en', 'version': '2.0.0', 'timestamp': '2016-07-10T23:17:59+02:00', 'status': 200}, 'message': 'Requests rendered with success'})
    responses.add(responses.POST, 'https://test.com', body=body, status=200)

    text_response = client.text_request('This is my text', token='tokentest', language='fr', endpoint='https://test.com')
    file_response = client.file_request(os.path.dirname(os.path.realpath(__file__)) + '/../utils/test.wav', token='tokentest', language='fr', endpoint='https://test.com')

    assert(type(text_response) == Response)
    assert(type(file_response) == Response)
