

# Create your models here.
from djoser import serializers as ser
from djoser.conf import User
# from rest_framework import serializers
from rest_framework import serializers

from app.models import Actived, Question, Answer


class ActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model= Actived
        fields ='__all__'
class OneUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','id', 'password')
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields=('ans','cost','reload_time')
class UserSerializer(ser.UserSerializer):
    # user_is_active = serializers.SlugRelatedField(slug_field='progress', read_only=True, many=False)
    user_is_active = ActiveSerializer(many=False)
    class Meta:
        model= User
        fields= ('username', 'groups', 'user_is_active', 'id')

# class ActivedSerializer(serializers)
class QuestSerializer(serializers.ModelSerializer):
    answer_for_quest = AnswerSerializer(many=True)
    class Meta:
        model=Question
        fields = '__all__'