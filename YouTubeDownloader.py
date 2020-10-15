from pytube import YouTube # imports library we need

link = input("Enter the YouTube link you would like to download: ") # asks the user for the link
yt = YouTube(link)

#Title of the video
print(f"Title: {yt.title}")
#Number of views the video has
print(f"Number of views: {yt.views}")
#The length of the video
print(f"Length of the video: {yt.length} seconds")
#Description of the video
print(f"Description of the video: {yt.description}")
#Rating
print(f"Rating: {yt.rating}")
#printing all the avilable streams
ys = yt.streams.get_highest_resolution()

#Starting to download

print("Downloading Video....")
ys.download()
print("Video Successfully Downloaded")
