from tkinter import *

toDoList=["Learn Python","Practice","Develop Application","Add Application to Git"]
Doinglist=[]
Completedlist=[]


def get_text():
    text = entry.get()
    if text not in toDoList and text !="":
        todolistbox.insert(END, text)
        entry.delete(0, END)
        return
    else:
        return

def movetodoing():
    cur = todolistbox.get(todolistbox.curselection())
    if cur not in Doinglist and cur != None:
        currdoinglist.insert(currdoinglist.size(),cur)
        todolistbox.delete(todolistbox.curselection())
        Doinglist.append(cur)
        return
    else:
        return
def movetoCompeleted():
    select = currdoinglist.get(currdoinglist.curselection())
    if select not in Completedlist:
        doneTasklistbox.insert(END, select)
        Completedlist.append(select)
        currdoinglist.delete(currdoinglist.curselection())
        return
    else:
        return
def delete():
    doneTasklistbox.delete(doneTasklistbox.curselection())
    return
window=Tk()
window.title("TO DO LISTBOX ")
window.geometry("800x400")


todolabel=Label(window,text="TO DO BOX").grid(row=1,column=0)

todolistbox=Listbox(window,font=("Arial",15),bd=5,bg="white",fg="blue",width=20)
todolistbox.grid(row=2,column=0)
todolistbox.config(height=10)

currdoinglabel=Label(window,text="PROCESSING BOX").grid(row=1,column=1)

currdoinglist=Listbox(window,font=("Arial",15),bd=5,bg="white",fg="green",width=20)
currdoinglist.grid(row=2,column=1)
currdoinglist.config(height=10)

doneTasklabel=Label(window,text="COMPLETED BOX").grid(row=1,column=2)

doneTasklistbox=Listbox(window,font=("Arial",15),bd=5,bg="white",fg="red",width=20)
doneTasklistbox.grid(row=2,column=2)
doneTasklistbox.config(height=10)



entry = Entry(window,width=20,bd=5)
entry.grid(row=0,column=0,columnspan=2)

todolistbox.insert(1,"Learn Python")
todolistbox.insert(2,"Practice")
todolistbox.insert(3,"Develop Application")
todolistbox.insert(4,"Add Application to Git")

addbutton=Button(window,text="Add Task",pady=4,padx=10,command=get_text,bg="gray",fg="white")
addbutton.grid(row=0,column=1)

movebutton=Button(window,text="Process",pady=5,padx=20,command=movetodoing,bg="green",fg="white")
movebutton.grid(row=5,column=0)

deletebutton=Button(window,text="Delete",pady=5,padx=20,command=delete,bg="black",fg="white")
deletebutton.grid(row=5,column=2)
moveToCompletedTaskButton=Button(window,text="Compelete",pady=5,padx=20,command=movetoCompeleted,bg="red",fg="white")
moveToCompletedTaskButton.grid(row=5,column=1)

window.mainloop()