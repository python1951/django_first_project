from first_app import views
from django.urls import path
app_name = 'first_app'

urlpatterns = [
    path('login/',views.login_view,name= "login"),
    path('success/',views.success_view,name='success'),
    path('', views.index, name='index'),
    path('login/',views.form_view,name = "form_view"),
    path('register/',views.register,name='register'),
    path('extended/',views.extended,name='extended'),
    path('loginn/',views.user_login,name="user_login"),
    path('logout/',views.user_logout,name='logout'),
    path('special/',views.special,name ="special"),

]
