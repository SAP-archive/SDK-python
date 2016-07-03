# -*- coding: utf-8 -*-

from .client import Client
from .response import Response
from .sentence import Sentence
from .entity import Entity
from .utils import Utils
from .errors import RecastError


__title__ = 'recastai'
__author__ = 'Paul Renvoisé'
__version__ = Utils.VERSION
__license__ = 'MIT'
__copyright__ = 'Copyright 2016 Recast.AI'

__all__ = ['Client', 'Response', 'Sentence', 'Entity', 'Utils', 'RecastError']
