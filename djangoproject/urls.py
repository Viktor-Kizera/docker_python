from django.contrib import admin
from django.urls import path
from myFirstApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my-view/', views.my_view, name='my-view'),
    path('', views.form_submission, name='home'),  # Шлях до головної сторінки
    path('form/', views.form_submission, name='form-view'),  # Шлях до обробки форми
    path('form-submission/', views.form_submission, name='result-view'),  # Шлях до відображення результату форми
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
