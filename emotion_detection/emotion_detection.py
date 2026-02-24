from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
import os
from dotenv import load_dotenv

load_dotenv()

def emotion_detector(text_to_analyze):
    if not text_to_analyze or not isinstance(text_to_analyze, str):
        return {'error': 'Invalid input: text must be a non-empty string'}
    try:
        authenticator = IAMAuthenticator(os.getenv('WATSON_API_KEY'))
        nlu = NaturalLanguageUnderstandingV1(
            version='2022-04-07',
            authenticator=authenticator
        )
        nlu.set_service_url(os.getenv('WATSON_URL'))
        response = nlu.analyze(
            text=text_to_analyze,
            features=Features(emotion=EmotionOptions())
        ).get_result()
        emotions = response['emotion']['document']['emotion']
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']
        emotion_scores = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
    except Exception as e:
        return {'error': f'Error during emotion detection: {str(e)}'}

if __name__ == '__main__':
    sample_text = "I am so happy and excited about this project!"
    result = emotion_detector(sample_text)
    print(result)