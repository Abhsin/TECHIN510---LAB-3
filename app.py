import streamlit as st

def main():
    st.title("To-Do App")
    
    # Get user input for task
    task = st.text_input("Add a new task:")
    
    # Retrieve existing tasks from session state
    tasks = st.session_state.get("tasks", [])
    
    # Display current tasks
    st.subheader("Current Tasks:")
    if not tasks:
        st.write("No tasks added yet.")
    else:
        for i, task_item in enumerate(tasks):
            st.write(f"{i+1}. {task_item}")
    
    # Add task to the list
    if st.button("Add Task") and task:
        tasks.append(task)
        st.session_state.tasks = tasks
        st.success(f"Task '{task}' added successfully!")

    # Clear tasks
    if st.button("Clear All Tasks"):
        st.session_state.tasks = []
        st.success("All tasks cleared!")

if __name__ == "__main__":
    main()
