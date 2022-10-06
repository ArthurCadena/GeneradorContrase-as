from django.shortcuts import render
import random
#from django.http import HttpResponse

# Create your views here.
def password(request):

    caracteres = list("abcdefghijklmnopqrstuvwxyz") #caracteres basicos en una lista
    contraseñaGenerada = ""
    longitud = int(request.GET.get("longitud"))#aqui escuchamos el query del formulario
    if request.GET.get("mayuscula"):
        caracteres.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))#Si se recibe la consulta de mayuscula se procede a ampliar la lista de la variable caracteres :D !!
    if request.GET.get("especial"):
        caracteres.extend(list("@´+´{{}()[]*+~'¿?><ñ,.-"))
    if request.GET.get("numeros"):
        caracteres.extend(list("1234567890"))
         
    for x in range(longitud):                                   #recorremos la lista y segun el query que envia el usuario en el formulario                                                       
        contraseñaGenerada += random.choice(caracteres)   #guardamos los datos en la variable contraseñaGenerada

    return render(request,'generator/password.html',{'password': contraseñaGenerada})#asociamos la contraseña a un diccionario para mostrarlo en la vista

    

def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')

