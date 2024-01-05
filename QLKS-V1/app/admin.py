from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from app import app, db
from app.models import TypeRoom, Room
from flask_login import logout_user, current_user
from flask import redirect
from app.models import UserRoleEnum

admin = Admin(app=app, name='QUẢN LÝ KHÁCH SẠN OU HOTEL', template_mode='bootstrap4')


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN


class MyRoomView(AuthenticatedAdmin):
    column_display_pk = True
    column_list = ['name', 'description', 'image', 'price', 'typeroom']
    column_searchable_list = ['name']
    column_filters = ['price', 'name']
    can_export = True
    can_view_details = True


class MyTypeRoomView(AuthenticatedAdmin):
    column_list = ['name', 'rooms']


class MyStatsView(AuthenticatedUser):
    @expose("/")
    def index(self):
        return self.render('admin/stats.html')


class MyLogOutView(AuthenticatedUser):
    @expose("/")
    def index(self):
        logout_user()
        return redirect('/admin')


admin.add_view(MyTypeRoomView(TypeRoom, db.session))
admin.add_view(MyRoomView(Room, db.session))
admin.add_view(MyStatsView(name='Báo cáo doanh thu'))
admin.add_view(MyLogOutView(name='Đăng xuất'))
