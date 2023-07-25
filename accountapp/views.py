from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView


def hello_world(request):
    return render(request, 'accountapp/hello_world.html')

class AccountCreateView(CreateView):
    model = User #연결할모델
    form_class = UserCreationForm #로그인폼
    success_url = reverse_lazy('accountapp:hello_world') #로그인성공시 연결할url
    template_name = 'accountapp/create.html'
