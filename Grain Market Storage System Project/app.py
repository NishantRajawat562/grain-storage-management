from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Create the database and tables if they don't exist
def create_tables():
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS storage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            warehouse_name TEXT NOT NULL,
            location TEXT NOT NULL,
            capacity INTEGER NOT NULL,
            available INTEGER NOT NULL
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS farmer_booking (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            farmer_name TEXT NOT NULL,
            contact_number TEXT NOT NULL,
            address TEXT NOT NULL,
            date_of_submission TEXT NOT NULL,
            storage_id INTEGER NOT NULL,
            storage_required INTEGER NOT NULL,
            FOREIGN KEY (storage_id) REFERENCES storage (id)
        )
    ''')

    conn.commit()
    conn.close()

create_tables()

@app.route('/')
def home():
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()
    c.execute('SELECT * FROM storage')
    storages = c.fetchall()
    conn.close()
    return render_template('home.html', storages=storages)

@app.route('/warehouse', methods=['GET', 'POST'])
def warehouse():
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()

    if request.method == 'POST':
        action = request.form['action']

        if action == 'add':
            warehouse_name = request.form['warehouse_name']
            location = request.form['location']
            capacity = int(request.form['capacity'])
            c.execute('INSERT INTO storage (warehouse_name, location, capacity, available) VALUES (?, ?, ?, ?)',
                      (warehouse_name, location, capacity, capacity))
            conn.commit()

        elif action == 'update':
            storage_id = int(request.form['storage_id'])
            warehouse_name = request.form['warehouse_name']
            location = request.form['location']
            capacity = int(request.form['capacity'])

            # Get previous available and capacity
            c.execute('SELECT capacity, available FROM storage WHERE id = ?', (storage_id,))
            old_capacity, old_available = c.fetchone()

            # Adjust available based on capacity change
            diff = capacity - old_capacity
            new_available = old_available + diff
            if new_available < 0:
                new_available = 0

            c.execute('UPDATE storage SET warehouse_name = ?, location = ?, capacity = ?, available = ? WHERE id = ?',
                      (warehouse_name, location, capacity, new_available, storage_id))
            conn.commit()

        elif action == 'delete':
            storage_id = int(request.form['storage_id'])
            c.execute('DELETE FROM storage WHERE id = ?', (storage_id,))
            conn.commit()

    c.execute('SELECT * FROM storage')
    storages = c.fetchall()

    c.execute('''
        SELECT farmer_booking.id, farmer_booking.farmer_name, farmer_booking.contact_number, farmer_booking.address,
               farmer_booking.date_of_submission, farmer_booking.storage_required, storage.warehouse_name
        FROM farmer_booking
        JOIN storage ON farmer_booking.storage_id = storage.id
    ''')
    bookings = c.fetchall()

    conn.close()
    return render_template('warehouse.html', storages=storages, bookings=bookings)

@app.route('/farmer', methods=['GET', 'POST'])
def farmer():
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()

    if request.method == 'POST':
        farmer_name = request.form['farmer_name']
        contact_number = request.form['contact_number']
        address = request.form['address']
        date_of_submission = request.form['date_of_submission']
        storage_id = int(request.form['storage_id'])
        storage_required = int(request.form['storage_required'])

        # Check if enough storage is available
        c.execute('SELECT available FROM storage WHERE id = ?', (storage_id,))
        available = c.fetchone()[0]

        if available >= storage_required:
            c.execute('INSERT INTO farmer_booking (farmer_name, contact_number, address, date_of_submission, storage_id, storage_required) VALUES (?, ?, ?, ?, ?, ?)',
                      (farmer_name, contact_number, address, date_of_submission, storage_id, storage_required))
            c.execute('UPDATE storage SET available = available - ? WHERE id = ?', (storage_required, storage_id))
            conn.commit()
        else:
            return "Not enough storage available!"

    c.execute('SELECT * FROM storage')
    storages = c.fetchall()
    conn.close()
    return render_template('farmer.html', storages=storages)

@app.route('/delete_booking/<int:booking_id>')
def delete_booking(booking_id):
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()

    # Get storage_id and storage_required
    c.execute('SELECT storage_id, storage_required FROM farmer_booking WHERE id = ?', (booking_id,))
    result = c.fetchone()
    if result:
        storage_id, storage_required = result
        # Delete the booking
        c.execute('DELETE FROM farmer_booking WHERE id = ?', (booking_id,))
        # Update storage
        c.execute('UPDATE storage SET available = available + ? WHERE id = ?', (storage_required, storage_id))
        conn.commit()

    conn.close()
    return redirect(url_for('warehouse'))

if __name__ == '__main__':
    app.run(debug=True)
