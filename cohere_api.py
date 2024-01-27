"""
Cohere api
"""

# !pip install cohere

import cohere
from cohere.responses.classify import Example

class Chatbot():


    co = cohere.Client('DGY7oZgN4dK8PExNW8BKfO6yNC3mKscV22D17OlZ')

    def __init__(self):
        return

    def generate(self, image_description: str) -> dict:
        generate_prompt = ("Using the description provided, craft one question following an empahthizing comment to "
                        "help draw out the nostalgic memories associated with this image. These questions are "
                        "designed to be conversational and non-intrusive, intending to encourage the individual to "
                        "reflect and share at their own pace, so refer to the past. Do not be too open ended or "
                        "add explanations of why you generated that text. Description for photo:")

        response = self.co.generate(
            model='command',
            prompt=generate_prompt + image_description,
            max_tokens=150,
            temperature=0.9,
            k=0,
            stop_sequences=[],
            return_likelihoods='NONE')

        return {"role": "Chatbot", "message": response[0].text}


    def chat(self, conversation: list) -> dict:
        chat_prompt = 'Continue the conversation naturally connecting from the chat_history'

        chatting = self.co.chat(
            model='command',
            message=chat_prompt,
            temperature=0.3,
            chat_history=conversation,
            connectors=[],
            documents=[]
        )

        return {"role": "Chatbot", "message": chatting.text}

    def classify(self, conversation: list) -> str:
        inputs = []

        examples = [
            Example("It was sad", "bad"),
            Example("There were waterslides and all kinds of food to taste!", "good"),
            Example("It made my day.", "good"),
            Example("I loved every minute of it;)", "good"),
            Example("I don't know", "bad"),
            Example("Very frustrating", "bad"),
            Example("It was lonely and pretty depressing", "bad"),
            Example("It was actually not bad, it was okay", "good"),
            Example("I mean, it was pretty intense", "bad"),
            Example("It gave me chills!", "good"),
        ]

        for i in range(len(conversation)):
            if conversation[i]["role"] == "User":
                inputs.append(conversation[i]["message"])

        response = self.co.classify(
            inputs=inputs,
            examples=examples,
        )

        if response.prediction == "good":
            return ("I hope you enjoyed our memory journey! "
                    "Cherish your memories and come back any time to chat with me about it!")
        else:
            return "Let our experiences pave our future, but not pull us down."
