import tkinter as tk
import sqlite3


def baglanti():
    conn = sqlite3.connect("yapilacaklar.db")
    if conn:
        print("Bağlantı başarılı.")
    else:
        print("Bağlantı kurulumadı.")

    return conn

def ekle():
    box.insert(tk.END, e.get())
    e.delete(0, tk.END)

def sil():
    if len(box.curselection()) > 0:
        index = box.curselection()[0]
        box.delete(index)

def kaydet():
    f = open('yapilacaklar.db', 'w', encoding='utf-8')
    gorevler = box.get(0, tk.END)
    f.writelines('\n'.join(gorevler))
    f.close()

def cikis():
    print("Listeden çıkış yapılıyor.")
    pencere.after(20, pencere.destroy)

dbconnect = baglanti()
pencere = tk.Tk()
pencere.title("Yapılacaklar Listesi")

f = tk.Frame(pencere)
f.pack()
box = tk.Listbox(f, width=50, height=10)
box.pack(side=tk.LEFT)
scroll = tk.Scrollbar(f, command=box.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
box.config(yscrollcommand=scroll.set)

e = tk.Entry(pencere, width=40)
e.pack()
b_ekle = tk.Button(pencere, text='Görev Ekle', command=ekle)
b_ekle.pack()
b_sil = tk.Button(pencere, text='Görevi Sil', command=sil)
b_sil.pack()
b_kaydet = tk.Button(pencere, text='Görevleri Kaydet', command=kaydet)
b_kaydet.pack()
b_cikis = tk.Button(pencere, text='Çıkış', command=cikis)
b_cikis.pack()

pencere.mainloop()
dbconnect.close()
