import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        emo_lst = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
        if emo_lst.index(max(emo_lst)) == 0:
            dominant_emotion = 'anger'
        elif emo_lst.index(max(emo_lst)) == 1:
            dominant_emotion = 'disgust'
        elif emo_lst.index(max(emo_lst)) == 2:
            dominant_emotion = 'fear'
        elif emo_lst.index(max(emo_lst)) == 3:
            dominant_emotion = 'joy'
        elif emo_lst.index(max(emo_lst)) == 4:
            dominant_emotion = 'sadness'
        shorthand_response = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion}
        return shorthand_response
    elif response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
