from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Optional

# Simulando um esquema de OAuth2 simples
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Função de dependência para validar tokens.
    Num cenário real, decodificaria o JWT e buscaria no banco de dados.
    Aqui apenas validamos se o token não é falso.
    """
    if token == "fake-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Retornaria o model User
    return {"username": "admin", "role": "admin"}

def verify_admin_role(current_user: dict = Depends(get_current_user)):
    """
    Validador de RBAC básico
    """
    if current_user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Operation not permitted"
        )
    return current_user
