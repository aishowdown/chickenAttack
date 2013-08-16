chickenAttack
=============
This repo contains the client code for the AI Showdown competition chickenAttack.  Please contribute back with improvements.

Story
    You just moved to the country and decided to start a chicken farm.  You dreamed of having thousands of free range chickens all throughout the country side... but then another chicken farmer moved in next door!  Your goal is to fatten up your chickens to outsell your competitor at the market and put him out of business.  You are in control of your chickens and can decide to have them get fat, eat healthy to lay eggs, or peck away at the other chickens.  Each space on the farm produces a different amount of seed, some provide more nutritious food to help you get chickens, others help fatten up your chicks to get more money at the market.  The game ends after 1000 turns and the person whose chickens have eaten the most fatty seeds wins.

Files

github: https://github.com/aishowdown/chickenAttack
download: https://github.com/aishowdown/chickenAttack/archive/master.zip

Game details
    Each player starts with a small amount of food, but no money or guys

On each turn:
    You are given all the locations of the chickens
    You decide where you want them to move (1 space per chicken per round)
    All the chickens move at the same time
    If more than one enemy chickens are occupying the same space they fight to the death.  The person with the most chickens keeps the space but loses chickens equal to the number of their opponents chickens.
    The chickens then eat their feed (only enough on each spot for one chicken per turn).
    Based on how much nutritious food your chickens have eaten, they lay eggs at your spawn point and the next round starts.

API
    Packaged with the game are two sample bots randomplayer.py and dumbplayer.py.  Use these as a jumping off point).  If you would like to write your bot in a different language see below.

Running a game
    Put your bot in the same directory as the given code and simply run game.py with the filenames of the two bots you want to use as the arguments.

python game.py mybot1.py mybot2.py

    This updates viz.html with the game data.  If you open viz.html in your browser you can see a game unfold.  (You might want to decrease the NUM_TURNS in game.py to make games load faster)

Competition
    The final competition will take place next Saterday, August 24th at 2pm Est.  It will be a double elimination style competition, and the results of each round will be viewable on www.aishowdown.com.  Every evening preceding the competition we will run practice rounds, upload your bot to the website to get insight in what other people are creating.


Other Languages
    We allow players to write clients in other languages.  To do this, you will need to write a script that takes in a port via command line.  Listen on this port for POST requests containing json data.  The map will be sent at the beginnning of the game to /map,  each round a post will be made to / with the current game state and expect json to be returned.  You can test these bots by running

python game.py nonnetworkedBot.py 2103

    where 2103 is the port your bot is listening on.


We need your help
    This is the first competition we are putting on and it has been a lot of hard work.  We would love to get any feedback you have on how to improve things.  We hope to host a competition every month.  If you would like to be involved in this (game designer, artist, tester, coder) or if you know a company that would be interested in sponsoring a tournament email us at aishowdown@gmail.com.






