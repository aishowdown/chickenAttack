chickenAttack
=============
This repo contains the client code for the AI Showdown competition chickenAttack.  Please contribute back with improvements.

Story
    You just moved to the country and decided to start a chicken farm.  You dreamed of having thousands of free range chickens all throughout the country side... but then another chicken farmer moved in next door!  Your goal is to outsell your competitor at the market and put him out of business.  You have extremely well trained chickens and can direct them to either earn you more money, produce more chicks, or peck away at the other chickens to try and claim their land for your own.  Each space on the farm is good for different things.  Some produce a greater quantity of food, resulting in more chicks with which you may occupy the board, while others will yield a higher profit at the market each round that you control them.  The game ends after 1000 turns and the farmer who has earned the most money wins.

Files

    github: https://github.com/aishowdown/chickenAttack
    download: https://github.com/aishowdown/chickenAttack/archive/master.zip

    I would recommend using git to clone the project so that you can easily ‘git pull’ down any bug fixes or updates that may be made throughout the week.

Game details
    Each player starts with a small amount of food, but no money or guys

    On each turn:
        You are given all the locations of the chickens
        You decide where you want them to move (max of 1 space per chicken per round)
        All the chickens move at the same time
        If enemy chickens end up occupying the same space during a round, they fight to the death.  The person with the most chickens keeps the space but loses chickens equal to the number of their opponents chickens they had to kill.
        Each space on the farm then produces some amount of food and earns some amount of money at market for that space’s current owner.
        Based on how much food your farm has produced, chicks are born at your spawn point and the next round starts.  (The cost of x chicks is x1.1 and the maximum number of chicks possible are produced, but you may keep any remainder for the next round)

API
    Packaged with the game are two sample bots randomplayer.py and dumbplayer.py.  Use these as a jumping off point.  There are somewhat extensive comments in the example bots explaining how to program your bot.  If you would like to write your bot in a different language see below.

Running a game
    Put your bot in the same directory as the given code and simply run game.py with the filenames of the two bots you want to use as the arguments.

python game.py mybot1.py mybot2.py

    If you open viz.html in your browser you can see a game unfold.

Competition
    The final competition will take place next Saturday, August 24th at 2pm Est.  It will be a double elimination style competition, and the results of each round will be viewable on www.aishowdown.com.  Every evening preceding the competition we will run practice rounds.  Upload your bot to the website to get insight in what other people are creating.


Other Languages
    We allow players to write clients in other languages.  To do this, you will need to write a script that takes in a port via command line.  Listen on this port for POST requests containing json data.  The map will be sent at the beginning of the game to /map,  each round a post will be made to / with the current game state and expect json to be returned.  You can test these bots by running

python game.py nonnetworkedBot.py 2103

    where 2103 is the port your bot is listening on.


We need your help
    This is the first competition we are putting on and it has been a lot of hard work.  We would love to get any feedback you have on how to improve things.  We hope to host a competition every month.  If you would like to be involved in this (game designer, artist, tester, coder) or if you know a company that would be interested in sponsoring a tournament email us at aishowdown@gmail.com.







