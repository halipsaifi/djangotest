from django.shortcuts import (
    render,
    redirect,
    render_to_response,
)
from .models import Participant
from .forms import DataForm
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm

# Create your views here.
def register_user(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/register_ok/')
        else:
            args['form'] = form
            return render(request, 'register.html', args)


    args['form'] = RegisterUserForm()
    return render_to_response('register.html', args)

def register_ok(request):
    return render_to_response('register_ok.html')

# DataForm view
def add(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/participants')
        else:
            args['form'] = form
            return render(request, 'add.html', args)

    args['form'] = DataForm()
    return render_to_response('add.html', args)

# list view

# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="/login/")
def list(request):
    if request.method == 'POST':
        pid = request.POST.get("participantId")
        action = request.POST.get("action")
        taget = Participant.objects.get(id=int(pid))
        taget.status = action
        taget.save()
        return redirect('/participants')
    else:
        list = Participant.objects.all()
        context = { 'list' : list }
        return render(request, 'list.html', context)
