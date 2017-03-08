# coding: utf-8

from recastai import Intent


class TestIntent(object):
  def test_instanciable(self):
    Intent({'slug': 'weather', 'confidence': 0.67})

  def test_attributes(self):
    intent = Intent({'slug': 'weather', 'confidence': 0.67})

    assert(intent.slug == 'weather')
    assert(intent.confidence == 0.67)
