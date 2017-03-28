# coding: utf-8

from .analyse import Analyse
from .converse import Converse


class Request(Analyse, Converse):
  def __init__(self, token=None, language=None, proxy=None):
    self.token = token
    self.language = language
    self.proxy = proxy
