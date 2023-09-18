import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)

    formatted_response = json.loads(response.text)
    formatted_emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = formatted_emotions['anger']
    disgust_score = formatted_emotions['disgust']
    fear_score = formatted_emotions['fear']
    joy_score = formatted_emotions['joy']
    sadness_score = formatted_emotions['sadness']


    response_dict = {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score
    }

    response_dict['dominant_emotion'] = max(response_dict, key=response_dict.get)

    return response_dict
