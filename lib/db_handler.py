import json
from typing import TextIO, Any

from python_multipart.decoders import SupportsWrite

from lib import customExceptions

db_loaded: bool = False


class Database:
    def __init__(self, db_name: str, db_path: str, db_type: str) -> None:
        self.db_name: str = db_name
        self.db_path: str = db_path
        self.db_type: str = db_type


def load_db(db: Database, encoding: str = "utf-8") -> dict:
    global db_loaded
    if db.db_type == 'json':
        data: dict = {"db_name": db.db_name, "db_path": db.db_path, "db_type": db.db_type}
        file: TextIO = open(db.db_path, 'r', encoding=encoding)
        data.update(json.load(file))
        file.close()
    else:
        raise customExceptions.UnsupportedArgumentException(f'Unsupported Argument {db.db_type} used...')
    db_loaded = True
    return data


def get_db_data(db: Database) -> Any:
    if not db_loaded:
        load_db(db)
    # ToDo: Implement actual loading functionality


def update_db_data(db: Database, data: Any, encoding: str = "utf-8") -> bool:
    operation_successful: bool = False
    if db.db_type == 'json':
        try:
            file: TextIO | SupportsWrite[str] = open(db.db_path, 'w', encoding=encoding)
            db_data: dict = json.load(file)
            db_data.update(data)
            json.dump(db_data, file)
            file.close()
            operation_successful = True
        except FileNotFoundError:
            pass
        except KeyError:
            pass
        except ValueError:
            pass
        else:
            operation_successful = True
    return operation_successful
