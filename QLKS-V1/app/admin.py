from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from app import app, db
from app.models import TypeRoom, Room


admin = Admin(app=app, name='QUẢN LÝ KHÁCH SẠN OU HOTEL', template_mode='bootstrap4')

class MyRoomView(ModelView):
    column_display_pk = True
    column_list = ['name', 'description', 'image', 'price']
    column_searchable_list = ['name']
    column_filters = ['price', 'name']

admin.add_view(ModelView(TypeRoom, db.session))
admin.add_view(MyRoomView(Room, db.session))