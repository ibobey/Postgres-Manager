from PG_MANAGER.PROTOCOL.IManager import *

from PG_MANAGER.QUERY.Queries import CREATE_TABLE_IF_NOT_EXISTS,SET_DEFAULT_TIMEZONE
from PG_MANAGER.QUERY.Queries import INSERT_INTO,GET_LAST_RECORD

import psycopg2.extensions
import psycopg2

from psycopg2 import OperationalError
from psycopg2.errors import UniqueViolation
import psycopg2.errors

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
        self.__connect_database()
        self.__create_table_if_not_exists()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__close_database_connection()

    def __repr__(self):
        return f"A Contex Manager Class : Database {self.__DBNAME}"

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
        try:
            self.__connection = psycopg2.connect(
                host = self.__HOST,
                port = self.__PORT,
                dbname = self.__DBNAME,
                user = self.__USER,
                password = self.__PASSWORD
            )
            self.cursor = self.__connection.cursor()

        except OperationalError as err:
            raise OperationalError("PGM ERR 101")

    def __close_database_connection(self) -> NoReturn:
        try:
            self.cursor.close()
            self.__connection.close()
        except OperationalError:
            raise OperationalError("PGM ERR 102")

    def commit(self) -> NoReturn:
        self.__connection.commit()

    def __create_table_if_not_exists(self) -> NoReturn:
        query = CREATE_TABLE_IF_NOT_EXISTS
        try:
            self.cursor.execute(query=query)
            self.commit()

        except OperationalError:
            raise OperationalError("PGM ERR 104")

    def __set_default_timezone(self) -> NoReturn:
        query = SET_DEFAULT_TIMEZONE
        try:
            self.cursor.execute(query=query)
            self.commit()
        except OperationalError:
            raise OperationalError("PGM ERR 105")

    # Arbitrary Methods

    def insert_into(self, data: list) -> bool:
        query = INSERT_INTO
        try:
            self.cursor.execute(query=query)
            self.commit()
            return True
        except UniqueViolation:
            self.__connection.rollback()
            return False
        except OperationalError:
            raise OperationalError("PGM ERR 106")

    def insert_many_into(self, data: List[list]) -> bool:
        query = INSERT_INTO

        for row in data:
            try:
                self.cursor.execute(query,row)
                self.commit()
            except UniqueViolation:
                continue
            except Exception:
                raise Exception("PGM ERR 107")
        return True

    def query(self, query: str) -> None:
        try:
            self.cursor.execute(query)
        except OperationalError:
            raise OperationalError("PGM ERR 108")

    def fetch_all(self) -> list:
        return self.cursor.fetchall()

    def get_last_record(self) -> list:
        query = GET_LAST_RECORD
        try:
            self.cursor.execute(query)
            last_record = self.cursor.fetchall()
            return last_record

        except OperationalError:
            raise OperationalError("PGM ERR 110")



