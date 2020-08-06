import requests
import json
  
def get_prediction():
    url = 'https://l47syleshe.execute-api.us-east-1.amazonaws.com/Predict/88b81708-fbb3-4e39-a70d-619326e202bc'
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r,'_content').decode("utf-8")
    return response

content = input("What was the email you got?")
uniqeW = input("How many unique words are there?")
totalW = input("How many words are their total?")

prediction = get_prediction(data={"content":content,"num_unique_words":uniqeW,"total_num_words":totalW})