# coding: utf8

from rust.core import business

from db.message import models as message_models


class RecallService(business.Service):
	"""
	撤回服务
	"""
	def recall(self, param_object):
		"""
		撤回
		"""
		message_models.Message.update(
			is_recalled=True
		).dj_where(id=param_object.id).execute()
