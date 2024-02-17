from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import SociosForm
from .lista_socios import datos_socios

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
    opciones = request.GET.get('opcion', '0')
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
    diccionario_empresas = {
        '00012002': {'Filial': 'San Salvador', 'Empresa': '2M SERVICES, S.A. DE C.V.', 'Nombre': ''},
        '00001593': {'Filial': 'Santa Ana', 'Empresa': '3 M INVERSIONES, S.A. DE C.V.', 'Nombre': ''},
        '00018628': {'Filial': 'San Salvador', 'Empresa': '360 MEDIA CONTENT, S.A. DE C.V.', 'Nombre': ''},
        '00006189': {'Filial': 'San Miguel', 'Empresa': 'A & D, S.A. DE C.V.', 'Nombre': '44743'},
        '00011251': {'Filial': 'San Salvador', 'Empresa': 'A & M INVERSIONES, S.A. DE C.V.', 'Nombre': ''},
    }
    #lista_empresas = [empresa['Empresa'] for empresa in diccionario_empresas.values()]
    lista_empresas = [empresa['Empresa'] for empresa in datos_socios.values()]
    return render(request, 'formulario.html', {'opciones': opciones, 'form':form, 'empresas': lista_empresas})
    #return render(request, 'formulario.html', {'opciones': opciones, 'form':form})