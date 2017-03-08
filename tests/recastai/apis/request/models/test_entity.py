# coding: utf-8

from recastai import Entity


class TestEntity(object):
  def test_instanciable(self):
    Entity('location', {'formatted': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London', 'confidence': 0.97})

  def test_attributes(self):
    entity = Entity('location', {'formatted': 'London, London, Greater London, England, United Kingdom', 'lat': 51.5073509, 'lng': -0.1277583, 'raw': 'London', 'confidence': 0.97})

    assert(entity.name == 'location')
    assert(entity.formatted == 'London, London, Greater London, England, United Kingdom')
    assert(entity.lat == 51.5073509)
    assert(entity.lng == -0.1277583)
    assert(entity.raw == 'London')
    assert(entity.confidence == 0.97)
