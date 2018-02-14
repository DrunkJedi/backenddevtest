from django.db import models


class Answer(models.Model):
    CAN_VIEW = 'can_view_answer'
    CAN_DELETE = 'can_delete_answer'
    CAN_UPDATE = 'can_change_answer'

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    count = models.IntegerField(choices=((1, ("Single")),
                                         (2, ("Pair"))),
                                default=1)
    drink = models.CharField(max_length=50)

    class Meta:
        permissions = (
            ('can_view_answer', 'Can view answer'),
            ('can_delete_answer', 'Can delete answer'),
            ('can_change_answer', 'Can change answer'),
        )
