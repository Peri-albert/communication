# coding: utf8

from rust.core.business import ParamObject
from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.paginator import TargetPage

from business.message.message_repository import MessageRepository
from business.message.encode_message_service import EncodeMessageService


@Resource('message.old_messages')
class AOldMessages(ApiResource):
	"""
	旧消息列表
	"""
	@param_required(['user', 'source_user_id', '?page:int', '?count_per_page:int', '?filters:json'])
	def get(self):
		"""
		获取历史消息
		"""
		user = self.params['user']
		filters = self.params.get('filters')
		target_page = TargetPage(self.params)
		param_object = ParamObject({
			'source_user_id': self.params['source_user_id'],
			'target_user_id': self.params['target_user_id'],
			'content': self.param['content']
		})
		messages = MessageRepository(user).get_unread_messages(param_object, filters, target_page)

		return {
			'messages': [EncodeMessageService(user).encode(message) for message in messages],
			'page_info': target_page.to_dict() if target_page else {}
		}