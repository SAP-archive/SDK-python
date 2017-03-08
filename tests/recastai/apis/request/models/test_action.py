# coding: utf-8

from recastai import Action


class TestAction(object):
  def test_instanciable(self):
    Action({'slug': 'greetings', 'done': True, 'reply': 'Hello there!'})

  def test_attributes(self):
    action = Action({'slug': 'greetings', 'done': True, 'reply': 'Hello there!'})

    assert(action.slug == 'greetings')
    assert(action.done == True)
    assert(action.reply == 'Hello there!')
