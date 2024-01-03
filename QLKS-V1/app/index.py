from flask import render_template, request
import dao
from app import app


@app.route('/')
def index():
    kw = request.args.get('kw')

    type = dao.load_typeroom()
    rooms = dao.load_rooms(kw=kw)

    return render_template('index.html', typeroom=type, rooms=rooms)


if __name__ == '__main__':
    from app import admin
    app.run(debug=True)