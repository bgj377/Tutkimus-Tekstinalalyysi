# -*- coding: cp1252 -*-

import snscrape.modules.twitter as sntwitter
import pandas as pd

#twiittien haku snscrape-ohjelmalla


twiitit = [] #lista
query = "digi terveys" #hakutermi
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    twiitit.append([tweet.date, tweet.user.username, tweet.rawContent])

#tallennetaan tietokehikkoon
df_1 = pd.DataFrame(twiitit, columns=['Date', 'Username', 'Tweet'])
#tallennetaan tietokehikko csv-tiedostoon
df_1.to_csv("digi terveys.csv", index=False, encoding='utf-8')

twiitit = []
query = "digitaalinen terveydenhuolto"
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    twiitit.append([tweet.date, tweet.user.username, tweet.rawContent])

#tallennetaan tietokehikkoon
df_2 = pd.DataFrame(twiitit, columns=['Date', 'Username', 'Tweet'])
#tallennetaan tietokehikko csv-tiedostoon
df_2.to_csv("digitaalinen terveydenhuolto.csv", index=False, encoding='utf-8')

twiitit = []
query = "digitalisaatio terveydenhuolto"
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    twiitit.append([tweet.date, tweet.user.username, tweet.rawContent])

#tallennetaan tietokehikkoon
df_3 = pd.DataFrame(twiitit, columns=['Date', 'Username', 'Tweet'])
#tallennetaan tietokehikko csv-tiedostoon
df_3.to_csv("digitalisaatio terveydenhuolto.csv", index=False, encoding='utf-8')

twiitit = []
query = "etälääkäri"
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    twiitit.append([tweet.date, tweet.user.username, tweet.rawContent])

#tallennetaan tietokehikkoon
df_4 = pd.DataFrame(twiitit, columns=['Date', 'Username', 'Tweet'])
#tallennetaan tietokehikko csv-tiedostoon
df_4.to_csv("etälääkäri.csv", index=False, encoding='utf-8')

twiitit = []
query = "etäterveydenhuolto"
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    twiitit.append([tweet.date, tweet.user.username, tweet.rawContent])

#tallennetaan tietokehikkoon
df_5 = pd.DataFrame(twiitit, columns=['Date', 'Username', 'Tweet'])
#tallennetaan tietokehikko csv-tiedostoon
df_5.to_csv("etäterveydenhuolto.csv", index=False, encoding='utf-8')

twiitit = []
query = "etävastaanotto"
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    twiitit.append([tweet.date, tweet.user.username, tweet.rawContent])

#tallennetaan tietokehikkoon
df_6 = pd.DataFrame(twiitit, columns=['Date', 'Username', 'Tweet'])
#tallennetaan tietokehikko csv-tiedostoon
df_6.to_csv("etävastaanotto.csv", index=False, encoding='utf-8')

twiitit = []
query = "sähköinen ajanvaraus"
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    twiitit.append([tweet.date, tweet.user.username, tweet.rawContent])

#tallennetaan tietokehikkoon
df_7 = pd.DataFrame(twiitit, columns=['Date', 'Username', 'Tweet'])
#tallennetaan tietokehikko csv-tiedostoon
df_7.to_csv("sähköinen ajanvaraus.csv", index=False, encoding='utf-8')

twiitit = []
query = "sähköinen hoito"
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    twiitit.append([tweet.date, tweet.user.username, tweet.rawContent])

#tallennetaan tietokehikkoon
df_8 = pd.DataFrame(twiitit, columns=['Date', 'Username', 'Tweet'])
#tallennetaan tietokehikko csv-tiedostoon
df_8.to_csv("sähköinen hoito.csv", index=False, encoding='utf-8')

twiitit = []
query = "sähköinen lääke"
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    twiitit.append([tweet.date, tweet.user.username, tweet.rawContent])

#tallennetaan tietokehikkoon
df_9 = pd.DataFrame(twiitit, columns=['Date', 'Username', 'Tweet'])
#tallennetaan tietokehikko csv-tiedostoon
df_9.to_csv("sähköinen lääke.csv", index=False, encoding='utf-8')

twiitit = []
query = "sähköinen lääkemääräys"
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    twiitit.append([tweet.date, tweet.user.username, tweet.rawContent])

#tallennetaan tietokehikkoon
df_10 = pd.DataFrame(twiitit, columns=['Date', 'Username', 'Tweet'])
#tallennetaan csv-tiedostoon
df_10.to_csv("sähköinen lääkemääräys.csv", index=False, encoding='utf-8')

twiitit = []
query = "sähköinen potilas"
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    twiitit.append([tweet.date, tweet.user.username, tweet.rawContent])

#tallennetaan tietokehikkoon
df_11 = pd.DataFrame(twiitit, columns=['Date', 'Username', 'Tweet'])
#tallennetaan tietokehikko csv-tiedostoon
df_11.to_csv("sähköinen potilas.csv", index=False, encoding='utf-8')

twiitit = []
query = "sähköinen terveydenhuolto"
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    twiitit.append([tweet.date, tweet.user.username, tweet.rawContent])

#tallennetaan tietokehikkoon
df_12 = pd.DataFrame(twiitit, columns=['Date', 'Username', 'Tweet'])
#tallennetaan tietokehikko csv-tiedostoon
df_12.to_csv("sähköinen terveydenhuolto.csv", index=False, encoding='utf-8')

twiitit = []
query = "sähköinen terveys"
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    twiitit.append([tweet.date, tweet.user.username, tweet.rawContent])

#tallennetaan tietokehikkoon
df_13 = pd.DataFrame(twiitit, columns=['Date', 'Username', 'Tweet'])
#tallennetaan tietokehikko csv-tiedostoon
df_13.to_csv("sähköinen terveys.csv", index=False, encoding='utf-8')

twiitit = []
query = "terveys verkkopalvelu"
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    twiitit.append([tweet.date, tweet.user.username, tweet.rawContent])

#tallennetaan tietokehikkoon
df_14 = pd.DataFrame(twiitit, columns=['Date', 'Username', 'Tweet'])
#tallennetaan tietokehikko csv-tiedostoon
df_14.to_csv("terveys verkkopalvelu.csv", index=False, encoding='utf-8')



#yhdistetään tietokehikon ja suodatetaan kaksoiskappaleista
aineisto_dup = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9,\
df_10, df_11, df_12, df_13, df_14]).drop_duplicates()

#listataan aineistosta poistettavat terveydenhuollon organisaatiot ja ammattilaiset
poistoLista = ["Kantapalvelut","Laakarilehti","Potlaakarilehti","Laakariliitto",\
"Apotti_OyAb","THLorg","STM_Uutiset","KU_Sote","helsinginsote","paijatha",\
"KlinikHealth","Digiterveys_Lab","sannimaria_i","mikkohuo","drjounilaurila",\
"VJormanainen","tuomOikarainen","mikkohuo","AnnaKarjalainen","miia_turpeinen",\
"Sote_laatu","mika_salminen"]

#Poistetaan terveydenhuollon organisaatiot ja ammattilaiset
aineisto = aineisto_dup[~aineisto_dup["Username"].isin(poistoLista)]
print(aineisto.shape)

aineisto.to_csv('Twiitit_v1.csv', index=False, encoding='utf-8')




