"""
Provides unified CLI tools, namely IO (printing)
"""
from __future__ import print_function

import textwrap
from termcolor import cprint
from datetime import datetime

def test():
    cli_hline()
    cli_stdout('debug', "A debug print should be plain (because we'll get a lot of em!)")
    cli_stdout('debug', "The next message is a 'err' message")
    cli_stdout('err', "Test Error In my project, I have a bunch of strings that are read in from a file. Most of them, when printed in the command console, exceed 80 characters in length and wrap around, looking ugly.")

    cli_stdout('debug', "The next message is a 'info' message")
    cli_stdout('info', "Information messages should look like this. They need to stand out and so a nice background color will be used")

    cli_stdout('debug', "The next message is a 'warn' message")
    cli_stdout('warn', "Warnings should also stand out")

    cli_stdout('debug', "The next message is a 'good' message")
    cli_stdout('good', "Outputs will use the good message and should have their unique color as well!")

def cli_hline(line_len = 120):
    """Creates a horiz line
    """

    print('='*line_len)

def wrap_text(txt, wrap_at = 80):
    """Wraps a text to the required wrap length
    """

    return [txt[i:i+wrap_at] for i in range(0, len(txt), wrap_at)]

def cli_stdout_prompt(print_time=True):
    """The standard prompt to use for all CLI stdout messages

    Args
        - print_time (bool, optional): when false, the next message will not have 
                                       a timestamp, but will still align
    """

    prompt_template = "{:>33}"

    if print_time:
        prompt = prompt_template.format('[%s] >> ' % datetime.now())
    else:
        prompt = prompt_template.format('>> ')
    
    print(prompt, end='')

def cli_stdout(form, message):
    """Should be standard function when printing
    """

    if form == 'err':
        head = "Error"
        head_font_col = 'white'
        head_back_col = 'on_red'

        body_font_col = 'red'
        body_back_col = None
    if form == 'debug':
        head = None

        body_font_col = 'white'
        body_back_col = None
    if form == 'info':
        head = None

        body_font_col = 'white'
        body_back_col = 'on_blue'
    if form == 'warn':
        head = None

        body_font_col = 'yellow'
        body_back_col = None
    if form == 'good':
        head = None

        body_font_col = 'green'
        body_back_col = None

    #Printing is done here
    if isinstance(message, str) or isinstance(message, unicode):
        message = wrap_text(message)

    cli_stdout_prompt()
    if head is None:
        cprint(message[0], body_font_col, body_back_col)
        message.pop(0)
    else:
        cprint(head, head_font_col, head_back_col)
   
    for msg in message:
        cli_stdout_prompt(print_time=False)
        cprint(msg, body_font_col, body_back_col)

if __name__ == '__main__':
    test()