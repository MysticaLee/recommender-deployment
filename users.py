import jwt, os, re

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model

JWT_SECRET = os.environ["JWT_SECRET"]
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(Model):  # DB Model
    id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
    password_hash = fields.CharField(128)

    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)


# router Models
User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic = pydantic_model_creator(
    User, name="UserIn", exclude_readonly=True
)  # User input


async def authenticate_user(username: str, password: str):
    # Check if user exists & if password is correct
    user = await User.get(username=username)
    if not user:  # User does not exist
        return False
    if not user.verify_password(password):  # Wrong password
        return False
    return user


async def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )


@router.post("/token")
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    user_obj = {
        "sub": f"user{user.id}",
        "name": re.sub(r"[\W_]", "", user.username).title(),
    }

    token = jwt.encode(user_obj, JWT_SECRET)

    return {"access_token": token, "token_type": "bearer"}


@router.post(
    "/create-user", response_model=User_Pydantic, dependencies=[Depends(verify_token)]
)
async def create_user(user: UserIn_Pydantic):
    user_obj = User(
        username=user.username, password_hash=bcrypt.hash(user.password_hash)
    )
    await user_obj.save()
    return await User_Pydantic.from_tortoise_orm(
        user_obj
    )  # convert tortoise orm obj into User_Pydantic object
