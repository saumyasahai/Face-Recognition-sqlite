
##################################
#                                #
# Code created by Saumya Sahai   #
#                                #  
################################## 

import Tkinter as tk
import os
import sqlite3
import subprocess
#from dataSetCreator import Id
    

root = tk.Tk()

def openNewFile():
    subprocess.Popen("dataSetCreator.py", shell = True)

def openNewFile1():
        subprocess.Popen("dataSetCreator.py", shell = True)        
        conn = sqlite3.connect("FaceBase1.db") # connect to database 
        c = conn.cursor()
        students_query = c.execute("SELECT id FROM People")
        results = c.fetchall() #all ids stored here
        # print(results)
        from dataSetCreator import name
        print(str(name))  #value of Id 


        c.execute("UPDATE Attendence SET Present='P' WHERE id=  " + str(name))
        res = c.execute("SELECT id from Attendence WHERE id = " +str(name))
        print(res)

frame = tk.Frame(root)
root.geometry('300x200')
frame.pack()

button = tk.Button(frame, 
                   text="NEW ENTRY",
                   command=openNewFile)
button.pack(side=tk.LEFT,padx = 20,pady = 70)
slogan = tk.Button(frame,
                   text="UPDATE ATTENDANCE",
                   command=openNewFile1)
slogan.pack(side=tk.LEFT,padx=10,pady=70)

root.mainloop()
