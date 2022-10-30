import cv2

framesPath = "/Users/victorchirino/Projects/slam-dunk-screenshots-bot/frames/"
videosFolderPath = "/Users/victorchirino/Projects/slam-dunk-screenshots-bot/videos/"

def extractImages(episode):
    count = 1
    if episode > 1:
      count = 21 # This is for avoid opening frames

    episodePath = f'{framesPath}episode-{episode}/'
    videoPath = f'{videosFolderPath}episode-{episode}.mp4'

    vidcap = cv2.VideoCapture(videoPath)
    success,image = vidcap.read()

    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*5000)) ## Screenshots every 5 seconds
        cv2.imwrite(episodePath + "frame-%d.jpg" % count, image)
        success,image = vidcap.read()
        print("Read a new frame: ", success)
        if success:
            count += 1
            if count > 254: # This is for avoid ending frames
                return 0
        else:
          return success
          

def main():
    episode = 13
    while True:
        if not extractImages(episode):
          episode += 1
        if episode > 25:
          break
        continue


if __name__ == '__main__':
    main()