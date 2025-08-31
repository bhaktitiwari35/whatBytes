from django.urls import path
from .views import (
    MappingListCreateView,
    MappingByPatientView,
    MappingDeleteView,
    MappingListView
)

urlpatterns = [
    path('', MappingListCreateView.as_view()),
    path('all/', MappingListView.as_view()),
    path('<int:patient_id>/', MappingByPatientView.as_view()),
    path('delete/<int:pk>/', MappingDeleteView.as_view()),
]
