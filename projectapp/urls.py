from projectapp import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("profile", views.profile, name= "profile"),
    path("posts", views.posts, name="posts"),
    path("posts/add/", views.add_post, name="add-post"),
    path("posts/<str:pk>/", views.post, name="post"),
    path("posts/<str:pk>/edit/", views.edit_post, name="edit_post"),
    path("user/form/", views.display_form, name="user_form"),
    path("user/create/", views.create_user, name="create_user"),
    path("user/custom_create/", views.custom_create_user, name="custom_create_user"),
    path("user/submit/", views.submit_form, name="submit_form"),
    path("user/students/create/", views.create_students, name="create_students"),
    path("user/login/", views.login, name="login"),
]