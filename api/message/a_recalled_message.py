# coding: utf8

from rust.core.business import ParamObject
from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.exceptions import BusinessError

from business.message.message_repository import MessageRepository
from business.message.recall_service import RecallService


@Resource('message.message')
class ARecalledMessage(ApiResource):
	"""
	撤回的消息
	"""
	@param_required(['user', 'id'])
	def put(self):
		"""
		撤回消息(限本人操作)
		"""
		user = self.params['user']
		message = MessageRepository(user).get_message_by_id(self.params['id'])
		if message.source_user_id != user.id:
			raise BusinessError(u'操作无权限')

		param_object = ParamObject({
			'id': self.params['message_id']
		})
		RecallService(user).recall(param_object)
		return {}
