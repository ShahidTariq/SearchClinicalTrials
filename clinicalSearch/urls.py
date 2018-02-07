from django.urls import include, path
from . import views
app_name = 'clinicalSearch'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('result/', views.Result.as_view(), name='result'),
    path('detail/', views.Detail.as_view(), name='detail'),
    path('nct/', views.SearchNct.as_view(), name='search_nct'),
    path('con/', views.SearchCon.as_view(), name='search_condition'),
    path('loc/', views.SearchLoc.as_view(), name='search_location'),

    path('addRecord/', views.AddRecords.as_view(), name='add_record'),
    path('getLocation/', views.GetLoc.as_view(), name='getLocation'),

]
