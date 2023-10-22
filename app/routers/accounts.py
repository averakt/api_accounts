# from app.schemas.posts import PostDetailsModel, PostModel
from app.schemas.accounts import Account, AccountBase, AccountCreate
from app.schemas.users import User
# from app.utils import posts as post_utils
from app.utils import accounts as account_utils
from app.utils.dependencies import get_current_user
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas import users

router = APIRouter()


@router.get("/accounts")
async def health_check():
    return {"Hello": "World"}


@router.post("/accounts", response_model=AccountBase, status_code=201)
async def create_account(account: AccountCreate, current_user=Depends(get_current_user)):
    account = await account_utils.create_account(account)
    return account

#
# @router.get("/posts")
# async def get_posts(page: int = 1):
#     total_cout = await post_utils.get_posts_count()
#     posts = await post_utils.get_posts(page)
#     return {"total_count": total_cout, "results": posts}
#
#


@router.get("/accounts/{account_id}", response_model=AccountBase)
async def get_account(account_id: int, current_user: users.User = Depends(get_current_user)):
    return await account_utils.get_account(account_id, current_user)


@router.put("/accounts/{account_id}", response_model=AccountBase)
async def update_account(
    account_id: int, account_data: AccountBase, current_user: users.User = Depends(get_current_user)
):
    account = await account_utils.get_account(account_id, current_user)
    # print(account)

    await account_utils.update_account(account_id=account_id, account=account_data, current_user=current_user)
    return await account_utils.get_account(account_id, current_user)


@router.delete("/accounts/{account_id}", status_code=204)
async def delete_account(account_id: int, current_user: users.User = Depends(get_current_user)):
    await account_utils.delete_account(account_id, current_user)
    # return {"204": "OK"}
