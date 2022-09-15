from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from stopWords import StopW
from tqdm import tqdm
from time import sleep
import os
import csv

class Ner:
    def __init__(self) :
        # tokenizer = AutoTokenizer.from_pretrained("mrm8488/bert-spanish-cased-finetuned-ner")
        # model = AutoModelForTokenClassification.from_pretrained("mrm8488/bert-spanish-cased-finetuned-ner")        
        self.nlp = pipeline(
        "ner",
        model="mrm8488/bert-spanish-cased-finetuned-ner",
        tokenizer=('mrm8488/bert-spanish-cased-finetuned-ner',  {"use_fast": False} 
        ))
    def get_ner(self,text,contDoc,idDoc,folderService):
        DATA=[["word", "entity"]]
        perlist=[]
        loclist=[]
        orglist=[]
        stops=StopW()
        coun=0
        for frase in tqdm(text):
            sleep(0.00001)
            coun+=1
            a=self.nlp(frase)
            str_orgs=""
            str_locs=""
            str_per=""
            for q in a:  
                if "PER" in q["entity"] and "#" not in q["word"] and q["word"] not in stops.get_stop_words("PER"):
                    str_per += str(q["word"] + " ")
                if "LOC" in q["entity"] and "#" not in q["word"] and q["word"] not in stops.get_stop_words("LOC"):
                    str_locs += str(q["word"] + " ")
                if "ORG" in q["entity"] and q["word"] not in stops.get_stop_words("ORG") and "#" not in q["word"] :
                    str_orgs += str(q["word"] + " ")
            listLocs=str_locs.split()
            listPer=str_per.split()
            listOrg=str_orgs.split()
            if len(listOrg)!=len(set(listOrg)):#si hay duplicados los divide y añade
                for z in listOrg:
                    orglist.append(z)           
            else: #si no hay duplicados
                if len(str_orgs)>1:
                    orglist.append(str_orgs[:-1])

            for h in listPer:
                perlist.append(h)
            for t in listLocs:
                loclist.append(t)  
        for words in loclist:
            passs=[words,"LOC"]
            DATA.append(passs)
        for words in perlist:
            passs=[words,"PER"]
            DATA.append(passs)
        for words in orglist:
            passs=[words,"ORG"]
            DATA.append(passs)

        #almaceno mis resultados
        if not os.path.exists('./RESULTS/'+str(folderService)):
            os.makedirs('./RESULTS/'+str(folderService))
        else : pass
        almacenaje=f"./RESULTS/{folderService}/"
        docuntoCSV=f"{idDoc}__{contDoc}.csv"
        with open(str(almacenaje+docuntoCSV), 'w',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(DATA)
        