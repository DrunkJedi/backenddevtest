# -*- coding: utf-8 -*-
import uuid
import hmac
from hashlib import sha1
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Token(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    user = models.OneToOneField(User,
                                related_name='auth_token_user', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expires = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        if not self.expires:
            now = timezone.now()
            self.expires = now + timezone.timedelta(minutes=40)
        return super(Token, self).save(*args, **kwargs)

    def generate_key(self):
        unique = uuid.uuid4()
        return hmac.new(unique.bytes, digestmod=sha1).hexdigest()

    def __unicode__(self):
        return self.key