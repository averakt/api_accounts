import os

import pytest
import subprocess


# This sets `os.environ`,
# If we placed it below the application import, it would raise an error
# informing us that 'TESTING' had already been read from the environment.
os.environ['TESTING'] = 'True'

from alembic import command
from alembic.config import Config
from app.models import database
from sqlalchemy_utils import create_database, drop_database
from sqlalchemy import create_engine
from sqlalchemy import text


@pytest.fixture(scope="module")
def temp_db():
    """ Create new DB for tests """
    create_database(database.TEST_SQLALCHEMY_DATABASE_URL)
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    alembic_cfg = Config(os.path.join(base_dir, "alembic.ini"))
    command.upgrade(alembic_cfg, "head")

    # В тестовую базу вставляем данные о допустимых валютах
    engine = create_engine(database.TEST_SQLALCHEMY_DATABASE_URL, echo=True)
    with engine.connect() as con:
        with open("fund.sql") as file:
            query = text(file.read())
            con.execute(query)

    try:
        yield database.TEST_SQLALCHEMY_DATABASE_URL
    finally:
        drop_database(database.TEST_SQLALCHEMY_DATABASE_URL)
