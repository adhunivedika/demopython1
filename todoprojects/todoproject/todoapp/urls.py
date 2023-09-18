from.import views
from django.urls import path

urlpatterns = [

    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('classindex/',views.Tasklistview.as_view(),name='classindex'),
    path('classdetail/<int:pk>/',views.TaskDetailview.as_view(),name='classdetail'),
    path('classupdates/<int:pk>/',views.Taskupdateview.as_view(),name='classupdates'),
    path('classdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='classdelete'),
]