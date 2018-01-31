from django.urls import include, path
from . import views
app_name = 'clinicalSearch'
urlpatterns = [
    path('', views.Index.as_view(), name='index')
]
