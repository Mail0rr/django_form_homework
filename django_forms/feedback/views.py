from django.shortcuts import render
from .forms import FeedbackForm
from .models import Feedback

def handle_feedback_form(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Дякуємо за ваш відгук!"
        else:
            message = "Будь ласка, виправте помилки у формі."
    else:
        form = FeedbackForm()
        message = None

    feedbacks = Feedback.objects.all().order_by("-created_at")
    return render(request, "forms/feedback.html", {"form": form, "message": message, "feedbacks": feedbacks})
