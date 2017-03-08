# coding: utf-8

from .apis import ConnectAPI, RequestAPI


class RecastAI():
  def __init__(self, token=None, language=None, proxy=None):
    for api in [ConnectAPI, RequestAPI]:
      setattr(self, api.__name__.strip('API').lower(), api(token=token, language=language, proxy=proxy))
