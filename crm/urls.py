from django.conf.urls import url
from . import views
from django.urls import path
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'crm'
urlpatterns = [

    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('food_list', views.food_list, name='food_list'),
    path('food/<int:pk>/edit/', views.food_edit, name='food_edit'),
    path('food/<int:pk>/delete/', views.food_delete, name='food_delete'),
    path('food/create/', views.food_new, name='food_new'),
    path('entry_list', views.entry_list, name='entry_list'),
    path('entry/create/', views.entry_new, name='entry_new'),
    path('entry/<int:pk>/edit/', views.entry_edit, name='entry_edit'),
    path('entry/<int:pk>/delete/', views.entry_delete, name='entry_delete'),
    path('entry/<int:pk>/summary/', views.summary, name='summary'),
    url(r'^foods_json/', views.FoodList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)