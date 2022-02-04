from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView


def hello_world(request):
    if request.method == "POST":
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        return render(request, 'accountapp/hello_world.html', context={'text':'abcd'})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'