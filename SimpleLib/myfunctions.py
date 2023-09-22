import os,json


class List:
    def Enum(liste):
        for i in liste:
            print(i)
    def AddAlphabet(list,show = False):
        if show == (not True):
            list.append("a")
            list.append("b")
            list.append("c")
            list.append("d")
            list.append("e")
            list.append("f")
            list.append("g")
            list.append("h")
            list.append("i")
            list.append("j")
            list.append("k")
            list.append("l")
            list.append("m")
            list.append("n")
            list.append("o")
            list.append("p")
            list.append("q")
            list.append("r")
            list.append("s")
            list.append("t")
            list.append("u")
            list.append("v")
            list.append("w")
            list.append("x")
            list.append("y")
            list.append("z")
        else:
            print("starting.")
            list.append("a")
            print("starting..")
            list.append("b")
            print("starting...")
            list.append("c")
            print("starting....")
            list.append("d")
            print("starting.....")
            list.append("e")
            print("starting.")
            list.append("f")
            print("starting..")
            list.append("g")
            print("starting...")
            list.append("h")
            print("starting....")
            list.append("i")
            print("starting.....")
            list.append("j")
            print("starting.")
            list.append("k")
            print("starting..")
            list.append("l")
            print("starting...")
            list.append("m")
            print("starting....")
            list.append("n")
            print("starting.....")
            list.append("o")
            print("starting.")
            list.append("p")
            print("starting..")
            list.append("q")
            print("starting...")
            list.append("r")
            print("starting....")
            list.append("s")
            print("starting.....")
            list.append("t")
            print("starting.")
            list.append("u")
            print("starting..")
            list.append("v")
            print("starting...")
            list.append("w")
            print("starting....")
            list.append("x")
            print("starting.....")
            list.append("y")
            print("starting......")
            list.append("z")
            print("Done!")



class Document:
    def Create(name):
        try:
            open(name+".txt","x")
        except:
            print("Erreur")
    def Write(doc,string):
        f = open(doc,"a")
        f.write(string)
        f.close()
        
    
    def Read(doc):
        f = open(doc,"r")
        print(f.read())
        f.close()

class Json:
    def read(file,part,precision=False,partP=None):
        if precision == False:
            f = open(file)
            try:
                return json.loads(part)
            except:
                print("This object doesn't exist!")
        
        elif precision == True:
            fileObject = open(file+".json", "r")
            jsonContent = fileObject.read()
            obj_python = json.loads(jsonContent)
            try:
                return obj_python[partP]
            except:
                print("This Part doesn't exist!")
    
    def write(file,string):
        with open(file+".json", "w") as f:
            json.dump(string, f)
    
