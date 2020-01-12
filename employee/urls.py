from rest_framework.routers import SimpleRouter
from employee.views import EmpOps,AddressOp
routerinstnace = SimpleRouter()
routerinstnace.register('employee',EmpOps)
routerinstnace.register('address',AddressOp)
urlpatterns = routerinstnace.urls

