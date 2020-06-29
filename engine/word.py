from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import urllib
import wikipedia
import os
import requests
import numpy as np
import matplotlib.pyplot as plt
import sys
        


source = sys.argv[1]
dest = sys.argv[2]
color = sys.argv[4]
text = sys.argv[3]
currdir = os.path.dirname(__file__)
sourcepath = os.path.join(currdir,'../source')
destpath = os.path.join(currdir,'../destination')
#mask  = np.array(Image.open(os.path.join( sourcepath, 'cc.jpg')))
# This function takes in your text and your mask and generates a wordcloud. 
def get_value(place1, place2, text, color):
    def get_wiki(query):
        title = wikipedia.search(query)[0]
        page = wikipedia.page(title)
        return page.content
    def generate_wordcloud(text):
        mask  = np.array(Image.open(os.path.join( sourcepath, place1)))
        word_cloud = WordCloud(width = 512, height = 512, background_color= color, stopwords=STOPWORDS, max_words=1000, mask=mask)
        word_cloud.generate(text)
        word_cloud.to_file(os.path.join(destpath, place2))
    
#Run the following to generate your wordcloud
    generate_wordcloud(get_wiki(text))
get_value(source, dest, text, color)    
