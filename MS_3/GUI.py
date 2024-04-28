#!/usr/bin/env python3
import tkinter as tk
from tkinter import PhotoImage
import mysql.connector


class Tooltip:
    def __init__(self, widget, text, view):
        self.widget = widget
        self.text = text
        self.view = view
        self.tooltip = None
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<Button-1>", self.show_view)

    def enter(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        label = tk.Label(self.tooltip, text=self.text, relief="solid", borderwidth=0.1)
        label.pack(ipadx=1)

    def leave(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

    def show_view(self, event=None):
        self.leave()
        self.view()


def show_welcome_view():
    menu_frame.grid_forget()  # Hide the menu view
    main_frame.grid_forget()
    register_frame.grid_forget()
    Welcome_view.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Show the main view


def show_main_view():
    menu_frame.grid_forget()  # Hide the menu view
    Welcome_view.grid_forget()
    register_frame.grid_forget()
    main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Show the main view


def show_loginERR():
    # Display confirmation message for the user
    err_label1 = tk.Label(root, text="Invalid Username or Email!!", fg="red")
    err_label2 = tk.Label(root, text="Try again or Register as a new user", fg="red")

    err_label1.grid(row=6, column=0)
    # Hide the confirmation label after 3000 milliseconds (3 seconds)
    root.after(3000, lambda: err_label1.grid_forget())
    err_label2.grid(row=7, column=0)
    # Hide the confirmation label after 3000 milliseconds (3 seconds)
    root.after(3000, lambda: err_label2.grid_forget())


def show_menu_view():
    main_frame.grid_forget()  # Hide the main view
    register_frame.grid_forget()
    create_fav_frame.grid_forget()
    channel_by_loc_frame.grid_forget()
    fav_frame.grid_forget()
    network_frame.grid_forget()
    rocket_frame.grid_forget()
    growing_sat_frame.grid_forget()
    channel_lang_frame.grid_forget()
    filter_channel_frame.grid_forget()
    menu_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Show the registration view


def register_user_view():
    menu_frame.grid_forget()  # Hide the main view
    register_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Show the registration view


def create_favorite_channels_list_view():
    menu_frame.grid_forget()  # Hide the main view
    create_fav_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Show the registration view


def show_channels_by_location_view():
    menu_frame.grid_forget()  # Hide the main view
    channel_by_loc_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Show the registration view


def show_favorite_list_coverage_view():
    menu_frame.grid_forget()  # Hide the main view
    fav_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Show the registration view
    try:
        mydb = mysql.connector.connect(
            host="******",
            user="*******",
            password="******",
            database="******",
            port=*****
        )
        email = entry_Email.get()

        # Create a cursor object
        cursor = mydb.cursor()
        # SQL query
        sql = f'''
                   SELECT
                   f.Channel_Name,
                   s.Satellite_Name, b.Freq_Num,
                   b.Freq_Polarisation,
                   COALESCE(e.Encryption_Type, 'Free') AS Encryption_Type
                   FROM Favourite f
                   INNER JOIN User u ON f.User_Email = u.Email
                   LEFT JOIN Satellite s ON u.Region LIKE CONCAT('%', s.Region, '%') OR s.Region LIKE CONCAT('%', u.Region, '%')
                   JOIN Broadcast b ON f.Channel_Name = b.Channel_Name
                   LEFT JOIN Encryption e ON b.Channel_Name = e.Channel_Name AND b.Satellite_Name = e.Satellite_Name
                   Where u.Email = '{email}'
              '''

        cursor.execute(sql)

        # Fetch all rows
        covarage = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        mydb.close()

        output = "Favourite Channels Covered based on your Location: \n Channel Name - Satellite Name - Frequency - Encryption"
        for info in covarage:
            output += format(info[0]) + ' - ' + format(info[1]) + ' - ' + format(info[2]) + ' ' + format(
                info[3]) + ' - ' + format(info[4]) + '\n'

        text_widget = tk.Text(fav_frame, height=60, width=90, wrap=tk.WORD, font=("Courier", 14))
        text_widget.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        # Add a scrollbar to the Text widget
        scrollbar = tk.Scrollbar(fav_frame, command=text_widget.yview, width=10, relief=tk.FLAT)
        scrollbar.grid(row=4, column=1, sticky='nsew')
        text_widget.config(yscrollcommand=scrollbar.set)

        # Insert the output text into the Text widget
        text_widget.insert(tk.END, output)

        # Display confirmation message for the user
        confirmation_label = tk.Label(root, text="Successful Run!", fg="green")
        confirmation_label.grid(row=6, column=0, padx=10, pady=5)
        # Hide the confirmation label after 3000 milliseconds (3 seconds)
        root.after(3000, lambda: confirmation_label.grid_forget())


    except mysql.connector.Error as err:
        # If there's an error during registration, display an error message
        print("Error during registration:", err)
        # Display confirmation message for the user
        confirmation_label = tk.Label(root, text="Error", fg="red")
        confirmation_label.grid(row=6, column=0, padx=10, pady=5)
        # Hide the confirmation label after 3000 milliseconds (3 seconds)
        root.after(3000, lambda: confirmation_label.grid_forget())


def show_top_networks_view():
    menu_frame.grid_forget()  # Hide the main view
    network_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Show the registration view
    try:
        mydb = mysql.connector.connect(
            host="******",
            user="*******",
            password="*******",
            database="*******",
            port=*****
        )

        # Create a cursor object
        cursor = mydb.cursor()
        # SQL query
        sql = '''
        select  c.network_name, count(distinct c.Channel_Name) as num_channels,
        count(b.Satellite_Name)/count(distinct b.Channel_Name) as avg_sat_per_channel
        FROM Channel c inner join Broadcast b
        ON c.Channel_Name = b.Channel_Name
        WHERE c.network_name IS NOT NULL
        GROUP BY c.network_name
        ORDER BY num_channels DESC
        LIMIT 5;

        '''

        cursor.execute(sql)

        # Fetch all rows
        Networks = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        mydb.close()

        output = "Top 5 TV Networks - AVG Satellites each Channel is on: \n"
        for network in Networks:
            output += format(network[0]) + ' - ' + format(network[2]) + '\n'

        text_widget = tk.Text(network_frame, height=20, width=60, wrap=tk.WORD, font=("Courier", 14))
        text_widget.grid(row=4, column=0, padx=10, pady=5, sticky="e")

        # Insert the output text into the Text widget
        text_widget.insert(tk.END, output)

        # Display confirmation message for the user
        confirmation_label = tk.Label(root, text="Successful Run!", fg="green")
        confirmation_label.grid(row=6, column=0, padx=10, pady=5)
        # Hide the confirmation label after 3000 milliseconds (3 seconds)
        root.after(3000, lambda: confirmation_label.grid_forget())


    except mysql.connector.Error as err:
        # If there's an error during registration, display an error message
        print("Error during registration:", err)
        # Display confirmation message for the user
        confirmation_label = tk.Label(root, text="Error", fg="red")
        confirmation_label.grid(row=6, column=0, padx=10, pady=5)
        # Hide the confirmation label after 3000 milliseconds (3 seconds)
        root.after(3000, lambda: confirmation_label.grid_forget())


def show_top_rockets_view():
    menu_frame.grid_forget()  # Hide the main view
    rocket_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Show the registration view
    try:
        mydb = mysql.connector.connect(
            host="******",
            user="*******",
            password="*******",
            database="*******",
            port=*****
        )
        # Create a cursor object
        cursor = mydb.cursor()
        # SQL query to retrieve channels based on satellite coverage
        sql = """
                SELECT Launching_Rocket, COUNT(Satellite_Name) AS satellite_count
                FROM Satellite
                GROUP BY Launching_Rocket
                ORDER BY satellite_count DESC
                LIMIT 5
                """

        cursor.execute(sql)

        # Fetch all rows
        rockets = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        mydb.close()

        output = "Top 5 Rockets: \n"
        for rocket in rockets:
            output += format(rocket[0]) + "\n"

        text_widget = tk.Text(rocket_frame, height=10, width=20, wrap=tk.WORD, font=("Courier", 14))
        text_widget.grid(row=4, column=0, padx=10, pady=5, sticky="e")

        # Insert the output text into the Text widget
        text_widget.insert(tk.END, output)

        # Display confirmation message for the user
        confirmation_label = tk.Label(root, text="Successful Run!", fg="green")
        confirmation_label.grid(row=6, column=0, padx=10, pady=5)
        # Hide the confirmation label after 3000 milliseconds (3 seconds)
        root.after(3000, lambda: confirmation_label.grid_forget())


    except mysql.connector.Error as err:
        # If there's an error during registration, display an error message
        print("Error during registration:", err)
        # Display confirmation message for the user
        confirmation_label = tk.Label(root, text="Error", fg="red")
        confirmation_label.grid(row=6, column=0, padx=10, pady=5)
        # Hide the confirmation label after 3000 milliseconds (3 seconds)
        root.after(3000, lambda: confirmation_label.grid_forget())


def show_top_growing_satellites_view():
    menu_frame.grid_forget()  # Hide the main view
    growing_sat_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Show the registration view
    try:
        mydb = mysql.connector.connect(
            host="******",
            user="*******",
            password="*******",
            database="*******",
            port=*****
        )

        selected_language = selected_language_var.get()
        # Create a cursor object
        cursor = mydb.cursor()
        # SQL query
        sql = '''
            SELECT s.Satellite_Name, count(b.Channel_Name)/DATEDIFF(CURDATE(),s.Launch_Date) as growth_rate
            from Broadcast b inner join Satellite s 
            on b.Satellite_Name = s.Satellite_Name
            group by s.Satellite_Name
            order by growth_rate DESC
            LIMIT 5;
           '''

        cursor.execute(sql)

        # Fetch all rows
        sats = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        mydb.close()

        output = "Top 5 growing Satellites: \n"
        for sat in sats:
            output += format(sat[0]) + '\n'

        text_widget = tk.Text(growing_sat_frame, height=20, width=30, wrap=tk.WORD, font=("Courier", 14))
        text_widget.grid(row=4, column=0, padx=10, pady=5, sticky="e")

        # Insert the output text into the Text widget
        text_widget.insert(tk.END, output)

        # Display confirmation message for the user
        confirmation_label = tk.Label(root, text="Successful Run!", fg="green")
        confirmation_label.grid(row=6, column=0, padx=10, pady=5)
        # Hide the confirmation label after 3000 milliseconds (3 seconds)
        root.after(3000, lambda: confirmation_label.grid_forget())


    except mysql.connector.Error as err:
        # If there's an error during registration, display an error message
        print("Error during registration:", err)
        # Display confirmation message for the user
        confirmation_label = tk.Label(root, text="Error", fg="red")
        confirmation_label.grid(row=6, column=0, padx=10, pady=5)
        # Hide the confirmation label after 3000 milliseconds (3 seconds)
        root.after(3000, lambda: confirmation_label.grid_forget())


def show_top_channels_by_language_view():
    menu_frame.grid_forget()  # Hide the main view
    channel_lang_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Show the registration view


def get_channels_by_lang():
    try:
        mydb = mysql.connector.connect(
            host="******",
            user="*******",
            password="*******",
            database="*******",
            port=*****
        )

        selected_language = selected_language_var.get()
        lang_code = selected_language.split(':')[0]
        lang_full = selected_language.split(':')[1]

        # Create a cursor object
        cursor = mydb.cursor()
        # SQL query
        sql = f"""
            SELECT Channel_Name, COUNT(Satellite_Name) as sat
            FROM Language 
            where Language = '{lang_code}'
            GROUP BY Channel_Name
            ORDER BY  sat desc
            limit 5; 
              """

        cursor.execute(sql)

        # Fetch all rows
        channels = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        mydb.close()

        output = f"Top 5 Channels For {lang_full}: \n"
        for channel in channels:
            output += format(channel[0]) + '\n'

        text_widget = tk.Text(channel_lang_frame, height=20, width=30, wrap=tk.WORD, font=("Courier", 14))
        text_widget.grid(row=4, column=0, padx=10, pady=5, sticky="e")

        # Insert the output text into the Text widget
        text_widget.insert(tk.END, output)

        # Display confirmation message for the user
        confirmation_label = tk.Label(root, text="Successful Run!", fg="green")
        confirmation_label.grid(row=6, column=0, padx=10, pady=5)
        # Hide the confirmation label after 3000 milliseconds (3 seconds)
        root.after(3000, lambda: confirmation_label.grid_forget())


    except mysql.connector.Error as err:
        # If there's an error during registration, display an error message
        print("Error during registration:", err)
        # Display confirmation message for the user
        confirmation_label = tk.Label(root, text="Error", fg="red")
        confirmation_label.grid(row=6, column=0, padx=10, pady=5)
        # Hide the confirmation label after 3000 milliseconds (3 seconds)
        root.after(3000, lambda: confirmation_label.grid_forget())


def show_filtered_channel_list_view():
    menu_frame.grid_forget()  # Hide the main view
    filter_channel_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Show the registration view


def get_filtered_list():
    try:
        mydb = mysql.connector.connect(
            host="******",
            user="*******",
            password="*******",
            database="*******",
            port=*****
        )

        region = region_var.get()
        satellite = satellite_var.get()
        defin = def_var.get()
        language = language_var.get()
        lang_code = language.split(':')[0]

        # Create a cursor object
        cursor = mydb.cursor()

        # Start building the SQL query
        sql = """
            SELECT b.Channel_Name
            FROM Broadcast b 
            INNER JOIN Satellite s ON s.Satellite_Name = b.Satellite_Name
            LEFT JOIN Language l ON l.Channel_Name = b.Channel_Name AND l.Satellite_Name = b.Satellite_Name
            WHERE 1=1
        """

        # Initialize parameters list
        params = []

        # Conditionally add the filters
        if region:
            sql += " AND s.Region = %s"
            params.append(region)

        if satellite:
            sql += " AND s.Satellite_Name = %s"
            params.append(satellite)

        if defin:
            sql += " AND b.Video_Definition = %s"
            params.append(defin)

        if lang_code:
            sql += " AND l.Language = %s"
            params.append(lang_code)

        # Add LIMIT clause
        sql += " LIMIT 2000;"

        # Execute the query with parameters
        cursor.execute(sql, params)

        # Fetch all rows
        channels = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        mydb.close()
        print(channels)

        output = f"Filtered Channel list: \n"
        for channel in channels:
            output += format(channel[0]) + '\n'

        text_widget = tk.Text(filter_channel_frame, height=20, width=30, wrap=tk.WORD, font=("Courier", 14))
        text_widget.grid(row=4, column=0, padx=10, pady=5, sticky="e")

        # Add a scrollbar to the Text widget
        scrollbar = tk.Scrollbar(filter_channel_frame, command=text_widget.yview, width=10, relief=tk.FLAT)
        scrollbar.grid(row=5, column=3, sticky='nsew')
        text_widget.config(yscrollcommand=scrollbar.set)

        # Insert the output text into the Text widget
        text_widget.insert(tk.END, output)

        # Display confirmation message for the user
        confirmation_label = tk.Label(root, text="Successful Run!", fg="green")
        confirmation_label.grid(row=6, column=0, padx=10, pady=5)
        # Hide the confirmation label after 3000 milliseconds (3 seconds)
        root.after(3000, lambda: confirmation_label.grid_forget())


    except mysql.connector.Error as err:
        # If there's an error during registration, display an error message
        print("Error during registration:", err)
        # Display confirmation message for the user
        confirmation_label = tk.Label(root, text="Error", fg="red")
        confirmation_label.grid(row=6, column=0, padx=10, pady=5)
        # Hide the confirmation label after 3000 milliseconds (3 seconds)
        root.after(3000, lambda: confirmation_label.grid_forget())


def validate_user():
    mydb = mysql.connector.connect(
            host="******",
            user="*******",
            password="*******",
            database="*******",
            port=*****
    )

    username = entry_username.get()  # Get the username from the entry field
    email = entry_Email.get()
    mycursor = mydb.cursor()

    # Execute a query to check if the username exists
    mycursor.execute("SELECT * FROM User WHERE username = %s AND Email = %s", (username, email))
    user = mycursor.fetchone()

    if user:
        # If the username exists, show the registration view
        show_menu_view()
    else:
        # If the username does not exist, display a message
        show_loginERR()
    mycursor.close()
    mydb.close()


def confirm_reg(confirmation_label=None):
    try:
        mydb = mysql.connector.connect(
            host="******",
            user="*******",
            password="*******",
            database="*******",
            port=*****
        )

        email = entry_email.get()
        username = entry_usernam.get()
        gender = entry_gender.get()
        birthdate = entry_bd.get()
        region = entry_region.get()
        location = entry_loc.get()

        cursor = mydb.cursor()

        # SQL query to insert user data into the database
        sql = "INSERT INTO User (email, username, gender, birthdate, region, location) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (email, username, gender, birthdate, region, location)
        cursor.execute(sql, values)

        # Commit changes to the database
        mydb.commit()
        cursor.close()
        mydb.close()
        entry_email.delete(0, tk.END)
        entry_usernam.delete(0, tk.END)
        entry_gender.delete(0, tk.END)
        entry_bd.delete(0, tk.END)
        entry_region.delete(0, tk.END)
        entry_loc.delete(0, tk.END)

        # Display confirmation message for the user
        confirmation_label = tk.Label(root, text="Registration confirmed!", fg="green")
        confirmation_label.grid(row=6, column=0, padx=10, pady=5)
        # Hide the confirmation label after 3000 milliseconds (3 seconds)
        root.after(3000, lambda: confirmation_label.grid_forget())

        # Call a different view
        show_main_view()  # Change this to the desired view function
    except mysql.connector.Error as err:
        # If there's an error during registration, display an error message
        print("Error during registration:", err)
        # Display confirmation message for the user
        confirmation_label = tk.Label(root, text="Registration denied!", fg="red")
        confirmation_label.grid(row=6, column=0, padx=10, pady=5)
        # Hide the confirmation label after 3000 milliseconds (3 seconds)
        root.after(3000, lambda: confirmation_label.grid_forget())


def create_favorite_list():
    try:
        mydb = mysql.connector.connect(
            host="******",
            user="*******",
            password="*******",
            database="*******",
            port=*****
        )

        cursor = mydb.cursor()

        user_email = entry_usmail.get()
        channel_name = entry_channel.get()

        # SQL query to insert the user's favorite channel into the Favorites table
        sql = "INSERT INTO Favourite (user_email, channel_name) VALUES (%s, %s)"
        values = (user_email, channel_name)
        cursor.execute(sql, values)

        # Commit the transaction
        mydb.commit()

        # Close the cursor and database connection
        cursor.close()
        mydb.close()

        entry_channel.delete(0, tk.END)

        # Display confirmation message for the user
        confirmation_label = tk.Label(root, text="Channel Added Successfully!", fg="green")
        confirmation_label.grid(row=6, column=0, padx=10, pady=5)
        # Hide the confirmation label after 3000 milliseconds (3 seconds)
        root.after(3000, lambda: confirmation_label.grid_forget())


    except mysql.connector.Error as err:
        # If there's an error during registration, display an error message
        print("Error during registration:", err)
        # Display confirmation message for the user
        confirmation_label = tk.Label(root, text="Channel Not Added!", fg="red")
        confirmation_label.grid(row=6, column=0, padx=10, pady=5)
        # Hide the confirmation label after 3000 milliseconds (3 seconds)
        root.after(3000, lambda: confirmation_label.grid_forget())


def get_channels_by_location():
    try:
        mydb = mysql.connector.connect(
            host="******",
            user="*******",
            password="*******",
            database="*******",
            port=*****
        )

        longitude = entry_long.get()

        # Create a cursor object
        cursor = mydb.cursor()

        # Convert longitude to numeric type
        min_longitude = "CAST({} AS DECIMAL) - 10".format(longitude)
        max_longitude = "CAST({} AS DECIMAL) + 10".format(longitude)

        # SQL query to retrieve channels based on satellite coverage
        sql = """
                SELECT Channel_Name
                FROM Broadcast b
                INNER JOIN Satellite s ON b.Satellite_Name = s.Satellite_Name
                WHERE CAST(s.Satellite_Position_Longitude AS DECIMAL) BETWEEN {} AND {}
                limit 2000
                """.format(min_longitude, max_longitude)

        cursor.execute(sql)

        # Fetch all rows
        channels = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        mydb.close()

        output = "Channels viewable from longitude {}: \n".format(longitude)
        for channel in channels:
            output += format(channel[0])

        label_outc = tk.Label(channel_by_loc_frame, text="Channels:")
        label_outc.grid(row=3, column=0, padx=10, pady=5, sticky="e")

        # Create a Text widget to display the channels with a scrollbar
        text_widget = tk.Text(channel_by_loc_frame, height=60, width=30, wrap=tk.WORD, font=("Courier", 14))
        text_widget.grid(row=4, column=0, padx=10, pady=5, sticky="e")

        # Add a scrollbar to the Text widget
        scrollbar = tk.Scrollbar(channel_by_loc_frame, command=text_widget.yview, width=10, relief=tk.FLAT)
        scrollbar.grid(row=4, column=1, sticky='nsew')
        text_widget.config(yscrollcommand=scrollbar.set)

        # Insert the output text into the Text widget
        text_widget.insert(tk.END, output)

        # Display confirmation message for the user
        confirmation_label = tk.Label(root, text="Successful Run!", fg="green")
        confirmation_label.grid(row=6, column=0, padx=10, pady=5)
        # Hide the confirmation label after 3000 milliseconds (3 seconds)
        root.after(3000, lambda: confirmation_label.grid_forget())


    except mysql.connector.Error as err:
        # If there's an error during registration, display an error message
        print("Error during registration:", err)
        # Display confirmation message for the user
        confirmation_label = tk.Label(root, text="Error", fg="red")
        confirmation_label.grid(row=6, column=0, padx=10, pady=5)
        # Hide the confirmation label after 3000 milliseconds (3 seconds)
        root.after(3000, lambda: confirmation_label.grid_forget())


# Create main window
root = tk.Tk()
root.title("TV Channels Application")

background_label = tk.Label(root)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

Welcome_view = tk.Frame(root, bg=root["bg"])
Welcome_view.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
welcome_label = tk.Label(Welcome_view, text="Welcome to TV Channels Application", bg=root["bg"], font=("courier", 18))
welcome_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

# Satellite image
TV_image = PhotoImage(file="/Users/faridabey/Documents/Database/project_satellite_tv/tv.png")
TV_label = tk.Label(Welcome_view, image=TV_image, bg=root["bg"])
TV_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

button_register = tk.Button(Welcome_view, text="Continue", command=show_main_view)
button_register.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="we")

# Main view frame
main_frame = tk.Frame(root, bg=root["bg"])

# Welcome message
welcome_label = tk.Label(main_frame, text="Welcome to TV Channels Application", bg=root["bg"], font=("courier", 18))
welcome_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

# Satellite image
satellite_image = PhotoImage(file="/Users/faridabey/Documents/Database/project_satellite_tv/sat.png")
satellite_label = tk.Label(main_frame, image=satellite_image, bg=root["bg"])
satellite_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Add labels and buttons to the main view
label_username = tk.Label(main_frame, text="Username:", bg=root["bg"])
label_username.grid(row=2, column=0, padx=10, pady=5, sticky="e")

label_password = tk.Label(main_frame, text="Email:", bg=root["bg"])
label_password.grid(row=3, column=0, padx=10, pady=5, sticky="e")

entry_username = tk.Entry(main_frame)
entry_username.grid(row=2, column=1, padx=10, pady=5, sticky="w")

entry_Email = tk.Entry(main_frame)
entry_Email.grid(row=3, column=1, padx=10, pady=5, sticky="w")

button_login = tk.Button(main_frame, text="Login", command=validate_user)
button_login.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="we")

