from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django import template
from .models import Peliculas, Productos_confiteria, Funciones
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.decorators.http import require_http_methods

def index(request):
    return render(request, "pages/index.html")

def cartelera(request):
    Pelicula = Peliculas.objects.all()

    return render(request, "pages/cartelera.html", {'pelicula': Pelicula})

def confiteria(request):
    Confiteria = Productos_confiteria.objects.all()
    return render(request, "pages/confiteria.html", {'confiteria': Confiteria})

def promociones(request):
    productos = Productos_confiteria.objects.all()
    for producto in productos:
        producto.descuento_productos = int(producto.descuento_productos * 100)
    return render(request, 'pages/promociones.html', {'promociones': productos})

def contacto(request):
    return render(request, "pages/contacto.html")

def compras(request):
    return render (request, "pages/compras.html")

def detalle(request, id):
    pelicula = Peliculas.objects.get(pk=id)
    funciones = Funciones.objects.filter(id_peliculas=id)

    # Agrupar por días
    funciones_por_dia = {}
    for funcion in funciones:
        fecha = funcion.fecha_funcion.strftime("%d-%b-%Y")
        if fecha not in funciones_por_dia:
            funciones_por_dia[fecha] = []
        funciones_por_dia[fecha].append(funcion.hora_funcion)

    return render(request, "pages/detalle.html", {'pelicula': pelicula, 'funciones_por_dia': funciones_por_dia})


@require_http_methods(["GET", "POST"])
def purchase_process(request):
    if request.method == "POST":
        # Procesar la compra
        cantidad_tickets = int(request.POST.get('ticketQuantity'))
        seleccion_butaca = request.POST.get('selectedSeats').split(',')
        metodo_pago = request.POST.get('paymentMethod')

        # Crear la compra
        purchase = Productos_confiteria.objects.create(
            ticket_quantity=cantidad_tickets,
            payment_method=metodo_pago
        )

        # Asociar las butacas seleccionadas
        for seat_number in seleccion_butaca:
            Productos_confiteria.objects.create(
                purchase=purchase,
                seat_number=int(seat_number)
            )

        # Procesar los snacks seleccionados
        for key, value in request.POST.items():
            if key.startswith('snack_quantity_'):
                nombre_producto = key.replace('snack_quantity_', '')
                quantity = int(value)
                if quantity > 0:
                    Productos_confiteria.objects.create(
                        purchase=purchase,
                        name=nombre_producto,
                        quantity=quantity
                    )

        # Redireccionar a una página de confirmación
        return redirect('purchase_confirmation', purchase_id=purchase.id)

    # Si es GET, mostrar el formulario
    return render(request, 'purchase_form.html')

def purchase_confirmation(request, purchase_id):
    purchase = Productos_confiteria.objects.get(id=purchase_id)
    return render(request, 'purchase_confirmation.html', {'purchase': purchase})