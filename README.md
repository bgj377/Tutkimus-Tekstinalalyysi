# Tutkimus-Tekstinalalyysi
Teen opinnäytetyötä aiheena terveydenhuollon digitaalisiin palveluihin liittyvän kansalaismielipiteen tutkimisesta tekstianalyysin avulla. Säilytän täällä opinnäytetyöhöni liittyviä tiedostoja

Työni aineisto sisältää twiittejä, jotka on haettu Twitteristä käyttäen hakutermeinä terveydenhuollon digipalveluihin liittyviä sanoja. Aineiston haku tehtiin päivämäärällä 20.4.2023 ja hakutermit on tallennettu tiedostoon "Twitterin hakutermit.txt". 

Twiittiaineistoa käytettiin tekstilouhintaan ja sille tehtiin *aihemallinnus* ja *tunneanalyysi*. Aihemallinnus tehtiin Pythonilla käyttäen epänegatiivista matriisifaktorointia. Tämä menetelmä vaati twiittien sisältämän tekstin esiprosessointia, jossa käytettiin Pythonin spaCyn-kirjaston työkaluja. Esiprosessointi sisälsi url-osoitteiden, sähköpostiosoitteiden ja emojien poistamisen tekstistä. Lisäksi isot kirjaimet muunnettiin pieniksi ja tekstistä poistettiin sanat, jotka eivät olleet substantiiveja, adjektiiveja, adverbeja, verbeja tai nimiä. Tekstistä pyrittiin myös suodattamaan *poistosanat*, jotka ovat kielessä yleisiä sanoja, jotka ovat analyysissa merkityksettömiä. Tekstistä poistettiin sanat, jotka olivat spaCyn suomentkielisellä poistosanalistalla. Näitä poistosanoja oli 822 ja ne ovat listattu tiedostoon "spaCyn poistosanalista.txt". Valmiiden poistosanojen lisäksi aihemallinnusta tehtäessä löydettiin uusia analyysia haittaavia sanoja, jotka luokiteltiin poistosanoiksi. Näitä itse valitsemiani poistosanoja oli 45 ja ne on listattu tiedostoon "omat poistosanat.txt".

Aihemallinnuksessa päädyttiin valitsemaan kuusi aihetta, jotka on merkitty oheisiin taulukkoihin. 

| Aihe 0                  | Aihe 1              | Aihe 2                | Aihe 3                 | Aihe 4                   |
| :---                    |                ---: |                  ---: |                   ---: |                     ---: |
| terveydenhuolto (13.28) | sähköinen (14.72)   | etälääkäri (26.48)    | etävastaanotto (17.01) | digiterveys (23.47)      |
| digitalisaatio (11.89)  | ajanvaraus (14.22)  | terveyspalvelu (2.90) | lääkäri (3.83)         | digitalhealth (2.94)     |
| digitaalinen (1.74)     | lääkemääräys (0.93) | hoito (2.66)          | potilas (1.21)         | terveysteknologia (1.34) |
| tekoäly (1.30)          | resepti (0.85)      | lääkäri (2.19)        | vastaanotto (1.07)     | ehealth (1.14)           |
| terveydenhuollo (1.12)  | asiointi (0.71)     | potilas (0.95)        | kännykkälääkäri (0.72) | digitaalinen (0.96)      |
