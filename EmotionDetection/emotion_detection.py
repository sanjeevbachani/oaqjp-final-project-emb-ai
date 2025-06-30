import requests, json   # Import the requests, json library to handle HTTP requests
def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detector service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    # Custom header specifying the model ID for the emotion detector service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    formatted_response = json.loads(response.text) # Parsing the JSON response from the API
    emotion_predictions_list = formatted_response['emotionPredictions'] # Access the 'emotionPredictions' key:
    # Access the first element of the 'emotionPredictions' list (index 0):
    first_prediction = emotion_predictions_list[0]
    # Access the 'emotion' key within the first prediction dictionary:
    emotion_scores = first_prediction['emotion']
    anger_score = emotion_scores['anger']   # Access specific emotion values
    joy_score = emotion_scores['joy']   # Access specific emotion values
    sadness_score = emotion_scores['sadness']   # Access specific emotion values
    fear_score = emotion_scores['fear']   # Access specific emotion values
    disgust_score = emotion_scores['disgust']   # Access specific emotion values
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score,
    'joy': joy_score,'sadness': sadness_score, 
    'dominant_emotion': dominant_emotion
            } # Return the response text from the API