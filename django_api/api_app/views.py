from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from django.db import connections
# Create your views here.

class ExternalDatabaseConnection:
    def __init__(self):
        pass

    def conn(self):
        return connections['processor_postgres_name'].cursor()
    
    def fetch_all_average_time_data(self):
        with self.conn() as cursor:
            cursor.execute(sql="SELECT * FROM processor_app_averagetime")
            rows = cursor.fetchall()
        return rows
    
    def fetch_all_most_viewed_data(self):
        with self.conn() as cursor:
            cursor.execute(sql="SELECT * FROM processor_app_mostviewedpage")
            rows = cursor.fetchall()
        return rows
    
    def insert_into_average_time_table(self, page_name, average_time):
        with self.conn() as cursor:
            cursor.execute('INSERT INTO processor_app_averagetime (page_name, average_time) VALUES (%s, %s)', [page_name, average_time])
    
    def insert_into_most_viewed_table(self, page_name, sum_of_viewed):
        with self.conn() as cursor:
            cursor.execute('INSERT INTO processor_app_mostviewedpage (page_name, sum_of_viewed) VALUES (%s, %s)', [page_name, sum_of_viewed])


class AverageTimeAPIView(APIView):
    def get(self, request):
        db = ExternalDatabaseConnection()
        try:
            rows = db.fetch_all_average_time_data()
            data = [{"page_name": row[1], "average_time": row[2]} for row in rows]
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        page_name = request.data.get('page_name')
        average_time = request.data.get('page_name')
        if not page_name or not average_time:
            return Response({"error": "Both 'page_name' and 'average_time' are required!"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            db = ExternalDatabaseConnection()
            db.insert_into_average_time_table(page_name=page_name, average_time=average_time)
            return Response({"message": f"Record added successfully: {page_name}, {average_time}"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class MostViewedPageAPIView(APIView):
    def get(self, request):
        db = ExternalDatabaseConnection()
        try:
            rows = db.fetch_all_most_viewed_data()
            data = [{"page_name": row[1], "sum_of_viewed": row[2]} for row in rows]
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        page_name = request.data.get("page_name")
        sum_of_viewed = request.data.get("sum_of_viewed")
        if not page_name or not sum_of_viewed:
            return Response({"error": "Both 'page_name' and 'sum_of_viewed' are required!"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            db = ExternalDatabaseConnection()
            db.insert_into_most_viewed_table(page_name=page_name, sum_of_viewed=sum_of_viewed)
            return Response({"message": f"Record added successfully: {page_name}, {sum_of_viewed}"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        