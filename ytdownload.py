from pytube import YouTube
link="https://youtu.be/QGvgGtmEv64"
yt=YouTube(link)
videos=yt.streams.all()
vid=list(enumerate(videos))
for i in vid:
  print(i)
strm=int(input("Enter: "))
videos[strm].download()
print("Successfully downloaded ")
  