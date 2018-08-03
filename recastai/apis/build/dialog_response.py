# coding: utf-8

from .dialog_message import DialogMessage
from .dialog_conversation import DialogConversation

from ..request.models import Response as NLPResponse


class DialogResponse(object):
  def __init__(self, messages, conversation, nlp, logs):
    if type(messages) is not list:
      raise ValueError('Invalid messages format: {}'.format(messages))
    self.messages = [DialogMessage(msg) for msg in messages]
    self.conversation = DialogConversation(conversation)
    self.nlp = NLPResponse(nlp)
    self.logs = logs
