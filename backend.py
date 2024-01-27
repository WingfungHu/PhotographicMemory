import datetime as dt

import cohere_API
import Image_API

class Pictures():
    def __init__(self, url, label=None):
        self.url = url
        # TODO
        # Make API Call Here and Store the tags caption information:
        self.tags = "PLACE_HOLDER_tag_picture_"+str(label)
        self.caption = "PLACE_HOLDER_caption_picture_"+str(label)
        self.added_date = dt.datetime()

    def get_url(self):
        return self.url
    def get_tags(self):
        return self.tags
    def get_caption(self):
        return self.caption
    

class Backend():
    # List to store all the pictures uploaded
    pictures = []
    # List to store the chat history
    chat_history = []
    
    def __init__(self):
        # TODO
        # I might need to initiate API calls here just to make sure they are working and functional
        
        return
    
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
        # Creates a pictures object and stores it in pictures array
        created_picture = Pictures(url, label=len(self.pictures))
        self.pictures.append(created_picture)
        return True
    
    def execute_chatbot_input(self, input):
        # First store the user input
        user_input = ("User", input)
        self.chat_history.append(user_input)

        # TODO
        # Then make API Call
        # 
        response = "PlaceholderValueForChatbotResponse"

        # Next, store the chatbot's response
        chatbot_response = ("Bot", response)
        self.chat_history.append(chatbot_response)

        # Finally return chatbot response
        return chatbot_response
    
    

    
    