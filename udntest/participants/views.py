from django.shortcuts import (
    render,
    redirect,
    render_to_response,
)
from .models import Participant
from .forms import DataForm
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf

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
