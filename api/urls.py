from rest_framework import routers
from .views import taskviewset, userapiviewset
from django.urls import path
from rest_framework.authtoken import views as auth_view

app_name='api'

urlpatterns=[

]

urlpatterns += [
    path('api-token-auth/', auth_view.obtain_auth_token)
]

router=routers.SimpleRouter()
router.register(r'task',taskviewset ,basename='task')
router.register( r'user',userapiviewset)

urlpatterns += router.urls

