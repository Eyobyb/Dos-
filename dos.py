import urllib.request
import _thread


# Define a function for the thread
def print_time(threadName , tradesNo , URL):
    counter=0
    while(True):
        with urllib.request.urlopen('http://'+URL) as response:
           html = response.read()
        print(threadName ,"" ,tradesNo)
        print()
        counter = counter+1
# Create two threads as follows
def functionRunner(traidNo,URL):
    try:
        for i in range(0,traidNo):
           _thread.start_new_thread( print_time, ("Thread",i,URL ) )
          
    except:
       print ("Error: unable to start thread")

    while 1:
       pass
def main():
    numbs = eval(input("Number Of trades?  : "))
    #you can use this url for example localhost:4000/api/movieList from the past project
    URL = input("URL? : http://")
    functionRunner(numbs,URL)
main()
