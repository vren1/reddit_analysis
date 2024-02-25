import tkinter as tk
from tkinter import ttk
from get_data import extractPosts
from create_graphs import createDataFrame, createScatterPlot
from sentiment_analysis import getAverageScoreWithVADER
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from copy import copy

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Function to handle button click
def submit():
    for frame in frames:
        clear_frame(frame)
    
    topic = entry1.get()

    posts = extractPosts(topic)

    text_widget = tk.Text(scoreFrame, height=1, width=10)
    text_widget.insert(tk.END, getAverageScoreWithVADER(copy(posts)))
    text_widget.pack()

    # Disable text editing (read-only)
    text_widget.config(state=tk.DISABLED)

    df = createDataFrame(posts)

    canvas = FigureCanvasTkAgg(createScatterPlot(df), master=graphFrame)
    canvas.get_tk_widget().pack()

    # table

    tree = ttk.Treeview(tableFrame, columns=list(df.columns), show='headings')

    for col in df.columns:
        tree.heading(col, text=col)
        
    tree.column("Submission text", width=1000)
    tree.column("Score", width=75)

    for i, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    tree.pack()


# Create the main application window
root = tk.Tk()
root.title("Reddit Posts Analysis")

# Create and place the first text field
label1 = tk.Label(root, text="Enter the topic you wish to search on:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

# Create and place the submission button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Create frames for output
scoreFrame = ttk.Frame(root)
tableFrame = ttk.Frame(root)
graphFrame = ttk.Frame(root)
frames = [scoreFrame, tableFrame, graphFrame]

scoreFrame.pack()
tableFrame.pack()
graphFrame.pack()

# Start the main event loop
root.mainloop()
