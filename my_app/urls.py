from django.urls import path
from . import views

# - predefined variable 'app_name' that django looks for to register the app namespace; for Url names
app_name = 'my_app'

# - paths from 'urlpatterns' are added at the end of current app level url route; e.g. http://127.0.0.1:8000/my_app/(path)
urlpatterns = [
    # - A single url example
    # path('', views.sample_view),

    # - dynamic routing
    path('<str:topic>/', views.news_view, name='topic-page'),

    # - for redirects
    path('<int:num_page>', views.num_page_view),

    path('', views.example_view, name='example'),
    path('variable/', views.variable_view, name='variable')
]