# https://glowingpython.blogspot.com/2014/09/text-summarization-with-nltk.html

from nltk.tokenize import sent_tokenize,word_tokenize # to split words and sentences
from nltk.corpus import stopwords # to delete the stopwords 
from collections import defaultdict # To avoid KeyError being,and it create new one instead.
from string import punctuation # to delete punctuation
from heapq import nlargest # Return a list with the n largest elements from the dataset defined by iterable

minimum_cut = .1
maximum_cut = .9
stop_words = set(stopwords.words('english') + list(punctuation))

				

def compute_frequencies(word_sent):
    """ 
      This function compute the frequency of each of word.
    """
    frequency = defaultdict(int)
    for s in word_sent:
      for word in s:
        if word not in stop_words:
          frequency[word] += 1
    # normalization and fitering for the frequencies
    max_val = float(max(frequency.values()))
    for w in list(frequency):
      frequency[w] = frequency[w]/max_val
      if frequency[w] >= maximum_cut or frequency[w] <= minimum_cut:
        del frequency[w]
    return frequency
#def
def summarize_txt(text, n):

    sents = sent_tokenize(text)
    assert n <= len(sents) 
    word_sent = [word_tokenize(s.lower()) for s in sents]
    freq = compute_frequencies(word_sent)
    ranking = defaultdict(int)
    for i,sent in enumerate(word_sent):
      for w in sent:
        if w in freq:
          ranking[i] += freq[w]
    sents_idx = rank(ranking, n)    
    return [sents[j] for j in sents_idx]

def rank(ranking, n):
    """ return the first n sentences with highest ranking """
    return nlargest(n, ranking, key=ranking.get)
