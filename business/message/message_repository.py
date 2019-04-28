# coding: utf8

from rust.core import business

from business.message.message import Message

from db.message import models as message_models


class MessageRepository(business.Service):

	def get_message_by_id(self, message_id):
		db_model = message_models.Message.select().dj_where(id=message_id, is_recalled=False).first()
		if db_model:
			return Message(db_model)
		
	def get_read_messages(self, param_object, filters=None, target_page=None):
		db_models = message_models.Message.select().dj_where(
			source_user_id=param_object.source_user_id,
			target_user_id=param_object.target_user_id,
			tag=message_models.TAG['OLD'],
			is_recalled=False
		)
		if filters:
			db_models = db_models.dj_where(**filters)

		if target_page:
			db_models = target_page.paginate(db_models)

		db_models = db_models.order_by('-id')
		return [Message(db_model) for db_model in db_models]
		
	def get_unread_messages(self, param_object, filters=None, target_page=None):
		db_models = message_models.Message.select().dj_where(
			source_user_id=param_object.source_user_id,
			target_user_id=param_object.target_user_id,
			tag=message_models.TAG['NEW'],
			is_recalled=False
		)
		if filters:
			db_models = db_models.dj_where(**filters)

		if target_page:
			db_models = target_page.paginate(db_models)

		db_models = db_models.order_by('id')
		return [Message(db_model) for db_model in db_models]

