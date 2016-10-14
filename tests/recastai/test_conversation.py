# coding: utf-8

import json
from recastai import Conversation
from recastai import Action
from recastai import Intent
from recastai import Entity


class TestConversation(object):
  def test_instanciable(self):
    Conversation(json.dumps({'results': {'uuid': 'db4837b0-8359-4505-9678-c4081a6f2ad8', 'source': 'What is the weather in Paris ?', 'replies': ['Do you already have an account?', 'This is a test?'], 'action': {'slug': 'murder', 'done': False, 'reply': 'do you already have an account?'}, 'next_actions': [{'slug': 'test', 'done': False, 'reply': 'This is a test?'}], 'memory':{'victim': None, 'client': None, 'mail-client': None, 'lieu': {'lat': 0.54, 'lng': 0.435}}, 'entities': {}, 'intents': [], 'conversation_token': '8641d38b059cde2826e3cdf2f9b00725', 'language': 'en', 'version': '2.0.0', 'timestamp': '2016-10-04T15:26:11.876Z', 'status': 200}, 'message': 'Converses rendered with success'}))

  def test_attributes(self):
    conversation = Conversation(json.dumps({'results': {'uuid': 'db4837b0-8359-4505-9678-c4081a6f2ad8', 'source': 'What is the weather in Paris ?', 'replies': ['Do you already have an account?', 'This is a test?'], 'action': {'slug': 'murder', 'done': False, 'reply': 'do you already have an account?'}, 'next_actions': [{'slug': 'test', 'done': False, 'reply': 'This is a test?'}], 'memory':{'victim': None, 'client': None, 'mail-client': None, 'lieu': {'lat': 0.54, 'lng': 0.435}}, 'entities': {}, 'intents': [], 'conversation_token': '8641d38b059cde2826e3cdf2f9b00725', 'language': 'en', 'version': '2.0.0', 'timestamp': '2016-10-04T15:26:11.876Z', 'status': 200}, 'message': 'Converses rendered with success'}))

    assert(conversation.raw == json.dumps({'results': {'uuid': 'db4837b0-8359-4505-9678-c4081a6f2ad8', 'source': 'What is the weather in Paris ?', 'replies': ['Do you already have an account?', 'This is a test?'], 'action': {'slug': 'murder', 'done': False, 'reply': 'do you already have an account?'}, 'next_actions': [{'slug': 'test', 'done': False, 'reply': 'This is a test?'}], 'memory':{'victim': None, 'client': None, 'mail-client': None, 'lieu': {'lat': 0.54, 'lng': 0.435}}, 'entities': {}, 'intents': [], 'conversation_token': '8641d38b059cde2826e3cdf2f9b00725', 'language': 'en', 'version': '2.0.0', 'timestamp': '2016-10-04T15:26:11.876Z', 'status': 200}, 'message': 'Converses rendered with success'}))
    assert(conversation.uuid == 'db4837b0-8359-4505-9678-c4081a6f2ad8')
    assert(conversation.source == 'What is the weather in Paris ?')
    assert(type(conversation.replies) is list)
    assert(type(conversation.replies[0]) is str)
    assert(type(conversation.action) is Action)
    assert(type(conversation.next_actions) is list)
    assert(type(conversation.next_actions[0]) is Action)
    assert(type(conversation.memory) is list)
    assert(type(conversation.memory[0]) is Entity)
    assert(type(conversation.entities) is list)
    assert(type(conversation.intents) is list)
    assert(conversation.conversation_token == '8641d38b059cde2826e3cdf2f9b00725')
    assert(conversation.language == 'en')
    assert(conversation.version == '2.0.0')
    assert(conversation.timestamp == '2016-10-04T15:26:11.876Z')
    assert(conversation.status == 200)

  def test_helpers(self):
    conversation = Conversation(json.dumps({'results': {'uuid': 'db4837b0-8359-4505-9678-c4081a6f2ad8', 'source': 'What is the weather in Paris ?', 'replies': ['Do you already have an account?', 'This is a test?'], 'action': {'slug': 'murder', 'done': False, 'reply': 'do you already have an account?'}, 'next_actions': [{'slug': 'test', 'done': False, 'reply': 'This is a test?'}], 'memory':{'victim': None, 'client': None, 'mail-client': None, 'lieu': {'lat': 0.54, 'lng': 0.435}}, 'entities': {}, 'intents': [], 'conversation_token': '8641d38b059cde2826e3cdf2f9b00725', 'language': 'en', 'version': '2.0.0', 'timestamp': '2016-10-04T15:26:11.876Z', 'status': 200}, 'message': 'Converses rendered with success'}))

    assert(conversation.reply() == conversation.replies[0])
    assert(conversation.next_action() == conversation.next_actions[0])
    assert(conversation.joined_replies() == ' '.join(conversation.replies))
    assert(conversation.joined_replies("\n") == "\n".join(conversation.replies))
    assert(conversation.get_memory() == conversation.memory)
    assert(conversation.get_memory('lieu') == [entity for entity in conversation.memory if entity.name.lower() == 'lieu'][0])
    assert(conversation.intent() == None)

  def test_missing(self):
    conversation = Conversation(json.dumps({'results': {'uuid': 'db4837b0-8359-4505-9678-c4081a6f2ad8', 'source': 'What is the weather in Paris ?', 'replies': [], 'action': None, 'next_actions': [], 'memory':{'victim': None, 'client': None, 'mail-client': None, 'lieu': []}, 'entities': {}, 'intents': [], 'conversation_token': '8641d38b059cde2826e3cdf2f9b00725', 'language': 'en', 'version': '2.0.0', 'timestamp': '2016-10-04T15:26:11.876Z', 'status': 200}, 'message': 'Converses rendered with success'}))
    assert(conversation.action is None)
    assert(conversation.reply() is None)
    assert(conversation.intent() is None)
    assert(conversation.next_action() is None)

  def test_static_methods(self):
    assert(getattr(Conversation, 'set_memory') != None)
    assert(getattr(Conversation, 'reset_memory') != None)
    assert(getattr(Conversation, 'reset_conversation') != None)
