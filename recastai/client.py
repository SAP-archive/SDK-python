# -*- coding: utf-8 -*-

import requests

from .response import Response
from .errors import RecastError
from .utils import Utils


class Client(object):
  def __init__(self, token=None, language=None):
    self.token = token
    self.language = language

  """
  Perform a text request to Recast.AI
  """
  def text_request(self, text, **options):
    token = options.get('token') or self.token
    if token is None:
      raise RecastError("Token is missing")

    language = options.get('language') or self.language

    body = {'text': text}
    if language is not None:
      body['language'] = language

    response = requests.post(Utils.API_ENDPOINT,
                             params=body,
                             headers={'Authorization': "Token " + token})
    if response.status_code != requests.codes.ok:
      raise RecastError(response.reason)

    return Response(response.text)

  """
  Perform a text request to Recast.AI
  """
  def file_request(self, file, **options):
    token = options.get('token') or self.token
    if token is None:
      raise RecastError("Token is missing")

    language = options.get('language') or self.language

    file = open(file, 'rb') if (type(file) is str) else file
    body = {'voice': file}
    if language is not None:
      body['language'] = language

    response = requests.post(Utils.API_ENDPOINT,
                             files=body,
                             headers={'Authorization': "Token " + token})
    if response.status_code != requests.codes.ok:
      raise RecastError(response.reason)

    return Response(response.text)
