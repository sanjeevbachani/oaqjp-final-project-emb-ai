from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector Watson Tool")
@app.route("/emotionDetector")
def emo_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    # Return a formatted string with the sentiment label and score
    
    anger_score = response['anger']
    joy_score = response['joy']
    sadness_score = response['sadness']
    disgust_score = response['disgust']
    fear_score = response['fear']
    dom_emotion = response['dominant_emotion']
    # Return a formatted string with the sentiment label and score
    formatted_string = f"For the given statement, the system response is 'anger' : {anger_score}, 'disgust' : {disgust_score}, 'fear' : {fear_score}, 'joy' : {joy_score} and 'sadness' : {sadness_score}. <br>The dominant emotion is <b>{dom_emotion}</b>"
    if dom_emotion is None:
        return "Invalid Text! Please try again!"
    else:
        return formatted_string
        
@app.route("/")
def render_index_page():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)