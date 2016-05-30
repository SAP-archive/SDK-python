from recastai import entity

class Sentence(object):
  def __init__(self, sentence):
    self.source = sentence['source']
    self.type = sentence['type']
    self.action = sentence['action']
    self.agent = sentence['agent']
    self.polarity = sentence['polarity']
    self.entities = [Entity(n, ee) for ee in e for n, e in sentence['entities']]
