# quote-leaderboard-bot

This bot was written with pycord. To install that, run `python3 -m pip install py-cord`. Setup the bot by filling in the missing info with `python3 ./setup.py` and providing the needed values. To run the bot, `python3 ./bot.py`. I realize security could be improved with environment variables but this wasn't meant to be hardened as that's not really needed.

This bot was written to keep track of how many times people are quoted in a specific channel (or channels). In order for quotes to register they must contain mentions for every person being quoted. Multiple people per message are allowed and will not cause an error, but a limitation in either Discord's API or pycord prevents multiple mentions of the same user (see [#1](https://github.com/bobbyl140/quote-leaderboard-bot/pull/1)).

NOTE: By default the bot runs silently. This means quotes will only be acknowledged by the reaction, and a message won't be sent back for invalid quotes. If your users are new to this bot, consider uncommenting the revelant lines under the `on_message()` function for a while.

Also note that this code is in no way optimized. I'm sorry.
