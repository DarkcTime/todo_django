from django.urls import path 
from todolist.views import redirect_view, todo, category


urlpatterns = [
    path('', redirect_view, name="redirect"),
    path('todo', todo, name="todolist"),
    path('category', category, name="caterogy")
]
