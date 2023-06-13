# Tutkimus-Tekstinalalyysi
Teen opinnäytetyötä aiheena terveydenhuollon digitaalisiin palveluihin liittyvän kansalaismielipiteen tutkimisesta tekstianalyysin avulla. Säilytän täällä opinnäytetyöhöni liittyviä tiedostoja

Työni aineisto sisältää twiittejä, jotka on haettu Twitteristä käyttäen hakutermeinä terveydenhuollon digipalveluihin liittyviä sanoja. Aineiston haku tehtiin päivämäärällä 20.4.2023 ja hakutermit on tallennettu tiedostoon "Twitterin hakutermit.txt". Aineistoon tuli 3075 twiittiä, jotka on tallennettu tiedostoon "Twiitit_v1.csv".

Twiittiaineistoa käytettiin tekstilouhintaan ja sille tehtiin *aihemallinnus* ja *tunneanalyysi*. Aihemallinnus tehtiin Pythonilla käyttäen epänegatiivista matriisifaktorointia. Tämä menetelmä vaati twiittien sisältämän tekstin esiprosessointia, jossa käytettiin Pythonin spaCyn-kirjaston työkaluja. Esiprosessointi sisälsi url-osoitteiden, sähköpostiosoitteiden ja emojien poistamisen tekstistä. Lisäksi isot kirjaimet muunnettiin pieniksi ja tekstistä poistettiin sanat, jotka eivät olleet substantiiveja, adjektiiveja, adverbeja, verbeja tai nimiä. Tekstistä pyrittiin myös suodattamaan *poistosanat*, jotka ovat kielessä yleisiä sanoja, jotka ovat analyysissa merkityksettömiä. Analyysissa ei käytetty sanoja, jotka olivat spaCyn suomentkielisellä poistosanalistalla. Näitä poistosanoja oli 822 ja ne ovat listattu tiedostoon "spaCyn poistosanalista.txt". Valmiiden poistosanojen lisäksi aihemallinnusta tehtäessä löydettiin uusia analyysia haittaavia sanoja, jotka luokiteltiin poistosanoiksi. Näitä itse valitsemiani poistosanoja oli 45 ja ne on listattu tiedostoon "omat poistosanat.txt".

Aihemallinnuksessa päädyttiin valitsemaan kuusi aihetta, jotka on merkitty oheisiin taulukkoihin. Aihe muodostuu aineiston twiiteissa olevista termeistä. Eri termit osallistuvat aiheen muodostamiseen erilaisilla prosenttiosuuksilla. Taulukkoihin on merkitty kunkin aiheen kannalta viisi tärkeintä termiä. Termeihin liittyvät numerot ilmoittavat, millä prosenttiosuudella termit osallistuivat aiheen muodostamiseen. Yksittäinen twiitti voi sisältää useita aiheita. Se aihe, jonka termit ovat eniten edustettuina twiitissa on twiitin hallitseva aihe.

| Aihe 0                  | Aihe 1              | Aihe 2                |
| :---                    | :---                | :---                  |   
| terveydenhuolto (13.53) | sähköinen (14.73)   | etälääkäri (26.49)    |
| digitalisaatio (12.17)  | ajanvaraus (14.22)  | terveyspalvelu (2.90) |
| digitaalinen (1.75)     | lääkemääräys (0.94) | hoito (2.66)          |
| tekoäly (1.32)          | resepti (0.85)      | lääkäri (2.19)        |
| lääkäri (0.83)          | asiointi (0.72)     | potilas (0.95)        |

| Aihe 3                 | Aihe 4                   | Aihe 5              |
| :---                   | :---                     | :---                |
| etävastaanotto (17.00) | digiterveys (23.58)      | terveys (12.18)     |
| lääkäri (3.83)         | digitalhealth (2.97)     | digi (9.32)         |
| potilas (1.21)         | terveysteknologia (1.35) | hyvinvointi (2.37)  |
| vastaanotto (1.07)     | ehealth (1.15)           | digitaalinen (1.40) |
| kännykkälääkäri (0.72) | digitaalinen (0.98)      | hoito (1.08)        |

Tunneanalyysi tehtiin VADER-tunnesanaston avulla. VADER on saatavilla vain englanninkielisenä, joten twiitit käännettiin englanniksi tunneanalyysia varten. VADER sisältää useita taivutusmuotoja sanoista, joten tunneanalyysia varten teksti ei vaadi raskasta esiprosessointia. Ainoa tehty muunnos oli isojen kirjainten muuntaminen pieniksi. Tunneanalyysi antoi kullekkin twiitille tunnearvon välille [-1, 1], jossa -1 on erittäin negatiivinen tunne ja 1 on erittäin positiivinen tunne. Tunteille määriteltiin myös tunneluokka, jossa twiitti määritellään negatiiviseksi, jos tunnearvo <= -0,4, positiivinen, jos tunnearvo >= 0,4 ja muuten neutraali. 

Aineisto, johon on merkitty jokaisen twiitin sisältö (suomeksi ja englanniksi), luontipäivämäärä, kirjoittajan käyttäjätunnus, hallitseva aihe, tunnearvo, tunneluokka sekä aihemallinnusta varten esiprosessoitu versio twiiteistä on tiedostossa "Twiitti-Aineisto.csv". Aihemallinnukseen ja tunneanalyysiin liittyvät Python-koodit ovat tiedostoissa "Aihemallinnus-1.py" ja "Tunneanalyysi-1.py".
