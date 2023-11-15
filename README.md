# quote-leaderboard-bot

This bot was written with pycord. To install it run `python3 -m pip install py-cord`. To run the bot, paste your token into the `run() `line at the end, paste the target Channel ID into the relevant line under the `on_message()` function (see below), and `python3 ./bot.py`. I realize security could be improved with environment variables but this wasn't meant to be hardened as that's not really needed.

This bot was written to keep track of how many times people are quoted in a specific channel. In order for quotes to register they must contain mentions for every person being quoted. Multiple people per message are allowed and supported, but a limitation in either Discord's API or pycord prevents multiple mentions of the same user.

This bot has the Channel ID hardcoded as I didn't write it to be portable. I may fix this at some point, but until I do, the Channel ID can be replaced with either another baked-in number or a check for a list of Channel IDs without too much difficulty.

Also note that this code is in no way optimized. I'm sorry.
