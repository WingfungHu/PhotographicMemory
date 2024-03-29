'''
Date: Friday, January 26 2024
Desc: This is the code designed with instructions to
        - Recieve an image url
        - pass the image url to online API
        - Preprocess the information
        - Send the information back to the backend
'''

import requests 

class Image_API:
    '''
    These are the keys and endpoints which allow us to access the computer vision serivces
    '''
    subscription_key = 'b2fce44dfd2b448c915051dcdec5426e'
    base_url = 'https://uofthacks11.cognitiveservices.azure.com//vision/v3.1/describe'

    def __init__(self):
        # empty
        return

    def get_image_description(self,url):
        
        assert self.subscription_key

        headers = {'Ocp-Apim-Subscription-Key': self.subscription_key, 'Content-Type': 'application/json'}
        params = {
            'language': 'en',  #Language is set to english
            'maxCandidates': '1',
        }
        #The url code for the picture, recieves the url from the 
        body = {
            'url': url
        }
        response = requests.post(self.base_url, headers=headers, params=params, json=body)
        response.raise_for_status()
        #stores the response which is a dictionary which stores another dictionary
        analysis = response.json()
        #returns
        return analysis['description']

        #print(analysis['description']['tags']) 

        ''' 
        image_tags = ' '.join(tag for tag in analysis['description']['tags'])
        print ('Image Tags: ',image_tags)
        '''
