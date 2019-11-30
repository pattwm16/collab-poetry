import gpt_2_simple as gpt2
import os
import requests
import re
from blessings import Terminal
import logging

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # FATAL
# logging.getLogger('tensorflow').setLevel(logging.FATAL)

# Helper functions ---
def corr(s):
    return re.sub(r'\.(?! )', '. ', re.sub(r' +', ' ', s))

def generate_text(user_inp, out_len=100):
    """consumes user text, returns short generated text
    param user_inp: user provided input seed
    param out_len: user provided length for output (default 100)
    returns: output string of length out_len
    """
    text = gpt2.generate(sess,
                  length=out_len,
                  temperature=0.7,
                  prefix=user_inp,
                  nsamples=5,
                  batch_size=5,
                  return_as_list=True)[0]
    return corr(text)

# Code body ---
# instantiate the model session
sess = gpt2.start_tf_sess()
# load the model
gpt2.load_gpt2(sess,
              run_name="run1",
              checkpoint_dir="checkpoint")

# start cli loop
term = Terminal()
while True:
    with term.location(0, term.height - 1):
        print('This is', term.underline('pretty!'))
        print(term.red + term.on_green + 'Red on green? Ick!' + term.normal)
        print(term.bright_red + term.on_bright_blue + 'This is even worse!' + term.normal)
        print("Enter your prompt:")
        prompt = str(input())
        if prompt == "end_program":
            break
        print(generate_text(prompt), flush=True)


print(corr(text))
