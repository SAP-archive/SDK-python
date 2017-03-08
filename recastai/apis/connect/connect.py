# coding: utf-8

from .message import Message


class Connect(Message):
  def __init__(self, token=None, language=None, proxy=None):
    self.token = token
    self.language = language
    self.proxy = proxy
