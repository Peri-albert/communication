# coding: utf8

from rust.core.business import ParamObject
from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.exceptions import BusinessError

from business.message.message_repository import MessageRepository
from business.message.recall_service import RecallService


@Resource('message.message')
class AMessage(ApiResource):

	@param_required(['user', 'message_id'])
	def put(self):
		user = self.params['user']
		param_object = ParamObject({
			'message_id': self.params['message_id']
		})
		message = MessageRepository(user).get_message_by_id(param_object)
		if message.source_user_id != user.id:
			raise BusinessError(u'操作无权限')

		RecallService(user).recall(param_object)
		return {}