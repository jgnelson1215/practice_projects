import requests, json

def sentiment_analyzer(text_to_analyze):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        # print(formatted_response)
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
        shorthand_response = {'label': label, 'score': score}
        return shorthand_response
    elif response.status_code == 500:
        return {'label': None, 'score': None}