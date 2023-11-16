# quote-leaderboard-bot

This bot was written with pycord. To install it run `python3 -m pip install py-cord`. Setup the bot by filling in the missing info by running `python3 ./setup.py` and providing the needed values. To run the bot, `python3 ./bot.py`. I realize security could be improved with environment variables but this wasn't meant to be hardened as that's not really needed.

This bot was written to keep track of how many times people are quoted in a specific channel. In order for quotes to register they must contain mentions for every person being quoted. Multiple people per message are allowed and will not cause an error, but a limitation in either Discord's API or pycord prevents multiple mentions of the same user (see [#1](https://github.com/bobbyl140/quote-leaderboard-bot/pull/1)).

This bot has the Channel ID hardcoded as I didn't write it to be portable. I may fix this at some point (see [#4](https://github.com/bobbyl140/quote-leaderboard-bot/issues/4), but until I do, the Channel ID can be replaced with either another baked-in number or a check for a list of Channel IDs without too much difficulty.

Also note that this code is in no way optimized. I'm sorry.
