import time

from behave import *
import json
import requests


@step("create request")
def request(context):
    apiUrl = "https://gorest.co.in/public/v2/users"
    path = "D:\Automation\InnsightProd_Framework_Hybrid_Behave\Features\API\steps\\response\\"
    name = "test.json"
    filename = path + name
    print(filename)
    chunk_size = 100
    # size of json

    # Send Get Request
    response = requests.get(apiUrl)
    exp_status_code = 200
    actual_status_code = response.status_code
    # print(response.raw)
    print(actual_status_code)
    if exp_status_code == actual_status_code:
        print('Response OK and json file saved into response folder with file name :: ' + name)
        with open(filename, 'wb') as fd:
            for chunk in response.iter_content(chunk_size):
                fd.write(chunk)
    else:
        print('Response Failed')
    # # Display Response Content
    data = open("D:\Automation\InnsightProd_Framework_Hybrid_Behave\Features\API\steps\\response\\test.json", "r").read()
    print(data)
    print("a")
    #
    def validateJSON(jsonData):
        try:
            json.loads(jsonData)
            print("Success")
        except ValueError as err:
            return False
        return True

    isValid = validateJSON(data)
    print("Given JSON string is Valid", isValid)
    #
    # # please make your own logic as per your requiements
    # # like read data and verify content with saved json file with your expected data
    #
    time.sleep()