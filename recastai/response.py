# -*- coding: utf-8 -*-

import json

from .sentence import Sentence


class Response(object):
  def __init__(self, response):
    self.raw = response

    response = json.loads(response)
    response = response['results']

    self.source = response['source']
    self.intents = response['intents']
    self.sentences = [Sentence(s) for s in response['sentences']]
    self.language = response['language']
    self.version = response['version']
    self.timestamp = response['timestamp']
    self.status = response['status']

  def intent(self):
    try:
      return self.intents[0]
    except IndexError:
      return None

  def sentence(self):
    try:
      return self.sentences[0]
    except IndexError:
      return None

  def get(self, name):
    for sentence in self.sentences:
      for entity in sentence.entities:
        if (entity.name.lower() == name.lower()):
          return entity

  def all(self, name):
    entities = []

    for sentence in self.sentences:
      for entity in sentence.entities:
        if (entity.name.lower() == name.lower()):
          entities.append(entity)

    return entities

  def entities(self):
    entities = []

    for sentence in self.sentences:
      for entity in sentence.entities:
        entities.append(entity)

    return entities
