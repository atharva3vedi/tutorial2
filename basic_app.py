import sys
from tkinter import filedialog
from PIL import Image, ImageTk
if "tkinter" not in sys.modules:
    import tkinter as tk
else:
    import tkinter as tk

class PresentationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Presentation Software")
        
        self.slides = []
        self.current_slide = 0
        
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()
        
        self.title_entry = tk.Entry(root, width=50)
        self.title_entry.pack()
        
        self.text_entry = tk.Entry(root, width=50)
        self.text_entry.pack()
        
        self.add_image_button = tk.Button(root, text="Add Image", command=self.add_image)
        self.add_image_button.pack()
        
        self.add_button = tk.Button(root, text="Add Slide", command=self.add_slide)
        self.add_button.pack()
        
        self.delete_button = tk.Button(root, text="Delete Slide", command=self.delete_slide)
        self.delete_button.pack()
        
        self.prev_button = tk.Button(root, text="Previous", command=self.prev_slide)
        self.prev_button.pack(side=tk.LEFT, padx=20, pady=10)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_slide)
        self.next_button.pack(side=tk.RIGHT, padx=20, pady=10)
        
        self.display_slide()
    
    def display_slide(self):
        self.canvas.delete("all")
        if self.slides:
            slide = self.slides[self.current_slide]
            text_x, text_y = 350, 200  # Start from center, move right
            text_box_width = 200  # Limit text to this width
            
            if slide.get("image"):
                image = slide["image"]
                self.canvas.create_image(100, 200, image=image, anchor=tk.CENTER)
                text_x = 300
            
            self.canvas.create_text(text_x, 100, text=slide.get("title", ""), font=("Arial", 20, "bold"), fill="black")
            self.canvas.create_text(text_x, text_y, text=slide.get("text", ""), font=("Arial", 16), fill="black", width=text_box_width, anchor="w")
        else:
            self.canvas.create_text(300, 200, text="No slides available", font=("Arial", 20), fill="black")
    
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
            new_slide = {"title": title, "text": text, "image": None}
            self.slides.append(new_slide)
            self.title_entry.delete(0, tk.END)
            self.text_entry.delete(0, tk.END)
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
            self.display_slide()
    
    def delete_slide(self):
        if self.slides:
            del self.slides[self.current_slide]
            if not self.slides:
                self.current_slide = 0
            else:
                self.current_slide = min(self.current_slide, len(self.slides) - 1)
            self.display_slide()

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = PresentationApp(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")