# coding: utf-8

import io
import requests

from .response import Response
from .conversation import Conversation
from .errors import RecastError
from .utils import Utils


class Client(object):
  def __init__(self, token=None, language=None):
    self.token = token
    self.language = language

  """
  Perform a text converse to Recast.AI
  """
  def text_converse(self, text, token=None, language=None, conversation_token=None, memory=None):
    token = token or self.token
    if token is None:
      raise RecastError("Token is missing")

    language = language or self.language

    body = {'text': text}
    if language is not None:
      body['language'] = language
    if conversation_token is not None:
      body['conversation_token'] = conversation_token
    if memory is not None:
      body['memory'] = memory

    response = requests.post(
      Utils.CONVERSE_ENDPOINT,
      json=body,
      headers={'Authorization': "Token {}".format(token)}
    )
    if response.status_code != requests.codes.ok:
      raise RecastError(response.reason)

    return Conversation(response.text)

  """
  Perform a text request to Recast.AI
  """
  def text_request(self, text, token=None, language=None):
    token = token or self.token
    if token is None:
      raise RecastError("Token is missing")

    language = language or self.language

    body = {'text': text}
    if language is not None:
      body['language'] = language

    response = requests.post(
      Utils.REQUEST_ENDPOINT,
      json=body,
      headers={'Authorization': "Token {}".format(token)}
    )
    if response.status_code != requests.codes.ok:
      raise RecastError(response.reason)

    return Response(response.text)

  """
  Perform a file request to Recast.AI
  """
  def file_request(self, filename, token=None, language=None):
    token = token or self.token
    if token is None:
      raise RecastError("Token is missing")

    language = language or self.language

    filename = open(filename, 'rb') if not isinstance(filename, io.IOBase) else filename
    body = { 'voice': filename }
    if language is not None:
      body['language'] = language

    response = requests.post(
      Utils.REQUEST_ENDPOINT,
      files=body,
      headers={'Authorization': "Token {}".format(token)}
    )
    if response.status_code != requests.codes.ok:
      raise RecastError(response.reason)

    return Response(response.text)
