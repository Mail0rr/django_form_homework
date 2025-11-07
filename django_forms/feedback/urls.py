from django.urls import path
from . import views

urlpatterns = [
    path("feedback/", views.handle_feedback_form, name="feedback"),
]