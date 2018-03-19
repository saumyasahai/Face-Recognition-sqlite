
##################################
#                                #
# Code created by Saumya Sahai   #
#                                #  
################################## 


import Tkinter as tk
import sqlite3

class ExampleApp(tk.Frame):
    ''' An example application for TkInter.  Instantiate
        and call the run method to run. '''
    def __init__(self, master):
        # Initialize window using the parent's constructor
        tk.Frame.__init__(self,
                          master,
                          width=500,
                          height=300)
        # Set the title
        self.master.title('Enter Details')
 
        # This allows the size specification to take effect
        self.pack_propagate(0)
 
        # We'll use the flexible pack layout manager
        self.pack()

        self.w = tk.Label(self, text="Enter Student's Roll Number ")
        self.w.pack()
        
        # The greeting selector
        # Use a StringVar to access the selector's value
        self.greeting_var = tk.StringVar()
        self.greeting = tk.Entry(self,
                                  textvariable=self.greeting_var)

        # The recipient text entry control and its StringVar
        
        ## code by Bhaskar
        conn = sqlite3.connect("FaceBase1.db") # connect to database 
        c = conn.cursor() # getting cursor
        subjects_query = c.execute("SELECT * FROM Subjects") # get all subjects from data base

        all_subjects = [] 
        self.subject_mappings = {}
        for i in subjects_query:
          all_subjects.append(str(i[0])) # make an array of all subjects listed in database
          self.subject_mappings[str(i[0])] = i[1] # map the subject name to unique id in database for query

        self.recipient_var = tk.StringVar()

        self.recipient = apply(tk.OptionMenu, (self, self.recipient_var) + tuple(all_subjects))
        self.recipient_var.set(all_subjects[0])
        ## end of code by Bhaskar
        
        # The go button
        self.go_button = tk.Button(self,
                                   text='Go',
                                   command=self.print_out)

        
        
        # Put the controls on the form
        self.text = tk.Text(self, wrap = tk.NONE, height = 17, width = 70) # make text widget
        self.text.insert(tk.INSERT, "Attendence\tDate \n") #heading for attendence table
        self.text.config(state=tk.DISABLED) # disable editing in text widget

        self.go_button.pack(fill=tk.X, side=tk.BOTTOM)
        self.greeting.pack(fill=tk.X, side=tk.TOP)
        self.recipient.pack(fill=tk.X, side=tk.TOP)
        self.text.pack(fill=tk.X, side=tk.TOP)
      
 
    def print_out(self):
        ''' Print a greeting constructed
            from the selections made by
            the user. '''
        try:

          subject = self.subject_mappings[str(self.recipient_var.get())] # get primary key of subject from dictionary created above
          student = self.greeting_var.get().title() # get the id of student (primary key)
          
          conn = sqlite3.connect("FaceBase1.db") # connect to database
          cur = conn.cursor() # cursor
          res = cur.execute("SELECT present, date FROM Attendence WHERE Student=" + str(student) + " AND Subject=" + str(subject)) # get the date and present record from the database

          
          results = []
          self.text.config(state=tk.NORMAL) # enable editing in text widget
          self.text.delete(1.0, tk.END) # delete everything from text widget
          
          present = 0

          for i in res: # iterating over query result
            results.append([str(i[0]), str(i[1])])
            if str(i[0]) == 'P':
              present += 1
          self.text.insert(tk.INSERT, "ATTENDENCE:"+ str(present*100/len(results))+"%\n") #write and calculate attendance %
          self.text.insert(tk.INSERT, "Attendence\tDate \n")
          for i in results:
            self.text.insert(tk.INSERT, str(i[0])+"\t\t"+str(i[1])+"\n") # write the query result
          self.text.config(state=tk.DISABLED) # disable editing in text widget
          
          conn.close() # close connection

          print('%s, %s!' % (self.greeting_var.get().title(),
                             self.recipient_var.get()))
        except:
          self.text.config(state=tk.NORMAL)
          self.text.delete(1.0, tk.END)
          self.text.insert(tk.INSERT, "ERROR") # in case anything goes wrong
          self.text.config(state=tk.DISABLED)

    def run(self):
        ''' Run the app '''
        self.mainloop()
 
app = ExampleApp(tk.Tk())
app.run()
