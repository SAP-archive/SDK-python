# coding: utf-8

import requests

from .models import Message as Model
from .utils import Utils

from ..errors import SapcaiError


class Message():
  def parse_message(self, request):
    return Model(request.get_data())

  def send_message(self, messages, conversation_id, token=None):
    token = token or self.token
    if token is None:
      raise SapcaiError("Token is missing")

    url = Utils.CONVERSATION_ENDPOINT % (conversation_id) + '/messages'
    response = requests.post(
      url,
      json={'messages': messages},
      headers={'Authorization': "Token {}".format(token)}
    )
    if response.status_code != requests.codes.created:
      raise SapcaiError(response.json().get('message'))

    return response

  def broadcast_message(self, messages, token=None):
    token = token or self.token
    if token is None:
      raise SapcaiError("Token is missing")

    url = Utils.MESSAGE_ENDPOINT % ('')
    response = requests.post(
      url,
      json={'messages': messages},
      headers={'Authorization': "Token {}".format(token)}
    )
    if response.status_code != requests.codes.created:
      raise SapcaiError(response.json().get('message'))

    return response
