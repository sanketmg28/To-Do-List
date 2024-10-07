from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize an empty to-do list
todo_list = []

@app.route('/')
def index():
    return render_template('index.html', todos=todo_list)

@app.route('/add', methods=['POST'])
def add_todo():
    # Get the task from the form
    task = request.form.get('task')
    if task:
        todo_list.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    # Remove the task based on its index
    if todo_id < len(todo_list):
        todo_list.pop(todo_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
