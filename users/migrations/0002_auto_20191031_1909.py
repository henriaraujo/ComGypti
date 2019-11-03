# Generated by Django 2.2.5 on 2019-10-31 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('users.user',),
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_agent',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_doctor',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_responsible',
        ),
    ]
