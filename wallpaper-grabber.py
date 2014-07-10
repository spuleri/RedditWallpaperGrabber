#grabbing wallpaper files from top posts of r/wallpapers and saving to local folder
import praw #->Python reddit API Wrapper
import urllib

def main():

  r = praw.Reddit(user_agent='wallpaper_grabber')
  submissions = r.get_subreddit('wallpapers').get_hot(limit=15) #getting top submissions and putting them in an array

  urls = [] #initializing empty array for the direct image links of the wallpapers
  for i in submissions:
  	urlstring = i.url  	
  	if urlstring.startswith('http://i.'): #checking to make sure the link is just the plain image file (and not an album)  	  
  	  urls.append(i.url) #adding the urls of the submission links to the urls array

  for j in urls:
  	urllib.urlretrieve(j, "F:\Dropbox\Programming\PythonStuff\RedditWallpaperGrabber\DownloadedWalls\%s.jpg" % (urls.index(j)))
  	#using the urllib library to download each url string to a local file on the computer
  	#change the path to a directory you'd like to save the wallpapers

if __name__ == '__main__':
  main()


