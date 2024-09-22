import customtkinter as ctk
import requests
import tkinter as tk

# Function to get lyrics from the API
def get_lyrics(artist, song):
    url = f'https://api.lyrics.ovh/v1/{artist}/{song}'
    response = requests.get(url)
    return response.json().get('lyrics', "Lyrics not found")

# Initialize the main window using customtkinter
root1 = ctk.CTk()
root1.title("Song Lyrics")
root1.geometry('700x600')


# Frame for input fields and buttons
frame1 = ctk.CTkFrame(root1)
frame1.pack(pady=20, padx=20)

# Variables to store song and artist info
song_name = ""
artist_name = ""

# Function to store the artist and song details
def store_song_info():
    global song_name, artist_name
    song_name = Name_text.get()
    artist_name = Artist_entry.get()

# Function to show the new window with scrollable lyrics
def show_song_details():
    # Store the song and artist information
    store_song_info()

    # Fetch the lyrics using the API
    lyrics = get_lyrics(artist_name, song_name)

    # Create a new window to display the lyrics
    root2 = ctk.CTkToplevel()
    root2.title("Song Lyrics")
    root2.geometry('700x600')

    # Scrollable frame to display lyrics
    frame2 = ctk.CTkScrollableFrame(root2, width=600, height=400)
    frame2.pack(pady=20, padx=20)

    # Add the lyrics inside the scrollable frame
    lyrics_label = tk.Label(frame2, text=lyrics, justify='left', wraplength=500, bg="lightcyan")
    lyrics_label.pack(padx=10, pady=10)

# Input fields for song name and artist
Name_label = ctk.CTkLabel(frame1, text='Song Name:')
Name_label.grid(row=0, column=0, padx=10, pady=10)

Name_text = ctk.CTkEntry(frame1, width=200)
Name_text.grid(row=0, column=1, padx=10, pady=10)

Artist_label = ctk.CTkLabel(frame1, text='Artist Name:')
Artist_label.grid(row=1, column=0, padx=10, pady=10)

Artist_entry = ctk.CTkEntry(frame1, width=200)
Artist_entry.grid(row=1, column=1, padx=10, pady=10)

#Show Lyrics 
show_btn = ctk.CTkButton(frame1, text="Show Lyrics", command=show_song_details)
show_btn.grid(row=2, column=1, padx=10, pady=20)

# Run the main loop
root1.mainloop()

