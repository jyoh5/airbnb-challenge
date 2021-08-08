from django.urls import path
from reviews.views import create_review, delete_review

app_name = "reviews"

urlpatterns = [
  path("create/<int:pk>", create_review, name="create"),
  path("delete/<int:pk>", delete_review, name="delete"),
]
