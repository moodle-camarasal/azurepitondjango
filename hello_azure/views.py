from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import SociosForm
from .lista_socios import datos_socios
from .miscursos import obtener_url_curso, obtener_url_pago, dic_cursos
from .models import MisDatos
from .managercsv import registroCSV


def index(request):
    print('Request for index page received')
    return render(request, 'hello_azure/index.html')
    
def panel(request):
    cuenta = registroCSV()
    myusuario = cuenta.obtener_filas_csv()
    #myusuario = MisDatos.objects.all().values()
    #template = loader.get_template('miregistros.html')
    context = {
        'mymiembros': myusuario,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'hello_azure/midashboard.html', context)

@csrf_exempt    
def nuevo_registro(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        estado = 'no'
        MisDatos.objects.create(usuario=usuario, password=password, estado=estado)
        return redirect('panel')
        #return render(request, 'hello_azure/midashboard.html')
    else:
        return render(request, 'hello_azure/nuevoregistro.html')

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
    id_curso_str = request.GET.get('id', '0')
    try:
        id_curso_int = int(id_curso_str)
    except ValueError:
        return HttpResponseBadRequest("ID de curso no válido")
    url_del_curso = obtener_url_curso(id_curso_int, dic_cursos)
    if url_del_curso is None:
        url_del_curso = 'https://cfevirtual.camarasal.com/'
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
    lista_empresas = [empresa['Empresa'] for empresa in datos_socios.values()]
    return render(request, 'formulario.html', {'opciones': opciones, 'form':form, 'url_cerrar': url_del_curso, 'empresas': lista_empresas})
