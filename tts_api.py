'''
Date: Saturday, January 27 2024
Description: recieves the generated text and converts it to speech
'''
import azure.cognitiveservices.speech as speechsdk
from pydub.playback import play
from pydub import AudioSegment
import os

class tts_api:
    #The subscription key and service region needed to access the service
    subscription_key = 'e370f7cc63b042f2a1dd21387391bc2d'
    service_region = 'https://eastus.api.cognitive.microsoft.com/'

    #creates access to the service
    def __init__(self):
        self.speech_config = speechsdk.SpeechConfig(subscription=self.subscription_key,region=self.service_region)

    def convert_to_speech(self,text, filename = "output_audio.wav"):
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
    
    def play_audio(self,filename):
        if filename and os.path.exists(filename):
            audio = AudioSegment.from_wav(filename)
            play(audio)
        else:
            print("Audio file not found.")




        