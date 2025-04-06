from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(), name='home'),
    path('donate/<str:username>/', views.DonatePageView.as_view(), name='donate'),
    path('payment/<str:id>/',views.PaymentView.as_view(), name='payment'),
    path('authors/',views.AuthorsView.as_view(), name='authors')
]