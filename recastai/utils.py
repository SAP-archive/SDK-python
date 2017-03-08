# coding: utf-8


class Utils():
  """Versioning"""
  MAJOR = '3'
  MINOR = '0'
  MICRO = '0'
  VERSION = "%s.%s.%s" % (MAJOR, MINOR, MICRO)

  """Endpoints"""
  TRAIN_ENDPOINT = 'https://api.recast.ai/v2/'
  CONNECT_ENDPOINT = 'https://api.recast.ai/connect/v1/'
  HOST_ENDPOINT = 'https://api.recast.ai/host/v1/'
  REQUEST_ENDPOINT = 'https://api.recast.ai/v2/'
  MONITOR_ENDPOINT = 'https://api.recast.ai/monitor/v1/'
