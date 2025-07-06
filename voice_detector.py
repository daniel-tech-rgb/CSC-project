import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr


def listen_and_detect():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    try:
        with mic as source:
            status_label.config(text="Listening...")
            window.update()
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)

        status_label.config(text="Recognizing...")
        window.update()
        text = recognizer.recognize_google(audio)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, text)
        status_label.config(text="Done!")

    except sr.WaitTimeoutError:
        messagebox.showerror("Timeout", "No speech detected. Please try again.")
        status_label.config(text="Ready")
    except sr.UnknownValueError:
        messagebox.showerror("Error", "Could not understand audio.")
        status_label.config(text="Ready")
    except sr.RequestError as e:
        messagebox.showerror("Error", f"Could not request results; {e}")
        status_label.config(text="Ready")


# Create the main window
window = tk.Tk()
window.title("Voice Detection GUI")
window.geometry("400x300")

# Add button to start voice detection
listen_button = tk.Button(window, text="Start Listening", command=listen_and_detect)
listen_button.pack(pady=20)

# Label to show status
status_label = tk.Label(window, text="Ready")
status_label.pack()

# Text box to show recognized speech
result_text = tk.Text(window, height=10, width=40)
result_text.pack(pady=10)

window.mainloop()
