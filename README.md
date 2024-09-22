"""
# Song Lyrics Extractor GUI

## Project Overview:
This is a Python-based graphical user interface (GUI) application that allows users to extract lyrics from songs. The application is built using **customtkinter** for a modern interface and integrates with the **Lyrics.ovh API** to fetch the song lyrics.

## Features:
- Simple and user-friendly GUI.
- Users can enter the song title and artist name to retrieve lyrics.
- Fetches lyrics using the Lyrics.ovh API.
- Displays lyrics in a scrollable window for easy reading.

## How It Works:
1. Enter the **song name** and **artist name** in the respective fields.
2. Click the **Show Lyrics** button.
3. A new window will appear with the song lyrics displayed.

## Installation:
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/song-lyrics-extractor.git
    ```
2. Install the required dependencies:
    ```bash
    pip install requests customtkinter
    ```
3. Run the Python script:
    ```bash
    python lyrics_gui.py
    ```

## Code Explanation:
- **customtkinter**: Used to build a modern GUI.
- **requests**: Used to make API calls to fetch song lyrics.
- The main functionality is in `get_lyrics()` which calls the Lyrics.ovh API and retrieves the lyrics of the specified song and artist.

## API Reference:
- **Lyrics.ovh API**: This is a free API to fetch song lyrics.

## Example:
![GUI Screenshot](example_screenshot.png)

## License:
This project is licensed under the MIT License.
"""

# Write the content to a README.md file
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)


# Song_Lyrics_GUI


![Screenshot 2024-09-22 205634](https://github.com/user-attachments/assets/ad7c4d31-123c-4e92-b7cd-4c8452fd9208)



![Screenshot 2024-09-22 205642](https://github.com/user-attachments/assets/77511b72-47aa-4794-b24f-01fcc0e54b0c)
