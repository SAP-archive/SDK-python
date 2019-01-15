# coding: utf-8


class DialogMessage(object):
  def __init__(self, msg):
    if type(msg) is not dict or 'type' not in msg or 'content' not in msg:
      raise ValueError('Invalid message format: {}'.format(msg))
    self.type = msg['type']
    self.content = msg['content']
