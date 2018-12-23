from django.shortcuts import render
from rest_framework import generics

from .models import Member
from .serializers import MemberSerializer

# Create your views here.
class MemberList(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(generics.RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

