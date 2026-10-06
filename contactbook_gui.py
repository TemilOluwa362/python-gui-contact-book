import tkinter as tk
contacts = {}
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x550")

def add_contact():
    name = name_entry.get().title()
    phone_number = phone_entry.get() 
    phone_number = "+234" + phone_number[1:]
    email = email_entry.get()
    contacts[name] = {"Phone": phone_number, "Email": email}
    name_entry.delete(0,tk.END)
    phone_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
def view_contact():
    output.delete("1.0", tk.END)
    if not contacts:
        output.insert(tk.END, "No contacts added!\n")
    else:
        for name, contact_info in contacts.items():
            output.insert(tk.END, name +"\n")
            output.insert(tk.END, contact_info["Phone"] + "\n") 
            output.insert(tk.END, contact_info["Email"] + "\n") 
def search_contact():
    contact_search = search_entry.get().title()
    output.delete("1.0", tk.END)
    if contact_search in contacts:
        output.insert(tk.END, contact_search +"\n")
        output.insert(tk.END, contacts[contact_search]["Phone"] +"\n")
        output.insert(tk.END, contacts[contact_search]["Email"] +"\n")
    else:
        output.insert(tk.END, "Contact not found!\n")
def delete_contact():
    contact_delete = search_entry.get().title()
    output.delete("1.0", tk.END)
    if contact_delete in contacts:
        del contacts[contact_delete]
        output.insert(tk.END, "Contact deleted!\n")
    else:
        output.insert(tk.END, "Contact not found!\n")

name_label = tk.Label(root, text="Contact name")
name_label.pack(anchor="w", padx=20)
name_entry = tk.Entry(root)
name_entry.pack(fill="x", padx=20, pady=5)
phone_label = tk.Label(root, text="Contact number")
phone_label.pack(anchor="w", padx=20)
phone_entry = tk.Entry(root)
phone_entry.pack(fill="x", padx=20, pady=5)
email_label = tk.Label(root, text="Contact email")
email_label.pack(anchor="w", padx=20)
email_entry = tk.Entry(root)
email_entry.pack(fill="x", padx=20, pady=5)
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack(fill="x", padx=20, pady=5)
view_button = tk.Button(root, text="View Contacts", command=view_contact)
view_button.pack(fill="x", padx=20, pady=5)
search_label = tk.Label(root, text="Search Contact By Name")
search_label.pack(anchor="w", padx=20)
search_entry =tk.Entry(root)
search_entry.pack(fill="x", padx=20, pady=5)
search_button = tk.Button(root, text="Search", command=search_contact)
search_button.pack(fill="x", padx=20, pady=5)
delete_button = tk.Button(root, text="Delete", command=delete_contact)
delete_button.pack(fill="x", padx=20, pady=5)
output= tk.Text(root, height=10, width=45)
output.pack(fill="both", expand=True, padx=20, pady=10)

root.mainloop()