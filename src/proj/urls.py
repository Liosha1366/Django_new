"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
# from hello_world.views import hello_world
# from django.views.generic import RedirectView
# from hello_world.views import create_aut_book_view
from hello_world import views as view_hello_world

from books import views as view_book


urlpatterns = [
    # path('', RedirectView.as_view(url='/hello-world/')),
    path('admin/', admin.site.urls),
    # path('hello-world/', hello_world),
    path('template/', view_book.StaticView.as_view()),

    path('Create-View/', view_book.CreateBookView.as_view()),
    path('update-View/<int:pk>/', view_book.UpdateBookView.as_view()),
    path('delete-View/<int:pk>/', view_book.DeleteBookView.as_view()),

    path('list-view/', view_book.ShowBookListView.as_view()),
    path('bk/create/seris', view_hello_world.create_seris_view),
    path('bk/create/genre', view_hello_world.create_genre_view),

    path('bk/create/aut_book', view_hello_world.create_aut_book_view),
    path('bk/create/publish', view_hello_world.create_publish_view),
    path('bk/create/seris', view_hello_world.create_seris_view),
    path('bk/create/genre', view_hello_world.create_genre_view),

    path('bk/update/publish/<int:pk>/', view_hello_world.update_publish_view),
    path('bk/update/aut_book/<int:pk>/', view_hello_world.update_aut_book_view),
    path('bk/update/seris/<int:pk>/', view_hello_world.update_seris_view),
    path('bk/update/gener/<int:pk>/', view_hello_world.update_gener_view),

    path('bk/delete/aut_book/<int:pk>/', view_hello_world.delete_aut_book_view),
    path('bk/delete/publish/<int:pk>/', view_hello_world.delete_publish_view),
    path('bk/delete/seris/<int:pk>/', view_hello_world.delete_seris_view),
    path('bk/delete/genre/<int:pk>/', view_hello_world.delete_genre_view),

    path('book/create', view_book.create_book_view),
    path('book/update/<int:pk>/', view_book.update_book_view),
    path('book/delete/<int:pk>/', view_book.delete_book_view),
    
]
