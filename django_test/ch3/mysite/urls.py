"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from polls import views


urlpatterns = [
    path('admin/', admin.site.urls),

    # 추가
    # 패턴 매칭은 위에서 아래로 검색되니 순서에 유의할 것
    # path('polls/', views.index, name='index'),
    # path('polls/<int:question_id>/', views.detail, name='detail'),
    # path('polls/<int:question_id>/results/', views.results, name='results'),
    # path('polls/<int:question_id>/vote/', views.vote, name='vote'),

    # 위 내용을 어플리케이션 별로 나누기 위해서 다음과 같이 정의함
    # 계층적으로 구성함
    path('polls/', include('polls.urls'))

]
