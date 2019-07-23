# Generated by Django 2.2.3 on 2019-07-23 10:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0003_auto_20190723_0018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='name',
        ),
        migrations.AddField(
            model_name='character',
            name='career_level',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='character',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation date'),
        ),
        migrations.AddField(
            model_name='player',
            name='first_name',
            field=models.CharField(default='Paweł', max_length=50, verbose_name='First name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Join date'),
        ),
        migrations.AddField(
            model_name='player',
            name='last_name',
            field=models.CharField(default='Grabinski', max_length=50, verbose_name='Last name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='nickname',
            field=models.CharField(default='Raroog', max_length=50, verbose_name='Nickname'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='character',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history.Player', verbose_name='Player'),
        ),
        migrations.AlterField(
            model_name='player',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='session',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='session',
            name='xp_for_all',
            field=models.IntegerField(default=0, verbose_name='Experience for all players'),
        ),
    ]