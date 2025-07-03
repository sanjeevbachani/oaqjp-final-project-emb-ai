import requests, json   # Import the requests, json library to handle HTTP requests
def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detector service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    # Custom header specifying the model ID for the emotion detector service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    formatted_response = json.loads(response.text) # Parsing the JSON response from the API
    if response.status_code == 200: #If the response status code is 200, extract the label and score from the response
        emotion_predictions_list = formatted_response['emotionPredictions'] # Access the 'emotionPredictions' key:
        first_prediction = emotion_predictions_list[0]  # Access the first element of the 'emotionPredictions' list (index 0):
        emotion_scores = first_prediction['emotion'] # Access the 'emotion' key within the first prediction dictionary:
        anger_score = emotion_scores['anger']   # Access specific emotion values
        joy_score = emotion_scores['joy']   # Access specific emotion values
        sadness_score = emotion_scores['sadness']   # Access specific emotion values
        fear_score = emotion_scores['fear']   # Access specific emotion values
        disgust_score = emotion_scores['disgust']   # Access specific emotion values
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        #return response.status_code
        return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score,'joy': joy_score,'sadness': sadness_score, 
        'dominant_emotion': dominant_emotion } # Return the response text from the API
    elif response.status_code == 400:
        #emotion_predictions_list = formatted_response['emotionPredictions'] # Access the 'emotionPredictions' key:
        #first_prediction = emotion_predictions_list[0]
        emotion_scores = None
        anger_score = None
        joy_score = None
        sadness_score = None
        fear_score = None
        disgust_score = None
        dominant_emotion = "test1"
        #return response.status_code
        return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score,'joy': joy_score,'sadness': sadness_score, 
        'Dominant_Emotion': dominant_emotion } # Return the response text from the API
    elif response.status_code == 500:
        #emotion_predictions_list = formatted_response['emotionPredictions'] # Access the 'emotionPredictions' key:
        #first_prediction = emotion_predictions_list[0]
        emotion_scores = None
        anger_score = None
        joy_score = None
        sadness_score = None
        fear_score = None
        disgust_score = None
        dominant_emotion = "test2"
        #return response.status_code
        return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score,'joy': joy_score,'sadness': sadness_score, 
        'Dominant_Emotion': dominant_emotion } # Return the response text from the API
    #return response.status_code
    