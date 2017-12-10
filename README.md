# Random love gifs

This is a small program that check every X seconds (or minutes or hours) if you sent a message to the person you like on Facebook. 
More exactly, if no message was sent in that interval X, then the program will send a random gif. 
You can add your own gifs to the predefined list, or completely wipe it and only put yours.


## How to use it?

First download the script:

`wget https://raw.githubusercontent.com/Magalame/Random-love-gifs-FBchat/master/random_love_gifs.py`

then launch it:

`python3 random_love_gifs.py`

You will first be asked about your email, the one you use for Facebook, then about your password. 

Then the program will ask you if you want to see your friend list printed. If it is the first time you use it please press yes, 
as next to each name will be printed an ID number, and you will need that number: that it the way the program recognize you want to send gifs too, 
it is much more pratical than dealing with names because of space, accents, homonyms, etc.

Right after you'll have to type the ID we just talked about, just copy paste it. 

Afterwards you'll be asked for the active period of the program: it will only be allowed to send gifs between a certain bracket, like from 9am to 10pm. 
Please use the 24h format, or you might get a weird result.

You will also have to specify the delay we talked about at the beginning: if you write 3600, then the program will check each hour if a message was sent the last hour. 

And eventually, you can type a little message you want to attach to the gif that will be sent!

## Todo:
* allow to specify the delay in hours/minutes rather than seconds
* allow to type in the gifs one can add instead of relying solely on command line arguments
