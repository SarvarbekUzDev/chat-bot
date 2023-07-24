import sqlalchemy.exc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .db_class import Base, Users


class DataBase():
	engine = create_engine("sqlite:///database.db",echo=True)
	# Base.metadata.create_all(bind=engine)

	Session = sessionmaker(bind=engine)
	session = Session()

	################################ Tabellar
	Users = Users

	def insert(self, cls):
		try:
			self.session.add(cls)
			self.session.commit()
			return cls
		except sqlalchemy.exc.IntegrityError as e: # Unique error
			# print(e)
			return False
		except sqlalchemy.exc.PendingRollbackError as e:
			self.session.rollback()
		finally:
			self.session.close()