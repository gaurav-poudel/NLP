#import spacy 
import streamlit as st
import re
#from spacy.tokens import token

from gensim.summarization import summarize

import spacy 
from textblob import TextBlob
import matplotlib.pyplot as plt 

from wordcloud import WordCloud, STOPWORDS
import wordcloud


def text_analyzer(my_text):
    nlp = spacy.load('en_core_web_sm')
    docx = nlp(my_text)
    tokens =[token.text for token in docx]
    alldata = [(' "Tokens":{},\n "Lemma":{}'.format(token.text,token.lemma_)) for token in docx]
    return alldata



def name_entity(my_text):
    nlp = spacy.load('en_core_web_sm')
    docx = nlp(my_text)
    tokens =[token.text for token in docx]

  
    docx = nlp(my_text)
    entities = [(entity.text,entity.label_)for entity in docx.ents]
    allData = ['"Tokens":{},\n"Entities":{}'.format(tokens,entities)]

    return allData






#st.header("Wiki Text Cleaning")

def cleaner(artical):
    artical = str(artical)

    rem_url = re.sub(r'http\S+', '',artical)
    
    rem_symbols = re.sub(r'[^\w\s ]','',rem_url)

    return rem_symbols


def main():
    sidebar_selection = ['Home','Cleaning','NLP']
    choice = st.sidebar.selectbox("Select Bar",sidebar_selection)
    if choice == 'Cleaning':
        st.header("Artical Cleaning")
        
        artical = st.text_area("Enter your artical(Large paragraph)","Text Here")

        if st.button("Clean Paragraph"):
            st.success(cleaner(artical))
            


        if st.button("Summarize The Artical"):
            #lean_text_to_summ = clean_text
            summary_result = summarize(artical)
            st.success(summary_result)

        if st.button("Word Cloud"):
            text = artical
            stopwords = STOPWORDS
            wc = WordCloud(
                background_color = 'white',
                stopwords=stopwords,
                height = 600,
                width = 400
            )

            wordcloud = WordCloud().generate(text)
            plt.imshow(wordcloud,interpolation='bilinear')
            plt.axis('off')
            plt.show()
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
        if st.button("Sentiment Analysis"):
            blob = TextBlob(artical)
            result_sentiment = blob.sentiment
            if result_sentiment.polarity > 0:
                st.markdown("Positive Sentiment ::: :smiley:  ")
            elif result_sentiment.polarity < 0:
                st.markdown("Negative Sentiment ::: :angry: ")
            else:
                st.markdown("Neutral Sentiment ::: 😐  ")
            st.success(result_sentiment)
            

            


    elif choice == 'Home':
        st.header("This is Text analysis")
        st.subheader("A project based on NLP techniques")
    
    
   #elif choice == 'NLP':
        #select_choice = ["Show token and lemma","Show Name Entity","Sentiment Analysis","Text Summarization"]
        #bar_choice = st.selectbox("Select",select_choice)



        #if bar_choice == "Show token and lemma":
            #text = st.text_area("Enter your text")
            
            

            #if st.button("Analysis"):
                #nlp_result = text_analyzer(text)
                #st.json(nlp_result)

        #if bar_choice == "Show Name Entity":
            #text = st.text_area("enter your text")
            
            

            #if st.button("Analysis"):
                #nlp_result = name_entity(text)
                #st.json(nlp_result)

        #if bar_choice == "Sentiment Analysis":
            #text = st.text_area("enter your text")
            
            

            #if st.button("Analysis"):
                #blob = TextBlob(text)
                #result_sentiment = blob.sentiment
                #st.success(result_sentiment)

        #if bar_choice == "Text Summarization":
            #text = st.text_area("enter your text")
            #if st.button("Summarize "):
                #summary_result = summarize(text)
                #st.success(summary_result)
                
                

        




main()











