from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    closed = db.Column(db.String(3), nullable=False, default='No')
    date_closed = db.Column(db.DateTime)

    def __repr__(self):
        return '<Task %r>' % self.id

db.create_all()

@application.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.closed).all()
        not_closed =  Todo.query.filter(Todo.closed.startswith('N')).all()
        return render_template('index.html', tasks=tasks, not_closed=not_closed)


@application.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@application.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)

@application.route('/close/<int:id>', methods = ['GET', 'POST'])
def close(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        num_rows_updated = Todo.query.filter_by(id=task.id).update(dict(closed='Yes',date_closed=datetime.utcnow()))
        db.session.commit()
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return e

    else:
        return render_template('close.html', task=task)


if __name__ == "__main__":
    application.run(debug=True)
