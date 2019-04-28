# coding: utf8

from rust.core import business

class EncodeMessageService(business.Service):
	"""
	封装消息Message数据的服务
	"""
	def encode(self, message):
		data = {
			'id': message.id,
			'source_user_id': message.source_user_id,
			'target_user_id': message.target_user_id,
			'content': message.content,
			'tag': message.tag
		}

		return data