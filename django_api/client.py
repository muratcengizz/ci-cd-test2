import requests

BASE_URL = "http://127.0.0.1:8002/api/"

def get_average_time_data():
    response = requests.get(url=BASE_URL + "average-time/")
    if response.status_code == 200:
        print("Average Time Data:")
        for element in response.json():
            print(f"Page Name: {element['page_name']}, Average Time: {element['average_time']}")
    else:
        print("Failed to fetch Average Time data:", response.json())

def get_most_viewed_data():
    response = requests.get(BASE_URL + "most-viewed/")
    if response.status_code == 200:
        print("Most Viewed Page Data:")
        for element in response.json():
            print(f"Page Name: {element['page_name']}, Sum of Viewed: {element['sum_of_viewed']}")
    else:
        print("Failed to fetch Most Viewed Page data:", response.json())

if __name__ == "__main__":
    get_average_time_data()
    get_most_viewed_data()