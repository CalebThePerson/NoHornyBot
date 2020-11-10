import requests 
from redditapi import MyReddit
import praw
import urllib.request
from RandomWordGenerator import RandomWord
from PIL import Image
import os
import time
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
# SafeSubs = ["aww","dankmemes"]
nonsafe = ["juicyasians","Naked"]
UrlArray = []

for sub in nonsafe:
    subreddit = MyReddit.subreddit(sub)


    # topics_dict = { "title":[], 
    #             "id":[], 
    #             "url":[] }

    for submission in subreddit.top(limit = 250):
        # topics_dict["title"].append(submission.title)
        # topics_dict["id"].append(submission.id)
        # topics_dict["url"].append(submission.url)
        UrlArray.append(submission.url)

print(UrlArray)

R = RandomWord(max_word_size=5)
started = time.time()

for picture in UrlArray:
    NewName = R.generate()
    os.chdir("/home/pi/Desktop/Code/NoHornyBot/SourceCode/Horny")
    # Thepicture = urllib.request.urlretrieve(picture, f"{NewName}.jpg")
    if ".jpg"or ".png" in picture:
        try:
            ThePicture = requests.get(picture)
            with open(f"{NewName}.png","wb") as file:
                file.write(ThePicture.content)
                file.close()
        except requests.exceptions.ConnectionError:
            print("I must wait weeb")
            time.sleep(120)
        except requests.exceptions.MissingSchema:
            pass
    # image = Image.open(f"{NewName}.jpg")

    # image.save(f"/NoHorny/{NewName}.jpg", )
print("done")
print(f"It took about {time.time() - started}")
