# coding: utf-8

import io
import requests

from .models import Conversation
from .utils import Utils

from ..errors import RecastError


class Converse():
  def converse_text(self, text, token=None, language=None, conversation_token=None, memory=None):
    token = token or self.token
    if token is None:
      raise RecastError("Token is missing")

    language = language or self.language

    # Build the body
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
      raise RecastError(response.json()['message'])

    return Conversation(response, token)

  def converse_file(self, filename, token=None, language=None, conversation_token=None, memory=None):
    token = token or self.token
    if token is None:
      raise RecastError("Token is missing")

    language = language or self.language

    filename = open(filename, 'rb') if not isinstance(filename, io.IOBase) else filename

    # Build the body
    body = {'voice': filename}
    if language is not None:
      body['language'] = language
    if conversation_token is not None:
      body['conversation_token'] = conversation_token
    if memory is not None:
      body['memory'] = memory

    response = requests.post(
      Utils.CONVERSE_ENDPOINT,
      files=body,
      headers={'Authorization': "Token {}".format(token)}
    )
    if response.status_code != requests.codes.ok:
      raise RecastError(response.json()['message'])

    return Conversation(response)
