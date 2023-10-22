import sqlalchemy
from .users import users_table
from datetime import datetime, timedelta

metadata = sqlalchemy.MetaData()

funds_table = sqlalchemy.Table(
    "funds",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("brief", sqlalchemy.String(3), unique=True, index=True),
    sqlalchemy.Column("name", sqlalchemy.String(20)),
    sqlalchemy.Column("code", sqlalchemy.String(3), unique=True, index=True),
)


account_table = sqlalchemy.Table(
    "resource",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("brief", sqlalchemy.String(20), unique=True),
    sqlalchemy.Column("name", sqlalchemy.String(255)),
    sqlalchemy.Column("fund_id", sqlalchemy.ForeignKey("funds.id")),
    sqlalchemy.Column("dateStart", sqlalchemy.DateTime(), default=datetime.now().utcnow(), nullable=False),
    sqlalchemy.Column("dateEnd", sqlalchemy.DateTime(), default="19000101", nullable=False),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey(users_table.c.id)),
)

