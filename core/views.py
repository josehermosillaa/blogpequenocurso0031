from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Article
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required 
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.

@login_required(login_url='/login/')
def home(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request,'core/articulos.html',context)

@login_required(login_url='/login/')
def content_view(request, id):
    article = Article.objects.get(id=id)
    context = {'article':article}
    
    return render(request, 'core/contenido.html', context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f"iniciaste sesion como: {username}.")
                return HttpResponseRedirect('/')
            else:
                messages.error(request,"username o password Incorrectos")
                return HttpResponseRedirect('/login')
        else:
            messages.error(request,"username o password Incorrectos")
            return HttpResponseRedirect('/login')
    form = AuthenticationForm()
    context = {'login_form':form}
    return render(request, 'core/login.html', context)

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # #obtenemos el contenttype del modelo
            # content_type = ContentType.objects.get_for_model(Article)
            # #obtenemos el permiso a asignar
            # es_miembro_1 = Permission.objects.get(
            #     codename='es_miembro_1',
            #     content_type=content_type
            # )
            user = form.save()
            #Agregar el permiso al usuario en el momento del registro
            # user.user_permissions.add(es_miembro_1)
            login(request, user)
            messages.success(request, "registrado satisfactoriamente")
        else:
            messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos")
        return HttpResponseRedirect('/register')
    form = UserRegisterForm()
    context = {"register_form": form}
    return render(request,"core/registro.html", context)


def logout_view(request):
    logout(request)
    messages.info(request, "Seha cerrado la sesion satisfactoriamente.")
    return HttpResponseRedirect('/login')