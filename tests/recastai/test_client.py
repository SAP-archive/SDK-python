# coding: utf-8

import pytest
import sys
import os
import json
import responses
from recastai import Client
from recastai import Response
from recastai import Conversation
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

    with pytest.raises(RecastError):
      client.text_converse('This is my text')

  @responses.activate
  def test_bad_request(self):
    client = Client('testtoken')

    body = json.dumps({'results': None, 'message': 'Request is invalid'})
    responses.add(responses.POST, 'https://api.recast.ai/v2/request', body=body, status=400)
    responses.add(responses.POST, 'https://api.recast.ai/v2/converse', body=body, status=400)

    with pytest.raises(RecastError):
      client.text_request('This is my text')

    with pytest.raises(RecastError):
      client.file_request(os.path.dirname(os.path.realpath(__file__)) + '/../utils/test.wav')

    with pytest.raises(RecastError):
      client.text_converse('This is my text')

  @responses.activate
  def test_text_request(self):
    client = Client('testtoken')

    body = json.dumps({'results': {'uuid': 'db4837b0-8359-4505-9678-c4081a6f2ad8', 'source': 'What is the weather in London tomorrow? And in Paris?', 'intents': [{'slug': 'weather', 'confidence': 0.67}], 'act': 'wh-query', 'type': 'desc:desc', 'sentiment': 'neutral', 'entities': {'action': [{'agent': 'the weather in London', 'tense': 'present', 'raw': 'is', 'confidence': 0.89}], 'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London', 'confidence': 0.97}, {'formated': 'Paris, Paris, Île-de-France, France', 'lat': 48.856614, 'lng': 2.3522219, 'raw': 'Paris', 'confidence': 0.83}], 'datetime': [{'iso': '2016-07-11T10:00:00+00:00', 'raw': 'tomorrow', 'confidence': 0.95}]}, 'language': 'en', 'version': '2.0.0', 'timestamp': '2016-07-10T23:17:59+02:00', 'status': 200}, 'message': 'Requests rendered with success'})
    responses.add(responses.POST, 'https://api.recast.ai/v2/request', body=body, status=200)

    response = client.text_request('This is my text')

    assert(type(response) == Response)

  @responses.activate
  def test_file_request(self):
    client = Client('testtoken')

    body = json.dumps({'results': {'uuid': 'db4837b0-8359-4505-9678-c4081a6f2ad8', 'source': 'What is the weather in London tomorrow? And in Paris?', 'intents': [{'slug': 'weather', 'confidence': 0.67}], 'act': 'wh-query', 'type': 'desc:desc', 'sentiment': 'neutral', 'entities': {'action': [{'agent': 'the weather in London', 'tense': 'present', 'raw': 'is', 'confidence': 0.89}], 'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London', 'confidence': 0.97}, {'formated': 'Paris, Paris, Île-de-France, France', 'lat': 48.856614, 'lng': 2.3522219, 'raw': 'Paris', 'confidence': 0.83}], 'datetime': [{'iso': '2016-07-11T10:00:00+00:00', 'raw': 'tomorrow', 'confidence': 0.95}]}, 'language': 'en', 'version': '2.0.0', 'timestamp': '2016-07-10T23:17:59+02:00', 'status': 200}, 'message': 'Requests rendered with success'})
    responses.add(responses.POST, 'https://api.recast.ai/v2/request', body=body, status=200)

    response = client.file_request(os.path.dirname(os.path.realpath(__file__)) + '/../utils/test.wav')

    assert(type(response) == Response)

  @responses.activate
  def test_text_converse(self):
    client = Client('testtoken')

    body = json.dumps({'results': {'uuid': 'db4837b0-8359-4505-9678-c4081a6f2ad8', 'source': 'What is the weather in Paris ?', 'replies': ['Do you already have an account?', 'This is a test?'], 'action': {'slug': 'murder', 'done': False, 'reply': 'do you already have an account?'}, 'next_actions': [{'slug': 'test', 'done': False, 'reply': 'This is a test?'}], 'memory':{'victim': None, 'client': None, 'mail-client': None, 'lieu': {'lat': 0.54, 'lng': 0.435}}, 'entities': {}, 'intents': [], 'conversation_token': '8641d38b059cde2826e3cdf2f9b00725', 'language': 'en', 'version': '2.0.0', 'timestamp': '2016-10-04T15:26:11.876Z', 'status': 200}, 'message': 'Converses rendered with success'})
    responses.add(responses.POST, 'https://api.recast.ai/v2/converse', body=body, status=200)

    response = client.text_converse('What is the weather in Paris?')

    assert(type(response) == Conversation)

  @responses.activate
  def test_overrides(self):
    client = Client('testtoken')

    body = json.dumps({'results': {'uuid': 'db4837b0-8359-4505-9678-c4081a6f2ad8', 'source': 'What is the weather in London tomorrow? And in Paris?', 'intents': [{'slug': 'weather', 'confidence': 0.67}], 'act': 'wh-query', 'type': 'desc:desc', 'sentiment': 'neutral', 'entities': {'action': [{'agent': 'the weather in London', 'tense': 'present', 'raw': 'is', 'confidence': 0.89}], 'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London', 'confidence': 0.97}, {'formated': 'Paris, Paris, Île-de-France, France', 'lat': 48.856614, 'lng': 2.3522219, 'raw': 'Paris', 'confidence': 0.83}], 'datetime': [{'iso': '2016-07-11T10:00:00+00:00', 'raw': 'tomorrow', 'confidence': 0.95}]}, 'language': 'en', 'version': '2.0.0', 'timestamp': '2016-07-10T23:17:59+02:00', 'status': 200}, 'message': 'Requests rendered with success'})
    responses.add(responses.POST, 'https://api.recast.ai/v2/request', body=body, status=200)
    body = json.dumps({'results': {'uuid': 'db4837b0-8359-4505-9678-c4081a6f2ad8', 'source': 'What is the weather in Paris ?', 'replies': ['Do you already have an account?', 'This is a test?'], 'action': {'slug': 'murder', 'done': False, 'reply': 'do you already have an account?'}, 'next_actions': [{'slug': 'test', 'done': False, 'reply': 'This is a test?'}], 'memory':{'victim': None, 'client': None, 'mail-client': None, 'lieu': {'lat': 0.54, 'lng': 0.435}}, 'entities': {}, 'intents': [], 'conversation_token': '8641d38b059cde2826e3cdf2f9b00725', 'language': 'en', 'version': '2.0.0', 'timestamp': '2016-10-04T15:26:11.876Z', 'status': 200}, 'message': 'Converses rendered with success'})
    responses.add(responses.POST, 'https://api.recast.ai/v2/converse', body=body, status=200)

    text_response = client.text_request('This is my text', token='tokentest', language='fr')
    file_response = client.file_request(os.path.dirname(os.path.realpath(__file__)) + '/../utils/test.wav', token='tokentest', language='fr')
    text_conversation = client.text_converse('This is my text', token='tokentest', language='fr', conversation_token='conversationtokentest', memory={'lieu':{'lat': 0.54, 'lng': 0.435}})

    assert(type(text_response) == Response)
    assert(type(file_response) == Response)
    assert(type(text_conversation) == Conversation)
