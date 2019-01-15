# coding: utf-8

import requests

from .action import Action
from .intent import Intent
from .entity import Entity

from ..utils import Utils

from ...errors import SapcaiError


class Conversation():
  def __init__(self, response, token):
    self.token = token

    self.raw = response.text

    response = response.json()
    response = response['results']

    self.uuid = response['uuid']
    self.source = response['source']
    self.replies = response['replies']
    self.action = Action(response['action']) if response['action'] else None
    self.next_actions = [Action(a) for a in response['next_actions']]
    self.memory = [Entity(n, e) for n, e in response['memory'].items() if e]
    self.sentiment = response['sentiment']
    self.entities = [Entity(n, ee) for n, e in response['entities'].items() for ee in e]
    self.intents = [Intent(i) for i in response['intents']]
    self.conversation_token = response['conversation_token']
    self.language = response['language']
    self.processing_language = response['processing_language']
    self.version = response['version']
    self.timestamp = response['timestamp']
    self.status = response['status']

  @property
  def reply(self):
    try:
      return self.replies[0]
    except IndexError:
      return None

  @property
  def next_action(self):
    try:
      return self.next_actions[0]
    except IndexError:
      return None

  def joined_replies(self, sep=' '):
    return sep.join(self.replies)

  def get_memory(self, key=None):
    if key is None:
      return self.memory

    for entity in self.memory:
      if (entity.name.lower() == key.lower()):
        return entity

    return None

  @property
  def intent(self):
    try:
      return self.intents[0]
    except IndexError:
      return None

  @property
  def is_vpositive(self):
    return self.sentiment == Utils.SENTIMENT_VPOSITIVE

  @property
  def is_positive(self):
    return self.sentiment == Utils.SENTIMENT_POSITIVE

  @property
  def is_neutral(self):
    return self.sentiment == Utils.SENTIMENT_NEUTRAL

  @property
  def is_negative(self):
    return self.sentiment == Utils.SENTIMENT_NEGATIVE

  @property
  def is_vnegative(self):
    return self.sentiment == Utils.SENTIMENT_VNEGATIVE

  def set_memory(self, memory):
    body = {'conversation_token': self.conversation_token, 'memory': memory}
    response = requests.put(
      Utils.CONVERSE_ENDPOINT,
      json=body,
      headers={'Authorization': "Token {}".format(self.token)}
    )
    if response.status_code != requests.codes.ok:
      raise SapcaiError(response.json().get('message', ''))

    response = response.json()
    response = response['results']
    return [Entity(n, e) for n, e in response['memory'].items() if e]

  def reset_memory(self, key=None):
    body = {'conversation_token': self.conversation_token}
    if key:
      body['memory'] = {key: None}
    response = requests.put(
      Utils.CONVERSE_ENDPOINT,
      json=body,
      headers={'Authorization': "Token {}".format(self.token)}
    )
    if response.status_code != requests.codes.ok:
      raise SapcaiError(response.json().get('message', ''))

    response = response.json()
    response = response['results']
    return [Entity(n, e) for n, e in response['memory'].items() if e]

  def reset_conversation(self):
    body = {'conversation_token': self.conversation_token}
    response = requests.delete(
      Utils.CONVERSE_ENDPOINT,
      json=body,
      headers={'Authorization': "Token {}".format(self.token)}
    )
    if response.status_code != requests.codes.ok:
      raise SapcaiError(response.json().get('message', ''))

    response = response.json()
    response = response['results']
    return [Entity(n, e) for n, e in response['memory'].items() if e]
