import re
import spacy
import requests
from bs4 import BeautifulSoup
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English

def scrapping(url):
    response = requests.get(url)
    html = response.text
    read = BeautifulSoup(html, 'lxml')
    paragraphs = []
    for p in read.findAll('p'):
        paragraphs.append(p.text)
    text = "".join(paragraphs)
    return text


def process(data):

    # # python -m spacy download en

    nlp = spacy.load('en_core_web_lg')
    data = re.sub('([\+\-()\d]{1,8})', '', data)
    data = re.sub('\[*?\]', '', data)
    data = re.sub('Kathmandu, June', '', data)
    data= re.sub('Subscribe.*$', '', data)
    data = re.sub(',', '', data)
    data = data.lower()

    # Load English tokenizer, tagger, parser, NER and word vectors
    nlp = English()

    # Create the pipeline 'sentencizer' component
    sbd = nlp.create_pipe('sentencizer')

    # Add the component to the pipeline
    nlp.add_pipe(sbd)

    #creation of doc object containing our token features
    doc = nlp(data)
    # create list of sentence tokens
    sents_list = []
    for sent in doc.sents:
        sents_list.append(sent.text)
    print(sents_list)
    
    x=' '.join(sents_list)
    return x

