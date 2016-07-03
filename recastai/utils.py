# -*- coding: utf-8 -*-


class Utils(object):
  """Versioning"""
  MAJOR = '1'
  MINOR = '0'
  MICRO = '11'
  VERSION = "{0}.{1}.{2}".format(MAJOR, MINOR, MICRO)

  """Endpoints"""
  API_ENDPOINT = 'https://api.recast.ai/v1/request'
  WS_ENDPOINT = 'wss://api.recast.ai/v1/request'
