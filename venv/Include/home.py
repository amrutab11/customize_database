from tkinter import *
from tkinter import messagebox


class myFrame(Frame):
    attributes = []
    List = []
    table_name = None
    dict = {}
    attributes2 = []

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.lbl_input=Label(master, text='Input')
        self.lbl_input.place(x=20, y=20)
        self.lbl_output=Label(master, text='Output')
        self.lbl_output.place(x=270,y=20)
        self.lbl_out=Label(master, text="text",bg="pink")
        self.lbl_out.place(x=250,y= 60,width=210,height=320)
        self.txt_input = Text(master)
        self.txt_input.place(x=20, y=60,height=320, width=210)
        self.btn_fire = Button(master,command=self.buttonClick, text = 'Fire', bg ="Cyan")
        self.btn_fire.place(x=150, y=400, width=200, height=30)

    def buttonClick(self):
        query = self.txt_input.get("1.0",END)
        token = query.split()
        str1 = ""
        print("len: "+str(len(token)))
        print("token[0] :"+ str(token[0]))
        if len(token) == 3:
            if token[0] == "delete":
                del self.List[0:]
                print(self.List)

            if token[0] == "drop":
                del self.List[0:]
                del self.attributes[0:]
                messagebox.showinfo("information", "Table is Droped")

        if len(token) == 4:
            if token[0] == "create":
                print("Table is creating")
                self.attributes = token[3].split(",")
                self.attributes[0] = self.attributes[0].strip("(")
                self.attributes[len(self.attributes)-1] = self.attributes[len(self.attributes)-1].strip(")")
                self.table_name=token[2]
                for temp in self.attributes:
                    self.dict[temp] = None
                print("attributes in create: " + str(self.attributes))
                print("Table is created")
                messagebox.showinfo("information", "Table is created")

            if token[0] == "select":
                print("In select statement")
                str1 = ""
                if token[3] != self.table_name:
                    messagebox.showinfo("Error", "Table does not exist")
                elif token[1] == "*":
                    print("attributes: "+str(self.attributes))
                    for i in self.attributes:
                         str1 = str1 + str(i) + "\t"
                    str1 = str1 + "\n"
                    for row in self.List:
                        for attr in self.attributes:
                            str1 = str1+str(row[attr])+"\t"
                        str1 = str1 + "\n"
                elif token[1] != "*":
                    self.attributes2 = token[1].split(",")
                    print("attributes: "+str(self.attributes2))
                    for i in self.attributes2:
                        str1 = str1 + str(i)+"\t"
                    str1 = str1 + "\n"
                    for row in self.List:
                        print("str1: "+str1)
                        for attr in self.attributes2:
                            str1 = str1+str(row[attr])+"\t"
                        str1 = str1 + "\n"
                self.lbl_out['text'] = str1

            if token[0] == "update":
                key_values= token[3].split(",")
                print(key_values)
                for pair in key_values:
                    key, value = pair.split("=")
                    print("Key: "+key+" Value: "+value)
                    for temp in self.List:
                        print("List of keys: "+str(self.attributes))
                        if key not in self.attributes:
                            messagebox.showinfo("information", "'"+key+"' Column does not exist")
                            break
                        if key in self.attributes:
                            temp[key] = value
                        messagebox.showinfo("information", "Table updated successfully")

        if len(token) == 5:
            if token[0] == "insert":
                print("In insert function")
                print("attributes in insert: "+str(self.attributes))
                self.values = token[4].split(",")
                self.values[0] = self.values[0].strip("(")
                self.values[len(self.values) - 1] = self.values[len(self.values) - 1].strip(")")
                print("values in insert: "+str(self.values))
                temp = {}
                print("temp : "+str(temp))
                for key in self.attributes:
                    for value in self.values:
                        temp[key] = value
                        self.values.remove(value)
                        break
                self.List.append(temp)
                print("List"+str(self.List))
                messagebox.showinfo("information", "Row inserted successfully with values "+str(temp))

            if token[0] == "delete":
                key, value = token[4].split("=")
                print("key: "+key+" value: "+value)
                for temp in self.List:
                    if temp[key] == value:
                        self.List.remove(temp)
                print("List: "+str(self.List))
                messagebox.showinfo("information", "Row deleted successfully with values " + str(key)+ " = " + str(value))

            if token[0] == "alter":
                self.attributes.append(token[4])
                for temp in self.List:
                    temp[token[4]] = None
                messagebox.showinfo("information",
                                    "Table altered successfully by adding column " + str(token[4]))

        if len(token) == 6:
            if token[0] == "insert":
                print("In insert function")
                self.attributes2 = token[3].split(",")
                self.attributes2[0] = self.attributes2[0].strip("(")
                self.attributes2[len(self.attributes2) - 1] = self.attributes2[len(self.attributes2) - 1].strip(")")
                self.values = token[5].split(",")
                print("attributes in insert: " + str(self.attributes))
                self.values[0] = self.values[0].strip("(")
                self.values[len(self.values) - 1] = self.values[len(self.values) - 1].strip(")")
                print("values in insert: " + str(self.values))
                temp = {}
                print("temp : " + str(temp))
                for key in self.attributes2:
                    for value in self.values:
                        if key in self.attributes:
                            temp[key] = value
                            self.values.remove(value)
                            break
                self.List.append(temp)
                print("List" + str(self.List))
                messagebox.showinfo("information", "Row inserted successfully with values " + str(temp))

            if token[0] == "alter":
                if token[3] == "drop":
                    self.attributes.remove(token[5])
                    for temp in self.List:
                        del temp[token[5]]
                    messagebox.showinfo("information",
                                    "Table altered successfully by removing column " + str(token[5]))

            if token[0] == "update":
                key_values= token[3].split(",")
                attr,val = token[5].split("=")
                print(key_values)
                for pair in key_values:
                    key, value = pair.split("=")
                    print("Key: "+key+" Value: "+value)
                    for temp in self.List:
                        print("List of keys: "+str(self.attributes))
                        if key not in self.attributes:
                            messagebox.showinfo("information", "'"+key+"' Column does not exist")
                        if key in self.attributes:
                            if temp[attr] == val:
                                temp[key] = value
                            messagebox.showinfo("information", "Table updated successfully")

if __name__ == "__main__":
    guiFrame = myFrame()
    guiFrame.place(height=500,width=500)
    guiFrame.mainloop()