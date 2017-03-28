# coding: utf-8

import json
import requests

from ..utils import Utils

from ...errors import RecastError

class Message():
  def __init__(self, request):
    request = json.loads(request)
    for k, v in request.items():
      setattr(self, k, v)

    self.conversation_id = request['message']['conversation']
    self.content = request['message']['attachment']['content']
    self.type = request['message']['attachment']['type']
