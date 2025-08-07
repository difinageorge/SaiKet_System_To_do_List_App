import streamlit as st

# ----- Task Class -----
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

# ----- ToDoList Class -----
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))


# ----- Session State Initialization -----
if "todo" not in st.session_state:
    st.session_state.todo = ToDoList()
if "new_task" not in st.session_state:
    st.session_state.new_task = ""


# ----- Callback to Add Task -----
def add_task_callback():
    task = st.session_state.new_task.strip()
    if task:
        st.session_state.todo.add_task(task)
    st.session_state.new_task = ""  # ✅ clear input safely


# ----- App UI -----
st.title("📝 To-Do List with Checkboxes")

# ----- Task Input Form -----
with st.form("add_task_form"):
    st.text_input("Enter task description:", key="new_task")
    submitted = st.form_submit_button("Add Task", on_click=add_task_callback)

# ----- Show Tasks -----
st.subheader("Your Tasks")

if not st.session_state.todo.tasks:
    st.info("No tasks yet. Add some!")
else:
    for idx, task in enumerate(st.session_state.todo.tasks):
        checked = st.checkbox(
            label=task.description,
            value=task.completed,
            key=f"task_{idx}"
        )
        # Reflect checkbox changes in the task
        if checked and not task.completed:
            task.mark_completed()
        elif not checked and task.completed:
            task.completed = False  # Optional toggle
