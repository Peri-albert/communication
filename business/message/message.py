# coding: utf8

from rust.core import business

from db.message import models as message_models


class Message(business.Model):
	"""
	消息
	"""
	__slots__ = (
		'id',
		'content',
		'is_recalled'
	)

	def __init__(self, db_model=None):
		super(Message, self).__init__(db_model)

	@property
	def source_user_id(self):
		return self.context['db_model'].source_user_id

	@property
	def target_user_id(self):
		return self.context['db_model'].target_user_id

	@property
	def tag(self):
		return message_models.TAG2TEXT[self.context['db_model'].tag]
