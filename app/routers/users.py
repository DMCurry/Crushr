from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("")
async def get_user():
    return [{"name": "dylan"}, {"name": "patricia"}]



@router.post("")
async def create_user(request):
    new_user = request
    return new_user