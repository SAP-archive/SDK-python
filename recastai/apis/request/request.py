# coding: utf-8

from .analyze import Analyze
from .converse import Converse


class Request(Analyze, Converse):
  def __init__(self, token=None, language=None, proxy=None):
    self.token = token
    self.language = language
    self.proxy = proxy
