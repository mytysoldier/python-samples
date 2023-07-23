from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("foo", views.foo, name="foo"),
    path("hello", views.hello, name="hello"),
    path("item/<int:item_code>", views.show_item, name="show_item"),
]
