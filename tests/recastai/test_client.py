# -*- coding: utf-8 -*-

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

    body = json.dumps({'results': {'source': "What's the weather in London?", 'intents': ['test'], 'sentences': [{'source': "What's the weather in London?", 'type': 'what', 'action': 'be', 'agent': 'the weather in london', 'polarity': 'positive', 'entities': {'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London'}]}}], 'language': 'en', 'version': '1.3.0', 'timestamp': '2016-05--1T17:33:00+02:00', 'status': 400}, 'message': 'Requests rendered with success.'})
    responses.add(responses.POST, 'https://api.recast.ai/v1/request', body=body, status=400)

    with pytest.raises(RecastError):
      client.text_request('This is my text')

    with pytest.raises(RecastError):
      client.file_request(os.path.dirname(os.path.realpath(__file__)) + '/../utils/test.wav')

  @responses.activate
  def test_text_request(self):
    client = Client('testtoken')

    body = json.dumps({'results': {'source': "What's the weather in London?", 'intents': ['test'], 'sentences': [{'source': "What's the weather in London?", 'type': 'what', 'action': 'be', 'agent': 'the weather in london', 'polarity': 'positive', 'entities': {'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London'}]}}], 'language': 'en', 'version': '1.3.0', 'timestamp': '2016-05--1T17:33:00+02:00', 'status': 200}, 'message': 'Requests rendered with success.'})
    responses.add(responses.POST, 'https://api.recast.ai/v1/request', body=body, status=200)

    response = client.text_request('This is my text')

    assert(type(response) == Response)

  @responses.activate
  def test_file_request(self):
    client = Client('testtoken')

    body = json.dumps({'results': {'source': "What's the weather in London?", 'intents': ['test'], 'sentences': [{'source': "What's the weather in London?", 'type': 'what', 'action': 'be', 'agent': 'the weather in london', 'polarity': 'positive', 'entities': {'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London'}]}}], 'language': 'en', 'version': '1.3.0', 'timestamp': '2016-05--1T17:33:00+02:00', 'status': 200}, 'message': 'Requests rendered with success.'})
    responses.add(responses.POST, 'https://api.recast.ai/v1/request', body=body, status=200)

    response = client.file_request(os.path.dirname(os.path.realpath(__file__)) + '/../utils/test.wav')

    assert(type(response) == Response)

  @responses.activate
  def test_overrides(self):
    client = Client('testtoken')

    body = json.dumps({'results': {'source': "What's the weather in London?", 'intents': ['test'], 'sentences': [{'source': "What's the weather in London?", 'type': 'what', 'action': 'be', 'agent': 'the weather in london', 'polarity': 'positive', 'entities': {'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London'}]}}], 'language': 'en', 'version': '1.3.0', 'timestamp': '2016-05--1T17:33:00+02:00', 'status': 200}, 'message': 'Requests rendered with success.'})
    responses.add(responses.POST, 'https://api.recast.ai/v1/request', body=body, status=200)

    text_response = client.text_request('This is my text', token='tokentest', language='fr')
    file_response = client.file_request(os.path.dirname(os.path.realpath(__file__)) + '/../utils/test.wav', token='tokentest', language='fr')

    assert(type(text_response) == Response)
    assert(type(file_response) == Response)
