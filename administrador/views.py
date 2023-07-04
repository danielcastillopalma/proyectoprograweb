from django.shortcuts import render

# Create your views here.
def menu(request):
    request.session["usuario"]="admin"
    usuario=request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, 'administrador/menu.html', context)