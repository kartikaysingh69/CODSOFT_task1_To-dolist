import tkinter as tk
from tkinter import simpledialog

class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Task Manager")
        self.tasks = []

        self.setup_interface()

    def setup_interface(self):
        self.root.configure(bg="lightgray")

        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.task_listbox.pack(padx=12, pady=12)

        self.add_button = tk.Button(self.root, text="Add New Task", command=self.add_task, bg="skyblue", fg="white")
        self.add_button.pack(padx=12, pady=6)

        self.update_button = tk.Button(self.root, text="Update Status", command=self.update_task_status, bg="green", fg="white")
        self.update_button.pack(padx=12, pady=6)

        self.show_all_button = tk.Button(self.root, text="Show All Tasks", command=self.show_all_tasks, bg="orange", fg="white")
        self.show_all_button.pack(padx=12, pady=6)

        self.completed_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.completed_listbox.pack(padx=12, pady=12)

        self.quit_button = tk.Button(self.root, text="Exit", command=self.root.quit, bg="red", fg="white")
        self.quit_button.pack(padx=12, pady=6)

    def add_task(self):
        new_task_title = simpledialog.askstring("New Task", "Enter the task:")
        if new_task_title:
            new_task = Task(new_task_title)
            self.tasks.append(new_task)
            self.task_listbox.insert(tk.END, new_task.title)

    def update_task_status(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            task = self.tasks[task_index]
            done = simpledialog.askinteger("Task Status", "Done or Not Done? (1 for Done, 0 for Done)")
            if done is not None:
                task.done = bool(done)
                self.update_task_display(task_index)
                self.update_completed_tasks()

    def update_task_display(self, index):
        task = self.tasks[index]
        status = "Done" if task.done else "Not Done"
        self.task_listbox.delete(index)
        self.task_listbox.insert(index, f"{task.title} - Status: {status}")

    def update_completed_tasks(self):
        self.completed_listbox.delete(0, tk.END)
        for task in self.tasks:
            if task.done:
                self.completed_listbox.insert(tk.END, task.title)

    def show_all_tasks(self):
        self.completed_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task.done else "Not Done"
            self.completed_listbox.insert(tk.END, f"{task.title} - Status: {status}")

def initiate():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    initiate()
