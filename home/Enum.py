import enum


class Type(enum.Enum):
    Home = 'Home page'
    News = 'News page'
    Learn = 'Learn page'


class Status(enum.Enum):
    Seccess = "Seccess"
    Error = "ERROR"