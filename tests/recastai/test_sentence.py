# -*- coding: utf-8 -*-

from recastai import Sentence
from recastai import Entity


class TestSentence(object):
  def test_instanciable(self):
    Sentence({'source': "What's the weather in London?", 'type': 'what', 'action': 'be', 'agent': 'the weather in london', 'polarity': 'positive', 'entities': {'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London'}]}})

  def test_attributes(self):
    sentence = Sentence({'source': "What's the weather in London?", 'type': 'what', 'action': 'be', 'agent': 'the weather in london', 'polarity': 'positive', 'entities': {'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London'}]}})

    assert(sentence.source == "What's the weather in London?")
    assert(sentence.type == 'what')
    assert(sentence.action == 'be')
    assert(sentence.agent == 'the weather in london')
    assert(sentence.polarity == 'positive')
    assert(type(sentence.entities) is list)
    assert(type(sentence.entities[0]) is Entity)

  def test_helpers(self):
    sentence = Sentence({'source': "What's the weather in London?", 'type': 'what', 'action': 'be', 'agent': 'the weather in london', 'polarity': 'positive', 'entities': {'location': [{'formated': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London'}]}})

    entity = None
    for e in sentence.entities:
      if e.name.lower() == 'location':
        entity = e
        break
    assert(sentence.get('location') == entity)
    entities = []
    for e in sentence.entities:
      if e.name.lower() == 'location':
        entities.append(e)
    assert(sentence.all('location') == entities)
