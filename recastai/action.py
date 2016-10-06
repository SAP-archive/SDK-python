# coding: utf-8


class Action(object):
  def __init__(self, action):
    self.slug = action['slug']
    self.done = action['done']
    self.reply = action['reply']
