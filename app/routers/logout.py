from fastapi import APIRouter, Response, status

router = APIRouter(prefix="/logout", tags=["logout"])

@router.post("", status_code=status.HTTP_204_NO_CONTENT)
async def logout(response: Response):
    """
    Clears the JWT cookie to log out the user.
    """
    response.delete_cookie(key="access_token", path="/", httponly=True)
    return {"message": "Logged out successfully"}