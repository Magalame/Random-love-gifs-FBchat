# -*- coding: UTF-8 -*-

from fbchat import Client
from fbchat.models import *
import datetime
import random
import time
import sys
import argparse

#------------------------Parsing arguments


parser = argparse.ArgumentParser()
parser.add_argument('-s','--start_time', action="store", dest="start_time")
parser.add_argument('-P','--stop_time', action="store", dest="stop_time")
parser.add_argument('-p','--password', action="store", dest="password")
parser.add_argument('-a','--email_address', action="store", dest="address")
parser.add_argument('-d','--destination_user', action="store", dest="destination")
parser.add_argument('-i','--user_id', action="store", dest="user_id")

args = parser.parse_args()

while not args.address:
    args.address = input("Please enter your adress:")

while not args.password:
    args.password = input("Please enter your password:")
    
while not args.destination:
    args.destination = input("Please enter the id of the person you want send gifs to:")

while not args.user_id:
    args.user_id = input("Please enter your user id:")

time_start_hour = args.start_time.split(':')[0]
time_start_min = args.start_time.split(':')[1]
time_stop_hour = args.stop_time.split(':')[0]
time_stop_min = args.stop_time.split(':')[1]

#-----------------------------------------

gifs= ["https://media.tenor.co/images/564eac526a8af795c90ce5985904096e/tenor.gif",
       "https://media.tenor.co/images/5d5565fe47af258d83b4caa2a668ccfa/tenor.gif",
       "https://media.tenor.co/images/c3759877cdcb86e25a1d305d5ac6fe4d/tenor.gif",
       "https://media.tenor.co/images/56ea2b419cd997350fb2d03c11ac724b/tenor.gif",
       "https://media3.giphy.com/media/f6y4qvdxwEDx6/200_d.gif",
       "https://media.tenor.co/images/23e82dfb8dbe7ef24e9dc8b2412411db/tenor.gif",
       "https://media.tenor.co/images/f6f20cda181ac07db50be80cdc4fa0c8/tenor.gif",
       "https://media.tenor.co/images/7daf1a191e6afe50c3ecf1ff446f1d4f/tenor.gif",
       "https://media.tenor.co/images/98764169e6a3003fc1fcf1feba434724/tenor.gif",
       "https://media.tenor.co/images/cd6f8d04b7d0e05f2d2b8ee5457cc4ee/tenor.gif",
       "https://media.tenor.co/images/77d90206206963c6aa5b05a2aa5c8c06/tenor.gif",
       "https://media.tenor.co/images/9c4a6d3cb294d01177a5b1e1544a5b9b/tenor.gif"]

client = Client(args.address, args.password)

SO = "<your SO's ID>"
me = "<yours>"

def printf(text):
    sys.stdout.write(str(text)+"\n")
    sys.stdout.flush()

while True:
    printf("---------------------------New loop---------------------------")
    messages = client.fetchThreadMessages(thread_id=args.destination, limit=50)
    for message in messages:
        if message.author == args.user_id:
            del messages
            break

    time_last_message = datetime.datetime.fromtimestamp(int(message.timestamp[:-3]))
    time_now = datetime.datetime.now()

    printf("Last message: \"" + message.text + "\" @ " + str(time_last_message))
    printf("Current time: " + str(time_now.time()))
    printf("Difference:" + str((time_now-time_last_message).seconds))

    if time_now.time() > datetime.time(time_start_hour, time_start_min) and time_now.time() < datetime.time(time_stop_hour, time_stop_min): 

        if (time_now-time_last_message).seconds > 3600:
            index=random.randrange(0,len(gifs))
            printf("Sending message number " + str(index))
            client.sendRemoteImage(gifs[index], message=Message(text="(petit calinou random <3 )"), thread_id=args.destination, thread_type=ThreadType.USER)
            printf("Image sent")

            delais = random.randrange(3600*2,3600*3)
            printf("Sleeping during " + str(delais) + "seconds")
            time.sleep(delais)
            #printf("Dors pendant " + str(delais) + "secondes")

        else:
            delais = random.randrange(0,3600*1)
            printf("Sleeping during " + str(delais) + "seconds")
            time.sleep(delais)

    else:
        delais = random.randrange(3600*3,3600*5)
        printf("Time doesn't fall in range, sleeping during " + str(delais) + "seconds")
        time.sleep(delais)



#local_time = utc_time.astimezone()
#print(local_time.strftime("%Y-%m-%d %H:%M:%S.%f%z (%Z)"))