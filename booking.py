import tkinter as tk
from tkcalendar import DateEntry

class bookingwndow(tk.Toplevel):
    def __init__(self, master = None,origin = None,record = None,index = None):
        super().__init__(master)
        self.master = master
        self.title("Booking")
        self.state("zoomed")
        self.config(bg= "#F8F8F8")
        self.origin = origin
        self.transient(master)
        self.header = tk.Label(
            self,
            text="Book a Flight",
            fg = "#34495E",
            bg= "#F8F8F8",  
            font = ("Baloo 2",44),
            borderwidth= 0,
            highlightthickness = 0
        )
        self.header.place(x = 40,y =70)

        self.frame = tk.Frame(
            self, 
            bg= "#E8EAEF",
            highlightthickness = 1,
            highlightbackground="#4285F4",
            highlightcolor="#FFFFFF"
        )

        self.name =tk.Entry(
            self.frame,
            font = ("Baloo 2",20),
            textvariable="Enter your full name: ",
            fg = "#000000",
            bg= "#FFFFFF",
            highlightthickness = 1,
            highlightcolor="#BDC3C7",
            width= 60
        )
        self.name_l = tk.Label(
                self.frame,
            text="Full Name",
            fg = "#000000",
            bg= "#ECF0F1",
            highlightthickness = 1,
            highlightcolor="#FFFFFF",
            font = ("Baloo 2",16)
        )

        self.num =tk.Entry(
            self.frame,
            font = ("Baloo 2",20),
            textvariable="e.g.FS123",
            fg = "#2C3E50",
            bg= "#FFFFFF",
            highlightthickness = 1,
            highlightcolor="#BDC3C7",
            width= 60
        )

        self.num_l = tk.Label(
            self.frame,
            text="Flight Number",
            fg = "#000000",
            bg= "#ECF0F1",
            highlightthickness = 1,
            highlightcolor="#FFFFFF",
            font = ("Baloo 2",16)
        )

        self.departure  =tk.Entry(
            self.frame,
            font = ("Baloo 2",20),
            textvariable="eg.Cairo",
            fg = "#2C3E50",
            bg= "#FFFFFF",
            highlightthickness = 1,
            highlightcolor="#BDC3C7",
            width= 60
        )

        self.departure_l = tk.Label(
                self.frame,
            text="Departure",
            fg = "#000000",
            bg= "#ECF0F1",
            highlightthickness = 1,
            highlightcolor="#FFFFFF",
            font = ("Baloo 2",16)
        )

        self.Destination = tk.Entry(
            self.frame,
            font = ("Baloo 2",20),
            textvariable="e.g.Amesterdam",
            fg = "#2C3E50",
            bg= "#FFFFFF",
            highlightthickness = 1,
            highlightcolor="#BDC3C7",
            width= 60
        )

        self.Destination_l = tk.Label(
                self.frame,
            text="Destination",
            fg = "#000000",
            bg= "#ECF0F1",
            highlightthickness = 1,
            highlightcolor="#FFFFFF",
            font = ("Baloo 2",16)
        )

        self.Date = DateEntry(
            self.frame,
            font = ("Baloo 2",20),
            textvariable="Pick a date",
            fg = "#2C3E50",
            bg= "#FFFFFF",
            highlightthickness = 1,
            highlightcolor="#BDC3C7",
            width= 60
        )

        self.Date_l = tk.Label(
                self.frame,
            text="Date",
            fg = "#000000",
            bg= "#ECF0F1",
            highlightthickness = 1,
            highlightcolor="#FFFFFF",
            font = ("Baloo 2",16)
        )

        self.seat = tk.Entry(
           self.frame,
            font = ("Baloo 2",20),
            textvariable="e.g. 12A",
            fg = "#2C3E50",
            bg= "#FFFFFF",
            highlightthickness = 1,
            highlightcolor="#BDC3C7",
            width= 60
        )

        self.seat_l = tk.Label(
            self.frame,
            text="Seat Number",
            fg = "#000000",
            bg= "#ECF0F1",
            highlightthickness = 1,
            highlightcolor="#FFFFFF",
            font = ("Baloo 2",16)
        )

        self.cancel_btn = tk.Button(
            self.frame,
            text = "Cancel",
            font = ("Baloo 2",12), 
            fg = "#ECF0F1",
            bg = "#34495E",
            width= 15,
            command=self.withdraw # i can use it because my class inherited the functions from toplevel class
        )

        self.book_btn = tk.Button(
            self.frame,
            text = "Book Flight",
            font = ("Baloo 2",12), 
            fg = "#FFFFFF",
            bg = "#2980B9",
            width= 15,
            command=self.book_btn
        )
        
        from database import save_update
        if record:
            self.index = index
            self.header.config(text= "Edit Reservation")
            entities = [self.name,self.num,self.departure,self.Destination,self.Date,self.seat] 
            for index, entity in enumerate(entities): # to start from 1 instead of 0
                entity.delete(0,tk.END)
                entity.insert(0,record[index + 1]) # to skip the id value
            self.book_btn.config(text="Update Reservation", width= 18,command= self.save)
            
                
        self.name_l.grid(row = 0,column=0,pady = 10,sticky = 'w',padx = 10)
        self.name.grid(row = 1,column=0,columnspan=2,sticky="ew",padx = 10)
        self.num_l.grid(row=2,column=0,pady = 10,sticky = 'w',padx = 10)
        self.num.grid(row=3,column=0,columnspan=2,sticky="ew",padx = 10)

        self.departure_l.grid(row= 4,column = 0,pady=10,sticky = 'w',padx =  15)
        self.departure.grid(row= 5,column = 0,padx = 8)

        self.Destination_l.grid(row= 4,column=1,pady=10,sticky = 'w',padx = 15)
        self.Destination.grid(row= 5,column=1,padx = 8)

        self.Date_l.grid(row = 6,column=0,sticky = 'w',padx = 15)
        self.Date.grid(row = 7,column=0,padx = 8,pady=5)

        self.seat_l.grid(row = 6,column=1,sticky = 'w',padx = 15)
        self.seat.grid(row = 7,column=1,padx = 8,pady = 5)


        self.cancel_btn.grid(row = 8, column= 0, sticky= 'e',padx=7,pady=10)
        self.book_btn.grid(row = 8, column=1,sticky= 'w',padx=7,pady=10)

        self.frame.pack(pady = 250)

    def book_btn(self):
        from reservation_list import reservationwindow
        from database import input
        
        Entries = [self.name,self.num,self.departure,self.Destination,self.Date,self.seat]
        labels = [self.name_l,self.num_l,self.departure_l,self.Destination_l,self.Date_l,self.seat_l]
        
        check = True
        for index, entry in enumerate(Entries):
            if len(entry.get()) < 2:
                check = False
                labels[index].config(fg = 'red')
                entry.delete(0,tk.END)
      
        if check:
            input(self.name.get(),self.num.get(),self.departure.get(),self.Destination.get(),self.Date.get(),self.seat.get())
            self.withdraw()
            reservationwindow(self.master,self.origin)
            
            for i in Entries:
                i.delete(0,tk.END)   
    
    
    def save(self):
        from database import save_update
        from reservation_list import reservationwindow
        save_update(self.index,self.name.get(),self.num.get(),self.departure.get(),self.Destination.get(),self.Date.get(),self.seat.get())
        self.withdraw()
        reservationwindow(self.master,self.origin)
        Entries = [self.name,self.num,self.departure,self.Destination,self.Date,self.seat]
        for entity in Entries:
            entity.delete(0,tk.END) 
 