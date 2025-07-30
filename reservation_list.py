import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  
import database 
import edit_reservation 


class reservationwindow(tk.Toplevel):
    def __init__(self,master,origin = None):
        super().__init__(master)
        self.master = master
        self.origin = origin
        self.title("Reservation")
        self.state("zoomed")
        self.config(bg="#F8F8F8")
        self.transient(master)
        res = edit_reservation.reserve_editing(self)  # made an instance of the class to use the class methods
        
        
        self.header = tk.Label(
            self,
            text="Your Reservation",
            fg = "#34495E",
            bg= "#F8F8F8",  
            font = ("Baloo 2",34),
            borderwidth= 0,
            highlightthickness = 0
        )


        self.frame = tk.Frame(
            self,
            width= 800,
            height= 260,
            bg= "#E8EAEF",
            highlightthickness = 1,
            highlightbackground="#4285F4",
            highlightcolor="#FFFFFF"
        )

        self.text = tk.Label(
            self,
            text="No reservations Found",
            fg = "#34495E",
            bg= "#E8EAEF",  
            font = ("Baloo 2",25),
            borderwidth= 0,
            highlightthickness = 0
        )

        self.des = tk.Label(
            self,
            text="You haven't booked any flights yet",
            fg = "#000000",
            bg= "#E8EAEF",  
            font = ("Baloo 2",20),
            highlightthickness = 1,
            highlightcolor="#FFFFFF"
        )

        self.book_new_flight = tk.Button(
            self,
            text = "Book New Flight",
            font = ("Baloo 2",14), 
            fg = "#FFFFFF",
            bg = "#2980B9",
            width= 15,
            command=res.book_again
        )

        self.book_your_first_flight = tk.Button(
            self,
            text = "Book your first flight",
            font = ("Baloo 2",16), 
            fg = "#FFFFFF", 
            bg = "#2980B9", 
            width= 18,
            command=res.book_again
        )
        
        self.back = tk.Button(
            self,
            text = "Home",
            font = ("Baloo 2",15), 
            fg = "#ECF0F1",
            bg = "#34495E",
            width= 7,
            command=self.withdraw
        )
        
        self.id_input = tk.Entry(
            self,
            font= ("Baloo 2", 20),
            fg = "#2C3E50",
            bg = "#FFFFFF",
            width= 16
        ) 
        
        self.edit = tk.Button(
            self,
            text = "Edit",
            font= ("Baloo 2", 12),
            fg = "#FFFFFF",
            bg = "#2980B9",
            width= 7,
            command= res.change
        )
        
        self.cancel = tk.Button(
            self,
            text= "Delete",
            font= ("Baloo 2", 12),
            fg = "#ECF0F1",
            bg = "#34495E",
            width= 7,
            command=res.cancel_clicked # lamda is used to pass the argument 
        )
        
        self.cancel_all = tk.Button(
            self,
            text= "Delete All reservations",
            font= ("Baloo 2", 15),
            fg = "white",
            bg = "red",
            width= 22,
            command= res.delete_table_content
        )
        
        
        self.idlabel = tk.Label(
            self,
            text = "Enter the ID",
            font= ("Baloo 2", 16),
            fg = "#000000",
            bg= "#F8F8F8"
        )
        
        columns = ("id", "name", "flight_number", "departure", "destination", "date", "seat_number")
        self.table = ttk.Treeview(self, columns= columns,show='headings')


        self.header.place(x = 60,y =70)
        self.book_new_flight.place(x = 1500,y =75)
        self.back.place(x= 1380, y= 76)

        if database.Count() == 0:
            self.text.place(x = 785,y = 300)
            self.des.place(x = 730,y = 340)
            self.book_your_first_flight.place(x = 835,y = 400)
            self.frame.pack(padx = 30,pady = 230)
            
        else:
            for col in columns:
                self.table.heading(col,text=col.replace("_",' ').title())
                self.table.column(col, width= 120)           
            
            for row in database.db_table():
                self.table.insert("",'end',values = row)
            self.cancel_all.place(x = 400, y = 880)
            self.cancel.place(x = 240, y = 950)
            self.edit.place(x = 120, y = 950)
            self.idlabel.place(x = 120, y =845)
            self.id_input.place(x = 110,y = 880)
            self.table.pack(padx = 25,pady = 230)
            