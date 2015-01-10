from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from django.core.validators import URLValidator
#from phonenumber_field.modelfields import PhoneNumberField

class MyProfile(UserenaBaseProfile):
	user = models.OneToOneField(User,unique=True,verbose_name=_('user'),related_name='my_profile')
	birth_date = models.DateTimeField(blank=True, null=True)
	address = models.TextField(blank=True, null=True)
	#telephone = models.PhoneNumberField(blank=True)
	about = models.TextField(blank=True, null=True)
	#city = models.TextField(blank=True, null=True)
	#GENDER_CHOICES = (('M', 'Male'),('F', 'Female'))
	#gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	# github = models.TextField(validators=[URLValidator()])
	# facebook = models.TextField(validators=[URLValidator()])
	# twitter = models.TextField(validators=[URLValidator()])
	# googleplus = models.TextField(validators=[URLValidator()])


