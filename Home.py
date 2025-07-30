import tkinter as tk # as tk used to shorten the name while coding
from booking import bookingwndow
from reservation_list import reservationwindow

class home():
    def __init__(self):
            
        self.root = tk.Tk()
        self.root.title("ByeByeBirdie reservation")
        self.root.state("zoomed")
        self.root.config(bg= "#F8F8F8")

        self.header = tk.Label(
            self.root,
            text = "welcome to ByeByeBirdie reservation",
            fg = "#34495E",
            bg= "#F8F8F8",  
            font = ("Baloo 2",45),
            borderwidth= 0,
            highlightthickness = 0
            )
        self.header.pack(pady= 30)

        self.describtion = tk.Label(
            self.root,
            text = "Book your flights and manages your reservations with our simple and intuitve system",
            fg = "#7F8C8D",
            bg= "#F8F8F8",  
            font = ("Poppins",20),
            height= 2,
            borderwidth= 0,
            highlightthickness = 0,
            wraplength= 600
            )
        self.describtion.pack()


        self.widget1 = tk.Frame(
            self.root,
            width = 500, 
            height = 500, 
            bg= "#E8EAEF",
            highlightthickness = 1,
            highlightbackground="#4285F4",
            highlightcolor="#FFFFFF"
            )
        self.widget1.rowconfigure(0,weight=1)
        self.widget1.rowconfigure(1,weight=1)
        self.widget1.rowconfigure(2,weight=1)

        self.widget2 = tk.Frame(
            self.root,
            width = 500, 
            height = 500, 
            bg= "#E8EAEF",
            highlightthickness = 1,
            highlightbackground="#4285F4",
            highlightcolor="#FFFFFF"
            )
        self.widget2.rowconfigure(0,weight=1)
        self.widget2.rowconfigure(1,weight=1)
        self.widget2.rowconfigure(2,weight=1)

        self.widget1.pack_propagate(False)
        self.widget2.pack_propagate(False)


        self.booking_label1 = tk.Label(
            self.widget1,
            text = "Book a Flight",
            font = ("Baloo 2",26),
            width = 17, 
            height =2,  
            fg = "#34495E",
            bg= "#E8EAEF",
            wraplength=400
            )       

        self.booking_label2 = tk.Label(
            self.widget1,
            text = '''Reserve your next flight by providing your details and flight information.''',
            font = ("Baloo 2",18), 
            height =4, 
            fg = "#7F8C8D",
            bg= "#E8EAEF",
            wraplength=400
            )

        self.btn1 = tk.Button(
            self.widget1,
            text = "Book a flight",
            font = ("Baloo 2",18),
            width = 14, 
            height =1,   
            fg = "#FFFFFF",
            bg= "#2980B9",
            command=self.book_btn_clicked
            )

        self.reservation_list = tk.Label(
            self.widget2,
            text = "View Reservations",
            font = ("Baloo 2",26),
            width = 17, 
            height =2,  
            fg = "#34495E",
            bg= "#E8EAEF",
            wraplength=400
            )

        self.reservation_text = tk.Label(
            self.widget2,
            text = '''Manage your existing reservations, view details, edit or cancel if needed.''',
            font = ("Baloo 2",18), 
            height =4,  
            fg = "#7F8C8D",
            bg= "#E8EAEF",
            wraplength=400,
            )

        self.btn2 = tk.Button(
            self.widget2,
            text = "View Reservations",
            font = ("Baloo 2",18),
            width = 17, 
            height =1,   
            fg = "#FFFFFF",
            bg= "#2980B9",
            command=self.veiw_reservation
            )


        self.booking_label1.grid(row = 0, column = 0)
        self.booking_label2.grid(row = 1, column = 0,pady = 5,padx=10)
        self.btn1.grid(row = 2, column = 0, pady = 8)
        self.reservation_list.grid(row = 0, column = 0)
        self.reservation_text.grid(row = 1, column = 0,pady= 5,padx=10)
        self.btn2.grid(row = 2, column = 0,pady= 8)


        self.widget1.pack(side=tk.LEFT, padx=220, pady=40)
        self.widget2.pack(side=tk.RIGHT, padx=220, pady=40)

        self.root.mainloop()
        
    def book_btn_clicked(self):
        bookingwndow(self.root,self)
    
    def veiw_reservation(self):
        reservationwindow(self.root,self) # the self is to send the home as a parameter to be used inside the other functions 
            
home()
