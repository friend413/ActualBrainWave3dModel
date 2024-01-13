import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import requests
from io import BytesIO

def load_image_from_url():
    """ Load an image from the URL specified in the URL entry field. """
    url = url_entry.get()
    try:
        response = requests.get(url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img.thumbnail((250, 250))  # Resize the image to fit the display area
        img_photo = ImageTk.PhotoImage(img)
        image_label.configure(image=img_photo)
        image_label.image = img_photo  # Keep a reference to avoid garbage collection
    except Exception as e:
        print(f"Error loading image: {e}")

def save_image():
    """ Save the currently displayed image. """
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"), 
                                                        ("JPEG files", "*.jpg"), 
                                                        ("All files", "*.*")])
    if file_path:
        img = image_label.image._PhotoImage__photo  # Access the underlying PhotoImage
        img.write(file_path, format='png')

def exit_app():
    """ Exit the application. """
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Image Viewer")

# URL Entry and Submit button
url_entry = tk.Entry(root, width=50)
url_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

submit_button = tk.Button(root, text="Get", command=load_image_from_url)
submit_button.pack(side=tk.TOP, pady=5)

# Image display area
image_label = tk.Label(root)
image_label.pack(padx=10, pady=10)

# Save and Exit buttons
save_button = tk.Button(root, text="Save Image", command=save_image)
save_button.pack(side=tk.LEFT, padx=10, pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
