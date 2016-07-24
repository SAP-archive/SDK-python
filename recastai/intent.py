# coding: utf-8


class Intent(object):
  def __init__(self, intent):
    self.name = intent['name']
    self.confidence = intent['confidence']
