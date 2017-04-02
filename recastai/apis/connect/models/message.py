# coding: utf-8

import re
import json


class Message():
  def __init__(self, request):
    request = json.loads(request)
    for k, v in request.items():
      setattr(self, re.sub('(?!^)([A-Z])', r'_\1', k).lower(), v)

    self.conversation_id = request['message']['conversation']
    self.content = request['message']['attachment']['content']
    self.type = request['message']['attachment']['type']
