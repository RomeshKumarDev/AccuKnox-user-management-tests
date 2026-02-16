import requests
url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

try:
    response=requests.get(url)
    if response.status_code==200:
        print("Application is healthy",response.status_code)
    else:
        print("Application is not healthy. Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("An error occurred while checking application health:", e)        