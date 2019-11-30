# Pocket Litter: An experiment in collaborative poetry
This repository is my final project for Digital Language Arts I.

# Motivation
By putting their art into the public sphere, artists must take responsibility for their work and its implications. The work is a product of their investment of time, energy, and creativity. The artist produces and the audience consumes. Additionally, much of the literary and visual cannon can be considered static--a piece is captured at one point in time. With my final project, I wanted to challenge this cannon on both levels. I wanted to produce a piece that (1) is produced by the audience and (2) is dynamic.

My final project, Pocket litter, is an experiment in collaborative poetry. I collected every piece of writing I've produced or downloaded on my computer to read and trained a neural net to produce words in that style. All it needs is a seed word or phrase--an investment of creativity from the audience. Who takes responsibility for the work produced by the piece? Is it the artist, who provided the architecture; the audience, who provided the spark of creativity; or the neural net, who put it all together?

# Methods
## Creating the corpus
In order to train a NLP model, you need a large collection of text. Fortunately, I've ported all my documents from computer to computer as I've gotten new ones. To create this corpus,

1. I collected every document with a `.doc` or `.docx` extension and put them in a single folder.
2. I wrote a script (`text_scraping.py`) that iterates through each document and aggregates the text in a `.txt` file.
3. Using Keras, I cleaned the text data and tokenized the corpus (`text_tokenize.py`)

## Training the model
Originally, I was planning on training my own model locally. However, given the time constraints of this project I ended up training the GPT2 model on my scraped corpus. Specifically, I used the [Google collab notebook](https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce#forceEdit=true&sandboxMode=true&scrollTo=8DKMc0fiej4N) created by [Max Woolf](http://minimaxir.com/). This notebook allows anyone to upload a text corpus, train a GPT2 model using a GPU, and provides an easy API to interact with the model. I trained the 124M model version for 1000 epochs.
