# coding: utf8

from rust.core import db as models

TAG = {
	'NEW': 0,
	'OLD': 1
}

TAG2TEXT = {
	TAG['NEW']: 'new',
	TAG['OLD']: 'old'
}


class Message(models.Model):
	"""
	注释
	"""
	source_user_id = models.IntegerField(default=0)  # 来源用户id
	target_user_id = models.IntegerField(default=0)  # 目标用户id
	content = models.TextField(default='')  # 消息内容
	tag = models.IntegerField(default=0)  # 标签(新/旧)
	is_recalled = models.BooleanField(default=False)  # 是否撤回

	class Meta(object):
		table_name = 'message_message'
