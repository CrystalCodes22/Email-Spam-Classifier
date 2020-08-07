import requests
import json
import matplotlib.pyplot as plt
import pandas as pd

def get_prediction(data):
    url = 'https://l47syleshe.execute-api.us-east-1.amazonaws.com/Predict/88b81708-fbb3-4e39-a70d-619326e202bc'
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    return response

content = input("What was the email you got?")
words_list = content.split()
uniqeW = len(words_list)
totalW = len(set(words_list))

prediction = json.loads(json.loads(get_prediction({"content":content,"num_unique_words":uniqeW,"total_num_words":totalW}))['body'])['predicted_label']
print(prediction)