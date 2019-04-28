# coding: utf8

from rust.core import business

from db.message import models as message_models


class ReadService(business.Service):
	"""
	阅读服务
	"""
	def read(self, messages):
		"""
		阅读
		"""
		message_ids = []
		for message in messages:
			message_ids.append(message.id)

		message_models.Message.update(
			tag = message_models.TAG['OLD']
		).dj_where(id__in=message_ids).execute()
