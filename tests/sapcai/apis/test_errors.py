# coding: utf-8

from sapcai import SapcaiError


class TestSapcaiError(object):
  def test_instanciable(self):
    SapcaiError('error')

  def test_message(self):
    e = SapcaiError('error')

    assert(str(e) == 'error')
