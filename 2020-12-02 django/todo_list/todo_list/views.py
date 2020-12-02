from django.http import HttpResponse
from django.template import loader
from .models import Tasks

def index(request):
    tasks = Tasks.objects.all()
    template = loader.get_template('index.html')
    context = {
        'tasks': tasks
    }
    return HttpResponse(template.render(context, request))