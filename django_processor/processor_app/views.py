from django.shortcuts import render
from django.db import connections
from .models import AverageTime, MostViewedPage
import random, os
# Create your views here.

def database_conn(query):
       with connections['postgresql_collector'].cursor() as cursor:
              cursor.execute(query)
              data = cursor.fetchall()
              return data

def processor():
        def average():
                sql_query = "SELECT page_viewed, avg(time_spent) AS total_time_spent FROM collector_app_browsingdata GROUP BY page_viewed ORDER BY total_time_spent DESC;"
                data = database_conn(query=sql_query)
                for row in data:
                       page_name, average_time_spent = row
                       if AverageTime.objects.filter(page_name=page_name).values():
                              pass
                       else:
                              AverageTime(page_name=page_name, average_time=average_time_spent).save()
                return data
        def most_viewed():
                sql_query = "SELECT page_viewed, SUM(time_spent) AS total_time_spent FROM collector_app_browsingdata GROUP BY page_viewed ORDER BY total_time_spent DESC LIMIT 1;"
                data = database_conn(query=sql_query)
                page_name, sum_of_viewed = max(data)
                if MostViewedPage.objects.filter(page_name=page_name).values():
                       pass
                else:
                        MostViewedPage(page_name=page_name, sum_of_viewed=sum_of_viewed).save()
                return max(data)
        return average(), most_viewed()
               
        

def index(request):
    html_file = "processor_app/index.html"
    context = {}
    rows = database_conn(query="SELECT * FROM collector_app_browsingdata")
    context['rows'] = rows
    context['message'] = "Data is fetched successfully."
    try:
        average, most_viewed = processor()
        context['average'] = average
        context['most_viewed'] = most_viewed
    except:
           pass

    return render(request, html_file, context)