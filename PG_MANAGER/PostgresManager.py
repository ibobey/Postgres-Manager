from PG_MANAGER.PROTOCOL.IManager import *

import psycopg2.extensions
import psycopg2

from psycopg2 import OperationalError
from psycopg2.errors import UniqueViolation, InFailedSqlTransaction
from psycopg2.errors import InvalidDatetimeFormat, InvalidTextRepresentation

from dotenv import load_dotenv
from os import getenv


class PostgresManager(IManager):

    # Database Management

    __connection: psycopg2.extensions.connection
    cursor = psycopg2.extensions.cursor

    # Credentials
    __HOST: str
    __PORT: int
    __DBNAME: str
    __USER: str
    __PASSWORD: str

    def __init__(self):
        self.__set_credentials()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __repr__(self):
        pass

    # Initialization Methods
    def __set_credentials(self) -> NoReturn:
        if load_dotenv(r"PG_MANAGER/CREDENTIALS/pg.env") is None:
            raise FileNotFoundError("Credentials Cannot Found")

        self.__HOST = getenv("HOST")
        self.__PORT = int(getenv("PORT"))
        self.__DBNAME = getenv("DBNAME")
        self.__USER = getenv("USER")
        self.__PASSWORD = getenv("PASSWORD")

    # Class Base Methods
    def __connect_database(self) -> NoReturn:
        pass

    def __close_database_connection(self) -> NoReturn:
        pass

    def commit(self) -> NoReturn:
        pass

    def __create_table_if_not_exists(self) -> NoReturn:
        pass

    def __set_database_default_timezone(self) -> NoReturn:
        pass

    # Arbitrary Methods

    def insert_into(self, data: list) -> bool:
        pass

    def insert_many_into(self, data: List[list]) -> bool:
        pass

    def query(self) -> None:
        pass

    def fetch_all(self) -> list:
        pass

    def get_last_record(self) -> list:
        pass

    def alter_record(self) -> bool:
        pass

    def delete_record(self) -> bool:
        pass
