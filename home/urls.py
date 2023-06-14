from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index' ),
    path('compare_code',views.compare_code,name='compare_code' ),
    path('questions',views.qs,name='questions' ),
    path('question/<int:id>',views.question,name='question' ),
    path('reset_attempts/', views.reset_attempts, name='reset_attempts'),

]
