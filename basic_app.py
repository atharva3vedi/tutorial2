from dotenv import load_dotenv
import sys
import json
import xml.etree.ElementTree as ET
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import tkinter as tk
from groq import Groq

class PresentationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Presentation Software")
        
        self.slides = []
        self.current_slide = 0

        # Top Frame for Controls
        self.top_frame = tk.Frame(root)
        self.top_frame.pack(fill=tk.X, pady=10)
        
        self.add_button = tk.Button(self.top_frame, text="+", font=("Arial", 14, "bold"), command=self.add_slide)
        self.add_button.pack(side=tk.LEFT, padx=10)
        
        self.delete_button = tk.Button(self.top_frame, text="Delete", command=self.delete_slide)
        self.delete_button.pack(side=tk.LEFT, padx=10)
        
        self.save_button = tk.Button(self.top_frame, text="Save", command=self.save_presentation)
        self.save_button.pack(side=tk.LEFT, padx=10)
        
        self.load_button = tk.Button(self.top_frame, text="Load", command=self.load_presentation)
        self.load_button.pack(side=tk.LEFT, padx=10)
        
        self.ai_summary_button = tk.Button(self.top_frame, text="AI Summary", command=self.summarize_text)
        self.ai_summary_button.pack(side=tk.LEFT, padx=10)
        
        # Main Canvas
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()
        
        # Input Fields
        self.title_entry = tk.Entry(root, width=50)
        self.title_entry.insert(0, "Enter Title")
        self.title_entry.pack(pady=5)
        
        self.text_entry = tk.Entry(root, width=50)
        self.text_entry.insert(0, "Enter Body Text")
        self.text_entry.pack(pady=5)
        
        self.add_image_button = tk.Button(root, text="Add Image", command=self.add_image)
        self.add_image_button.pack(pady=5)
        
        # AI Summary Sidebar
        self.summary_label = tk.Label(root, text="AI Summary:", font=("Arial", 12, "bold"))
        self.summary_label.pack()
        
        self.summary_text = tk.Text(root, width=50, height=5, state=tk.DISABLED)
        self.summary_text.pack()
        
        # Navigation Buttons
        self.nav_frame = tk.Frame(root)
        self.nav_frame.pack(fill=tk.X, pady=10)
        
        self.prev_button = tk.Button(self.nav_frame, text="Previous", command=self.prev_slide)
        self.prev_button.pack(side=tk.LEFT, padx=20)
        
        self.next_button = tk.Button(self.nav_frame, text="Next", command=self.next_slide)
        self.next_button.pack(side=tk.RIGHT, padx=20)
        
        self.display_slide()

    def summarize_text(self):
        if not self.slides:
            return

        # Get text from the currently displayed slide
        title = self.slides[self.current_slide].get("title", "")
        text = self.slides[self.current_slide].get("text", "")

        client = Groq(api_key='NqhPjEaSzG71SkfkM')

        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": f"Summarize this: Title: {title}, Body: {text}"}],
            model="llama-3.3-70b-versatile",
        )

        summary = chat_completion.choices[0].message.content if chat_completion.choices else "No summary available."

        self.summary_text.config(state=tk.NORMAL)
        self.summary_text.delete("1.0", tk.END)
        self.summary_text.insert(tk.END, summary)
        self.summary_text.config(state=tk.DISABLED)

    
    def display_slide(self):
        self.canvas.delete("all")
        if self.slides:
            slide = self.slides[self.current_slide]
            text_x, text_y = 300, 200  # Default to center
            text_box_width = 200  # Limit text width
            
            if slide.get("image"):
                image = slide["image"]
                self.canvas.create_image(100, 200, image=image, anchor=tk.CENTER)
                text_x = 350  # Shift text if image is present
            
            self.canvas.create_text(300, 100, text=slide.get("title", ""), font=("Arial", 20, "bold"), fill="black", anchor="center")
            self.canvas.create_text(text_x, text_y, text=slide.get("text", ""), font=("Arial", 16), fill="black", width=text_box_width, anchor="center" if not slide.get("image") else "w")
        else:
            self.canvas.create_text(300, 200, text="No slides available", font=("Arial", 20), fill="black", anchor="center")
    
    def next_slide(self):
        if self.slides and self.current_slide < len(self.slides) - 1:
            self.current_slide += 1
            self.display_slide()
    
    def prev_slide(self):
        if self.slides and self.current_slide > 0:
            self.current_slide -= 1
            self.display_slide()
    
    def add_slide(self):
        title = self.title_entry.get()
        text = self.text_entry.get()
        
        if title or text:
            new_slide = {"title": title, "text": text, "image": None, "image_path": None}
            self.slides.append(new_slide)
            self.title_entry.delete(0, tk.END)
            self.text_entry.delete(0, tk.END)
            self.title_entry.insert(0, "Enter Title")
            self.text_entry.insert(0, "Enter Body Text")
            if len(self.slides) == 1:
                self.current_slide = 0
            self.display_slide()
    
    def add_image(self):
        if not self.slides:
            return
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((100, 100))
            photo = ImageTk.PhotoImage(image)
            self.slides[self.current_slide]["image"] = photo
            self.slides[self.current_slide]["image_path"] = file_path
            self.display_slide()
    
    def delete_slide(self):
        if self.slides:
            del self.slides[self.current_slide]
            if not self.slides:
                self.current_slide = 0
            else:
                self.current_slide = min(self.current_slide, len(self.slides) - 1)
            self.display_slide()
    
    def save_presentation(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            slides_data = [{"title": slide["title"], "text": slide["text"], "image_path": slide["image_path"]} for slide in self.slides]
            with open(file_path, "w") as file:
                json.dump(slides_data, file, indent=4)
    
    def load_presentation(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, "r") as file:
                slides_data = json.load(file)
                self.slides = slides_data
                for slide in self.slides:
                    if slide.get("image_path"):
                        image = Image.open(slide["image_path"])
                        image = image.resize((100, 100))
                        slide["image"] = ImageTk.PhotoImage(image)
                self.current_slide = 0 if self.slides else None
                self.display_slide()

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = PresentationApp(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")
