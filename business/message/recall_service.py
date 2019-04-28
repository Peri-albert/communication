# coding: utf8

from rust.core import business

from db.message import models as message_models


class RecallService(business.Service):

	def recall(self, param_object):
		message_models.Message.update(
			is_recalled=True
		).dj_where(id=param_object.message_id).execute()