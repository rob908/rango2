from django.shortcuts import render
def index(request):   
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Rango says hey there partner!")
