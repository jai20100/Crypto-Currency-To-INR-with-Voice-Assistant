                              #Here is Currency_Converter_With_Voice_Assistant

#These are required modules
import requests 
import tkinter as tk
from tkinter import OptionMenu, Label
from tkinter import *
from num2words import num2words
from gtts import gTTS
import os

# bfvhbfvh
#class with name CurrencyConverter
class CurrencyConverter(tk.Frame):
    # Here we define a function with name __init__ and parameters as shown
    def __init__(self,parent,*args,**kwargs):
        tk.Frame.__init__(self,parent,*args,**kwargs)
       # Here we declared all variable names using StringVar()
        self.grid(padx=(20,30), pady= (30,20))
        self.app_font = ("Helvetica", 20, "bold")
        self.parent = parent
        self.parent.title("CryptoCurrencyConverter(WithVoiceAssistant)")
        self.parent.columnconfigure(0,weight=2)
        self.base_currency = tk.StringVar()
        self.base_currency.set("Base Currency")
        self.target_currency = tk.StringVar()
        self.target_currency.set("Target Currency")
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

        Choice1 = {"INR", "USD", "EUR", "GBP","CAD", "DKK"}
        Choice2 = {"BTC", "ETH","BNB", "USDT","USDC", "BUSD"}
        
        Label_Source = tk.Label(self, textvariable=self.base_text, fg="black",bg="grey", font= "comicsansms 14 bold" )
        Label_Source.grid(row=0, column=0)
        popupMenuF = OptionMenu(self, self.Choice_from, *Choice2)
        popupMenuF.grid(row=0,column=1)

        Label_Target = tk.Label(self, textvariable=self.target_text, fg="black",bg="grey",font= "comicsansms 14 bold")
        Label_Target.grid(row=0, column=5)
        popupMenuTO = OptionMenu(self, self.Choice_To, *Choice1)
        popupMenuTO.grid(row=0,column=7)

        Label_Result = tk.Label(self, textvariable= self.Result_value2, fg="black", font=self.app_font)
        Label_Result.grid(row=1, column=8)

        self.input__ = tk.Label(self, text ="Enter", font=self.app_font, width=8)
        self.input__= Entry(jairoot)
        self.input__.place(x=55, y=65)

        Converting_Button = tk.Button(self, text="Convert", command=self.Convert, bg="green", fg="black",width=6, height=1,borderwidth=4, relief=GROOVE)
        Converting_Button.grid(row=9, column=1)
        Close_Button = tk.Button(self, text="Close", command=self.close,bg="red", fg="black", width=6, height=1,borderwidth=4, relief=GROOVE)
        Close_Button.grid(row=9, column=7)
        Audio_Button = tk.Button(self,text="Hear It", command=self.Hear, bg="blue", fg="black", width=6, height=1,borderwidth=4, relief=GROOVE)
        Audio_Button.grid(row=9, column=4)

    def Convert(self):
        if(self.input__.get()==""):
            Result = "ERROR: Enter any Value to Convert"
            self.Result_value2.set(Result)
        else:
            from__ = self.Choice_from.get()
            to__ = self.Choice_To.get()
            response = requests.get(f"https://api.nomics.com/v1/exchange-rates?key=d2ed4bee6312d6dc37e5f52ee2fbdc254d18d556")
            Data = response.json()
            l1= list(filter(lambda person: person['currency'] == from__, Data))
            l2 = list(filter(lambda person: person['currency'] == to__, Data)) 
            a_key = "rate"
            v1 = [dict[a_key] for dict in l1]
            v2 = [dict[a_key] for dict in l2]
            n_2 = float(v2[0])
            n_1 = float(v1[0])
            p1 = self.input__.get()
            Result = float(p1)*(n_1/n_2)
            Result = format(Result, ".4f")
            self.Result_value1.set(Result)
            c1 = "{:,}".format(float(Result))
            self.Result_value2.set(c1)


    def Hear(self):
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
    def close(self):
        if(self.input__.get()==""):
            self.parent.destroy()
        else:
            self.parent.destroy()
            if(self.j1.get()==""):
                pass
            else:
                os.remove("InSpeech.mp3")
            
        
jairoot = tk.Tk()

# Setting an icon For GUI
jairoot.wm_iconbitmap("Icon1.ico")
CurrencyConverter(jairoot)

# Running main loop
jairoot.mainloop()


    









       