button_register = tk.Button(main_frame, text="New User", command=register_user_view)
button_register.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="we")

# menu view frame
menu_frame = tk.Frame(root, bg=root["bg"])
button_register_user = tk.Button(menu_frame, text="Register a User")
button_register_user.grid(row=0, column=0, padx=10, pady=5)
Tooltip(button_register_user, "Register a user", register_user_view)

button_create_favorite_channels_list = tk.Button(menu_frame, text="Create Favorites List")
button_create_favorite_channels_list.grid(row=1, column=0, padx=10, pady=5)
Tooltip(button_create_favorite_channels_list, "Create a new list of favorite channels",
        create_favorite_channels_list_view)

button_show_channels_by_location = tk.Button(menu_frame, text="View Channels by Location")
button_show_channels_by_location.grid(row=2, column=0, padx=10, pady=5)
Tooltip(button_show_channels_by_location, "Show channels viewable from a certain location",
        show_channels_by_location_view)

button_show_favorite_list_coverage = tk.Button(menu_frame, text="View Favorite List Coverage")
button_show_favorite_list_coverage.grid(row=3, column=0, padx=10, pady=5)
Tooltip(button_show_favorite_list_coverage,
        "Show coverage of favorite list based on your location, along with their details",
        show_favorite_list_coverage_view)

