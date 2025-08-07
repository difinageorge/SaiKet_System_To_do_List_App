# ✅ To-Do List Web App - Streamlit

This project was completed as part of my **Python Development Internship** at **SaiKet Systems** (Task 01).  
The objective was to build a simple yet functional **To-Do List Web App** using **Streamlit**, where users can add tasks, mark them as complete, and manage their daily goals interactively.

---

## 🚀 Live Demo

This is a local Python web application built using Streamlit.  
You can run it on your system by following the instructions below.

---

## 📌 Task Objective

Develop a **Python-based GUI To-Do List Application** that:

- Lets users add new tasks.
- Displays all tasks dynamically with their status.
- Allows users to mark tasks as completed.
- Visually distinguishes completed tasks with a tick.
- Updates the task list in real-time using session state.

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit** (for building the web UI)
* **Session State** (for persistent task tracking across interactions)

---

## 📁 Project Structure

```

gui.py                     # Main Streamlit app file
requirements.txt           # Project dependencies
README.md                  # Project documentation

````

---

## 🧠 How It Works

1. The user enters a task into the text input field and clicks **Add Task**.
2. The task is stored in `st.session_state` and displayed immediately.
3. Tasks are shown with check or cross icons based on their completion status.
4. Users can click **Mark Done** next to a task to mark it as completed.
5. The app instantly reflects the updated status without page reload.

---

## ▶️ How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/difinageorge/SaiKet_System_To_do_List_App.git
   cd SaiKet_System_To_do_List_App
   ```


2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**:

   ```bash
   streamlit run gui.py
   ```

4. Open `http://localhost:8501` in your browser and start managing your tasks!

---

## 📸 Screenshots

*(Coming soon...)*

---

## 🧩 Features

* Interactive task management interface
* Real-time UI updates using Streamlit’s session state
* Task completion toggling
* Auto-clearing task input after submission
* Simple and minimal UI

---

## 🔧 Future Enhancements

* Add due dates and task priority
* Include option to delete tasks
* Add persistent storage (e.g., database or local file)
* Deploy on Streamlit Cloud or Heroku for online access

---

## 🎓 Internship & Task Details

* **Internship Track**: Python Development
* **Internship Provider**: SaiKet Systems
* **Task Name**: To-Do List App
* **Environment**: Python + Streamlit

---

## 📬 Contact

* **Difina George**
* 📧 [difina.georgecs@gmail.com](mailto:difina.georgecs@gmail.com)
* 📍 Kerala, India
