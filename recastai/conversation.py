# coding: utf-8

import json
import requests

from .action import Action
from .intent import Intent
from .entity import Entity
from .errors import RecastError
from .utils import Utils

class Conversation(object):
  def __init__(self, response):
    self.raw = response

    response = json.loads(response)
    response = response['results']

    self.uuid = response['uuid']
    self.source = response['source']
    self.replies = response['replies']
    self.action  = Action(response['action'])
    self.next_actions = [Action(a) for a in response['next_actions']]
    self.memory = [Entity(n, e) for n, e in response['memory'].items() if e]
    self.entities = [Entity(n, ee) for n, e in response['entities'].items() for ee in e]
    self.intents = [Intent(i) for i in response['intents']]
    self.conversation_token = response['conversation_token']
    self.language = response['language']
    self.version = response['version']
    self.timestamp = response['timestamp']
    self.status = response['status']

  def reply(self):
    try:
      return self.replies[0]
    except IndexError:
      return None

  def next_action(self):
    try:
      return self.next_actions[0]
    except IndexError:
      return None

  def joined_replies(self, sep=' '):
    return sep.join(self.replies)

  def get_memory(key=None):
    if key == None:
      return self.memory

    return self.memory[key]

  @classmethod
  def set_memory(cls, token, conversation_token, memory):
    body = { 'conversation_token': conversation_token, 'memory': memory }
    response = requests.put(
      Utils.CONVERSE_ENDPOINT,
      json=body,
      headers={'Authorization': "Token {}".format(token)}
    )
    if response.status_code != requests.code.ok:
      raise RecastError.new(response.reason)

    response = json.loads(response)
    response = response['results']
    return [Entity(n, e) for n, e in response['memory'].items() if e]

  @classmethod
  def reset_memory(cls, token, conversation_token, key=None):
    body = {'conversation_token': conversation_token}
    if key:
      body['memory'] = { key: None }
    response = requests.put(
      Utils.CONVERSE_ENDPOINT,
      json=body,
      headers={'Authorization': "Token {}".format(token) }
    )
    if response.status_code != requests.code.ok:
      raise RecastError.new(response.reason)

    response = json.loads(response)
    response = response['results']
    return [Entity(n, e) for n, e in response['memory'].items() if e]

  @classmethod
  def reset_conversation(cls, token, conversation_token):
    body = {'conversation_token': conversation_token}
    response = requests.delete(
      Utils.CONVERSE_ENDPOINT,
      json=body,
      headers={'Authorization': "Token {}".format(token)}
    )
    if response.status_code != requests.code.ok:
      raise RecastError.new(response.reason)

    response = json.loads(response)
    response = response['results']
    return [Entity(n, e) for n, e in response['memory'].items() if e]
