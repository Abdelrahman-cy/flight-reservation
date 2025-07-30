from tkinter import messagebox
class reserve_editing():
    def __init__(self,parent):
        self.parent = parent
    def change(self):
        from database import update
        from booking import bookingwndow
        i = self.parent.id_input.get() # to get the id 
        if i == '':
            messagebox.showerror("Warning","There is no ID to modify")
            return 1
        
        record = update(i)
        self.parent.withdraw() #used to withdraw the current window without destroying it giving us a chnace to access the elements and show up the new one 
        bookingwndow(self.parent.master,self.parent,record,i)
        

    def cancel_clicked(self):
        from database import delete
        from booking import bookingwndow
        from reservation_list import reservationwindow
        i = self.parent.id_input.get()
        if i == '':
            messagebox.showerror("Warning","There is no ID to Delete")
            return 1
        delete(i)   
        self.parent.withdraw()
        reservationwindow(self.parent.master,self.parent)
        
    def book_again(self):
        from booking import bookingwndow
        self.parent.withdraw() #used to withdraw the current window without destroying it giving us a chnace to access the elements and show up the new one 
        bookingwndow(self.parent.master,self.parent)
        
    def delete_table_content(self):
        from database import delete_all
        from reservation_list import reservationwindow
        delete_all()
        self.parent.withdraw()
        reservationwindow(self.parent.master, self.parent)
        