button_show_top_networks = tk.Button(menu_frame, text="Top TV Networks")
button_show_top_networks.grid(row=1, column=1, padx=10, pady=5)
Tooltip(button_show_top_networks, "Show top 5 TV Networks by number of channels", show_top_networks_view)

button_show_top_rockets = tk.Button(menu_frame, text="Top Rockets")
button_show_top_rockets.grid(row=0, column=1, padx=10, pady=5)
Tooltip(button_show_top_rockets, "Show top 5 rockets in terms of satellites they put in orbit",
        show_top_rockets_view)

button_show_top_growing_satellites = tk.Button(menu_frame, text="Top Growing Satellites")
button_show_top_growing_satellites.grid(row=2, column=1, padx=10, pady=5)
Tooltip(button_show_top_growing_satellites, "Show top 5 growing satellites", show_top_growing_satellites_view)

button_show_top_channels_by_language = tk.Button(menu_frame, text="Top Channels by language")
button_show_top_channels_by_language.grid(row=3, column=1, padx=10, pady=5)
Tooltip(button_show_top_channels_by_language, "Show top 5 channels for your choice of language",
        show_top_channels_by_language_view)

button_show_filtered_channel_list = tk.Button(menu_frame, text="Display Channels Filtered by Category")
button_show_filtered_channel_list.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
Tooltip(button_show_filtered_channel_list,
        "Show list of channels filtered by region, sattelite, video definition, and language",
        show_filtered_channel_list_view)
