from django.contrib import admin
from django.urls import path
from tasks import views


app_name='tasks'
urlpatterns = [
path('detail/<int:task_id>',views.detailtask.as_view(), name='detail' ),
path('delete/<int:task_id>',views.deletetask.as_view(), name='delete' ),
path('create/',views.ceratetask.as_view(), name='create' ),
path('update/<int:task_id>',views.updatetask.as_view(), name='update' ),
    
]