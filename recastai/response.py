import json
from recastai import sentence

class Response(object):
  def __init__(self, response):
    self.raw = response

    response = json.loads(response)
    response = response['results']

    self.source = response['source']
    self.intents = response['intents']
    self.sentences = [Sentence(s) for s in response['sentences']]
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
        if (entity.name.lower() is name.lower()):
          return entity


  def all(self, name=None):
    entities = []

    for sentence in self.sentences:
      for entity in sentence.entities:
        if (name is None) or (entity.name.lower() is name.lower()):
          entities << entity

    return entities
