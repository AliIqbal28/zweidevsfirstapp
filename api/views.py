from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from api.models import SoftwareHouse, Employee
from api.serializers import SoftwareHouseSerializer, EmployeeSerializer, SimpleEmployeeSerializer


class SoftwareHouseViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = SoftwareHouseSerializer
    queryset = SoftwareHouse.objects.prefetch_related("employees").all()


class EmployeeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EmployeeSerializer
        return SimpleEmployeeSerializer

    def get_queryset(self):
        return Employee.objects.select_related("software_house").filter(software_house_id=self.kwargs['softwarehouse_pk'])

    def get_serializer_context(self):
        return {'software_house_id': self.kwargs['softwarehouse_pk']}
