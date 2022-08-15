from rest_framework import serializers
from api.models import SoftwareHouse, Employee


class SimpleEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "first_name", "last_name", "email"]


class SoftwareHouseSerializer(serializers.ModelSerializer):
    employees = SimpleEmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = SoftwareHouse
        fields = ["id", "name", "about", "employees"]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "first_name", "last_name", "created_at", "software_house", "designation", "email", "phone",
                  "birth_date"]

    def create(self, validated_data):
        software_house_id = self.context['software_house_id']
        return Employee.objects.create(software_house_id=software_house_id, **validated_data)
