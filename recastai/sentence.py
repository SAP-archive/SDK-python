# -*- coding: utf-8 -*-

from .entity import Entity


class Sentence(object):
  def __init__(self, sentence):
    self.source = sentence['source']
    self.type = sentence['type']
    self.action = sentence['action']
    self.agent = sentence['agent']
    self.polarity = sentence['polarity']
    entities = sentence['entities']
    self.entities = [Entity(n, ee) for n, e in entities.items() for ee in e]

  def get(self, name):
    for entity in self.entities:
      if entity.name.lower() == name.lower():
        return entity

  def all(self, name):
    entities = []

    for entity in self.entities:
      if entity.name.lower() == name.lower():
        entities.append(entity)

    return entities
