from django.urls import path
from . import views

urlpatterns = [
	path('sum/<int:num1>/<int:num2>',views.sum),
	path('diff/<int:num1>/<int:num2>',views.diff),
	path('pro/<int:num1>/<int:num2>',views.pro),
	path('quo/<int:num1>/<int:num2>',views.quo),
	path('calculate/<int:num1>',views.calculate),
]