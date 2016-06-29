# -*- coding: utf-8 -*-

from recastai import Entity


class TestEntity(object):
  def test_instanciable(self):
    Entity('entity', {'value': 'value', 'raw': 'raw'})

  def test_attributes(self):
    entity = Entity('entity', {'value': 'value', 'raw': 'raw'})

    assert(entity.name == 'entity')
    assert(entity.value == 'value')
    assert(entity.raw == 'raw')
