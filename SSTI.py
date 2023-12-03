from django.template import Context, Template
from django.http import HttpResponse

def ssti(request):
    if 'name' in request.GET:
        t = Template('Hello, {{ name }}!')
        c = Context({'name': request.GET['name']})
        rendered = t.render(c)
        return HttpResponse(rendered)
    else:
        return HttpResponse('Please provide a name')
