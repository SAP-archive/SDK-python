# coding: utf-8


class Entity():
  def __init__(self, name, entity):
    self.name = name

    for k, v in entity.items():
      setattr(self, k, v)

  def __repr__(self):
    attributes = []
    for method in dir(self):
      if not method.startswith('__') and method != 'name':
        value = getattr(self, method)
        attributes.append("{}={}".format(method, value))

    return "{} ({})".format(self.name, ', '.join(attributes))
