                           #Here is Currency_Converter_With_Voice_Assistant

#These are required modules
import requests 
import tkinter as tk
from tkinter import OptionMenu, Label
from tkinter import *
from num2words import num2words
from gtts import gTTS
import os

#Here We initialize Tkinter
ITW_root = tk.Tk()

#class with name CurrencyConverter
class CurrencyConverter(tk.Frame):
    # Here we define a function with name __init__ and parameters as shown
    def __init__(self,parent,*args,**kwargs):
        tk.Frame.__init__(self,parent,*args,**kwargs)

 #We plot grid here and set font of parent

        self.grid(padx=(20,30), pady= (30,20))
        self.app_font = ("Helvetica", 20, "bold")
        self.parent = parent
        self.parent.title("CryptoCurrencyConverter(WithVoiceAssistant)")
        self.parent.columnconfigure(0,weight=2)

# Here we declared all required variable names using StringVar() function

        self.base_currency = tk.StringVar()
        self.base_currency.set("Base Currency") # stores Base currency, which we want to convert
        self.target_currency = tk.StringVar()
        self.target_currency.set("Target Currency")  # Stores Target currency, To which we want to covert
        self.base_text = tk.StringVar()
        self.base_text.set("From:")
        self.target_text = tk.StringVar()
        self.target_text.set("To:")
        self.amount = tk.StringVar()
        self.amount.set("0")
        self.j1 = tk.StringVar()
        self.j1.set("")
        self.Result_value1 = tk.StringVar()
        self.Result_value1.set("0")
        self.Result_value2 = tk.StringVar()
        self.Result_value2.set("0")
        self.Choice_from = tk.StringVar()
        self.Choice_from.set("BTC")
        self.Choice_To = tk.StringVar()
        self.Choice_To.set("INR")

#We listed only top currencies here and stored in chocies

        Choice1 = {"INR", "USD", "EUR", "GBP","CAD", "DKK"}
        Choice2 = {"BTC", "ETH","BNB", "USDT","USDC", "BUSD"}

# Here we Define Lables like "FROM" "TO"  and PopUpMenu 
        
        Label_Source = tk.Label(self, textvariable=self.base_text, fg="black",bg="grey", font= "comicsansms 14 bold" )
        Label_Source.grid(row=0, column=0)
        popupMenuF = OptionMenu(self, self.Choice_from, *Choice2)
        popupMenuF.grid(row=0,column=1)

        Label_Target = tk.Label(self, textvariable=self.target_text, fg="black",bg="grey",font= "comicsansms 14 bold")
        Label_Target.grid(row=0, column=5)
        popupMenuTO = OptionMenu(self, self.Choice_To, *Choice1)
        popupMenuTO.grid(row=0,column=7)

#Defining Final Result Displaying Label

        Label_Result = tk.Label(self, textvariable= self.Result_value2, fg="black", font=self.app_font)
        Label_Result.grid(row=1, column=8)

#Here We take input from user as an interger

        self.input__ = tk.Label(self, text ="Enter", font=self.app_font, width=8)
        self.input__= Entry(ITW_root)
        self.input__.place(x=55, y=65)

#Here we define Coverting Button and give Commands To them

        Converting_Button = tk.Button(self, text="Convert", command=self.Convert, bg="green", fg="black",width=6, height=1,borderwidth=4, relief=GROOVE)
        Converting_Button.grid(row=9, column=1)
        Close_Button = tk.Button(self, text="Close", command=self.close,bg="red", fg="black", width=6, height=1,borderwidth=4, relief=GROOVE)
        Close_Button.grid(row=9, column=7)
        Audio_Button = tk.Button(self,text="Hear It", command=self.Hear, bg="blue", fg="black", width=6, height=1,borderwidth=4, relief=GROOVE)
        Audio_Button.grid(row=9, column=4)

#Here is Functionality of Covert button

    def Convert(self):

    #this If-Else condition throughs an error , if user hits Convert button without giving any input value
        if(self.input__.get()==""):
            Result = "ERROR: Enter any Value to Convert" #If user gives nothing in input and hit convert button There shows an error
            self.Result_value2.set(Result)
        else:
            from__ = self.Choice_from.get()
            to__ = self.Choice_To.get()

        #Pulls Data from API and stores in Data

            response = requests.get(f"https://api.nomics.com/v1/exchange-rates?key=d2ed4bee6312d6dc37e5f52ee2fbdc254d18d556")
            Data = response.json()  # converts HTML response to json Format

    # Here "l1" stores filtered list of Dictonary, containing Selected currency and its Exchange Rate

            l1= list(filter(lambda person: person['currency'] == from__, Data))
    # Here "l2" stores filtered list of Dictonary, containing Selected currency and its Exchange Rate
            l2 = list(filter(lambda person: person['currency'] == to__, Data)) 
            a_key = "rate"
    # v1 stores rate of l1

            v1 = [dict[a_key] for dict in l1]
    # v2 stores rate of l2
            v2 = [dict[a_key] for dict in l2]
            n_2 = float(v2[0])
            n_1 = float(v1[0])
    # p1 stores user input value
            p1 = self.input__.get()

# Logic of Conversion:

# Rate = Base Currency / USD
# RateOf_From = Selected FROM Currency / USD
# RateOf_To = Selected TO Currency / USD
# Required rate = RateOf_From / RateOf_To
# Result = User_Input(user input) * Required Rate 

            Result = float(p1)*(n_1/n_2)
            Result = format(Result, ".4f")
            self.Result_value1.set(Result)
        # Adds comma(,) to result and stores in c1
            c1 = "{:,}".format(float(Result))  
            self.Result_value2.set(c1)

#Here is Functionality of Hear button

    def Hear(self):
  
    #this If-Else condition throughs an error , if user hits hear button without giving any input value
        if(self.input__.get()==""):
            Result = "ERROR: Enter any Value to Hear"
            self.Result_value2.set(Result)
        else:
            r1 = self.Result_value1.get()
            self.Result_value1.set(r1)
            j1 = num2words(r1)
            language = "en"
            speech1 = gTTS(text=j1, lang=language, slow= False)
            speech1.save("InSpeech.mp3")
            os.system("InSpeech.mp3")

#Here is Functionality of Close button

    def close(self):
        if(self.input__.get()==""):
            self.parent.destroy()
        else:
            self.parent.destroy()
            if(self.j1.get()==""):
                pass
            else:
                os.remove("InSpeech.mp3") # Deletes InSpeech.mp3 After close app, to save storage
            

# Setting an icon For GUI
ITW_root.wm_iconbitmap("Icon1.ico")
CurrencyConverter(ITW_root) #Calling class

# Running main loop
ITW_root.mainloop()
