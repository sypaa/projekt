from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('pdf/<pk>.pdf', views.PDFUserDetailView.as_view(), name='pdf'),
    path('admin/', admin.site.urls),
    path('pdfs/', views.pdf_list, name='list')
]
