from rest_framework import serializers
from guardian.shortcuts import assign_perm, get_objects_for_user
from django.db import transaction
from .models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

    def save(self, **kwargs):
        with transaction.atomic():
            user = self.context['request'].user
            obj = super(AnswerSerializer, self).save(**kwargs)
            assign_perm(Answer.CAN_VIEW, user, obj)
            assign_perm(Answer.CAN_DELETE, user, obj)
            assign_perm(Answer.CAN_UPDATE, user, obj)
            return obj

        return super(AnswerSerializer, self).save(**kwargs)