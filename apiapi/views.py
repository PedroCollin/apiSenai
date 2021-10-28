from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Question
from .serializers import QuestionSerializer
# Create your views here.


class QuestionViewSet(viewsets.ModelViewSet):
    """
       API endpoint that allows users to be viewed or edited.
       """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

