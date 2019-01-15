# coding: utf-8


class Action():
  def __init__(self, action):
    self.slug = action['slug']
    self.done = action['done']
    self.reply = action['reply']

  def __repr__(self):
    attributes = []
    for method in dir(self):
      if not method.startswith('__') and method != 'slug':
        value = getattr(self, method)
        attributes.append("{}={}".format(method, value))

    return "{} ({})".format(self.name, ', '.join(attributes))
