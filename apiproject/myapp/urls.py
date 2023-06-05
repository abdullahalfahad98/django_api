from django.urls import path
from myapp import views

urlpatterns = [
    path('myapi/', views.BlogList.as_view()),
    path('detail/<int:pk>/', views.ApiDetail.as_view()),
    path('mydetail/<int:pk>/', views.ContactDetail.as_view()),
    path('gav/', views.ContactList.as_view()),
]