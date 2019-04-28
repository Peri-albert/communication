# coding: utf8

from rust.core.business import ParamObject
from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required

from business.message.message_factory import MessageFactory


@Resource('message.message')
class AMessage(ApiResource):
	"""
	消息
	"""
	@param_required(['user', 'target_user_id', 'content'])
	def put(self):
		"""
		创建消息
		"""
		user = self.params['user']
		param_object = ParamObject({
			'source_user_id': self.params['source_user_id'],
			'target_user_id': self.params['target_user_id'],
			'content': self.param['content']
		})
		message = MessageFactory(user).create(param_object)
		return {
			'id': message.id
		}

