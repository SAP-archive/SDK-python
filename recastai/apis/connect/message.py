# coding: utf-8

import requests

from .models import Message as Msg
from .utils import Utils

from ..errors import RecastError


class Message():
  def parse_message(self, request):
    return Msg(request.body, self.token)

  def send_message(self, payload, conversation_id):
    response = requests.post(
      Utils.CONVERSATION_ENDPOINT + conversation_id + '/messages',
      json=payload, # Is this ok?
      headers={'Authorization': "Token {}".format(token)}
    )
    if response.status_code != requests.codes.ok:
      raise RecastError(response.reason)

    return response

  def broadcast_message(self, payload):
    response = requests.post(
      Utils.MESSAGE_ENDPOINT,
      json=payload, # TODO: is this ok?
      headers={'Authorization': "Token {}".format(token)}
    )
    if response.status_code != requests.codes.ok:
      raise RecastError(response.reason)

    return response
