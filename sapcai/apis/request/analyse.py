# coding: utf-8

import io
import requests

from .models import Response
from .utils import Utils

from ..errors import SapcaiError


class Analyse():
  def analyse_text(self, text, token=None, language=None):
    token = token or self.token
    if token is None:
      raise SapcaiError("Token is missing")

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
      raise SapcaiError(response.json().get('message', ''))

    return Response(response.json()['results'])
