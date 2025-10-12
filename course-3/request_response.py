from django.http import HttpResponse
from django.template import loader 


def index(request): 
    return HttpResponse("Hello World") 

def index(request): 
    template = loader.get_template('demoapp/index.html') 
    context={}  
    return HttpResponse(template.render(context, request)) 

def index(request): 
    path = request.path 
    method = request.method 
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
'''.format(path, method) 
    return HttpResponse(content) 