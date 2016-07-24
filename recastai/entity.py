# coding: utf-8


class Entity(object):
  def __init__(self, name, entity):
    self.name = name

    for k, v in entity.items():
      setattr(self, k, v)
