from django.urls import path
from todolist.views import register, login_user, logout_user, home
from todolist.views import delete_task, toggle_finished

app_name = "todolist"
urlpatterns = [
    path("toggle_finished/<int:task_id>/", toggle_finished, name="toggle_finished"),
    path("delete_task/<int:task_id>/", delete_task, name="delete_task"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("", home, name="home"),
]
