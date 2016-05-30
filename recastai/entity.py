class Entity(object):
  def __init__(self, name, data):
    self.name = name

    for k, v in data.iteritems():
      setattr(self, k, v)
