# -*- coding: cp1252 -*-

#Koodin luoja: Arne B�cklund

import sys
import spacy
from textacy import preprocessing as tprep
import pandas as pd
import numpy as np
from spacy.lang.fi.stop_words import STOP_WORDS as stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.decomposition import NMF


#ladataan aineisto datakehikkoon df
df=pd.read_csv("Twiitit_v1.csv",delimiter=",")


#ladataan spacyn suomenkielinen sanasto
nlp = spacy.load('fi_core_news_sm')

#funktio, jolla muunnettaan tekstist� url-osoiteet, s�hk�postiosoitteet ja emojit
#muotoon, jossa ne on helppo lis�t� poistosanoihin
def suodatus(teksti):
    teksti = tprep.replace.urls(teksti)
    teksti = tprep.replace.emails(teksti)
    teksti = tprep.replace.emojis(teksti)
    return teksti


for i, row in df.iterrows():
    df.at[i, "Tweet_mod"] = suodatus(row["Tweet"])


#suodatettuun dataan otetaan mukaan vain sanoja, jotka ovat
#substantiiveja, nimi�, adjektiiveja, adverbeja tai verbeja
nouns_adjectives_verbs = ["NOUN", "PROPN", "ADJ", "ADV", "VERB"]
for i, row in df.iterrows():
    #alkioidaan twiittien sis�lt�m� teksti
    doc = nlp(str(row["Tweet_mod"]))
    #perusmuotoistaminen
    #df.at[i, "lemmas"] = " ".join([token.lemma_ for token in doc])
    #perusmuotoistaminen, sanaluokkarajaus ja isot kirjaimet pieniksi
    df.at[i, "Suodatettu_Twiitti"] = " ".join([token.lemma_.lower() for token in doc
                     if token.pos_ in nouns_adjectives_verbs])


#lis��n poistosanoja spacyn tarjoamaan poistosanalistaan
stopwords2 = list(stopwords)+["url","emoji","email","co","yle","kuuntelee","piiri",\
                              "_pekko","toimia","k�ytt�","saada","tuoda",\
                              "lukea","suomalainen","tietotalo","kela",\
                              "osa","apteekki","korvauksen","terveystalo",\
                              "ottaa","hoitaa","tulevaisuus","suomi",\
                              "uutiset","t�ydent��","sote","silm�","sopia",\
                              "korvaa","varata","jyv�skyl�","laajeta",\
                              "palvelu","avata","p�iv�","jyvaskyla","klo",\
                              "stetoskoopilla","poliisi","webinaari","nokia",\
                              "kaupunki","l��k�r","digitaalise"]

#poistetaan poistosanat luotavasta matriisista
tfidf_text = TfidfVectorizer(stop_words=stopwords2, min_df=5)
#Dokumentti-termimatriisin muodostaminen
V_text_matrix = tfidf_text.fit_transform(df["Suodatettu_Twiitti"].map(str))
#Dokumentti-termimatriisissa on 1098 termi�
print(V_text_matrix.shape)

print("\nAihemallinnus menetelm�ll�:")
print("Ep�negatiivinen matriisifaktorointi\n")


#valitaan malliin kuusi aihetta
TOTAL_TOPICS=6

#sovitetaan ep�negatiivisen matriisifaktoroinnin malli
nmf_text_model = NMF(n_components=TOTAL_TOPICS, random_state=42)
nmf_model = NMF(n_components=TOTAL_TOPICS, solver="cd", max_iter=500,
                random_state=42, alpha=.1, l1_ratio=.85)
#Dokumentti-aihematriisi
W_text_matrix = nmf_text_model.fit_transform(V_text_matrix)
print(W_text_matrix.shape)
#Aihe-termimatriisi
H_text_matrix = nmf_text_model.components_
print(H_text_matrix.shape)


#funktio n�ytt�m��n mallin aiheet, joista n�ytet��n my�s 5 yleisint� termi�
def display_topics(model, features, no_top_words=5):
    for topic, word_vector in enumerate(model.components_):
        total = word_vector.sum()
        largest = word_vector.argsort()[::-1] 
        print("\nTopic %02d" % topic)
        for i in range(0, no_top_words):
            print("  %s (%2.2f)" % (features[largest[i]],
                  word_vector[largest[i]]*100.0/total))

display_topics(nmf_text_model, tfidf_text.get_feature_names_out())

pd.options.display.float_format = '{:,.3f}'.format
#t�h�n datakehikkoon tulee tieto siit� mink� osuuden twiiteist� aiheet muodostavat 
dt_df = pd.DataFrame(W_text_matrix, columns=['A'+str(i) for i in range(0, TOTAL_TOPICS)])

#luodaan datakehikko aiheiden lis��mist� varten
aihe_df = pd.DataFrame(columns=['Aihe', 'Aihe_2', 'Aihe_3'])

#laitetaan datakehikkoon kunkin 3 hallitsevinta aihetta laskevassa j�rjestyksess�
for i in range(len(dt_df)):
    top_topics = list(dt_df.columns[np.argsort(-
                            np.absolute(dt_df.iloc[i].values))[:3]])
    aihe_df.loc[i,'Aihe']=top_topics[0] #T�m� on dokumentin hallitseva aihe
    aihe_df.loc[i,'Aihe_2']=top_topics[1] #Toiseksi t�rkein aihe
    aihe_df.loc[i,'Aihe_3']=top_topics[2] #Kolmanneksi t�rkein aihe
    

print("\n",aihe_df.head(10))

#katsotaan twiittien jakautuminen aiheisiin
print(aihe_df.groupby("Aihe").agg('count'))


#liitet��n aineiston sis�lt�v��n datakehikkoon tieto aiheesta
aineisto_v = pd.merge(df, aihe_df['Aihe'], left_index=True, right_index=True)
#valitaan seuraavat tiedot uuteen datakehikkoon
aineisto_v2 = aineisto_v.loc[:,['Date','Username','Aihe','Tweet','Suodatettu_Twiitti']]
#tallennetaan csv-muotoiseen tiedostoon
aineisto_v2.to_csv('Twiitit_v2.csv', index=False, encoding='utf-8')



