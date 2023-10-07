from pytube import Playlist,YouTube

#function downloading 
def Download(link,x,title):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    print(f"..... Starting Downloading Video number {x+1} ")
    try:
        youtubeObject.download()
        print(f"{title}")
        print(f"Video number {x+1} has been DOWNLOADED *****")
    except:
        print(f"An error has occurred at Downloading video number {x+1}")

# getting the playlist you want to download 
print(".........................................")
url = input("Enter your Playlist URL :")

vlinks = Playlist(url)
print("")
print("Playlist name : ",vlinks.title)
print("NO of video : ",len(vlinks))
print("\n\n\n")
 # loops download each one of the videos 
for i in range(0,len(vlinks)):
	Download(vlinks[i],i,YouTube(vlinks[i]).title)
