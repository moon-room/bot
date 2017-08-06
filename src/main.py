from helpers import set_interval
import constants
import rex
import twitter
import logician


def moon_call():
    symbols = rex.get_market_symbols()

    for symbol in symbols:
        modified = "$" + symbol

        tweets = twitter.search(modified)
        relevant_tweets = logician.strip_irrelevant(tweets)
        score = logician.judge(relevant_tweets)
        # TODO: store score to symbol_score database

    # telegram results over a certain threshold.


set_interval(moon_call, constants.DEFAULT_MINS)
