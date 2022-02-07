from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import QuickFillMoins.Algorithmes.UniformQuickFill as UFF
import os
import time
import psutil
import random
import json
import sys
from backend.settings import BASE_DIR





class QuickFillExecutionList(APIView):    
    def get(self, request, format=None):
            datas = {"Cette requetes montre que tu volais un peu experiment je te comprends mais cette application n'as pas de faille de securite ne pers pas ton temps"}
            return Response(datas)
        
        
    def post(self, request, format=None):

                DataEntreeBrute = eval(request.data.get("data").get("DataEntreeBrute"))
                DataGlobal = eval(request.data.get("data").get("DataGlobal"))
                Test = UFF.UniformQuickFill()
                Test.GetClassC()
                Entrer = DataGlobal[0]["Entrer"]
                IndiceColoneSortie = len(Entrer.keys())+1
                ListeEntreFormeAtraiter = {}
                MonElment  = {}
                Maformuledecoupe = []
                programme = []
                s = []
                ListeDesElementsPourProgramme = {}
                ListeDesElementsPourProgrammeFinal = []
                ClesPourProgrammeDejaTraiter = []
                NewListOfStructureElements = []
                TraiementEntrer = []
                datas = {}

            
            
        
                for elt in DataGlobal:
                        if json.dumps(elt["Entrer"]) in ClesPourProgrammeDejaTraiter:
                                continue
                        else:
                                newListe = []
                                for ett in DataGlobal:
                                        if ett["Entrer"] == elt["Entrer"]:
                                                newListe.append(ett)
                                                ElementToAdd = {}
                                                ElementToAdd[list(ett.keys())[0]] = ett[list(ett.keys())[0]]
                                
                        
                                ListeDesElementsPourProgramme[json.dumps(elt)] = newListe
                                ClesPourProgrammeDejaTraiter.append(json.dumps(elt["Entrer"]))
                            
            
            
                for elt in ListeDesElementsPourProgramme:
                        ListeDesElementsPourProgramme[elt] = sorted(ListeDesElementsPourProgramme[elt], key = lambda i: list(i.keys())[0])
            

                
                for elt in ListeDesElementsPourProgramme:
                        for NouvelleCleEntree in ListeDesElementsPourProgramme[elt]:
                                NouvelleCleEntreesplit =  list(NouvelleCleEntree.keys())[0]
                                NouvelleValeurEntree = NouvelleCleEntreesplit.split('***')
                                ListeDesElementsPourProgrammeFinal.append(({NouvelleValeurEntree[0]:NouvelleCleEntree[NouvelleCleEntreesplit]},NouvelleValeurEntree[1]))      
                

            


                MonElment = ListeDesElementsPourProgramme[list(ListeDesElementsPourProgramme.keys())[0]]



                for ett in MonElment:

                        key = list(ett.keys())[0]
                        if ett[key] == "ConstStr":
                                
                                decoupekeyval = key.split("***")
                                Formuletest = "ConstStr(" + decoupekeyval[1] + ")"
                                
                        else:
                                Formuletest = Test.ExpressionConcatenateAbsolute3(ett["Entrer"],ett[key],ett["KeyOfElement"])
                                
                                


                        Maformuledecoupe.append(Formuletest)


        
           
                for elt in DataEntreeBrute:
                        Traite1 = {}
                        i = 0
                        chaineRetire = []
                        for ett in Maformuledecoupe:
                                i=i+1

                                if(ett.startswith("ConstStr")):
                                        Traite1["b"+str(i)] = ett
                                else:
                                        TraiementEntrer = elt["Entrer"]
                                

                                Traite1["b"+str(i)] = Test.ExecuteFonctionDecoupe(ett,TraiementEntrer)
                        


                        ListeEntreFormeAtraiter[json.dumps(elt)] = [elt["position"],Traite1,elt["Entrer"]]
     

            
           



              
            
                for elt in ListeDesElementsPourProgramme:
                        newdict1 = {}
                        NewEntrer = []
                        NewSortie = []
                        for elt2 in ListeDesElementsPourProgramme[elt]:
                                newdict1[list(elt2.keys())[0]] = elt2[list(elt2.keys())[0]]
                                NewEntrer = elt2["Entrer"]
                                NewSortie = elt2["Output"]
                        
                        
                        NewListOfStructureElements.append([newdict1,NewEntrer,NewSortie])
                    

                        
                            
                
                start = time.time()              
                programmes =  []



                for i in range(len(ListeDesElementsPourProgrammeFinal)):
                        programmes.append(list(Test.GenerateStringProgram3([ListeDesElementsPourProgrammeFinal[i]])))
                



                
                if len(programmes) == 1:
                        programmes = programmes[0]
                else:
                        programmes = Test.JoinAllElements(programmes)
                        

                        
                time.sleep(1)
                end = time.time()
  

                random_index = random.randint(0,len(programmes)-1)
                datas["NombreExemples"] = len(programmes)
                datas["IndiceColoneSortie"] = IndiceColoneSortie
            
            
                
                for elt in DataEntreeBrute:
                        elt["Output"] = Test.ExecuteElement(ListeEntreFormeAtraiter[json.dumps(elt)][1],programmes[random_index])
                   
            
                # sys.getsizeof() retourne la taille de la memoire en octets
                datas["memoryQuickfill"] = sys.getsizeof(programmes)/1024
                

                timewastQuickfill = end - start

                datas["timewastQuickfill"] = timewastQuickfill
                datas["DataFinalToBeReplace"] = DataEntreeBrute


                datas["indiceduprogrammechoisi"] = random_index
                datas["listedesprogrammes"] = programmes





                return Response(datas)
    
    
    @classmethod
    def get_extra_actions(cls):
        return []









