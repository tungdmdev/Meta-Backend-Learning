from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from datetime import datetime

def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers['Age'] = 20

    msg = f"""<br>
        <br>Path: {path}
        <br>Address: {address}
        <br>Scheme: {scheme}
        <br>Method: {method}
        <br>User agent: {user_agent}
        <br>Path info: {path_info}
        <br>Response header: {response.headers}

    """    
    response = HttpResponse(msg, content_type ='text/html', charset = 'utf-8')
    return response

def homepage(request):
    return HttpResponse("Welcome to Little Lemon!")

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = """<h1 style="color: #F4CE14;"> This is Little Lemon again! </h1>"""
    return HttpResponse(text)

def pathview(request, name, id): 
    return HttpResponse("Name:{} UserID:{}".format(name, id))

def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id))

def showform(request): 
    return render(request, "form.html") 

def getform(request): 
    if request.method == "POST": 
        id=request.POST['id'] 
        name=request.POST['name'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id))

def menuitems(request, dish):
    items = {
        'pasta': 'abcd',
        'falafel': 'cdef',
        'cheesecake': 'ghik',
    }

    description = items[dish]

    return HttpResponse(f"<h2> {dish} </h2>" + description)

#Mapping URLs with Params
def drinks(request, drink_name):
    drink = {
        'mocha' : 'type of coffee',
        'tea' : 'type of hot beverage',
        'lemonade': 'type of refreshment'
    }
    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2> " + choice_of_drink)

#Handle error in views

def handler404(request, exception):
    return HttpResponse("404: Page not found! <br><br> <button onclick="" href='':""> Go to hone page</button>")