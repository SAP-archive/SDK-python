# coding: utf-8


class Intent(object):
  def __init__(self, intent):
    self.slug = intent['slug']
    self.confidence = intent['confidence']
