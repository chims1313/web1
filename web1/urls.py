from django.contrib import admin
from django.urls import path
from core import views 

urlpatterns = [
    path('',views.home,name="home"),
    path('faq/',views.faq,name="faq"),
    path('quienes-somos/',views.quienes_somos,name="quienes-somos"),
    path('productos/',views.productos,name="productos"),
    path('admin/', admin.site.urls),
]
