# coding: utf-8

import io
import requests

from .models import Response
from .utils import Utils

from ..errors import RecastError


class Analyse():
  def analyse_text(self, text, token=None, language=None):
    token = token or self.token
    if token is None:
      raise RecastError("Token is missing")

    language = language or self.language

    # Build the body
    body = {'text': text}
    if language is not None:
      body['language'] = language

    response = requests.post(
      Utils.REQUEST_ENDPOINT,
      json=body,
      headers={'Authorization': "Token {}".format(token)}
    )
    if response.status_code != requests.codes.ok:
      raise RecastError(response.json()['message'])

    return Response(response)

  def analyse_file(self, filename, token=None, language=None):
    token = token or self.token
    if token is None:
      raise RecastError("Token is missing")

    language = language or self.language

    filename = open(filename, 'rb') if not isinstance(filename, io.IOBase) else filename

    # Build the body
    body = {'voice': filename}
    if language is not None:
      body['language'] = language

    response = requests.post(
      Utils.REQUEST_ENDPOINT,
      files=body,
      headers={'Authorization': "Token {}".format(token)}
    )
    if response.status_code != requests.codes.ok:
      raise RecastError(response.json()['message'])

    return Response(response)
