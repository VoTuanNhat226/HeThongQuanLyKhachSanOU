from flask import render_template, request, redirect
import dao
from app import app, login
from flask_login import login_user

@app.route('/')
def index():
    kw = request.args.get('kw')
    pricefrom = request.args.get('pricefrom')
    priceto = request.args.get('priceto')
    type_id = request.args.get('type_id')
    type = dao.load_typeroom()
    rooms = dao.load_rooms(kw=kw, type_id=type_id, pricefrom=pricefrom, priceto=priceto)

    return render_template('index.html', typeroom=type, rooms=rooms)


@app.route('/room/<id>')
def view_room(id):
    return render_template('viewroom.html', room=dao.get_room_by_id(id))

@app.route('/admin/login', methods=['post'])
def login_admin_process():
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)
    return redirect('/admin')

@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


@app.route('/booking')
def book_room():
    kw = request.args.get('kw')
    rooms = dao.load_bookrooms(kw)
    return render_template('booking.html', rooms=rooms)

if __name__ == '__main__':
    from app import admin
    app.run(debug=True)