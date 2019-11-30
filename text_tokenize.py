# LITR 0110D Final Project
# Purpose: Tokenize the text scraped from word files
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow import keras
from tensorflow.keras.layers import *
import tensorflow as tf
import numpy as np
from keras import preprocessing
from keras.preprocessing.text import text_to_word_sequence

# open the corpus file
corpus = open("/Users/Will/Desktop/myfile.txt","r")
raw_text = corpus.read()
print("File read in")

tokenizer = Tokenizer(nb_words=9000)
text = raw_text.split( "\\n" )
print("Text split on newline")
tokenizer.fit_on_texts(text)
print("Tokenizer fit on text")
total_words = len( tokenizer.word_index ) + 1
print("Found {} total words".format(total_words))
input_sequences = []

print("Training on {} lines of text".format(len(text)))
for line in text:
    token_list = tokenizer.texts_to_sequences([line])[0]
    print("{} tokens".format(len(token_list)))
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i + 1]
        input_sequences.append(n_gram_sequence)
print("Created token list and n_grams")

sequence_lengths = list()
for x in input_sequences:
    sequence_lengths.append( len( x ) )
max_sequence_len = max( sequence_lengths )
print("The max sequence length is {}".format(max_sequence_len))

input_sequences = np.array(pad_sequences(input_sequences,
                                         maxlen=max_sequence_len+1, padding='pre'))
x, y = input_sequences[:, :-1], input_sequences[:, -1]
y = keras.utils.to_categorical(y, num_classes=total_words)
print("Text preprocessed")

dropout_rate = 0.3
activation_func = keras.activations.relu

SCHEMA = [

    Embedding( total_words , 10, input_length=max_sequence_len ),
    LSTM( 32 ) ,
    Dropout(dropout_rate),
    Dense( 32 , activation=activation_func ) ,
    Dropout(dropout_rate),
    Dense( total_words, activation=tf.nn.softmax )

]
model = keras.Sequential(SCHEMA)
model.compile(
    optimizer=keras.optimizers.Adam() ,
    loss=keras.losses.categorical_crossentropy ,
    metrics=[ 'accuracy' ]
)
model.summary()

model.fit(
    x,
    y,
    batch_size=50 ,
    epochs=150,
)

def predict(seed_text , seed=10 ):

    for i in range( seed ):

        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=
        max_sequence_len , padding='pre')
        predicted = model.predict_classes(token_list, verbose=0 )
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word

    return seed_text

print(
  predict(
    input( 'Enter some starter text ( I want ... ) : ') ,
    int( input( 'Enter the desired length of the generated sentence : '))
  )
)

result = text_to_word_sequence(text)
print(result)
