import requests 
from redditapi import MyReddit
import praw
import urllib.request
from RandomWordGenerator import RandomWord
from PIL import Image

'''
remember to create a redditapi file with this 
MyReddit = praw.Reddit(client_id="",
                     client_secret="",  #your client secret
                     user_agent="", #user agent name
                     username = "",
                     password = "") 
'''
#Creating the Non Horny Folder

#Getting The food images 
#, "dankmemes", "goodanimememes"
SafeSubs = ["FoodPorn","goodanimememes"]

UrlArray = []

for sub in SafeSubs:
    subreddit = MyReddit.subreddit(sub)


    # topics_dict = { "title":[], 
    #             "id":[], 
    #             "url":[] }

    for submission in subreddit.top(limit = 5):
        # topics_dict["title"].append(submission.title)
        # topics_dict["id"].append(submission.id)
        # topics_dict["url"].append(submission.url)
        UrlArray.append(submission.url)

print(UrlArray)

R = RandomWord(max_word_size=5)

for picture in UrlArray:
    NewName = R.generate()
    os.chdir("/Users/calebtheperson/PythonProjects/NoHornyBot/SourceCode/NoHorny")
    Thepicture = urllib.request.urlretrieve(picture, f"{NewName}.jpg")
    # image = Image.open(f"{NewName}.jpg")

    # image.save(f"/NoHorny/{NewName}.jpg", )
