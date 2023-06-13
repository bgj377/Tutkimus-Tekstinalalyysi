
#koodin luoja: Arne Bäcklund

import sys
import spacy
import pandas as pd
import numpy as np
import statistics
from datetime import datetime
from spacy.lang.en.stop_words import STOP_WORDS as stopwords
from googletrans import Translator
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import opinion_lexicon
from nltk.tokenize import word_tokenize

#Googlen käännöstyökalu
translator = Translator()

df=pd.read_csv("Twiitit_v2.csv",delimiter=",")


#Tehdään "Päivämäärä"-muuttuja, joka on tyyppiä Date
for i, row in df.iterrows():
    rivi = row["Date"]
    paivays = rivi[0:10] #halutaan mukaan vain vuodet, kuukaudet ja päivät
    df.at[i, "Päivämäärä"] = datetime.strptime(paivays, '%Y-%m-%d')

#Määritellään uudet nimet sarakkeille
column_mapping = {
    'Date': None, # ei tule mukaan
    'Päivämäärä':'Päivämäärä',
    'Username': 'Käyttäjätunnus',
    'Aihe': 'Aihe',
    'Tweet': 'Twiitti',
    'Suodatettu_Twiitti':'Suodatettu_Twiitti'
}

columns = [c for c in column_mapping.keys() if column_mapping[c] != None]

#Uudelleennimeäminen
df = df[columns].rename(columns=column_mapping)
print(df.columns)


#Käännetään twiitit englanniksi omaan muuttujaansa
for i, row in df.iterrows():
    result = translator.translate(str(row["Twiitti"]))
    df.at[i,"Twiitti_englanniksi"] = result.text.lower()

print(df["Twiitti_englanniksi"].head(10))
print(df.loc[11:22,["Twiitti_englanniksi"]])

print("\nTunneanalyysi menetelmällä: VADER-tunnesanasto\n")

#tunnearvo välillä -1: erittäin negatiivinen 1: erittäin positiiivinen
def tunne_Vader(teksti):
    #tekstin esiprosessointi: alkiointi ja suurten kirjainten muuntaminen pieniksi
    alkiot = word_tokenize(teksti)
    analyzer = SentimentIntensityAnalyzer()
    rimpsu = ""
    for sana in alkiot:
        rimpsu = rimpsu + str(sana)+ " "
    #käytetään Vader-tunneanalyysia twiittiin
    v_arvot = analyzer.polarity_scores(rimpsu)
    #otetaan yhdistetty tunnearvo twiitille
    yhd_tunnearvo = v_arvot['compound']
    return yhd_tunnearvo

#luokitellaan tunteet yhdistetyn tunnearvon kynnysarvojen avulla
def tunne_Luokka(yhd_tunne):
    #kynnysarvot
    ala_kynnys = -0.4
    yla_kynnys = 0.4
    if yhd_tunne <= ala_kynnys:
        luokka = "negatiivinen"
    elif yhd_tunne >= yla_kynnys:
        luokka = "positiivinen"
    else:
        luokka = "neutraali"
    return luokka

print(df.loc[0:20,['Twiitti_englanniksi','Tunneluku','Tunneluokka']])


for i, row in df.iterrows():
    df.at[i,"Tunneluku"] = tunne_Vader(row["Twiitti_englanniksi"])

for i, row in df.iterrows():
    df.at[i,"Tunneluokka"] = tunne_Luokka(row["Tunneluku"])

#järjestetään twiitit aiheen mukaan
ain = df.sort_values(by=["Aihe"])
#tallennetaan csv-tiedostoon
ain.to_csv('Twiitti_Aineisto.csv', index=False, encoding='utf-8')
