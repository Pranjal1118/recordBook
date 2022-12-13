from django.urls import path
from . import views
urlpatterns = [
               path('', views.loginfn),
               path('sign', views.register),
               path('show', views.show),
               path('emp', views.emp),
               path('edit/<int:id>', views.edit),
               path('update/<int:id>', views.update),
               path('del/<int:id>', views.delete),
               path('search', views.search),
               path('scode', views.search_by_code),
            ]