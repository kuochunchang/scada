from django.urls import path
import main.views as views


urlpatterns = [
    path('', views.MainView.as_view(), name='home'),
]
