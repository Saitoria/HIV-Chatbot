from flask import Flask,request #import some things to run our server
import string
from nltk.corpus import stopwords
stopwords = stopwords.words('swahili')
import re
from flask.templating import render_template

app = Flask(__name__) #initialize the appq

chats={
	"ukimwi ni nini":"Ukimwi ni(Upungufu wa Kinga Mwilini) ni ugonjwa unaotokana na virusi viitwavyo VVU ",
    "vvu ni nini":"VVU(Virusi vya ukimwi) ni virusi vinashambulia mwili kwa kuondoa nguvu zake za kupambana na maambukizi nyemelezi yanayosababisha maradhi.",
    "nini dalili za ukimwi":"Maambukizi makali(mafua,kuhara,inflamesheni za koo),<br> Awamu fiche(homa,kukonda,matatizo ya tumbo),</br> Ukosefu wa Kinga Mwilini(husababisha mtu kupata magonjwa mbalimbali)",
	"ukimwi unaambukizwaje":"Kupitia ngono,Viowevu vya mwili,Mama hadi mtoto",
	"je, ukimwi una tiba":"Hakuna tiba au chanjo; hata hivyo,<br> matibabu ya kudhibiti virusi yanaweza kupunguza mwendo wa ugonjwa huu na huenda yakapelekea urefu wa maisha kuwa karibu na kawaida.<br> Ingawa matibabu ya kupunguza makali hupunguza hatari ya kifo ",
    "lini na wapi vvu zilianza":"UKIMWI huchukuliwa kama janga — yaani mlipuko wa ugonjwa katika eneo kubwa, na ambao ungali unaenea. UKIMWI ulitambuliwa mara ya kwanza na Vituo vya Kuzuia na Kudhibiti Magonjwa huko Marekani mwaka , ilhali kisababishi chake - VVU - kilitambuliwa mwanzoni mwa muongo huo nchini huko. ",
    "uchunguzi wa ukimwi":"Watu wengi walioambukizwa VVU huzalisha zindiko maalum katika wiki 3 hadi 12 tangu maambukizi ya kwanza.Utambuzi wa VVU vya kimsingi hufanywa kabla ya kuzalishwa kwa zindiko mpya kwa kupima RNA ya VVU ",
    "njia ya kujikinga na ukimwi":"Ukimwi hukingwa kwa Kondomu,Kuzuia maambukizi ya mama kwa mtoto,Tohara,Kuzuia ngono zembe,Mawaidha na elimu,kupitia kuchangia vifaa vyenye ncha kali na muathirika",
    "matarajio ya kuishi":"Wastani wa muda wa kuishi baada ya kuambukizwa unakadiriwa kuwa kati ya miaka 9-1  bila matibabu, ikitegemea aina ya VVU. Baada ya utambuzi wa UKIMWI, iwapo matibabu hayapo, uwezo wa kuishi huwa kati ya miezi 6-19.matarajio ya urefu wa maisha hadi miaka 20-50  kwa anaepokea matibabu",
    "watu wangapi wana ukimwi":"VVU/UKIMWI ni janga la kimataifa. Kufikia mwaka 2018 walau watu wapatao 37,900,000 walikuwa wakiishi na VVU na kila mwaka watu milioni 2 wengine wanambukizwa. Zaidi ya nusu ni wanawake na milioni 2.6 ni watoto chini ya miaka 15.",
    "jamii na utamaduni":"Ukimwi unasababisha unyanyapaa,athari za kiuchumi,mayatima"
}

@app.route("/")
def home():
    return render_template('gui.html')

