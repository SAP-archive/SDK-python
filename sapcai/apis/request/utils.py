# coding: utf-8


class Utils():
  """Endpoints"""
  REQUEST_ENDPOINT = 'https://api.cai.tools.sap/v2/request'
  CONVERSE_ENDPOINT = 'https://api.cai.tools.sap/v2/converse'

  """Act constants"""
  ACT_ASSERT = 'assert'
  ACT_COMMAND = 'command'
  ACT_WH_QUERY = 'wh-query'
  ACT_YN_QUERY = 'yn-query'

  """Type constants"""
  TYPE_ABBREVIATION = 'abbr:'
  TYPE_ENTITY = 'enty:'
  TYPE_DESCRIPTION = 'desc:'
  TYPE_HUMAN = 'hum:'
  TYPE_LOCATION = 'loc:'
  TYPE_NUMBER = 'num:'

  """Sentiment constants"""
  SENTIMENT_VPOSITIVE = 'vpositive'
  SENTIMENT_POSITIVE = 'positive'
  SENTIMENT_NEUTRAL = 'neutral'
  SENTIMENT_NEGATIVE = 'negative'
  SENTIMENT_VNEGATIVE = 'vnegative'
