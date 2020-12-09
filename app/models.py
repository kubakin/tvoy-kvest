from datetime import datetime

from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Actived(models.Model):
    key = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE , related_name='user_is_active')
    active = models.BooleanField('Активные', default=False)
    progress = models.PositiveSmallIntegerField('Progress', default=0)
    score = models.IntegerField('score', default=0)
    lastHelp = models.TimeField('time', default=datetime(1970, 1, 1), blank=True)
    people = models.PositiveSmallIntegerField('Кол-во человек', default=2)
    progressAnswer = models.SmallIntegerField('Текущая подсказка', default=0)
    number = models.CharField('Номер телефона', max_length=50, default='')
    team_name = models.CharField('Название команды', max_length=50, default='')
    def __str__(self):
        # return (self.key + str(self.progress))
        return 'Название команды:{}, Прогресс:{}. Баллы:{}, Телефон:{}'.format(self.team_name, self.progress, self.score, self.number)

class Question(models.Model):
    name = models.CharField('Название', max_length=100)
    image = models.ImageField("image", upload_to='image', blank=True, null=True)
    text = models.TextField('Текст задания')
    cost = models.IntegerField('Cost of quest', default=0)
    code = models.CharField('Code', max_length=100)
    def __str__(self):
        return self.name


class Answer(models.Model):
    ans = models.CharField('подсказка', max_length=200)
    quest = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer_for_quest')
    cost = models.IntegerField('Cost of answer', default=0)
    reload_time = models.IntegerField('Время перезарядки подсказки',default=0)
    def __str__(self):
        return 'Вопрос:{}, Ответ:{}'.format(self.quest, self.ans)