import gpt_2_simple as gpt2
import os
import requests
import re
from blessings import Terminal
import logging
import textwrap 


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # FATAL
logging.getLogger('tensorflow').setLevel(logging.FATAL)

# Helper functions ---
def corr(s):
	return re.sub(r'\.(?! )', '. ', re.sub(r' +', ' ', s))

def generate_text(user_inp, out_len=300):
	"""consumes user text, returns short generated text
	param user_inp: user provided input seed
	param out_len: user provided length for output (default 100)
	returns: output string of length out_len
	"""
	text = gpt2.generate(sess,
				  length=out_len,
				  temperature=0.74,
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
			  run_name="run2",
			  checkpoint_dir="checkpoint")

# start cli loop
wrapper = textwrap.TextWrapper(width=50) 
term = Terminal()
os.system('cls' if os.name == 'nt' else 'clear')
while True:
	with term.location(0, term.height - 1):
		print(term.cyan + term.bold + "Tell me your full name:" + term.normal)
		name = str(input())
		print(term.cyan + term.bold + "How should we start our poem?" + term.normal)
		prompt = str(input())
		if prompt == "end_program":
			break
		output = generate_text(prompt)
		string = wrapper.fill(text=output)
		os.system('cls' if os.name == 'nt' else 'clear')
		print("{}, by {}".format(prompt, name))
		print("--------------------------------------------------")
		print(string, flush=True)
		print("--------------------------------------------------")

		input(term.bold("\nPress Enter to continue..."))
		os.system('cls' if os.name == 'nt' else 'clear')


print(corr(text))
