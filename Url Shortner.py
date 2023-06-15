import tkinter as tk
import pyshorteners

class URLShortenerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("URL Shortener")
        self.root.geometry("300x150")
        self.root.configure(bg='black')
        self.long_url = tk.StringVar()
        self.short_url = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        long_url_label = tk.Label(self.root, text="Long URL:", background="black", foreground="white")
        long_url_label.pack()
        long_url_entry = tk.Entry(self.root, textvariable=self.long_url)
        long_url_entry.pack()
        shorten_button = tk.Button(self.root, text="Shorten URL", command=self.shorten_url,background="black", foreground="light blue")
        shorten_button.pack()
        short_url_label = tk.Label(self.root, text="Short URL:", background="black", foreground="white")
        short_url_label.pack()
        short_url_display = tk.Entry(self.root, textvariable=self.short_url, state="readonly")
        short_url_display.pack()

    def shorten_url(self):
        long_url = self.long_url.get()
        shortener = pyshorteners.Shortener()
        shortened_url = shortener.tinyurl.short(long_url)
        self.short_url.set(shortened_url)
root = tk.Tk()
app = URLShortenerApp(root)
root.mainloop()