# Add a back button to return to the main view
button_back = tk.Button(menu_frame, text="Back")
button_back.grid(row=10, column=1, columnspan=1, sticky="n")
Tooltip(button_back, "Go Back to Main Menu", show_main_view)

# register new user frame
register_frame = tk.Frame(root, bg=root["bg"])

label_email = tk.Label(register_frame, text="Email:")
label_email.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_email = tk.Entry(register_frame)
entry_email.grid(row=1, column=1, padx=10, pady=5, sticky="w")

label_usernam = tk.Label(register_frame, text="Username:")
label_usernam.grid(row=2, column=0, padx=10, pady=5, sticky="e")

entry_usernam = tk.Entry(register_frame)
entry_usernam.grid(row=2, column=1, padx=10, pady=5, sticky="w")

label_gender = tk.Label(register_frame, text="Gender:")
label_gender.grid(row=3, column=0, padx=10, pady=5, sticky="e")

entry_gender = tk.Entry(register_frame)
entry_gender.grid(row=3, column=1, padx=10, pady=5, sticky="w")

label_bd = tk.Label(register_frame, text="Birthdate:")
label_bd.grid(row=4, column=0, padx=10, pady=5, sticky="e")

entry_bd = tk.Entry(register_frame)
entry_bd.grid(row=4, column=1, padx=10, pady=5, sticky="w")

