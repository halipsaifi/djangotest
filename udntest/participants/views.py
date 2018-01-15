from django.shortcuts import (
    render,
    redirect,
    render_to_response,
)
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Participant
from .forms import DataForm
# for ec_auth
from .forms import ECUserForm
from .services import ec_auth, username_present
# for class based views
from django.views.generic import View
from django.contrib.auth.models import User

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
        context = { 'list' : list,
                    'username' : request.user.username,
                    'firstname' : request.user.first_name,
                    'lastname' : request.user.last_name,
                    'email' : request.user.email}
        return render(request, 'list.html', context)

#for ec-auth
# replace register_user with ec_user login form
class ECUserFormView(View):
    form_class = ECUserForm
    template = 'login.html'
    message = ''

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template, {'form' : form, 'message' : ''})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #call HMS eComons authentication service
            #if OK, login or create a new if not exists yet
            if ec_auth(username, password):
                if username_present(username):
                    user = User.objects.get(username=username)
                    login(request, user)
                    return redirect('/participants?exist')
                else:
                    r = ec_auth(username, password)
                    user = User.objects.create_user(username=r['username'],
                    email=r['email'], first_name=r['firstname'], last_name=r['lastname'])
                    user.set_unusable_password()
                    user = User.objects.get(username=username)
                    login(request, user)
                    return redirect('/participants?new')

        return render(request, self.template, {'form' : form, 'message' : 'incorrect Username or Password'})
