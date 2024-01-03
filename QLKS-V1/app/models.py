from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db


class TypeRoom(db.Model):
    __tablename__ = 'typeroom'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    rooms = relationship('Room', backref='typeroom', lazy=True)


class Room(db.Model):
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(200), nullable=False)
    image = Column(String(200), nullable=False)
    price = Column(Float, default=0)
    typeroom_id = Column(Integer, ForeignKey(TypeRoom.id), nullable=False)

if __name__ == '__main__':
    from app import app
    with app.app_context():
        # type1 = TypeRoom(name='Phòng President')
        # type2 = TypeRoom(name='Phòng Premium')
        # type3 = TypeRoom(name='Phòng Luxury')
        # type4 = TypeRoom(name='Phòng Studio')
        # type5 = TypeRoom(name='Phòng Executive')
        # db.session.add_all([type1, type2, type3, type4, type5])
        # db.session.commit()

        room1 = Room(name='Phòng President Suite Hướng biển',
                     description='THE ROOM FOR THE PRESIDENT, THE HEADS OF STATE',
                     image='https://rosaalbaresort.com/wp-content/uploads/2023/10/RAS3-2048x1365.jpg',
                     price=5000000,
                     typeroom_id=1)
        room2 = Room(name='Phòng Premium Deluxe Hướng Biển',
                     description='A DISTINGUISHED YET COMFORTABLE AMBIENCE',
                     image='https://rosaalbaresort.com/wp-content/uploads/2023/10/PDT11-scaled.jpg',
                     price=3000000,
                     typeroom_id=2)
        room3 = Room(name='Phòng Luxury Deluxe Hướng Biển',
                     description='INSPIRE ROMANTIC MEMORIES WITH A TRULY CHARMING RETREAT',
                     image='https://rosaalbaresort.com/wp-content/uploads/2023/10/SD5-2048x1365.jpg',
                     price=2000000,
                     typeroom_id=3)
        room4 = Room(name='Phòng Studio Deluxe Hướng Biển',
                     description='INSPIRE ROMANTIC MEMORIES WITH A TRULY CHARMING RETREAT',
                     image='https://rosaalbaresort.com/wp-content/uploads/2023/10/ST4-2048x1365.jpg',
                     price=1500000,
                     typeroom_id=4)
        room5 = Room(name='Phòng Executive Deluxe Hướng Biển',
                     description='THE TASTEFULLY DECORATED OFFER A HIGH LEVEL OF LUXURY',
                     image='https://rosaalbaresort.com/wp-content/uploads/2023/10/ES3-2048x1365.jpg',
                     price=1000000,
                     typeroom_id=5)
        db.session.add_all([room1, room2, room3, room4, room5])
        db.session.commit()

        # db.create_all()
