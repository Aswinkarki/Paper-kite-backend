from django.urls import path
from .views import EmailDataView, EmailDataDetailView

urlpatterns = [
    path('emaildata/', EmailDataView.as_view(), name='email-data-list'),
    path('emaildata/<str:email>/', EmailDataDetailView.as_view(), name='email-data-detail'),
]
