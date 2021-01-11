from tkinter import *

root=Tk()
root.geometry("500x300")
#root.resizable(False,False) #commented it so it can be resized,un-comment it to fix the size
root.title("Website Blocker")

#making the blocker work
def Blocker():
    Website_lists=Websites.get(1.0,END)
    Website=list(Website_lists.split(","))

    #now open the file and put the website link in it
    with open(host_path,'r+') as host_file :
        file_content=host_file.read()
        for Website in file_content:
            if Website in   file_content:
                Label(root,text='Already blocked', font=('arial 12 bold')).place(x=200,y=200)
                pass
            else:
                host_file.write(ip_address+""+Website+"\n")
                Label(root,text='Succesfully Blocked', font=('arial 12 bold')).place(x=230,y=200)


Label(root,text="Website blocker", font='arial 20 bold').pack()
Label(root,text="Made by Aditya N Bhatt", font="arial 10 bold").pack()

# creating the blocker
host_path='C:\Windows\System32\drivers\etc\hosts'
ip_address= '127.0.0.1'

#creating the entry butoon to feed the valuyes
Label(root,text="enter the website",font="arial 12 bold").place(x=5,y=60)
Websites = Text(root,font = 'arial 10',height='2', width = '40', wrap = WORD, padx=5, pady=5)
Websites.place(x=140,y=60)

#create block button
block=Button(root,text="Block!!",font='arial 12 bold',pady=5, width=6, bg='red',activebackground='white',command=Blocker)
block.place(x=230,y=150)


root.mainloop()