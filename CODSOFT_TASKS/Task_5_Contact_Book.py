import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = []


        # Creating Labels for inserting in the contact book
        self.name_label = tk.Label(root, text="Name:")
        self.name_entry = tk.Entry(root)
        self.phone_label = tk.Label(root, text="Mobile:")
        self.phone_entry = tk.Entry(root)
        self.email_label = tk.Label(root, text="Email ID:")
        self.email_entry = tk.Entry(root)
        self.address_label = tk.Label(root, text="Address/Place:")
        self.address_entry = tk.Entry(root)


        # Adding Buttons to the GUI Interface
        self.add_button = tk.Button(root, text="Add New Contact", command=self.add_contact)
        self.view_button = tk.Button(root, text="View All Contacts", command=self.view_contacts)
        self.search_button = tk.Button(root, text="Search in Contact", command=self.search_contact)
        self.update_button = tk.Button(root, text="Update a Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete a Contact", command=self.delete_contact)
        
        
        # Performing placement of Grids
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.phone_label.grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        self.email_label.grid(row=2, column=0, padx=10, pady=5)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        self.address_label.grid(row=3, column=0, padx=10, pady=5)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=10)
        self.update_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=10)
    
    
    #Defining the Adding of Contatcts
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone:
            contact = {"Name": name, "Mobile": phone, "Email ID": email, "Address/Place": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Warning", "Please Enter the required fields.")
    
    
    #Defining the Viewing of the Contacts
    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts to display or show.")
            return
        contact_list = "\n".join([f"{contact['Name']}: {contact['Mobile']}" for contact in self.contacts])
        messagebox.showinfo("Contacts List", contact_list)
    
    
    #Defining the Search of the Contact
    def search_contact(self):
        search_query = simpledialog.askstring("Search", "Enter Person's name or mobile number:")
        if search_query:
            results = [contact for contact in self.contacts if
                       search_query.lower() in contact['Name'].lower() or search_query in contact['Phone']]
            if results:
                contact_list = "\n".join([f"{contact['Name']}: {contact['Mobile']}" for contact in results])
                messagebox.showinfo("Search Results", contact_list)
            else:
                messagebox.showinfo("Search Results", "No contacts by the search found.")
        else:
            messagebox.showwarning("Warning", "Please enter a search query.")
    
    
    #Defining Update and Delete Contact 
    def update_contact(self):
        pass
    def delete_contact(self):
        pass


#Main Area
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
