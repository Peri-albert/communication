# coding: utf8

from rust.core import business

from business.message.message import Message
from db.message import models as message_models


class MessageFactory(business.Service):

	def create(self, param_object):

		db_model = message_models.Message.create(
			source_user_id = param_object.source_user_id,
			target_user_id=param_object.target_user_id,
			content=param_object.source_user_id
		)

		return Message(db_model)

