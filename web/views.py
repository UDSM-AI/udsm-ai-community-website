from django.shortcuts import render
from .models import About, Highlight, Event, StudentReview,TeamLead


# Create your views here.
def home_view(request):
    about_content = About.objects.all()
    highlights = Highlight.objects.all()
    events = Event.objects.all()
    reviews = StudentReview.objects.all()
    team = TeamLead.objects.all()

    context = {
        "page_title": "Community",
        "about_content": about_content,
        "highlights": highlights,
        "events": events,
        "reviews": reviews,
        "team": team
    }
    return render(request, "web/home_page.html", context)