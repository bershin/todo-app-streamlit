import streamlit as st
import functions

print("program start")
todos = functions.get_todos()

def add_todo():
    print("add_todo executed")
    local_todo = st.session_state["new_todo"].strip() + "\n"
    todos.append(local_todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

st.title("ToDo app")
st.subheader("This ia my todo app")
st.write("Welcome to my todo app")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add item", on_change=add_todo, key="new_todo")
st.session_state
print("program end")