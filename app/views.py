from django.contrib.auth.decorators import login_required
from djoser.conf import User
from rest_framework import viewsets, status
from rest_framework.response import Response

from app.models import Actived, Question
from app.serializers import UserSerializer, ActiveSerializer, QuestSerializer, OneUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # def perform_create(self):
    #     print('work')
    # def create(self, request):
    #     print(request.data)

class UserOneViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = OneUserSerializer
    def create(self, request):
        # super().request.user.set_password(request.data['password'])
        self.serializer_class = OneUserSerializer(data = {'username':request.data['username'], 'password':request.data['password']})
        #self.requset_password(request.data['password'])
        if self.serializer_class.is_valid():
            id = self.serializer_class.save().id
            self.serializer_class = ActiveSerializer(data = {'key': id, 'people': request.data['people'], 'number': request.data['number'],'team_name': request.data['team_name']})
            if self.serializer_class.is_valid():
                self.serializer_class.save()
                return Response('success', status=status.HTTP_201_CREATED)
        # print('good')

class QuestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestSerializer


class ActiveViewSet(viewsets.ModelViewSet):
    queryset = Actived.objects.all()
    serializer_class = ActiveSerializer
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return PersonListSerializer
    #     if self.action == 'retrieve':
    #         return PersonDetailSerializer