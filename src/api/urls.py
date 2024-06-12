from django.urls import path, include

from api.views.create_user_view import CreateUserView
from api.views.get_user_view import GetUserView
from api.views.search_user_view import SearchUserView


user_urlpatterns = [
    path('create/', CreateUserView.as_view()),
    path('<int:user_id>/', GetUserView.as_view()),
    path('search', SearchUserView.as_view())
]

urlpatterns = [
    path('user/', include(user_urlpatterns)),
]

