# coding: utf-8


class Utils(object):
  """Versioning"""
  MAJOR = '2'
  MINOR = '0'
  MICRO = '12'
  VERSION = "{0}.{1}.{2}".format(MAJOR, MINOR, MICRO)

  """Endpoints"""
  API_ENDPOINT = 'https://api.recast.ai/v2/request'
  WS_ENDPOINT = 'wss://api.recast.ai/v2/request'

  """Act constants"""
  ACT_ASSERT = 'assert'
  ACT_COMMAND = 'command'
  ACT_WH_QUERY = 'wh-query'
  ACT_YN_QUERY = 'yn-query'

  """Sentiment constants"""
  SENTIMENT_POSITIVE = 'positive'
  SENTIMENT_NEUTRAL = 'neutral'
  SENTIMENT_NEGATIVE = 'negative'
