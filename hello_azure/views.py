from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import SociosForm

def index(request):
    print('Request for index page received')
    return render(request, 'hello_azure/index.html')

@csrf_exempt
def hello(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        if name is None or name == '':
            print("Request for hello page received with no name or blank name -- redirecting")
            return redirect('index')
        else:
            print("Request for hello page received with name=%s" % name)
            context = {'name': name }
            return render(request, 'hello_azure/hello.html', context)
    else:
        return redirect('index')

def myform(request):
    opciones = request.GET.get('options', '0')
    if request.method == 'POST':
        form = SociosForm(request.POST)
        if form.is_valid():
            myDiccionario = {
                'mynombre': form.cleaned_data['nombre'],
                'mycorreo': form.cleaned_data['correo'],
                'myphone': form.cleaned_data['telefono'],
                'myempresa': nombre_empresa,
            }
            #return redirect(templateHtml)
    else:
        form = SociosForm()
    return render(request, 'formulario.html', {'opciones': opciones, 'form':form})