class QuickFillExecutionListWithFilter(APIView):    
    def get(self, request, format=None):
            datas = {"Cette requetes montre que tu volais un peu experiment je te comprends mais cette application n'as pas de faille de securite ne pers pas ton temps"}
            return Response(datas)
        
        
    def post(self, request, format=None):
            
            
                DataEntreeBrute = eval(request.data.get("data").get("DataEntreeBrute"))
                DataGlobal = eval(request.data.get("data").get("DataGlobal"))
                MesSorties = eval(request.data.get("data").get("MesSorties"))
                Test = UFF.UniformQuickFill()
                Test.GetClassC()
                Entrer = DataGlobal[0]["Entrer"]
                IndiceColoneSortie = len(Entrer.keys())+1
                ListeEntreFormeAtraiter = {}
                MonElment  = {}
                Maformuledecoupe = []
                programme = []
                s = []
                ListeDesElementsPourProgrammeFinal = []
                ListeDesElementsPourProgramme = {}
                ClesPourProgrammeDejaTraiter = []
                NewListOfStructureElements = []
                ListeFilterFormetraiter= {}

            
        
                for elt in DataGlobal:
                        
                        if json.dumps(elt["Entrer"]) in ClesPourProgrammeDejaTraiter:
                                continue
                        else:
                                newListe = []
                                for ett in DataGlobal:
                                        if ett["Entrer"] == elt["Entrer"]:
                                                newListe.append(ett)
                                                ElementToAdd = {}
                                                ElementToAdd[list(ett.keys())[0]] = ett[list(ett.keys())[0]]
                                
                        
                                ListeDesElementsPourProgramme[json.dumps(elt)] = newListe
                                
                                ClesPourProgrammeDejaTraiter.append(json.dumps(elt["Entrer"]))
                            
            
            
                for elt in ListeDesElementsPourProgramme:
                        ListeDesElementsPourProgramme[elt] = sorted(ListeDesElementsPourProgramme[elt], key = lambda i: list(i.keys())[0])
            

                for elt in ListeDesElementsPourProgramme:
                        for NouvelleCleEntree in ListeDesElementsPourProgramme[elt]:
                                NouvelleCleEntreesplit =  list(NouvelleCleEntree.keys())[0]
                                NouvelleValeurEntree = NouvelleCleEntreesplit.split('***')
                                ListeDesElementsPourProgrammeFinal.append(({NouvelleValeurEntree[0]:NouvelleCleEntree[NouvelleCleEntreesplit]},NouvelleValeurEntree[1]))      
                


                MonElment = ListeDesElementsPourProgramme[list(ListeDesElementsPourProgramme.keys())[0]]
          
                for ett in MonElment:

                        key = list(ett.keys())[0]
                        if ett[key] == "ConstStr":
                                
                                decoupekeyval = key.split("***")
                                Formuletest = "ConstStr(" + decoupekeyval[1] + ")"
                                
                        else:
                                Formuletest = Test.ExpressionConcatenateAbsolute3(ett["Entrer"],ett[key],ett["KeyOfElement"])
                                
                                
                        Maformuledecoupe.append(Formuletest)
        
           
           
           





                for elt in DataEntreeBrute:
                        Traite1 = {}
                        i = 0
                        chaineRetire = []
                        for ett in Maformuledecoupe:
                                i=i+1
                                if(ett.startswith("ConstStr")):
                                        Traite1["b"+str(i)] = ett
                                else:
                                        TraiementEntrer = elt["Entrer"]
                                        Traite1["b"+str(i)] = Test.ExecuteFonctionDecoupe(ett,TraiementEntrer)
                        

                        
                        ListeEntreFormeAtraiter[json.dumps(elt)] = [elt["position"],Traite1,elt["Entrer"]]
     

            
            

                for elt in ListeDesElementsPourProgramme:
                        newdict1 = {}
                        NewEntrer = []
                        NewSortie = []
                        for elt2 in ListeDesElementsPourProgramme[elt]:
                                newdict1[list(elt2.keys())[0]] = elt2[list(elt2.keys())[0]]
                                NewEntrer = elt2["Entrer"]
                                NewSortie = elt2["Output"]
                        
                        
                        NewListOfStructureElements.append([newdict1,NewEntrer,NewSortie])

             

       
                for elt in MesSorties:
                        Traite1 = {}
                        i = 0
                        for ett in Maformuledecoupe:
                                i=i+1
                                if(ett.startswith("ConstStr")):
                                        Traite1["b"+str(i)] = ett
                                else:
                                        Traite1["b"+str(i)] = Test.ExecuteFonctionDecoupe(ett,elt["Entrer"])
                        

                        ListeFilterFormetraiter[json.dumps(elt)] = [Traite1,elt["Output"]]
                                   


                                                     

                
                start = time.time()              
                programmes =  []
                datas = {}


                for i in range(len(ListeDesElementsPourProgrammeFinal)):
                        programmes.append(list(Test.GenerateStringProgram3([ListeDesElementsPourProgrammeFinal[i]])))
                
                
                if len(programmes) == 1:
                        programmes = programmes[0]
                else:
                        programmes = Test.JoinAllElements(programmes)
                               
                        
                time.sleep(1)
                end = time.time()
  

                random_index = random.randint(0,len(programmes)-1)
                datas["NombreExemples"] = len(programmes)
                datas["IndiceColoneSortie"] = IndiceColoneSortie
                

                for elt in DataEntreeBrute:
                        elt["Output"] = Test.ExecuteFonction(programme[random_index],ListeEntreFormeAtraiter[json.dumps(elt)][1])
                        
            
            
                """ 
                for elt in DataEntreeBrute:
                        elt["Output"] = Test.ExecuteElement(ListeEntreFormeAtraiter[json.dumps(elt)][1],programmes[random_index])
                    """
            
                # sys.getsizeof() retourne la taille de la memoire en octets
                datas["memoryQuickfill"] = sys.getsizeof(programmes)/1024
                

                timewastQuickfill = end - start

                datas["timewastQuickfill"] = timewastQuickfill
                datas["DataFinalToBeReplace"] = DataEntreeBrute


                datas["indiceduprogrammechoisi"] = random_index
                datas["listedesprogrammes"] = programmes








                return Response(datas)
    
    
    @classmethod
    def get_extra_actions(cls):
        return []






