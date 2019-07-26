# Generated by Django 2.2.3 on 2019-07-25 22:54

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation date')),
                ('story', models.CharField(default='Once upon a time...', max_length=5000)),
                ('career_path', models.CharField(max_length=50)),
                ('career_level', models.PositiveIntegerField(default=1)),
                ('total_xp', models.IntegerField(default=0)),
                ('spent_xp', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('join_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Join date')),
                ('nickname', models.CharField(max_length=50, verbose_name='Nickname')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('game_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date played')),
                ('description', models.CharField(max_length=2000)),
                ('xp_for_all', models.IntegerField(default=0, verbose_name='Experience for all players')),
                ('characters', models.ManyToManyField(related_name='characters', to='history.Character')),
                ('game_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history.Player')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history.Player', verbose_name='Player'),
        ),
    ]
