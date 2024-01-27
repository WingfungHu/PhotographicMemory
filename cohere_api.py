"""
Cohere api
"""

# !pip install cohere

import cohere

co = cohere.Client('DGY7oZgN4dK8PExNW8BKfO6yNC3mKscV22D17OlZ')


def generate(self, image_description: str) -> dict:
    generate_prompt = ("Using the description provided, craft one question following an empahthizing comment to "
                       "help draw out the nostalgic memories associated with this image. These questions are "
                       "designed to be conversational and non-intrusive, intending to encourage the individual to "
                       "reflect and share at their own pace, so refer to the past. Do not be too open ended or "
                       "add explanations of why you generated that text. Description for photo:")

    response = co.generate(
        model='command',
        prompt=generate_prompt + image_description,
        max_tokens=150,
        temperature=0.9,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE')

    return {"role": "Chatbot", "message": response[0].text}


def chat(conversation: list) -> dict:
    chat_prompt = 'Continue the conversation naturally connecting from the chat_history'

    chat = co.chat(
        model='command',
        message=chat_prompt,
        temperature=0.3,
        chat_history=conversation,
        connectors=[],
        documents=[]
    )

    return {"role": "Chatbot", "message": chat.text}
