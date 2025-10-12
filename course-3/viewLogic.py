from django.shortcuts import render     

def myview(request): 
    if request.method=='GET': 
        val = request.GET['key'] 
        #perform read or delete operation on the model 
    if request.method=='POST': 
        val = request.POST['key'] 
        #perform insert or update operation on the model 

    return render(request, 'mytemplate.html', context) 
 
from django.views import View 
class MyView(View): 
    def get(self, request): 
        # logic to process GET request
        return HttpResponse('response to GET request') 
 
    def post(self, request): 
        # <logic to process POST request> 
        return HttpResponse('response to POST request') 

      