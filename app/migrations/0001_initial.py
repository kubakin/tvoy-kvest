# Generated by Django 3.1.2 on 2020-10-29 17:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image', verbose_name='image')),
                ('text', models.TextField(verbose_name='Текст задания')),
                ('cost', models.IntegerField(default=0, verbose_name='Cost of quest')),
                ('code', models.CharField(max_length=100, verbose_name='Code')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans', models.CharField(max_length=200, verbose_name='подсказка')),
                ('cost', models.IntegerField(default=0, verbose_name='Cost of answer')),
                ('reload_time', models.IntegerField(default=0, verbose_name='Время перезарядки подсказки')),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_for_quest', to='app.question')),
            ],
        ),
        migrations.CreateModel(
            name='Actived',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False, verbose_name='Активные')),
                ('progress', models.PositiveSmallIntegerField(default=0, verbose_name='Progress')),
                ('score', models.IntegerField(default=0, verbose_name='score')),
                ('lastHelp', models.TimeField(blank=True, default=datetime.datetime(1970, 1, 1, 0, 0), verbose_name='time')),
                ('people', models.PositiveSmallIntegerField(default=2, verbose_name='Кол-во человек')),
                ('progressAnswer', models.SmallIntegerField(default=0, verbose_name='Текущая подсказка')),
                ('number', models.CharField(default='', max_length=50, verbose_name='Номер телефона')),
                ('team_name', models.CharField(default='', max_length=50, verbose_name='Название команды')),
                ('key', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_is_active', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]