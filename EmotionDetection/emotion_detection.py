import requests
import json
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
    
    if response.status_code == 400:
        return {
                "anger": None, 
                "disgust": None, 
                "fear": None, 
                "joy": None, 
                "sadness": None, 
                "dominant_emotion":None,
                "status_code": 400
                }    
    
    # Assuming your variable is named json_output
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions,key=emotions.get)
    # 3. Append the dominant_emotion to the dictionary
    emotions['dominant_emotion'] = dominant_emotion
    return emotions
    