@app.route("/ask")
def ask():
    question = request.args.get('msg').lower()

    def clean_string(text):
        text = ''.join([word for word in text if word not in string.punctuation])
        text = text.lower()
        text = ' '.join([word for word in text.split() if word not in stopwords])
        return text

    cleaned = clean_string(question)

    if(re.search("mambo|za asubuhi|za mchana|za jioni|hi|habari|hello",cleaned)):
        return "Habari zangu ni nzuri, na ni matumaini yangu na wewe unaendelea vizuri"

    elif(re.search("dalili|ishara",cleaned) and re.search("vvu|ukimwi",cleaned) and re.search("nini",cleaned)):
        return chats["nini dalili za ukimwi"]
    elif(re.search("unaambukizwaje|unakuwaje|unapataje|pata|ambukizwa|unasababishwa|unapatikanaje|unapatikana",cleaned) and re.search("vvu|ukimwi",cleaned) and re.search("nini",cleaned)):
        return chats["ukimwi unaambukizwaje"]
    elif(re.search("tiba|kinga|chanjo|ponyaje|inatibu",cleaned) and re.search("vvu|ukimwi",cleaned) and re.search("nini",cleaned)):
        return chats["je, ukimwi una tiba"]
    elif(re.search("zilianza|ulianzaje|mwanzo|chanzo|ulianza|lini|ulianza|wapi",cleaned) and re.search("vvu|ukimwi",cleaned) and re.search("nini",cleaned)):
        return chats["lini na wapi vvu zilianza"]
    elif(re.search("zilianza|ulianzaje|mwanzo|chanzo|ulianza|lini|ulianza|wapi",cleaned) and re.search("vvu|ukimwi",cleaned) and re.search("nini",cleaned)):
        return chats["lini na wapi vvu zilianza"]
    elif(re.search("unachunguzwaje|unapimwaje|kupima|kuchunguza",cleaned) and re.search("vvu|ukimwi",cleaned) and re.search("nini",cleaned)):
        return chats["uchunguzi wa ukimwi"]
    elif(re.search("unajikingaje|unajistiri|unajizuiaje|kuzuia|kukinga|kujikinga",cleaned) and re.search("vvu|ukimwi",cleaned) and re.search("nini",cleaned)):
        return chats["njia ya kujikinga na ukimwi"]

    elif(re.search("nini|kitu gani|maana",cleaned) and re.search("ukimwi",cleaned)):
        return chats["ukimwi ni nini"]
    elif(re.search("nini|kitu gani|maana",cleaned) and re.search("vvu",cleaned)):
        return chats["vvu ni nini"]

    elif(re.search("dalili|ishara",cleaned) and re.search("vvu|ukimwi",cleaned)):
        return chats["nini dalili za ukimwi"]
    elif(re.search("unaambukizwaje|unakuwaje|unapataje|pata|ambukizwa|unasababishwa|unapatikanaje|unapatikana",cleaned) and re.search("vvu|ukimwi",cleaned)):
        return chats["ukimwi unaambukizwaje"]
    elif(re.search("tiba|kinga|chanjo|ponyaje|inatibu",cleaned) and re.search("vvu|ukimwi",cleaned)):
        return chats["je, ukimwi una tiba"]
    elif(re.search("zilianza|ulianzaje|mwanzo|chanzo|ulianza|lini|ulianza|wapi",cleaned) and re.search("vvu|ukimwi",cleaned)):
        return chats["lini na wapi vvu zilianza"]
    elif(re.search("zilianza|ulianzaje|mwanzo|chanzo|ulianza|lini|ulianza|wapi",cleaned) and re.search("vvu|ukimwi",cleaned)):
        return chats["lini na wapi vvu zilianza"]
    elif(re.search("unachunguzwaje|unapimwaje|kupima|kuchunguza",cleaned) and re.search("vvu|ukimwi",cleaned)):
        return chats["uchunguzi wa ukimwi"]
    elif(re.search("unajikingaje|unajistiri|unajizuiaje|kuzuia|kukinga|kujikinga",cleaned) and re.search("vvu|ukimwi",cleaned)):
        return chats["njia ya kujikinga na ukimwi"]
    elif(re.search("anatarajiwa|kuishi",cleaned) and re.search("vvu|ukimwi",cleaned)):
        return chats["matarajio ya kuishi"]
    elif(re.search("wangapi|idadi|jumla",cleaned) and re.search("vvu|ukimwi",cleaned)):
        return chats["watu wangapi wana ukimwi"]
    elif(re.search("jamii|mazara|utamaduni",cleaned) and re.search("vvu|ukimwi",cleaned)):
        return chats["jamii na utamaduni"]

    else:
        return "samahani naomba uulize tena, sijaelewa swali lako vizuri"

if __name__ == "__main__":
    app.run(debug=True)
