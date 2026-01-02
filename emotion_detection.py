import requests

def emotion_detector(text_to_analyze):
    """Analyse a given text.
    uses emotion detector

    Returns:
        json: Person if found, with status of 200
        404: If not found
        400: If argument id is missing
        422: If argument id is present but invalid
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=header)
    #formatted_response = json.loads(response.text)
    
    return response.text
    