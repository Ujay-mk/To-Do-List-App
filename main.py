from flask import Flask, render_template , redirect, request
import json
import os 

app = Flask(__name__)
if os.path.exists('task.json'):
    with open('task.json', 'r') as f:
        tasks = json.load(f)
else:
    tasks = []
index = 0
def write_task_in_json(filename,list):
   with open(filename, 'w') as f:
         json.dump(list, f)


#App Start
@app.route('/',methods =['GET','POST'] )
def main():
    global tasks
    if request.method == 'POST':
        task =request.form['task']
        tasks.append(task)
        write_task_in_json('task.json',tasks)
        return redirect('/')
    else:    
       
        return render_template('index.html',tasks=tasks,index=index)

@app.route('/delete/<int:index>',methods =['GET','POST'] )
def delete(index):
    if request.method == 'POST':
        tasks.pop(index)
        write_task_in_json('task.json',tasks)
       
        return redirect('/')
    
    else:    
       return redirect('/')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('pnf.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)