class QuickFillExecutionListManyBlock(APIView):    
    def get(self, request, format=None):
            datas = {"Cette requetes montre que tu volais un peu experiment je te comprends mais cette application n'as pas de faille de securite ne pers pas ton temps"}
            return Response(datas)
        
        
    def post(self, request, format=None):
            
            
                DataEntreeBrute = eval(request.data.get("data").get("DataEntreeBrute"))
                DataGlobal = eval(request.data.get("data").get("DataGlobal"))
                Test = UFF.UniformQuickFill()
                Test.GetClassC()
                Entrer = DataGlobal[0]["Entrer"]
                IndiceColoneSortie = len(Entrer.keys())+1
                ListeEntreFormeAtraiter = {}
                MonElment  = {}
                Maformuledecoupe = []
                programme = []
                programmes = []
                datas = {}
                s = []
                ListeDesElementsPourProgrammeFinal = {}
                ListeDesElementsPourProgramme = {}
                ClesPourProgrammeDejaTraiter = []
                NewListOfStructureElements = []

            
            
        
                for elt in DataGlobal:
                        
                        if json.dumps(elt["Entrer"]) in ClesPourProgrammeDejaTraiter:
                                continue
                        else:
                                newListe = []
                                for ett in DataGlobal:
                                        if ett["Entrer"] == elt["Entrer"]:
                                                newListe.append(ett)
                                                ElementToAdd = {}
                                                ElementToAdd[list(ett.keys())[0]] = ett[list(ett.keys())[0]]
                                
                        
                                ListeDesElementsPourProgramme[json.dumps(elt)] = newListe
                                
                                ClesPourProgrammeDejaTraiter.append(json.dumps(elt["Entrer"]))
                            
            
            
                for elt in ListeDesElementsPourProgramme:
                        ListeDesElementsPourProgramme[elt] = sorted(ListeDesElementsPourProgramme[elt], key = lambda i: list(i.keys())[0])
            

                for elt in ListeDesElementsPourProgramme:
                        blocs = []
                        for NouvelleCleEntree in ListeDesElementsPourProgramme[elt]:
                                NouvelleCleEntreesplit =  list(NouvelleCleEntree.keys())[0]
                                NouvelleValeurEntree = NouvelleCleEntreesplit.split('***')
                                blocs.append(({NouvelleValeurEntree[0]:NouvelleCleEntree[NouvelleCleEntreesplit]},NouvelleValeurEntree[1])) 
                                ListeDesElementsPourProgrammeFinal[elt] = blocs

            
            
            
                MonElment = ListeDesElementsPourProgramme[list(ListeDesElementsPourProgramme.keys())[0]]

            
                for ett in MonElment:

                        key = list(ett.keys())[0]
                        if ett[key] == "ConstStr":
                                
                                decoupekeyval = key.split("***")
                                Formuletest = "ConstStr(" + decoupekeyval[1] + ")"
                                
                        else:
                                Formuletest = Test.ExpressionConcatenateAbsolute3(ett["Entrer"],ett[key],ett["KeyOfElement"])
                        
                        


                        Maformuledecoupe.append(Formuletest)
 

                for elt in DataEntreeBrute:
                        Traite1 = {}
                        i = 0
                        chaineRetire = []
                        for ett in Maformuledecoupe:
                                i=i+1
                                if(ett.startswith("ConstStr")):
                                        Traite1["b"+str(i)] = ett
                                else:
                                        TraiementEntrer = elt["Entrer"]
                                        Traite1["b"+str(i)] = Test.ExecuteFonctionDecoupe(ett,TraiementEntrer)
                        

                        
                        ListeEntreFormeAtraiter[json.dumps(elt)] = [elt["position"],Traite1,elt["Entrer"]]
     

            
                for elt in ListeDesElementsPourProgramme:
                        newdict1 = {}
                        NewEntrer = []
                        NewSortie = []
                        for elt2 in ListeDesElementsPourProgramme[elt]:
                                newdict1[list(elt2.keys())[0]] = elt2[list(elt2.keys())[0]]
                                NewEntrer = elt2["Entrer"]
                                NewSortie = elt2["Output"]
                        
                        
                        NewListOfStructureElements.append([newdict1,NewEntrer,NewSortie])

                start = time.time()   
                for cle in ListeDesElementsPourProgrammeFinal:
                        for i in range(len(ListeDesElementsPourProgrammeFinal[cle])):
                                programme = []
                                programme = programme.append(list(Test.GenerateStringProgram3([ListeDesElementsPourProgrammeFinal[elti]])))
                                programmes.append(programme)
                

                FinalPrograms = []

                for elt in programmes :
                        FinalPrograms.append(set(Test.JoinAllElements(elt)))

                FinalPrograms = FinalPrograms.pop().intersection(*FinalPrograms)

                        
                time.sleep(1)
                end = time.time()
  
                
                random_index = random.randint(0,len( FinalPrograms)-1)
                datas["NombreExemples"] = len( FinalPrograms)
                datas["IndiceColoneSortie"] = IndiceColoneSortie
                
            
            
                for elt in DataEntreeBrute:
                        elt["Output"] = Test.ExecuteFonction( FinalPrograms[random_index],ListeEntreFormeAtraiter[json.dumps(elt)][1])
                        
            
            
                timewastQuickfill = end - start

                datas["timewastQuickfill"] = timewastQuickfill
                datas["DataFinalToBeReplace"] = DataEntreeBrute
                datas["indiceduprogrammechoisi"] = random_index
                datas["listedesprogrammes"] = programme


                

                return Response(datas)
    
    
    @classmethod
    def get_extra_actions(cls):
        return []
 

