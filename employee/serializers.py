from rest_framework.serializers import ModelSerializer
from employee.models import EmpModel,Address

class AddressSer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class EmpModelSer(ModelSerializer):
    #addrs = AddressSer(many=True)
    class Meta:
        model = EmpModel
        fields = '__all__'

