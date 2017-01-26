#!/usr/bin/env python
"""
Interactive Interface for the Twitter Sentiment Analysis App
Usage:
    my_program fetch <username>
    my_program wordfrequency
    my_program sentiment
    my_program (-i | --interactive)
    my_program (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit

from tweet import *
from util import *
from analysis import *

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class AnalyzerCmd (cmd.Cmd):
    intro = '''                 Twitter Sentiment Analysis\n
               Type help to view list of commands\n'''
    prompt = 'TWEET SENTIMENT ANALYSIS:> '
    file = None

    @docopt_cmd
    def do_fetch(self, args):
        """Usage: fetch <username>"""
        self.tweets = get_tweets((args['<username>']))

    @docopt_cmd
    def do_sentiment(self, args):
        """Usage: sentiment """
        print(alchemy(' '.join(self.tweets)))

    @docopt_cmd
    def do_wordfrequency(self, args):
        """Usage: wordfrequency """
        print(most_freq_words(tweets_to_words(self.tweets)))

    def do_home(self):
        pass

    def do_quit(self, args):
        """Quits out of Interactive Mode."""
        print('Exiting ....')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    AnalyzerCmd().cmdloop()

print(opt)
