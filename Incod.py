from tkinter import*
main = Tk()
main.geometry("700x440")
main.title("Incod")

alphabet=[]
ans=[]


lib1 = {"a":"a00",
"b":"a01","c":"a02","d":"a03","e":"a04","f":"a05","g":"a06","h":"a07","q":"a08","w":"a09","s":"a10","r":"a11","t":"a12","y":"a13","u":"a14","i":"a15","o":"a16","p":"a17","j":"a18","k":"a19","l":"a20","m":"a21","n":"a22","x":"a23","v":"a24","z":"a25","A":"a26","P":"a27","Q":"a28","Z":"a29","L":"a30","N":"a31",
"M":"a32","G":"a33","H":"a34","K":"a35","J":"a36","U":"a37","W":"a38","T":"a39","R":"a40","E":"a41","X":"a42","C":"a43","V":"a44","B":"a45","D":"a46","F":"a47","I":"a48","O":"a49","Y":"a50","S":"a51"," ":"a52","`":"a53","@":"a54","!":"a55","#":"a56","&":"a57","-":"a58","_":"a59",",":"a60",".":"a61","?":"a62",";":"a63",
"(":"a64",")":"a65",":":"a66","1":"a100","7":"a101","2":"a102","5":"a103","3":"a104","8":"a105","4":"a106","9":"a107","6":"a108","0":"a109"
       }

lib2 = {"00":"a","01":"b","02":"c","03":"d","04":"e","05":"f","06":"g","07":"h","08":"q","09":"w","10":"s","11":"r","12":"t","13":"y","14":"u",
"15":"i","16":"o","17":"p","18":"j","19":"k","20":"l","21":"m","22":"n","23":"x","24":"v","25":"z","26":"A","27":"P","28":"Q","29":"Z","30":"L",
"31":"N","32":"M","33":"G","34":"H","35":"K","36":"J","37":"U","38":"W","39":"T","40":"R","41":"E","42":"X","43":"C","44":"V","45":"B","46":"D",
"47":"F","48":"I","49":"O","50":"Y","51":"S","52":" ","53":"`","54":"@","55":"!","56":"#","57":"&","58":"-","59":"_","60":",","61":".","62":"?",
"63":";","64":"(","65":")","66":":","100":"1","101":"7","102":"2","103":"5","104":"3","105":"8","106":"4","107":"9","108":"6","109":"0"
       }       
Default = "Select Encoder/Decoder --- ^^^ ^^^"
T1 = StringVar()
T1.set(Default)
inputBox = Entry(main,textvariable=T1,width=90,relief=GROOVE)
inputBox.grid(row=1,column=0)
TextBox=Text(main)



temp=[]

def display():
    TextBox.delete("1.0",END)
    if ShiftVar.get() == 0:
        prm.Encoder()
    if ShiftVar.get() == 1:
        prm.Decoder()
    

ShiftVar=IntVar()
ShiftVar.set(7)
DisplayButton = Button(main,text=">",width=10,command=display).grid(row=1,column=1)

TextBox.grid(row=2,column=0,columnspan=2,padx=30)





class Program():
    
    Plib={}
    def __init__(self):
        pass

    def Encoder(self):
        
        TextBox.delete("1.0",END)
        
        strg = ''
        alphabet=[]
        temp=[]
        inputBox=T1.get()
        strInput=inputBox
        for i in strInput:
            alphabet.append(i)

        print(alphabet)
        print(alphabet[0])
        

        for i in alphabet:
            if i in prm.Plib:
                temp.append(prm.Plib[i])
        
        for i in range(len(temp)):
            strg+=temp[i]

        print(len(temp))
        TextBox.insert("end",strg)
        print(f"Secret Code is : {strg}")
        
    def Decoder(self):
        TextBox.delete("1.0",END)
        
        strg = ''
        alphabet=[]
        temp=[]
        inputBox=T1.get()
        strInput=inputBox
        x=strInput.split("a")
        print(f"value of x : {x}")
        for i in x:
            alphabet.append(i)
        alphabet.pop(0)

        for i in alphabet:
            if i in prm.Plib:
                temp.append(prm.Plib[i])
        
        for i in range(len(temp)):
            strg+=temp[i]

        print(len(temp))
        TextBox.insert("end",strg)
        print(f"Secret Code is : {strg}")
        
prm=Program()
prm.Plib=lib1
def shift():
    if ShiftVar.get() == 0:
        print("Encode")
        T1.set("Encoding")
        prm.Plib=lib1
        prm.Encoder()
        
    if ShiftVar.get() == 1:
        print("Decode")
        T1.set("a46a04a02a16a03a15a22a06")
        prm.Plib=lib2
        prm.Decoder()
        
ShiftFrame = Frame(main)
ShiftFrame.grid(row=0,column=0)
ShiftButton = Radiobutton(ShiftFrame,text="Decode",value=1,variable=ShiftVar,command=shift).grid(row=0,column=1)
ShiftButton1 = Radiobutton(ShiftFrame,text="Encode",value=0,variable=ShiftVar,command=shift).grid(row=0,column=0)

mainloop()
