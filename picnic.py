from tkinter import*
import random
root=Tk()
root.geometry("500x500")
root.title("Lucky Friend-1D")

label1=Label(root)
label1.place(relx=0.5, rely=0.5, anchor=CENTER)
label2=Label(root)
label2.place(relx=0.5, rely=0.3, anchor=CENTER)
list1=["Bottle","Tiffen","Juice","Chocalates","Chips","Blanket"]
print(list1)




def rn():
    length=len(list1)
    ranu1=random.randint(0, length)
    random1=list1[ranu1]
    label2["text"]=list1
    label1["text"]=random1

button=Button(root,text="Generate Stuff",command=rn)
button.place(relx=0.5, rely=0.4, anchor=CENTER)

root.mainloop()