from django.urls import path
from .views import FormDataView, FormDataDetailView

urlpatterns = [
    path('formdata/', FormDataView.as_view(), name='form-data-list'),
    path('formdata/<int:form_id>/', FormDataDetailView.as_view(), name='form-data-detail'),
]
