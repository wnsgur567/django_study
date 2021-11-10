from django.urls import path
from . import views

# app_name 은 url pattern 다른 어플리케이션과 충돌나는걸 방지해줌
# namespace 와 같은 놈
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
