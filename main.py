import pandas
import tkinter as tk
import requests
import csv


def SATS_MULTIPLIER():
    return 0.0000000000000001

window = tk.Tk()              # creo una schermata
window.geometry('600x200')    # dimensioni della finestra
window.title("Bitcoin wallet balance")
window.grid_columnconfigure(0, weight="1")

window.resizable(False, False)

btcBalanceBox = tk.Text()
btcBalanceBox.place(x=200, y=135, width=200, height=20)
btcBalanceBox.configure(state='disabled')

inputBoxAddr = tk.Entry()
inputBoxAddr.place(x=110, y=25, width=400)

label = tk.Label(window, text="Address:",
                 font=("Helvetica",15))
label.place(x=20, y=18)

def getBalance():
        try:
                inputAddr = inputBoxAddr.get()
                address_url = 'https://blockchain.info/rawaddr/'+inputAddr

                df = pandas.read_json(address_url)
                balance = df['final_balance']
                value = ""

                for i in balance:
                        value = value + str(i)

                satValue = int(value)
                btcValue = satValue * SATS_MULTIPLIER()

                btcBalanceBox.configure(state='normal')
                btcBalanceBox.delete('1.0', tk.END)
                btcBalanceBox.insert('1.0', str(btcValue))
                btcBalanceBox.configure(state='disabled')

                labelBtc = tk.Label(window, text="btc",
                                    font=("Helvetica", 15))
                labelBtc.place(x=410, y=130)
        except:
                btcBalanceBox.configure(state='normal')
                btcBalanceBox.delete('1.0', tk.END)
                btcBalanceBox.insert('1.0', "Input error!")
                btcBalanceBox.configure(state='disabled')



# Pulsante get balance
button_insert = tk.Button(text="GET BALANCE", command= lambda :  getBalance(), height=2, width=20)          # lambda non loso, da approfondire
button_insert.place(x=250, y=70, width=100)

if __name__ == "__main__":
    window.mainloop()







