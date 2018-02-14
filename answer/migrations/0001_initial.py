# Generated by Django 2.0 on 2018-02-11 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('count', models.IntegerField(choices=[(1, 'Single'), (2, 'Pair')], default=1)),
                ('drink', models.CharField(max_length=50)),
            ],
            options={
                'permissions': (('can_view_answer', 'Can view answer'), ('can_delete_answer', 'Can delete answer'), ('can_change_answer', 'Can change answer')),
            },
        ),
    ]