label_region = tk.Label(register_frame, text="Region:")
label_region.grid(row=5, column=0, padx=10, pady=5, sticky="e")

entry_region = tk.Entry(register_frame)
entry_region.grid(row=5, column=1, padx=10, pady=5, sticky="w")

label_location = tk.Label(register_frame, text="Location:")
label_location.grid(row=6, column=0, padx=10, pady=5, sticky="e")

entry_loc = tk.Entry(register_frame)
entry_loc.grid(row=6, column=1, padx=10, pady=5, sticky="w")

# Add a back button to return to the menu
button_back = tk.Button(register_frame, text="Back")
button_back.grid(row=10, column=1, columnspan=1, sticky="we")
Tooltip(button_back, "Back to WELCOME ", show_welcome_view)

button_confirm = tk.Button(register_frame, text="Confirm", command=confirm_reg)
button_confirm.grid(row=10, column=2, columnspan=1, padx=10, pady=5, sticky="we")

# create fav frame
create_fav_frame = tk.Frame(root, bg=root["bg"])

label_user_email = tk.Label(create_fav_frame, text="Your email:")
label_user_email.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_usmail = tk.Entry(create_fav_frame)
entry_usmail.grid(row=1, column=1, padx=10, pady=5, sticky="w")

label_chan = tk.Label(create_fav_frame, text="channel name:")
label_chan.grid(row=2, column=0, padx=10, pady=5, sticky="e")

entry_channel = tk.Entry(create_fav_frame)
entry_channel.grid(row=2, column=1, padx=10, pady=5, sticky="w")

button_confirm = tk.Button(create_fav_frame, text="Confirm", command=create_favorite_list)
button_confirm.grid(row=10, column=2, columnspan=1, padx=10, pady=5, sticky="we")

# Add a back button to return to the menu
button_back = tk.Button(create_fav_frame, text="Back")
button_back.grid(row=10, column=3, columnspan=1, sticky="we")
Tooltip(button_back, "Go Back to Menu", show_menu_view)

# channel by location frame
channel_by_loc_frame = tk.Frame(root, bg=root["bg"])

label_long = tk.Label(channel_by_loc_frame, text="Longitudinal position:")
label_long.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_long = tk.Entry(channel_by_loc_frame)
entry_long.grid(row=1, column=1, padx=10, pady=5, sticky="w")
button_confirm = tk.Button(channel_by_loc_frame, text="Confirm", command=get_channels_by_location)
button_confirm.grid(row=10, column=2, columnspan=1, sticky="we")

# Add a back button to return to the menu
button_back = tk.Button(channel_by_loc_frame, text="Back")
button_back.grid(row=10, column=1, columnspan=1, sticky="we")
Tooltip(button_back, "Go Back to Menu", show_menu_view)

# favlist viewability
fav_frame = tk.Frame(root, bg=root["bg"])
# Add a back button to return to the menu
button_back = tk.Button(fav_frame, text="Back")
button_back.grid(row=10, column=1, columnspan=1, sticky="n")
Tooltip(button_back, "Go Back to Menu", show_menu_view)

network_frame = tk.Frame(root, bg=root["bg"])
# Add a back button to return to the menu
button_back = tk.Button(network_frame, text="Back")
button_back.grid(row=10, column=1, columnspan=1, sticky="n")
Tooltip(button_back, "Go Back to Menu", show_menu_view)

rocket_frame = tk.Frame(root, bg=root["bg"])
# Add a back button to return to the menu
button_back = tk.Button(rocket_frame, text="Back")
button_back.grid(row=10, column=1, columnspan=1, sticky="n")
Tooltip(button_back, "Go Back to Menu", show_menu_view)

