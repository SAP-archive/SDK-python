# -*- coding: utf-8 -*-

from recastai import RecastError


class TestRecastError(object):
  def test_instanciable(self):
    RecastError('error')

  def test_message(self):
    error = RecastError('error')

    assert(error.message == 'error')
