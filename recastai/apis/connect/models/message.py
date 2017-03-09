# coding: utf-8

import requests

from ..utils import Utils

from ...errors import RecastError

class Message():
  def __init__(self, response, token):
    self.token = token

    self.raw = response.text

    response = response.json()

    for k, v in response.items():
      setattr(self, k, v)

    self.content = response['message']['attachement']['content']
    self.type = response['message']['attachement']['type']
    self.conversation_id = response['message']['conversation_id']
    self.replies = []

  def add_reply(self, reply):
    self.replies.append(reply)

  def reply(self, replies=[]):
    if type(replies) is str or type(replies) is bytes:
      replies = [replies]

    response = requests.post(
      Utils.CONVERSATION_ENDPOINT + self.conversation_id + '/messages',
      json={'messages': self.replies + replies},
      headers={'Authorization': "Token {}".format(token)}
    )
    if response.status_code != requests.codes.ok:
      raise RecastError(response.reason)

    return response
