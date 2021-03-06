import logging
import time
from twitter import Twitter, OAuth
import os

consumer_key = os.environ.get('TWITTER_BOT_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_BOT_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_BOT_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_BOT_ACCESS_TOKEN_SECRET')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def twitter_Oauth():
  return OAuth(token=access_token,
    token_secret=access_token_secret,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret)

def upload_media(auth, image_data):
    t_up = Twitter(domain='upload.twitter.com', auth=auth)
    media_id = t_up.media.upload(media=image_data)["media_id_string"]
    return media_id


def main():
    frame_id = 1
    episode = 1
    auth= twitter_Oauth()
    t = Twitter(auth=auth)

    while True:
        frames_folder = f"episode-{episode}"
        image= f"frames/{frames_folder}/frame_{frame_id}.jpg"
        try:
          file = open(image, 'rb')
        except:
          print(f"Image file not found {image}")
          frame_id = 1
          episode += 1
          continue

        image_data = file.read()
        media_id = upload_media(auth, image_data)

        try: 
          t.statuses.update(media_ids=",".join([media_id]))
          print("Tweet posted OK")
        except:  
          print('Error')

        logger.info("Waiting...")
        frame_id += 1
        time.sleep(60*60*1) # 1 hours

if __name__ == '__main__':
    main()
