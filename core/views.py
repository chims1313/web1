from django.shortcuts import render

def home(request):
    return render(request,"core/home.html", {"actual_endpoint": "inicio"})

def faq(request):
    return render(request,"core/faq.html", {"actual_endpoint": "faq"})

def quienes_somos(request):
    return render(request, "core/quienes_somos.html", {"actual_endpoint": "quienes-somos"})

def productos(request):
    return render(request, "core/productos.html", {"actual_endpoint": "productos"})
