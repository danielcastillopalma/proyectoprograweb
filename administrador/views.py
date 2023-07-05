from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
def admin_check(user):
    if user.username=="admin":
        return True
    else:
      return False
  

@login_required

def menu(request):
    request.session["usuario"]=request.user.username
    usuario=request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, 'administrador/menu.html', context)




