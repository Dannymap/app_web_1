import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Tareas Pendientes")
st.subheader("Esta es mi App para hacer cosas.")
st.write("<h1>Esta App es para aumentar tu <b>productividad</b>.<h1>",
         unsafe_allow_html=True)

st.text_input(label="", placeholder="Agregar nuevas tareas...",
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()