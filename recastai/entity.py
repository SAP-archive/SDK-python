# -*- coding: utf-8 -*-


class Entity(object):
  def __init__(self, name, data):
    self.name = name

    for k, v in data.items():
      setattr(self, k, v)
