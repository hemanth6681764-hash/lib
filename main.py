# main.py

import tkinter as tk
from tkinter import messagebox
from books_data import add_book, find_book, delete_book, update_book, check_availability, get_all_books

root = tk.Tk()
root.title("Library Book Management")
root.geometry("1920x1000")

tk.Label(root, text="Library Book Management System", font=("Arial", 45)).pack(pady=80)

# --- Add Book ---
def open_add_book():
    win = tk.Toplevel()
    win.title("Add Book")

    tk.Label(win, text="Book ID").grid(row=0, column=0)
    tk.Label(win, text="Book Name").grid(row=1, column=0)
    tk.Label(win, text="Author").grid(row=2, column=0)

    id_entry = tk.Entry(win)
    name_entry = tk.Entry(win)
    author_entry = tk.Entry(win)

    id_entry.grid(row=0, column=1)
    name_entry.grid(row=1, column=1)
    author_entry.grid(row=2, column=1)

    def submit():
        add_book(id_entry.get(), name_entry.get(), author_entry.get())
        messagebox.showinfo("Success", "Book Added")
        win.destroy()

    tk.Button(win, text="Add", command=submit).grid(row=3, columnspan=2)

# --- Search Book ---
def open_search_book():
    win = tk.Toplevel()
    win.title("Search Book")

    tk.Label(win, text="Enter Book ID").pack()
    id_entry = tk.Entry(win)
    id_entry.pack()

    def search():
        book = find_book(id_entry.get())
        if book:
            messagebox.showinfo("Found", f"Name: {book['name']}\nAuthor: {book['author']}\nStatus: {book['status']}")
        else:
            messagebox.showerror("Not Found", "Book not found")

    tk.Button(win, text="Search", command=search).pack()

# --- Delete Book ---
def open_delete_book():
    win = tk.Toplevel()
    win.title("Delete Book")

    tk.Label(win, text="Enter Book ID").pack()
    id_entry = tk.Entry(win)
    id_entry.pack()

    def delete():
        if delete_book(id_entry.get()):
            messagebox.showinfo("Deleted", "Book Deleted")
        else:
            messagebox.showerror("Error", "Book Not Found")
        win.destroy()

    tk.Button(win, text="Delete", command=delete).pack()

# --- Update Book ---
def open_update_book():
    win = tk.Toplevel()
    win.title("Update Book")

    tk.Label(win, text="New Name").grid(row=0, column=0)
    tk.Label(win, text="Book ID").grid(row=1, column=0)
    tk.Label(win, text="New Author").grid(row=2, column=0)

    id_entry = tk.Entry(win)
    name_entry = tk.Entry(win)
    author_entry = tk.Entry(win)

    id_entry.grid(row=0, column=1)
    name_entry.grid(row=1, column=1)
    author_entry.grid(row=2, column=1)

    def update():
        if update_book(id_entry.get(), name_entry.get(), author_entry.get()):
            messagebox.showinfo("Success", "Book Updated")
        else:
            messagebox.showerror("Error", "Book Not Found")
        win.destroy()

    tk.Button(win, text="Update", command=update).grid(row=3, columnspan=2)

# --- Check Availability ---
def open_check_availability():
    win = tk.Toplevel()
    win.title("Check Availability")

    tk.Label(win, text="Enter Book ID").pack()
    id_entry = tk.Entry(win)
    id_entry.pack()

    def check():
        status = check_availability(id_entry.get())
        if status:
            messagebox.showinfo("Available", f"Status: {status}")
        else:
            messagebox.showerror("Error", "Book Not Found")

    tk.Button(win, text="Check", command=check).pack()

# --- View All Books ---
def open_view_books():
    win = tk.Toplevel()
    win.title("View All Books")

    books = get_all_books()
    if not books:
        tk.Label(win, text="No books available").pack()
        return

    for book in books:
        tk.Label(win, text=f"ID: {book['id']} | Name: {book['name']} | Author: {book['author']} | Status: {book['status']}").pack()

# --- Buttons on Main Window ---
button_style = {
    "width": 26,           # Width in characters
    "height": 1,           # Height in text lines
    "font": ("Arial", 25), # Font and size
    "bg": "#ffffff",       # Background color
    "relief": "raised"     # Button style (flat, raised, sunken, etc.)
}

tk.Button(root, text="1. Add New Book", command=open_add_book, **button_style).pack(pady=5)
tk.Button(root, text="2. Search Book", command=open_search_book, **button_style).pack(pady=5)
tk.Button(root, text="3. Delete Book", command=open_delete_book, **button_style).pack(pady=5)
tk.Button(root, text="4. Check Availability", command=open_check_availability, **button_style).pack(pady=5)
tk.Button(root, text="5. Update Book", command=open_update_book, **button_style).pack(pady=5)
tk.Button(root, text="6. View All Books", command=open_view_books, **button_style).pack(pady=5)


root.mainloop()
