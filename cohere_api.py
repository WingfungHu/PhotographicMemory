"""
Cohere api
"""

# !pip install cohere

import cohere

co = cohere.Client('DGY7oZgN4dK8PExNW8BKfO6yNC3mKscV22D17OlZ')


class Chatbot():
    """
  For cohere calls
  """
    def __int__(self):
        conversation = []
        image_description = ""
        generate_prompt = "Using the description provided, craft one question following an empahthizing comment to help draw out the nostalgic memories associated with this image. These questions are designed to be conversational and non-intrusive, intending to encourage the individual to reflect and share at their own pace, so refer to the past. Do not be too open ended or add explanations of why you generated that text. Description for photo: "

    def generate(self, generate_prompt: str, image_description: str, conversation: list) -> str:

        response = co.generate(
            model='command',
            prompt=generate_prompt + image_description,
            max_tokens=150,
            temperature=0.9,
            k=0,
            stop_sequences=[],
            return_likelihoods='NONE')

        conversation.append({"role": "Chatbot", "message": response[0].text})

        return response[0].text


    user_input = "It was for halloween! Lot's of fun!"

    conversation.append({"role": "User", "message": user_input})

    history = 'Continue the conversation naturally connecting from the chat_history'

    print(conversation)

    chat = co.chat(
        model='command',
        message=history,
        temperature=0.3,
        chat_history=conversation,
        connectors=[],
        documents=[]
    )

    conversation.append({"role": "Chatbot", "message": chat.text})

    # until user_input == "end chat" => while loop

    print(conversation)
