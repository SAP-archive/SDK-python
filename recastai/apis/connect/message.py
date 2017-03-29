# coding: utf-8

import requests

from .models import Message as Msg
from .utils import Utils

from ..errors import RecastError


class Message():
  def parse_message(self, request):
    return Msg(request.get_data())

  def send_message(self, payload, conversation_id, token=None):
    token = token or self.token
    if token is None:
      raise RecastError("Token is missing")

    response = requests.post(
      Utils.CONVERSATION_ENDPOINT + conversation_id + '/messages',
      json={'messages': payload},
      headers={'Authorization': "Token {}".format(token)}
    )
    if response.status_code != requests.codes.created:
      raise RecastError(response.json()['message'])

    return response

  def broadcast_message(self, payload, token=None):
    token = token or self.token
    if token is None:
      raise RecastError("Token is missing")

    response = requests.post(
      Utils.MESSAGE_ENDPOINT,
      json={'messages': payload},
      headers={'Authorization': "Token {}".format(token)}
    )
    if response.status_code != requests.codes.created:
      raise RecastError(response.json()['message'])

    return response
