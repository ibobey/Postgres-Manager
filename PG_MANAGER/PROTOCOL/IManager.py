import psycopg2.extensions
from typing import Protocol
from typing import NoReturn,List
import psycopg2.extensions


class IManager(Protocol):

    # Database Management

    __connection: psycopg2.extensions.connection
    cursor = psycopg2.extensions.cursor

    # Credentials
    __HOST: str
    __PORT: int
    __DBNAME: str
    __USER: str
    __PASSWORD: str

    # Initialization Methods
    def __set_credentials(self) -> NoReturn:
        ...

    # Class Base Methods
    def __connect_database(self) -> NoReturn:
        ...

    def __close_database_connection(self) -> NoReturn:
        ...

    def commit(self) -> NoReturn:
        ...

    def __create_table_if_not_exists(self) -> NoReturn:
        ...

    def __set_default_timezone(self) -> NoReturn:
        ...

    # Arbitrary Methods

    def insert_into(self, data: list) -> bool:
        ...

    def insert_many_into(self, data: List[list]) -> bool:
        ...

    def query(self) -> None:
        ...

    def fetch_all(self) -> list:
        ...

    def get_last_record(self) -> list:
        ...

    def alter_record(self) -> bool:
        ...

    def delete_record(self) -> bool:
        ...
