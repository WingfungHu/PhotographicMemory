from cohere_api import Chatbot
from Image_API import Image_API
# TODO uncomment this:  Commenting it out now because its not a class or a function so whenever we start up the website it makes an API call
# import Image_API
# from flask import app

class Pictures():
    def __init__(self, url=None, tags=None, caption=None, label=None):
        self.url = url
        self.tags = tags
        self.caption = caption
        self.label = label
        # Make API Call Here and Store the tags caption information:
        # self.analysis = get_image_decsription(url=url)
        # if self.url:
        #     self.tags = self.analysis["tags"]
        #     self.caption = self.analysis["caption"]
        # else:
        #     print("Picture API call returned nothing for url:", url, file=sys.stderr)
        #     self.tags = "PLACE_HOLDER_tag_picture_"+str(label)
        #     self.caption = "PLACE_HOLDER_caption_picture_"+str(label)

        return
        # self.added_date = dt.datetime()

    def get_url(self):
        return self.url
    def get_tags(self):
        return self.tags
    def get_caption(self):
        return self.caption
    def __str__(self) -> str:
        str_return = ""
        str_return += "URL: " + self.url + " \n"
        str_return += "tags: " + self.tags + " \n"
        str_return += "caption: " + self.caption + " \n"
        # str_return += "added_date: " + self.added_date + " \n"
        return str_return



class Backend():
    # List to store all the pictures uploaded
    pictures = []
    # List to store the chat history
    chat_history = []

    def __init__(self):
        # TODO
        # I might need to initiate API calls here just to make sure they are working and functional
        self.image_api = Image_API()
        self.chatbot = Chatbot()
        return

    def print_current_state(self):
        state = {
            "pictures": self.pictures,
            "history": self.chat_history
        }
        return state

    def get_all_pictures(self):
        return self.pictures

    def get_single_picture(self, idx):
        return self.pictures[idx]

    def get_subset_pictures(self, picture_ids):
        # Given a set of picture IDs, which is its indicies, return that subset of pictures
        list_to_return = []
        for i in range(self.pictures):
            if i in picture_ids:
                list_to_return.append(self.pictures[i])
        return list_to_return

    def remove_single_picture(self, idx=None, url=None):
        # Given an index or url of picture, remove that picture from the set
        if idx is not None and url is None:
            self.pictures.pop(idx)
        elif idx is None and url is not None:
            idx_to_remove = -1
            for i in range(len(self.pictures)):
                if self.pictures[i].get_url() == url:
                    idx_to_remove = i
                    break
            if idx_to_remove != -1:
                self.pictures.pop(idx_to_remove)

    def upload_picture(self, url):

        # Make API call to obtain tags and captions
        description_dict = self.image_api.get_image_description(url)
        print("Dictionary Dict: " )
        print(description_dict)

        tag = description_dict["tags"]
        caption = description_dict["captions"]
        # tag = description_dict["tags"]

        # Creates a pictures object and stores it in pictures array
        created_picture = Pictures(url, tag, caption, label=len(self.pictures))
        print("HASDASDASD==================")
        self.pictures.append(created_picture)

        # Call CohereG.,Generate here first time image is uploaded
        image_tags = ', '.join(tag for tag in description_dict['tags'])
        image_text = ' '.join(text["text"] for text in description_dict['captions'])
        print("Image Tags:")
        print(image_tags)
        print("Image Text:")
        print(image_text)
        image_descriptions = image_tags + ": " + image_text
        print("Image Description")
        print(image_descriptions)
        generate_response = self.chatbot.generate(image_descriptions)

        # Add Chatbot Generate Response to chat history
        self.chat_history.append(generate_response)
        return generate_response

    def execute_chatbot_input(self, input):
        # First store the user input
        # user_input = ("User", input)
        user_input = input["userInput"]
        self.chat_history.append({"role": "User", "message": user_input})
        print(self.chat_history)
        # API Call to Cohere for Chat
        response = self.chatbot.chat(self.chat_history)
        # response = "PLACEHOLDER FOR BOT RESPONSE"
        print("CHATBOT RESPONSE")
        print(response)
        # Next, store the chatbot's response
        self.chat_history.append(response)
        # self.chat_history.append({"role": "Chatbot", "message": response})

        # Finally return chatbot response
        return response["message"]
