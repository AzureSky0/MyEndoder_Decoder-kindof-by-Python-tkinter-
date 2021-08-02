from tkinter import*
main = Tk()
main.geometry("700x440")
main.title("MyDecoder")

alphabet=[]
ans=[]

lib = {"00":"a",
       "01":"b",
       "02":"c",
       "03":"d",
       "04":"e",
       "05":"f",
       "06":"g",
       "07":"h",
       "08":"q",
       "09":"w",
       "10":"s",
       "11":"r",
       "12":"t",
       "13":"y",
       "14":"u",
       "15":"i",
       "16":"o",
       "17":"p",
       "18":"j",
       "19":"k",
       "20":"l",
       "21":"m",
       "22":"n",
       "23":"x",
       "24":"v",
       "25":"z",
       "26":"A",
       "27":"P",
       "28":"Q",
       "29":"Z",
       "30":"L",
       "31":"N",
       "32":"M",
       "33":"G",
       "34":"H",
       "35":"K",
       "36":"J",
       "37":"U",
       "38":"W",
       "39":"T",
       "40":"R",
       "41":"E",
       "42":"X",
       "43":"C",
       "44":"V",
       "45":"B",
       "46":"D",
       "47":"F",
       "48":"I",
       "49":"O",
       "50":"Y",
       "51":"S",
       "52":" ",
       "53":"`",
       "54":"@",
       "55":"!",
       "56":"#",
       "57":"&",
       "58":"-",
       "59":"_",
       "60":",",
       "61":".",
       "62":"?",
       "63":";",
       "64":"(",
       "65":")",
       "66":":",
       "100":"1",
       "101":"7",
       "102":"2",
       "103":"5",
       "104":"3",
       "105":"8",
       "106":"4",
       "107":"9",
       "108":"6",
       "109":"0"
       }





       
Default = "Enter The Code"
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
    
    x=strInput.split("a")
    print(x)
    for i in x:
        alphabet.append(i)

    alphabet.pop(0)
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

print(alphabet)
print(alphabet[0])
temp=[]

for i in alphabet:
    if i in lib:
        temp.append(lib[i])

print(len(temp))

for i in range(len(temp)):
    str+=temp[i]

print(f"Secret Code is : {str}")    
