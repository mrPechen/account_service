from django.urls import path

from api.views.create_user_view import CreateUserView

urlpatterns = [
    path('create/', CreateUserView.as_view()),
]