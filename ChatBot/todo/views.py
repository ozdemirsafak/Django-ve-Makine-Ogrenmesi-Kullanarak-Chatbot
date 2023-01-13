from django.shortcuts import render,HttpResponse

from django.http import JsonResponse
import json
import numpy as np
import pickle
from tensorflow import keras


with open("C:/Users/Şafak/Desktop/ChatBot/todo/turkish_intents.json",encoding="UTF-8") as file:
    data = json.load(file)

model = keras.models.load_model('C:/Users/Şafak/Desktop/ChatBot/todo/chat_model')

    # load tokenizer object
with open('C:/Users/Şafak/Desktop/ChatBot/todo/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

    # load label encoder object
with open('C:/Users/Şafak/Desktop/ChatBot/todo/label_encoder.pickle', 'rb') as enc:
    lbl_encoder = pickle.load(enc)

# Create your views here.
def index(request):
    return render(request,"index.html")

def events(request):
    return render(request,"events.html")

def chat(request):
    return render(request,"chat.html")

def deneme(request):
    message = request.POST.get("message");
    return HttpResponse(message)

def chatbot_messages(request):
    message = request.GET.get('message', None)
    max_len = 30

    if message:
        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([message]),
                                                                          truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])
        tag_control = False
        print("tag ", tag)
        for i in data['intents']:
            if i['tag'] == tag:
                resonse = np.random.choice(i['responses'])
                tag_control = True
                break

        if not tag_control:
            resonse = "Sizi anlayamadım"

        return JsonResponse(
            {
                "response_message": resonse
            },
            safe=True
        )