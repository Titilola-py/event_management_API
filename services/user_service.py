from typing import Dict, List, Optional
from schemas.user_schema import User, UserCreate, UserUpdate

users_db: Dict[int, User] = {}
user_id_counter = 1

def create_user(user_data: UserCreate) -> User:
    global user_id_counter

    for existing_user in users_db.values():
        if existing_user.email == user_data.email:
            raise ValueError("Email already exists")
        
    user = User(
        id=user_id_counter,
        name=user_data.name
        email=user_data.email,
        is_active=True
    )    
    users_db[user_id_counter] = user
    user_id_counter += 1
    return user

def get_user(user_id: int) -> Optional[User]:
    return users_db.get(user_id)

def get_all_users() -> List[User]:
    return list(users_db.values())

def update_user(user_id: int, user_data: UserUpdate) -> Optional[User]:
    if user_id not in users_db:
        return None
    
    user = users_db[user_id]
    update_data = user_data.model_dump(exclude_unset=True)

    if "email" in update_data:
        for uid, exixting_user in users_db.items():
            if uid != user_id and exixting_user.email == update_data["email"]:
                raise ValueError("Email already exists")
            
    for field, value in update_data.items():
        setattr(user, field, value)

    return user 

def delete_user(user_id: int) -> bool:
    if user_id in users_db:
        del users_db[user_id]
        return True
    return False

def deactivate_user(user_id: int) -> Optional[User]:
    if user_id not in users_db:
        return None

    users_db[user_id].is_active = False
    return users_db[user_id]
          