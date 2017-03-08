# coding: utf-8

from recastai import RecastError


class TestRecastError(object):
  def test_instanciable(self):
    RecastError('error')

  def test_message(self):
    e = RecastError('error')

    assert(str(e) == 'error')
