from django.urls import path
from .views import home_page_view, add_employee, edit_employee, delete_employee

urlpatterns = [
    path('', home_page_view, name='home'),
    path('add/', add_employee, name='add_employee'),
    path('edit/<int:id>/', edit_employee, name='edit_employee'),     # NEW
    path('delete/<int:id>/', delete_employee, name='delete_employee'), # NEW
]