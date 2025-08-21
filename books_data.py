import csv
import os

filename = "hemanth_book_store.csv"

# Initialize CSV file with header if not exists
if not os.path.exists(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'name', 'author', 'status'])

def add_book(book_id, name, author):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([book_id, name, author, 'Available'])

def find_book(book_id):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == book_id:
                return row
    return None

def delete_book(book_id):
    found = False
    rows = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] != book_id:
                rows.append(row)
            else:
                found = True
    if found:
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'name', 'author', 'status'])
            writer.writeheader()
            writer.writerows(rows)
    return found

def update_book(book_id, new_name, new_author):
    found = False
    rows = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == book_id:
                row['name'] = new_name
                row['author'] = new_author
                found = True
            rows.append(row)
    if found:
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'name', 'author', 'status'])
            writer.writeheader()
            writer.writerows(rows)
    return found

def check_availability(book_id):
    book = find_book(book_id)
    return book['status'] if book else None

def get_all_books():
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)
