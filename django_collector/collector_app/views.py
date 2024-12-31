from django.shortcuts import render
from .models import BrowsingData
import random
# Create your views here.

def create_user_id():
    return random.randint(10000, 99999)

def index(request):
    html_file = "collector_app/index.html"
    context = {}
    if request.method == "POST":
        try:
            page_viewed_user_input = request.POST.get("page_viewed", "")
            time_spent_user_input = request.POST.get("time_spent", "")
            random_user_id = create_user_id()
            BrowsingData(user_id=random_user_id , page_viewed=page_viewed_user_input, time_spent=time_spent_user_input).save()
            context['message'] = "Data added successfully."
        except Exception as e:
            context['message'] = f"The error occurs. {e}"
    else:
        pass
    return render(request, html_file, context=context)