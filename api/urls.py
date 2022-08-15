from rest_framework_nested import routers
from api.views import *

router = routers.DefaultRouter()
router.register('softwarehouse', SoftwareHouseViewSet, basename='softwarehouse')

# Nested Routers
employee_router = routers.NestedDefaultRouter(router, 'softwarehouse', lookup='softwarehouse')
employee_router.register('employee', EmployeeViewSet, basename='employee')

# URLConf
urlpatterns = router.urls + employee_router.urls
