# coding: utf-8

from .intent import Intent
from .entity import Entity

from ..utils import Utils

import json


class Response():
  def __init__(self, response):
    self.raw = json.dumps({'results': response})
    self.uuid = response['uuid']
    self.source = response['source']
    self.intents = [Intent(i) for i in response['intents']]
    self.act = response['act']
    self.type = response['type']
    self.sentiment = response['sentiment']
    self.entities = [Entity(n, ee) for n, e in response['entities'].items() for ee in e]
    self.language = response['language']
    self.processing_language = response['processing_language']
    self.version = response['version']
    self.timestamp = response['timestamp']
    self.status = response['status']

  @property
  def intent(self):
    try:
      return self.intents[0]
    except IndexError:
      return None

  def get(self, name):
    for entity in self.entities:
      if (entity.name.lower() == name.lower()):
        return entity

  def all(self, name):
    entities = []

    for entity in self.entities:
      if (entity.name.lower() == name.lower()):
        entities.append(entity)

    return entities

  @property
  def is_assert(self):
    return self.act == Utils.ACT_ASSERT

  @property
  def is_command(self):
    return self.act == Utils.ACT_COMMAND

  @property
  def is_wh_query(self):
    return self.act == Utils.ACT_WH_QUERY

  @property
  def is_yn_query(self):
    return self.act == Utils.ACT_YN_QUERY

  @property
  def is_abbreviation(self):
    return Utils.TYPE_ABBREVIATION in self.type

  @property
  def is_entity(self):
    return Utils.TYPE_ENTITY in self.type

  @property
  def is_description(self):
    return Utils.TYPE_DESCRIPTION in self.type

  @property
  def is_human(self):
    return Utils.TYPE_HUMAN in self.type

  @property
  def is_location(self):
    return Utils.TYPE_LOCATION in self.type

  @property
  def is_number(self):
    return Utils.TYPE_NUMBER in self.type

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
