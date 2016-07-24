# coding: utf-8

from recastai import Intent


class TestSentence(object):
  def test_instanciable(self):
    Intent({'name': 'weather', 'confidence': 0.67})

  def test_attributes(self):
    intent = Intent({'name': 'weather', 'confidence': 0.67})

    assert(intent.name == 'weather')
    assert(intent.confidence == 0.67)
