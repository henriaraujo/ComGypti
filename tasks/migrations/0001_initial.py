# Generated by Django 2.2.5 on 2019-10-25 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institutions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agentUsernameDesignation', models.CharField(max_length=12)),
                ('public_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.PublicEntity')),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutions.PublicEntity')),
            ],
        ),
    ]
