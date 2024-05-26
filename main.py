import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import date

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bajwa123",
    database="library_system"
)

cursor = db.cursor()

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.configure(bg="#2c3e50")
        self.root.geometry("800x600")

        # Add main buttons in the middle of the window
        self.create_main_buttons()

    def create_main_buttons(self):
        btn_books = tk.Button(self.root, text="Books", command=self.books_menu, bg="#2980b9", fg="#ecf0f1", width=15, height=2)
        btn_books.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        btn_members = tk.Button(self.root, text="Members", command=self.members_menu, bg="#27ae60", fg="#ecf0f1", width=15, height=2)
        btn_members.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        btn_borrowings = tk.Button(self.root, text="Borrowings", command=self.borrowings_menu, bg="#e67e22", fg="#ecf0f1", width=15, height=2)
        btn_borrowings.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        btn_publishers = tk.Button(self.root, text="Publishers", command=self.publishers_menu, bg="#8e44ad", fg="#ecf0f1", width=15, height=2)
        btn_publishers.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        btn_exit = tk.Button(self.root, text="Exit", command=self.root.quit, bg="#c0392b", fg="#ecf0f1", width=15, height=2)
        btn_exit.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    def books_menu(self):
        self.clear_screen()
        book_menu = tk.Menu(self.root)
        self.root.config(menu=book_menu)
        book_menu.add_command(label="Add Book", command=self.add_book)
        book_menu.add_command(label="View Books", command=self.view_books)
        book_menu.add_command(label="Delete Book", command=self.delete_book)
        book_menu.add_command(label="Update Book", command=self.update_book)
        book_menu.add_command(label="Back", command=self.create_main_buttons)

    def members_menu(self):
        self.clear_screen()
        member_menu = tk.Menu(self.root)
        self.root.config(menu=member_menu)
        member_menu.add_command(label="Add Member", command=self.add_member)
        member_menu.add_command(label="View Members", command=self.view_members)
        member_menu.add_command(label="Delete Member", command=self.delete_member)
        member_menu.add_command(label="Update Member", command=self.update_member)
        member_menu.add_command(label="Back", command=self.create_main_buttons)

    def borrowings_menu(self):
        self.clear_screen()
        borrow_menu = tk.Menu(self.root)
        self.root.config(menu=borrow_menu)
        borrow_menu.add_command(label="Borrow Book", command=self.borrow_book)
        borrow_menu.add_command(label="Return Book", command=self.return_book)
        borrow_menu.add_command(label="Back", command=self.create_main_buttons)

    def publishers_menu(self):
        self.clear_screen()
        publisher_menu = tk.Menu(self.root)
        self.root.config(menu=publisher_menu)
        publisher_menu.add_command(label="Add Publisher", command=self.add_publisher)
        publisher_menu.add_command(label="View Publishers", command=self.view_publishers)
        publisher_menu.add_command(label="Delete Publisher", command=self.delete_publisher)
        publisher_menu.add_command(label="Update Publisher", command=self.update_publisher)
        publisher_menu.add_command(label="Back", command=self.create_main_buttons)

    def add_publisher(self):
        self.clear_screen()
        tk.Label(self.root, text="Add Publisher").pack()
        tk.Label(self.root, text="Name").pack()
        name_entry = tk.Entry(self.root)
        name_entry.pack()
        tk.Label(self.root, text="Address").pack()
        address_entry = tk.Entry(self.root)
        address_entry.pack()
        tk.Button(self.root, text="Add", command=lambda: self.add_publisher_db(name_entry.get(), address_entry.get())).pack()

    def add_publisher_db(self, name, address):
        cursor.execute("INSERT INTO publisher (name, address) VALUES (%s, %s)", (name, address))
        db.commit()
        messagebox.showinfo("Success", "Publisher added successfully!")

    def view_publishers(self):
        self.clear_screen()
        cursor.execute("SELECT * FROM publisher")
        for (publisher_id, name, address) in cursor:
            tk.Label(self.root, text=f"ID: {publisher_id}, Name: {name}, Address: {address}").pack()

    def delete_publisher(self):
        self.clear_screen()
        tk.Label(self.root, text="Delete Publisher").pack()
        tk.Label(self.root, text="Publisher ID").pack()
        publisher_id_entry = tk.Entry(self.root)
        publisher_id_entry.pack()
        tk.Button(self.root, text="Delete", command=lambda: self.delete_publisher_db(publisher_id_entry.get())).pack()

    def delete_publisher_db(self, publisher_id):
        cursor.execute("DELETE FROM publisher WHERE publisher_id = %s", (publisher_id,))
        db.commit()
        messagebox.showinfo("Success", "Publisher deleted successfully!")

    def update_publisher(self):
        self.clear_screen()
        tk.Label(self.root, text="Update Publisher").pack()
        tk.Label(self.root, text="Publisher ID").pack()
        publisher_id_entry = tk.Entry(self.root)
        publisher_id_entry.pack()
        tk.Label(self.root, text="New Name").pack()
        name_entry = tk.Entry(self.root)
        name_entry.pack()
        tk.Label(self.root, text="New Address").pack()
        address_entry = tk.Entry(self.root)
        address_entry.pack()
        tk.Button(self.root, text="Update", command=lambda: self.update_publisher_db(publisher_id_entry.get(), name_entry.get(), address_entry.get())).pack()

    def update_publisher_db(self, publisher_id, name, address):
        cursor.execute("UPDATE publisher SET name = %s, address = %s WHERE publisher_id = %s", (name, address, publisher_id))
        db.commit()
        messagebox.showinfo("Success", "Publisher updated successfully!")

    def add_book(self):
        self.clear_screen()
        tk.Label(self.root, text="Add Book").pack()
        tk.Label(self.root, text="Title").pack()
        title_entry = tk.Entry(self.root)
        title_entry.pack()
        tk.Label(self.root, text="Author").pack()
        author_entry = tk.Entry(self.root)
        author_entry.pack()
        tk.Label(self.root, text="Copies").pack()
        copies_entry = tk.Entry(self.root)
        copies_entry.pack()
        tk.Button(self.root, text="Add", command=lambda: self.add_book_db(title_entry.get(), author_entry.get(), copies_entry.get())).pack()

    def add_book_db(self, title, author, copies):
        cursor.execute("INSERT INTO books (title, author, available_copies) VALUES (%s, %s, %s)", (title, author, copies))
        db.commit()
        messagebox.showinfo("Success", "Book added successfully!")

    def view_books(self):
        self.clear_screen()
        cursor.execute("SELECT * FROM books")
        for (book_id, title, author, available_copies) in cursor:
            tk.Label(self.root, text=f"ID: {book_id}, Title: {title}, Author: {author}, Available Copies: {available_copies}").pack()

    def delete_book(self):
        self.clear_screen()
        tk.Label(self.root, text="Delete Book").pack()
        tk.Label(self.root, text="Book ID").pack()
        book_id_entry = tk.Entry(self.root)
        book_id_entry.pack()
        tk.Button(self.root, text="Delete", command=lambda: self.delete_book_db(book_id_entry.get())).pack()

    def delete_book_db(self, book_id):
        cursor.execute("DELETE FROM books WHERE book_id = %s", (book_id,))
        db.commit()
        messagebox.showinfo("Success", "Book deleted successfully!")

    def update_book(self):
        self.clear_screen()
        tk.Label(self.root, text="Update Book").pack()
        tk.Label(self.root, text="Book ID").pack()
        book_id_entry = tk.Entry(self.root)
        book_id_entry.pack()
        tk.Label(self.root, text="New Title").pack()
        title_entry = tk.Entry(self.root)
        title_entry.pack()
        tk.Label(self.root, text="New Author").pack()
        author_entry = tk.Entry(self.root)
        author_entry.pack()
        tk.Label(self.root, text="New Copies").pack()
        copies_entry = tk.Entry(self.root)
        copies_entry.pack()
        tk.Button(self.root, text="Update", command=lambda: self.update_book_db(book_id_entry.get(), title_entry.get(), author_entry.get(), copies_entry.get())).pack()

    def update_book_db(self, book_id, title, author, copies):
        cursor.execute("UPDATE books SET title = %s, author = %s, available_copies = %s WHERE book_id = %s", (title, author, copies, book_id))
        db.commit()
        messagebox.showinfo("Success", "Book updated successfully!")

    def add_member(self):
        self.clear_screen()
        tk.Label(self.root, text="Add Member").pack()
        tk.Label(self.root, text="Name").pack()
        name_entry = tk.Entry(self.root)
        name_entry.pack()
        tk.Label(self.root, text="Email").pack()
        email_entry = tk.Entry(self.root)
        email_entry.pack()
        tk.Button(self.root, text="Add", command=lambda: self.add_member_db(name_entry.get(), email_entry.get())).pack()

    def add_member_db(self, name, email):
        cursor.execute("INSERT INTO members (name, email) VALUES (%s, %s)", (name, email))
        db.commit()
        messagebox.showinfo("Success", "Member added successfully!")

    def view_members(self):
        self.clear_screen()
        cursor.execute("SELECT * FROM members")
        for (member_id, name, email) in cursor:
            tk.Label(self.root, text=f"ID: {member_id}, Name: {name}, Email: {email}").pack()

    def delete_member(self):
        self.clear_screen()
        tk.Label(self.root, text="Delete Member").pack()
        tk.Label(self.root, text="Member ID").pack()
        member_id_entry = tk.Entry(self.root)
        member_id_entry.pack()
        tk.Button(self.root, text="Delete", command=lambda: self.delete_member_db(member_id_entry.get())).pack()

    def delete_member_db(self, member_id):
        cursor.execute("DELETE FROM members WHERE member_id = %s", (member_id,))
        db.commit()
        messagebox.showinfo("Success", "Member deleted successfully!")

    def update_member(self):
        self.clear_screen()
        tk.Label(self.root, text="Update Member").pack()
        tk.Label(self.root, text="Member ID").pack()
        member_id_entry = tk.Entry(self.root)
        member_id_entry.pack()
        tk.Label(self.root, text="New Name").pack()
        name_entry = tk.Entry(self.root)
        name_entry.pack()
        tk.Label(self.root, text="New Email").pack()
        email_entry = tk.Entry(self.root)
        email_entry.pack()
        tk.Button(self.root, text="Update", command=lambda: self.update_member_db(member_id_entry.get(), name_entry.get(), email_entry.get())).pack()

    def update_member_db(self, member_id, name, email):
        cursor.execute("UPDATE members SET name = %s, email = %s WHERE member_id = %s", (name, email, member_id))
        db.commit()
        messagebox.showinfo("Success", "Member updated successfully!")

    def borrow_book(self):
        self.clear_screen()
        tk.Label(self.root, text="Borrow Book").pack()
        tk.Label(self.root, text="Member ID").pack()
        member_id_entry = tk.Entry(self.root)
        member_id_entry.pack()
        tk.Label(self.root, text="Book ID").pack()
        book_id_entry = tk.Entry(self.root)
        book_id_entry.pack()
        tk.Button(self.root, text="Borrow", command=lambda: self.borrow_book_db(member_id_entry.get(), book_id_entry.get())).pack()

    def borrow_book_db(self, member_id, book_id):
        cursor.execute("SELECT available_copies FROM books WHERE book_id = %s", (book_id,))
        available_copies = cursor.fetchone()[0]
        if available_copies > 0:
            cursor.execute("INSERT INTO borrowings (book_id, member_id, borrow_date) VALUES (%s, %s, %s)",
                           (book_id, member_id, date.today()))
            cursor.execute("UPDATE books SET available_copies = available_copies - 1 WHERE book_id = %s", (book_id,))
            db.commit()
            messagebox.showinfo("Success", "Book borrowed successfully!")
        else:
            messagebox.showerror("Error", "No available copies of this book.")

    def return_book(self):
        self.clear_screen()
        tk.Label(self.root, text="Return Book").pack()
        tk.Label(self.root, text="Borrowing ID").pack()
        borrowing_id_entry = tk.Entry(self.root)
        borrowing_id_entry.pack()
        tk.Button(self.root, text="Return", command=lambda: self.return_book_db(borrowing_id_entry.get())).pack()

    def return_book_db(self, borrowing_id):
        cursor.execute("SELECT book_id FROM borrowings WHERE borrowing_id = %s", (borrowing_id,))
        book_id = cursor.fetchone()[0]
        cursor.execute("UPDATE books SET available_copies = available_copies + 1 WHERE book_id = %s", (book_id,))
        cursor.execute("UPDATE borrowings SET return_date = %s WHERE borrowing_id = %s", (date.today(), borrowing_id))
        db.commit()
        messagebox.showinfo("Success", "Book returned successfully!")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()

# Close the database connection
cursor.close()
db.close()
