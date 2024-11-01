from django.urls import path 
from todolist_app import views

urlpatterns = [
    path('',views.home,name="home-todo"),
    path("tasks/",views.tasks,name='tasks'),
    path("contact-us",views.contact,name="contact-us"),
    path("biography/",views.see_developer_biography,name="biography"),
    path("delete/<int:id>",views.delete_task,name="delete_task"),
    path("edit/<int:id>",views.edit_task,name="edit_task"),
    path("complete/<int:id>",views.complete_task,name="complete_task"),
    path("pending/<int:id>",views.pending_task,name="pending_task"),
]
