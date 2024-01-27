'''
Date: Saturday, January 27 2024
Description: recieves the generated text and converts it to speech
'''
import azure.cognitiveservices.speech as speechsdk
from pydub.playback import play
from pydub import AudioSegment
import os
from flask import Flask, request, send_file#NEW
from flask_cors import CORS

app = Flask(__name__)#NEW

class tts_api:
    #The subscription key and service region needed to access the service
    subscription_key = 'e370f7cc63b042f2a1dd21387391bc2d'
    service_region = 'https://eastus.api.cognitive.microsoft.com/'

    #creates access to the service
    def __init__(self):
        self.speech_config = speechsdk.SpeechConfig(subscription=self.subscription_key,region=self.service_region)

@app.route('/convert', methods=['POST'])#NEW
def convert_to_speech():
    text = request.form['text']
    tts_service = tts_api()
    audio_file = tts_service.convert_to_speech(text)

    if audio_file:
        return send_file(audio_file, as_attachment=True)
    else:
        return "Conversion failed", 500
    '''
    #Audio config that specifies output audio file 
    # ***** check to see if you have to create that file or if it creates itself *****
    audio_config = speechsdk.audio.AudioOutputConfig(filename=filename)

    #creates speech synthesizer with specified audio config
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=audio_config)

    #tts conversion
    result = speech_synthesizer.speak_text_async(text).get()

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print ("Speech Synthesized to [{}]".format(filename))
        return filename
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print ("Speech Synthesis cancelled: {}".format(cancellation_details.reason))

    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
    return None
    '''
    '''
    #This method may need editing/replacing from
    #Start
    def play_audio(self,filename):
        if filename and os.path.exists(filename):
            audio = AudioSegment.from_wav(filename)
            play(audio)
        else:
            print("Audio file not found.")
    
       # Test the TextToSpeechService class
        def test_text_to_speech():
            tts_service = tts_api()
            
            # Convert text to speech
            audio_file = tts_service.convert_to_speech("Hello, this is a test of Microsoft's text to speech API.")

            # Play the audio file
            if audio_file:
                tts_service.play_audio(audio_file)
            else:
                print("Failed to convert text to speech.")
    #Finish       

         # Run the test
        test_text_to_speech()
    '''
#NEW    
if __name__ == '__main__':
    app.run(debug=True)   
CORS(app)





        