# coding: utf-8

import requests

from .utils import Utils
from .dialog_conversation import DialogConversation
from .dialog_response import DialogResponse

from ..errors import SapcaiError


class Build:
  def __init__(self, token=None, language=None, proxy=None):
    self.token = token
    self.proxy = proxy
    self.language = language

  def headers(self):
    return {'Authorization': 'Token {}'.format(self.token)}

  def token_required(func):
    def wrapper(self, *args, **kwargs):
      if self.token is None:
        raise ValueError('Token must be set')
      return func(self, *args, **kwargs)
    return wrapper

  @token_required
  def dialog(self, msg, conversation_id, language=None, **options):

    log_level = "info" if options.get('log_level') is None else options.get('log_level')
    proxy = {} if options.get('proxy') is None else options.get('proxy')

    if language is None:
      language = self.language

    params = {'message': msg, 'conversation_id': conversation_id, 'log_level': log_level}
    if options.get('memory'):
      params['memory'] = options['memory']

    if language is not None:
      params['language'] = language

    response = requests.post('{}/dialog'.format(Utils.BUILD_ENDPOINT), json=params, headers=self.headers(), proxies=proxy)
    if response.status_code != requests.codes.ok:
      raise SapcaiError(response.json().get('message'))
    json = response.json()['results']
    return DialogResponse(json['messages'], json['conversation'], json['nlp'], json['logs'])

  @token_required
  def update_conversation(self, user, bot, version, conversation_id, opts):
    if 'memory' in opts and type(opts['memory']) is not dict:
      raise ValueError('Memory parameter must be a dict')
    url = '{}/users/{}/bots/{}/versions/{}/builder/conversation_states/{}'.format(Utils.BUILD_ENDPOINT, user, bot, version, conversation_id)
    response = requests.put(url, json=opts, headers=self.headers())
    if response.status_code != requests.codes.ok:
      raise SapcaiError(response.json().get('message'))
    return DialogConversation(response.json()['results'])

  @token_required
  def delete_conversation(self, user, bot, version, conversation_id):
    url = '{}/users/{}/bots/{}/versions/{}/builder/conversation_states/{}'.format(Utils.BUILD_ENDPOINT, user, bot, version, conversation_id)
    response = requests.delete(url, headers=self.headers())
    if response.status_code != requests.codes.no_content:
      raise SapcaiError(response.json().get('message'))
    return True

  @token_required
  def get_conversation(self, user, bot, version, conversation_id):
    url = '{}/users/{}/bots/{}/versions/{}/builder/conversation_states/{}'.format(Utils.BUILD_ENDPOINT, user, bot, version, conversation_id)
    response = requests.get(url, headers=self.headers())
    if response.status_code != requests.codes.ok:
      raise SapcaiError(response.json().get('message'))
    return DialogConversation(response.json()['results'])
