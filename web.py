import streamlit as st
import functions
import os

tasks = functions.get_tasks()

def add_task():
    task_to_add = st.session_state["new_task"]  + "\n"
    tasks.append(task_to_add)
    functions.write_tasks(tasks)


if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as file:
        pass

st.title("My To-Do App")
st.subheader("This is my to-do app.")

for index, task in enumerate(tasks):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        tasks.pop(index)
        functions.write_tasks(tasks)
        del st.session_state[task]
        st.rerun()

st.text_input(label=" ", placeholder="Add new task...",
              on_change=add_task, key="new_task")
