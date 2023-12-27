from django.urls import path
from todolist.views import (
    add_task,
    toggle_finished,
    delete_task,
    register,
    login_user,
    logout_user,
    home,
)

app_name = "todolist"

task_patterns = [
    path("add_task/", add_task, name="add_task"),
    path("toggle_finished/<int:task_id>/", toggle_finished, name="toggle_finished"),
    path("delete_task/<int:task_id>/", delete_task, name="delete_task"),
]

auth_patterns = [
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]

urlpatterns = (
    [
        path("", home, name="home"),
    ]
    + task_patterns
    + auth_patterns
)