growing_sat_frame = tk.Frame(root, bg=root["bg"])
# Add a back button to return to the menu
button_back = tk.Button(growing_sat_frame, text="Back")
button_back.grid(row=10, column=1, columnspan=1, sticky="n")
Tooltip(button_back, "Go Back to Menu", show_menu_view)

channel_lang_frame = tk.Frame(root, bg=root["bg"])

# Label for dropdown
label_lang = tk.Label(channel_lang_frame, text="Choose a language:")
label_lang.grid(row=1, column=0, padx=10, pady=5, sticky="e")

# Dropdown menu options
languages = [
    'Afr: Afrikaans', 'Alb: Albanian', 'Amh: Amharic', 'Ara: Arabic', 'Arm: Armenian', 'Asm: Assamese',
    'Aze: Azerbaijani',
    'Baq: Basque', 'Bel: Belarusian', 'Bem: Bemba', 'Ben: Bengali', 'Ber: Berber', 'Bho: Bhojpuri', 'Bos: Bosnian',
    'Bul: Bulgarian',
    'Bur: Burmese', 'Cat: Catalan', 'Chi: Chinese', 'Cze: Czech', 'Dan: Danish', 'Div: Dhivehi (Maldivian)',
    'Dut: Dutch', 'Eng: English',
    'Est: Estonian', 'Ewe: Ewe', 'Fin: Finnish', 'Fre: French', 'Geo: Georgian', 'Ger: German', 'Gla: Scottish Gaelic',
    'Gle: Irish',
    'Glg: Galician', 'Gre: Greek', 'Guj: Gujarati', 'Hau: Hausa', 'Heb: Hebrew', 'Hin: Hindi', 'Hok: Hmong',
    'Hrv: Croatian',
    'Hun: Hungarian', 'Ibo: Igbo', 'Ice: Icelandic', 'Ind: Indonesian', 'Ita: Italian', 'Jpn: Japanese', 'Kan: Kannada',
    'Kaz: Kazakh',
    'Khm: Khmer', 'Kho: Khasi', 'Kin: Kinyarwanda', 'Kir: Kyrgyz', 'Kor: Korean', 'Kur: Kurdish', 'Lah: Lahnda',
    'Lao: Lao', 'Lav: Latvian',
    'Lin: Lingala', 'Lit: Lithuanian', 'Ltz: Luxembourgish', 'Mac: Macedonian', 'Mal: Malayalam', 'Mar: Marathi',
    'May: Malay', 'Mlg: Malagasy',
    'Mlt: Maltese', 'Mon: Mongolian', 'Nep: Nepali', 'Nor: Norwegian', 'Nya: Chichewa (Nyanja)', 'Ori: Odia (Oriya)',
    'Orm: Oromo', 'Pan: Punjabi',
    'Per: Persian', 'Pol: Polish', 'Por: Portuguese', 'Prs: Dari (Persian)', 'Pus: Pashto',
    'Qaa: Reserved for local use', 'Rum: Romanian',
    'Run: Rundi (Kirundi)', 'Rus: Russian', 'Sin: Sinhala', 'Slo: Slovak', 'Slv: Slovenian', 'Sna: Shona',
    'Som: Somali', 'Spa: Spanish',
    'Srp: Serbian', 'Swa: Swahili', 'Swe: Swedish', 'Syr: Syriac', 'Tam: Tamil', 'Tel: Telugu', 'Tet: Tetum',
    'Tgk: Tajik', 'Tgl: Tagalog',
    'Tha: Thai', 'Tib: Tibetan', 'Tir: Tigrinya', 'Tuk: Turkmen', 'Tur: Turkish', 'Twi: Twi', 'Uig: Uyghur',
    'Ukr: Ukrainian', 'Urd: Urdu',
    'Uzb: Uzbek', 'Vie: Vietnamese', 'Wel: Welsh', 'Xho: Xhosa', 'Yor: Yoruba', 'Yue: Cantonese', 'Zul: Zulu',
    'Zza: Zaza'
]
selected_language_var = tk.StringVar(root)

# Dropdown menu
dropdown_lang = tk.OptionMenu(channel_lang_frame, selected_language_var, *languages)
dropdown_lang.grid(row=1, column=1, padx=10, pady=5, sticky="w")

button_confirm = tk.Button(channel_lang_frame, text="Confirm", command=get_channels_by_lang)
button_confirm.grid(row=10, column=2, columnspan=1, sticky="we")
# Add a back button to return to the menu
button_back = tk.Button(channel_lang_frame, text="Back")
button_back.grid(row=10, column=1, columnspan=1, sticky="we")
Tooltip(button_back, "Go Back to Menu", show_menu_view)

filter_channel_frame = tk.Frame(root, bg=root["bg"])

