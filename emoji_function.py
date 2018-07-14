# -*- coding: utf-8 -*-
from __future__ import print_function, division
import api_helper
import json
import csv
import numpy as np
import pandas as pd
import tensorflow as tf
from deepmoji.sentence_tokenizer import SentenceTokenizer
from deepmoji.model_def import deepmoji_emojis
from deepmoji.global_variables import PRETRAINED_PATH, VOCAB_PATH

maxlen = 30
batch_size = 32

emoji_lookup = pd.read_csv("emoji-lookup.csv", encoding='utf-8').iloc[:,1].tolist()

with open(VOCAB_PATH, 'r') as f:
    vocabulary = json.load(f)
st = SentenceTokenizer(vocabulary, maxlen)
model = deepmoji_emojis(maxlen, PRETRAINED_PATH)
graph = tf.get_default_graph()



def get_emoji(sentences):
    global graph
    with graph.as_default(): 
        tokenized, _, _ = st.tokenize_sentences(sentences)
        prob = model.predict(tokenized)
        emoji = []
        for i, t in enumerate(sentences):
            emoji.append(zip(emoji_lookup,prob[i]))
    return emoji