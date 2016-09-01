# coding: utf-8

import io
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
  def text_request(self, text, token=None, language=None, endpoint=None):
    token = token or self.token
    if token is None:
      raise RecastError("Token is missing")

    language = language or self.language
    endpoint = endpoint or Utils.API_ENDPOINT

    body = { 'text': text }
    if language is not None:
      body['language'] = language

    response = requests.post(endpoint,
                             params=body,
                             headers={'Authorization': "Token {}".format(token)})
    if response.status_code != requests.codes.ok:
      raise RecastError(response.reason)

    return Response(response.text)

  """
  Perform a file request to Recast.AI
  """
  def file_request(self, filename, token=None, language=None, endpoint=None):
    token = token or self.token
    if token is None:
      raise RecastError("Token is missing")

    language = language or self.language
    endpoint = endpoint or Utils.API_ENDPOINT

    filename = open(filename, 'rb') if not isinstance(filename, io.IOBase) else filename
    body = { 'voice': filename }
    if language is not None:
      body['language'] = language

    response = requests.post(endpoint,
                             files=body,
                             headers={ 'Authorization': "Token {}".format(token) })
    if response.status_code != requests.codes.ok:
      raise RecastError(response.reason)

    return Response(response.text)
