import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to add car information to the MySQL database
def add_car_info():
    make = make_entry.get()
    model = model_entry.get()
    year = year_entry.get()

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="kiash1234",
            database="cars_tiknter"
        )

        cursor = connection.cursor()
        sql = "INSERT INTO cars (make, model, year) VALUES (%s, %s, %s)"
        values = (make, model, year)
        cursor.execute(sql, values)
        connection.commit()
        connection.close()
        messagebox.showinfo("Success", "Car information added to the database.")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error: {error}")

# Create a Tkinter window
window = tk.Tk()
window.title("Car Information App")

# Create and place labels and entry fields
make_label = tk.Label(window, text="Make:")
make_label.pack()
make_entry = tk.Entry(window)
make_entry.pack()

model_label = tk.Label(window, text="Model:")
model_label.pack()
model_entry = tk.Entry(window)
model_entry.pack()

year_label = tk.Label(window, text="Year:")
year_label.pack()
year_entry = tk.Entry(window)
year_entry.pack()

# Create and place the "Add Car" button
add_button = tk.Button(window, text="Add Car", command=add_car_info)
add_button.pack()

# Start the Tkinter main loop
window.mainloop()
