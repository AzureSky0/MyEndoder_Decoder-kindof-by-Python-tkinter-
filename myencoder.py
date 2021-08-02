from tkinter import*
main = Tk()
main.geometry("700x440")
main.title("MyEncoder")

alphabet=[]
ans=[]


lib = {"a":"a00",
       "b":"a01",
       "c":"a02",
       "d":"a03",
       "e":"a04",
       "f":"a05",
       "g":"a06",
       "h":"a07",
       "q":"a08",
       "w":"a09",
       "s":"a10",
       "r":"a11",
       "t":"a12",
       "y":"a13",
       "u":"a14",
       "i":"a15",
       "o":"a16",
       "p":"a17",
       "j":"a18",
       "k":"a19",
       "l":"a20",
       "m":"a21",
       "n":"a22",
       "x":"a23",
       "v":"a24",
       "z":"a25",
       "A":"a26",
       "P":"a27",
       "Q":"a28",
       "Z":"a29",
       "L":"a30",
       "N":"a31",
       "M":"a32",
       "G":"a33",
       "H":"a34",
       "K":"a35",
       "J":"a36",
       "U":"a37",
       "W":"a38",
       "T":"a39",
       "R":"a40",
       "E":"a41",
       "X":"a42",
       "C":"a43",
       "V":"a44",
       "B":"a45",
       "D":"a46",
       "F":"a47",
       "I":"a48",
       "O":"a49",
       "Y":"a50",
       "S":"a51",
       " ":"a52",
       "`":"a53",
       "@":"a54",
       "!":"a55",
       "#":"a56",
       "&":"a57",
       "-":"a58",
       "_":"a59",
       ",":"a60",
       ".":"a61",
       "?":"a62",
       ";":"a63",
       "(":"a64",
       ")":"a65",
       ":":"a66",
       "1":"a100",
       "7":"a101",
       "2":"a102",
       "5":"a103",
       "3":"a104",
       "8":"a105",
       "4":"a106",
       "9":"a107",
       "6":"a108",
       "0":"a109"
       }
       
Default = "Enter A string"
T1 = StringVar()
T1.set(Default)
inputBox = Entry(main,textvariable=T1,width=90,relief=GROOVE)
inputBox.grid(row=0,column=0)
TextBox=Text(main)



temp=[]

def display():
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
        if i in lib:
            temp.append(lib[i])
    
    for i in range(len(temp)):
        strg+=temp[i]

    print(len(temp))
    TextBox.insert("end",strg)
    print(f"Secret Code is : {strg}")



DisplayButton = Button(main,text=">",width=10,command=display).grid(row=0,column=1)

TextBox.grid(row=1,column=0,columnspan=2,padx=30)



mainloop()    
