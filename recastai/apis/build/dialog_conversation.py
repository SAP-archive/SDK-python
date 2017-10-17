# coding: utf-8


class DialogConversation(object):
  def __init__(self, conv):
    self.id = conv.get('conversation_id', conv.get('id', None))
    self.language = conv.get('language', None)
    self.memory = conv['memory']
    self.skill = conv.get('skill', conv.get('last_skill', None))
    self.skill_occurences = conv.get('skill_occurences', conv.get('last_skill_occurences', None))
