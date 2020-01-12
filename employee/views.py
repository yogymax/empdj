from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from employee.models import EmpModel,Address
from employee.serializers import EmpModelSer,AddressSer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
#from rest_framework.renderers import StaticHTMLRenderer

class EmpOps(ModelViewSet):#6--get-2,put,patch,del,post
    queryset = EmpModel.actemps.all()
    serializer_class = EmpModelSer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        value = {"error":'Record Not deleted...'}
        if instance:
            instance.active='N'
            instance.save()
            value = {"success":"Record Removed...!"}
        return Response(value,status=status.HTTP_200_OK)


    def create(self, request, *args, **kwargs):
        empinfo = request.data
        if empinfo['age']>=22:
            return super().create(request)
        else:
            return Response({"error" : "Invalid Age "}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'], name='All Emp Salaries')
    def get_all_salaries(self, request, *args, **kwargs):
        totalsal = sum([emp.salary for emp in EmpModel.actemps.all()])
        value = {"status": "COST To The Company : {}".format(totalsal)}
        print(value)
        return Response(value,status=status.HTTP_200_OK)



class AddressOp(ReadOnlyModelViewSet):#get-2
    queryset = Address.objects.all()
    serializer_class = AddressSer

