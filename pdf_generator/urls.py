from django.urls import path, include

from . import views

app_name = 'pdf_generator'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Generator PDF
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
]