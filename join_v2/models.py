from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import *
from django.utils.translation import ugettext_lazy as _

# class Todolist(models.Model):
# 	"""docstring for Todolist"""
	
# 	uuid = models.AutoField(primary_key=True)
# 	name = models.CharField(max_length=200, unique=True)
# 	user = models.ForeignKey(User)
# 	created_on = models.DateTimeField(default=timezone.now)

# class Tasks(models.Model):
# 	"""docstring for Tasks"""
	
# 	uuid = models.AutoField(primary_key=True)
# 	name = models.CharField(max_length=200, unique=True)
# 	owner = models.ForeignKey(User, related_name='u')
# 	assigned_to = models.ForeignKey(User, related_name='o')
# 	created_on = models.DateTimeField(default=timezone.now)
# 	is_resolved = models.BooleanField(_(u'Resolved?'), default=False)
# 	todo = models.ForeignKey(Todolist)




class Todo(models.Model):
	user = models.ForeignKey(User, related_name='u')
	todo = models.CharField(max_length=50)
	flag = models.CharField(max_length=2, default='1')
	priority = models.CharField(max_length=2, default='0')
	pubtime = models.DateTimeField(auto_now_add=True)
	# assigned_to = models.ForeignKey(User, related_name='a')

	def __unicode__(self):
		return u'%d %s %s' % (self.id, self.todo, self.flag)

	class Meta:
		ordering = ['priority', 'pubtime']