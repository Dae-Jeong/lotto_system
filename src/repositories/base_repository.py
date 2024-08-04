from databases import DBManager


class BaseRepository:
    def __init__(self, db_manager: DBManager = DBManager()):
        self.db_manager = db_manager
