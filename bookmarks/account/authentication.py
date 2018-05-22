from django.contrib.auth.models import User


class EmailAuthBackend(object):
	"""认证通过邮件"""
	def authenticate(self, username=None, password=None):
		try:
			user = User.objects.get(email=username)
			if user.check_password(password):
				return user
			else:
				return None
		except User.DoesNotExist:
			return None

	def get_user(self, name_id):
		try:
			return User.objects.get(pk=name_id)
		except User.DoesNotExist:
			return None
		return None