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
from .forms import ECUserForm

from django.views.generic import View

# Create your views here.
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

#for ec-auth
# replace old register_user with ec_user form view
class ECUserFormView(View):
    form_class = ECUserForm
    template = 'login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template, {'form' : form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
