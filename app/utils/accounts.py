from datetime import datetime

from app.models.database import database
from app.models.accounts import account_table
from app.models.users import users_table
from app.schemas import accounts as account_schema
from sqlalchemy import desc, func, select
from datetime import datetime, timedelta


async def create_account(account: account_schema.AccountBase):
    query = (
        account_table.insert()
        .values(
            brief=account.brief,
            name=account.name,
            fund_id=account.fund_id,
            dateStart=datetime.now().utcnow(),
            dateEnd=datetime.strptime('1900-01-01 00:00:00.000000', '%Y-%m-%d %H:%M:%S.%f'),
            user_id=account.user_id
        )
        .returning(
            account_table.c.id,
            account_table.c.brief,
            account_table.c.name,
            account_table.c.fund_id,
            account_table.c.dateStart,
            account_table.c.dateEnd,
            account_table.c.user_id,
        )
    )
    account = await database.fetch_one(query)

    # Convert to dict and add user_name key to it
    account = dict(zip(account, account.values()))
    # account["user_name"] = user["name"]
    return account


async def get_account(account_id: int, current_user):
    query = (
        select(
            [
                account_table.c.id,
                account_table.c.brief,
                account_table.c.name,
                account_table.c.fund_id,
                account_table.c.dateStart,
                account_table.c.dateEnd,
                account_table.c.user_id,
            ]
        )
        # .select_from(account_table.join(users_table))
        .select_from(account_table)
        .where(account_table.c.id == account_id)
    )
    return await database.fetch_one(query)


# async def get_posts(page: int):
#     max_per_page = 10
#     offset1 = (page - 1) * max_per_page
#     query = (
#         select(
#             [
#                 account_table.c.id,
#                 account_table.c.created_at,
#                 account_table.c.title,
#                 account_table.c.content,
#                 account_table.c.user_id,
#                 users_table.c.name.label("user_name"),
#             ]
#         )
#         .select_from(account_table.join(users_table))
#         .order_by(desc(account_table.c.created_at))
#         .limit(max_per_page)
#         .offset(offset1)
#     )
#     return await database.fetch_all(query)
#
#
# async def get_posts_count():
#     query = select([func.count()]).select_from(account_table)
#     return await database.fetch_val(query)


async def update_account(account_id: int, account: account_schema.AccountBase, current_user):
    query = (
        account_table.update()
        .where(account_table.c.id == account_id)
        .values(brief=account.brief, name=account.name, dateStart=account.dateStart, dateEnd=account.dateEnd)
    )
    return await database.execute(query)


async def delete_account(account_id: int, current_user):
    # query_token_del = tokens_table.delete().where(tokens_table.c.user_id == user_id)
    # await database.execute(query_token_del)

    query = account_table.delete().where(account_table.c.id == account_id)
    return await database.fetch_one(query)
