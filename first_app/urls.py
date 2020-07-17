from first_app import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.form_view,name = "form_view")

]
