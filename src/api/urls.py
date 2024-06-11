from django.urls import path

from api.views.create_user_view import CreateUserView
from api.views.get_user_view import GetUserView

urlpatterns = [
    path('create/', CreateUserView.as_view()),
    path('<int:user_id>/', GetUserView.as_view()),
]
