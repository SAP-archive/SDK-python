# coding: utf-8


class Intent():
  def __init__(self, intent):
    self.slug = intent['slug']
    self.confidence = intent['confidence']

  def __repr__(self):
    attributes = []
    for method in dir(self):
      if not method.startswith('__') and method != 'slug':
        value = getattr(self, method)
        attributes.append("{}={}".format(method, value))

    return "{} ({})".format(self.slug, ', '.join(attributes))
