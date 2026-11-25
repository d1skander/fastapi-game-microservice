from fastapi import APIRouter


router = APIRouter(prefix="/users", tags=["Пользователи"])

#Регистрация
@router.post("/user")
def registration_user(shema: None,
                      db: None):
    pass

#Отдать данные пользователя
@router.get("/user")
def get_user(current: None):
    pass

#Авторизация
@router.post("/auth")
def authentication_user(form_data: None,
                        db: None):
    pass