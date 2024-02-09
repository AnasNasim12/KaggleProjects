from pytube import YouTube
import os
import moviepy.editor as mp
from tkinter import Tk, filedialog, Label, Entry, Button, messagebox

def download_audio(video_url, output_path):
    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_file = audio_stream.download(output_path=output_path)
        return audio_file
    except Exception as e:
        messagebox.showerror("Error", "An error occurred: " + str(e))
        return None

def choose_output_path():
    root = Tk()
    root.attributes("-topmost", True)  # Bring the window to the front
    root.withdraw()  # Hide the root window
    folder_path = filedialog.askdirectory(title="Choose Save Location")
    root.destroy()
    return folder_path

def download_and_convert():
    video_url = url_entry.get()
    output_path = choose_output_path()

    if not output_path:
        messagebox.showerror("Error", "No save location selected. Exiting.")
        return

    # Download audio
    audio_file = download_audio(video_url, output_path)

    if audio_file:
        try:
            # Convert the downloaded audio to mp3 format
            video_clip = mp.AudioFileClip(audio_file)
            audio_file_mp3 = os.path.join(output_path, os.path.splitext(os.path.basename(audio_file))[0] + '.mp3')
            video_clip.write_audiofile(audio_file_mp3)
            video_clip.close()

            messagebox.showinfo("Success", "Audio downloaded and converted successfully to:\n" + audio_file_mp3)
        except Exception as e:
            messagebox.showerror("Error", "An error occurred while converting the audio to mp3: " + str(e))
    else:
        messagebox.showerror("Error", "Failed to download audio.")

# Create GUI window
root = Tk()
root.title("YouTube Audio Downloader")

# Create URL entry
url_label = Label(root, text="YouTube Video URL:")
url_label.grid(row=0, column=0, padx=5, pady=5)
url_entry = Entry(root, width=50)
url_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

# Create Download button
download_button = Button(root, text="Download Audio", command=download_and_convert)
download_button.grid(row=1, column=1, padx=5, pady=5)

# Run GUI application
root.mainloop()
