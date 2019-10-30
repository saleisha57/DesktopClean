from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_profile, name='create-profile'),
    path('<int:pk>', views.view_profile, name='view-profile'),
    path('<int:pk>/edit', views.edit_profile, name='edit-profile'),
    path('searchresults', views.search_results, name='search-results'),

    path('login', views.login, name="login"),
    path('create_account', views.create_account, name='create-account')
]