# Create dropdown menus for region, satellite name (HD or SD), and language
region_options = [' Asia & Pacific', ' Atlantic', ' Europe & Africa & Middle East', ' North & South America']
def_options = ["HD", "SD"]
satellite_options = [
    'ABS 2', 'ABS 2A', 'ABS 3A', 'ABS 4', 'ABS 6', 'ABS 7 (drifting west)', 'AMC 14', 'AMC 15', 'AMC 21', 'AMC 3',
    'AMC 6',
    'Al Yah 1', 'Al Yah 2', 'Al Yah 3', 'Alcomsat 1', 'Amazonas 2', 'Amazonas 3', 'Amazonas 5', 'Amazonas Nexus',
    'Amos 17',
    'Amos 3', 'Amos 4', 'Amos 7', 'Angosat 2', 'Anik F1', 'Anik F1R', 'Anik F2', 'Anik F3', 'Anik F4', 'Anik G1',
    'Apstar 6C',
    'Apstar 6D', 'Apstar 7', 'Apstar 9', 'Arabsat 5A', 'Arabsat 5C', 'Arabsat 6A', 'Arsat 1', 'Arsat 2', 'AsiaSat 4',
    'AsiaSat 5',
    'AsiaSat 6 (Thaicom 7)', 'AsiaSat 7', 'AsiaSat 9', 'Astra 1KR', 'Astra 1L', 'Astra 1M', 'Astra 1N', 'Astra 2A',
    'Astra 2C',
    'Astra 2E', 'Astra 2F', 'Astra 2G', 'Astra 3B', 'Astra 3C', 'Astra 4A', 'Azerspace 1', 'Azerspace 2 (Intelsat 38)',
    'BRIsat',
    'BSAT 3A', 'BSAT 3B', 'BSAT 3C (JCSAT 110R)', 'BSAT 4A', 'BSAT 4B', 'Badr 4', 'Badr 5', 'Badr 6', 'Badr 7',
    'Badr 8',
    'Bangabandhu 1', 'Belintersat 1', 'BulgariaSat 1', 'CMS 1', 'ChinaSat 10', 'ChinaSat 11', 'ChinaSat 12',
    'ChinaSat 16',
    'ChinaSat 19', 'ChinaSat 1D', 'ChinaSat 1E', 'ChinaSat 26', 'ChinaSat 2A', 'ChinaSat 2C', 'ChinaSat 2D',
    'ChinaSat 2E',
    'ChinaSat 6B', 'ChinaSat 6C', 'ChinaSat 6D', 'ChinaSat 6E', 'ChinaSat 9', 'ChinaSat 9A (drifting west)',
    'ChinaSat 9B',
    'Cosmos 2520', 'Cosmos 2526', 'EDRS C', 'EchoStar 10', 'EchoStar 105 (SES 11)', 'EchoStar 11', 'EchoStar 14',
    'EchoStar 15',
    'EchoStar 16', 'EchoStar 17', 'EchoStar 18', 'EchoStar 19', 'EchoStar 21', 'EchoStar 23', 'EchoStar 9 (Galaxy 23)',
    'Eutelsat 10B', 'Eutelsat 113 West A (drifting west)', 'Eutelsat 115 West B', 'Eutelsat 117 West A',
    'Eutelsat 117 West B',
    'Eutelsat 12 West G', 'Eutelsat 139 West A', 'Eutelsat 16A', 'Eutelsat 172B', 'Eutelsat 174A', 'Eutelsat 21B',
    'Eutelsat 33E',
    'Eutelsat 33F', 'Eutelsat 36B', 'Eutelsat 3B', 'Eutelsat 5 West B', 'Eutelsat 65 West A', 'Eutelsat 7 West A',
    'Eutelsat 70B',
    'Eutelsat 7B', 'Eutelsat 7C', 'Eutelsat 8 West B', 'Eutelsat 9B', 'Eutelsat Ka-Sat 9A', 'Eutelsat Konnect',
    'Eutelsat Konnect VHTS',
    'Eutelsat Quantum', 'Express 103', 'Express 80', 'Express AM44', 'Express AM5', 'Express AM6', 'Express AM7',
    'Express AM8', 'Express AMU1',
    'Express AMU3', 'Express AMU7', 'Express AT1', 'Express AT2', 'G-Sat 10', 'G-Sat 11', 'G-Sat 14', 'G-Sat 15',
    'G-Sat 16', 'G-Sat 17',
    'G-Sat 18', 'G-Sat 19', 'G-Sat 24', 'G-Sat 29', 'G-Sat 30', 'G-Sat 31', 'G-Sat 6', 'G-Sat 7', 'G-Sat 7A', 'G-Sat 8',
    'G-Sat 9',
    'Galaxy 11', 'Galaxy 14', 'Galaxy 16', 'Galaxy 17', 'Galaxy 18', 'Galaxy 19', 'Galaxy 28', 'Galaxy 30', 'Galaxy 31',
    'Galaxy 32',
    'Galaxy 33', 'Galaxy 34', 'Galaxy 35', 'Galaxy 36', 'Galaxy 37 (Horizons 4)', 'Galaxy 3C', 'Hellas Sat 2',
    'Hellas Sat 3', 'Hellas Sat 4',
    'Hispasat 30W-5', 'Hispasat 30W-6', 'Hispasat 36W-1', 'Hispasat 74W-1', 'Horizons 2', 'Horizons 3e', 'Hotbird 13E',
    'Hotbird 13F', 'Hotbird 13G',
    'Hylas 1 (drifting west)', 'Hylas 2', 'Hylas 4', 'Insat 3D', 'Insat 3DR', 'Intelsat 10 (drifting 0.4W (day))',
    'Intelsat 10-02', 'Intelsat 11',
    'Intelsat 14', 'Intelsat 15', 'Intelsat 16', 'Intelsat 17', 'Intelsat 18', 'Intelsat 19', 'Intelsat 1R',
    'Intelsat 20', 'Intelsat 21', 'Intelsat 22',
    'Intelsat 23', 'Intelsat 25', 'Intelsat 28', 'Intelsat 30', 'Intelsat 31', 'Intelsat 33e', 'Intelsat 34',
    'Intelsat 35e', 'Intelsat 36', 'Intelsat 37e',
    'Intelsat 39', 'Intelsat 40e', 'Intelsat 5', 'Intelsat 9 (drifting east)', 'Intelsat 901', 'Intelsat 902',
    'Intelsat 904', 'Intelsat 905', 'Intelsat 906',
    'JCSAT 12', 'JCSAT 15', 'JCSAT 16', 'JCSAT 17', 'JCSAT 1C', 'JCSAT 2B', 'JCSAT 3A', 'JCSAT 4B', 'JCSAT 5A',
    'Jupiter 3 (EchoStar 24)', 'KazSat 2',
    'KazSat 3', 'Koreasat 5', 'Koreasat 5A', 'Koreasat 6', 'Koreasat 7', 'LaoSat 1', 'Luch 5A', 'Luch 5B', 'Measat 3a',
    'Measat 3b', 'Measat 3d',
    'Merah Putih 2', 'Mexsat Bicentenario', 'Morelos 3', 'NSS 10', 'NSS 11', 'NSS 12', 'NSS 9', 'NigComSat 1R',
    'Nilesat 201', 'Nilesat 301', 'Nimiq 2',
    'Nimiq 4', 'Nimiq 5', 'Nimiq 6', 'Nusantara Satu', 'Optus 10', 'Optus C1', 'Optus D1', 'Optus D2', 'Optus D3',
    'Paksat 1R', 'QuetzSat 1',
    'Rascom QAF 1R', 'SES 1', 'SES 10', 'SES 12', 'SES 14', 'SES 15', 'SES 16 (GovSat 1)', 'SES 17', 'SES 18', 'SES 19',
    'SES 2', 'SES 20', 'SES 21',
    'SES 22', 'SES 3', 'SES 4', 'SES 5', 'SES 6', 'SES 7', 'SES 8', 'SES 9', 'SGDC', 'ST 2', 'Sirius FM 5',
    'Sirius FM 6', 'Sirius XM 5', 'Sirius XM 7',
    'Sirius XM 8', 'Sky Brasil 1', 'Sky Mexico 1', 'Spaceway 2', 'SpainSat', 'Star One C2', 'Star One C3',
    'Star One C4', 'Star One D1', 'Star One D2',
    'Superbird B3', 'Superbird C2', 'T10', 'T11', 'T12', 'T14', 'T15', 'T16', 'T5', 'T8', 'T9S', 'TDRS 10', 'TDRS 11',
    'TDRS 12', 'TDRS 13', 'TDRS 3',
    'TDRS 5 (drifting 1.4E (day))', 'TDRS 6', 'TDRS 7', 'TDRS 8', 'TKSat 1', 'Telkom 3S', 'Telkom 4', 'Telstar 11N',
    'Telstar 12 Vantage', 'Telstar 14R',
    'Telstar 18 Vantage', 'Telstar 19 Vantage', 'TerreStar 1', 'Thaicom 4', 'Thaicom 6', 'Thaicom 8', 'Thor 5',
    'Thor 6', 'Thor 7', 'TurkmenÄlem (MonacoSat)',
    'Türksat 3A', 'Türksat 4A', 'Türksat 4B', 'Türksat 5A', 'Türksat 5B', 'ViaSat 1', 'ViaSat 2', 'ViaSat 3 Americas',
    'Vinasat 1', 'Vinasat 2', 'WGS 3',
    'WildBlue 1', 'XM 3', 'Yamal 202', 'Yamal 300K', 'Yamal 401', 'Yamal 402', 'Yamal 601'
]

