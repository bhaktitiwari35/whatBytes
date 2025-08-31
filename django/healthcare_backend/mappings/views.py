from rest_framework import generics, permissions
from .models import Mapping
from .serializers import MappingSerializer
from patients.models import Patient

class MappingListCreateView(generics.ListCreateAPIView):
    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

class MappingListView(generics.ListAPIView):
    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

class MappingByPatientView(generics.ListAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return Mapping.objects.filter(patient_id=patient_id)

class MappingDeleteView(generics.DestroyAPIView):
    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]
