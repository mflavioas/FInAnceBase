from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from apps.api.auth import get_current_user

router = APIRouter(tags=["Autenticação"])

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Simula o login retornando um token de acesso.
    Na vida real verificaria credenciais no DB ou Provedor de Identidade.
    """
    if form_data.username == "admin" and form_data.password == "admin":
        return {"access_token": "secret-admin-token", "token_type": "bearer"}
    elif form_data.username == "curator" and form_data.password == "curator":
        return {"access_token": "secret-curator-token", "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password"
        )

@router.get("/users/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user
