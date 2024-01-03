from app.models import TypeRoom, Room

def load_typeroom():
    return TypeRoom.query.all()


def load_rooms(kw=None):
    rooms = Room.query
    if kw:
        rooms = rooms.filter(Room.name.contains(kw))
    return rooms.all()