language_options = [
    'Afr: Afrikaans', 'Alb: Albanian', 'Amh: Amharic', 'Ara: Arabic', 'Arm: Armenian', 'Asm: Assamese',
    'Aze: Azerbaijani',
    'Baq: Basque', 'Bel: Belarusian', 'Bem: Bemba', 'Ben: Bengali', 'Ber: Berber', 'Bho: Bhojpuri', 'Bos: Bosnian',
    'Bul: Bulgarian',
    'Bur: Burmese', 'Cat: Catalan', 'Chi: Chinese', 'Cze: Czech', 'Dan: Danish', 'Div: Dhivehi (Maldivian)',
    'Dut: Dutch', 'Eng: English',
    'Est: Estonian', 'Ewe: Ewe', 'Fin: Finnish', 'Fre: French', 'Geo: Georgian', 'Ger: German', 'Gla: Scottish Gaelic',
    'Gle: Irish',
    'Glg: Galician', 'Gre: Greek', 'Guj: Gujarati', 'Hau: Hausa', 'Heb: Hebrew', 'Hin: Hindi', 'Hok: Hmong',
    'Hrv: Croatian',
    'Hun: Hungarian', 'Ibo: Igbo', 'Ice: Icelandic', 'Ind: Indonesian', 'Ita: Italian', 'Jpn: Japanese', 'Kan: Kannada',
    'Kaz: Kazakh',
    'Khm: Khmer', 'Kho: Khasi', 'Kin: Kinyarwanda', 'Kir: Kyrgyz', 'Kor: Korean', 'Kur: Kurdish', 'Lah: Lahnda',
    'Lao: Lao', 'Lav: Latvian',
    'Lin: Lingala', 'Lit: Lithuanian', 'Ltz: Luxembourgish', 'Mac: Macedonian', 'Mal: Malayalam', 'Mar: Marathi',
    'May: Malay', 'Mlg: Malagasy',
    'Mlt: Maltese', 'Mon: Mongolian', 'Nep: Nepali', 'Nor: Norwegian', 'Nya: Chichewa (Nyanja)', 'Ori: Odia (Oriya)',
    'Orm: Oromo', 'Pan: Punjabi',
    'Per: Persian', 'Pol: Polish', 'Por: Portuguese', 'Prs: Dari (Persian)', 'Pus: Pashto',
    'Qaa: Reserved for local use', 'Rum: Romanian',
    'Run: Rundi (Kirundi)', 'Rus: Russian', 'Sin: Sinhala', 'Slo: Slovak', 'Slv: Slovenian', 'Sna: Shona',
    'Som: Somali', 'Spa: Spanish',
    'Srp: Serbian', 'Swa: Swahili', 'Swe: Swedish', 'Syr: Syriac', 'Tam: Tamil', 'Tel: Telugu', 'Tet: Tetum',
    'Tgk: Tajik', 'Tgl: Tagalog',
    'Tha: Thai', 'Tib: Tibetan', 'Tir: Tigrinya', 'Tuk: Turkmen', 'Tur: Turkish', 'Twi: Twi', 'Uig: Uyghur',
    'Ukr: Ukrainian', 'Urd: Urdu',
    'Uzb: Uzbek', 'Vie: Vietnamese', 'Wel: Welsh', 'Xho: Xhosa', 'Yor: Yoruba', 'Yue: Cantonese', 'Zul: Zulu',
    'Zza: Zaza'
]

region_var = tk.StringVar(root)
def_var = tk.StringVar(root)
satellite_var = tk.StringVar(root)
language_var = tk.StringVar(root)

# Create dropdown menus
region_dropdown = tk.OptionMenu(filter_channel_frame, region_var, *region_options)
def_dropdown = tk.OptionMenu(filter_channel_frame, def_var, *def_options)
satellite_dropdown = tk.OptionMenu(filter_channel_frame, satellite_var, *satellite_options)
language_dropdown = tk.OptionMenu(filter_channel_frame, language_var, *language_options)

# Grid the dropdown menus
region_dropdown.grid(row=1, column=1)
def_dropdown.grid(row=2, column=1)
satellite_dropdown.grid(row=3, column=1)
language_dropdown.grid(row=4, column=1)
button_confirm = tk.Button(filter_channel_frame, text="Confirm", command=get_filtered_list)
button_confirm.grid(row=10, column=2, columnspan=1, sticky="we")
# Add a back button to return to the menu
button_back = tk.Button(filter_channel_frame, text="Back")
button_back.grid(row=10, column=1, columnspan=1, sticky="n")
Tooltip(button_back, "Go Back to Menu", show_menu_view)

# Run the application
root.mainloop()
