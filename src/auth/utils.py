from passlib.context import CryptContext

password_context = CryptContext(
    schemes = ['bcrypt']
)

def generate_password_hash(password: str):
    hash = password_context.hash(password)
    return hash

def verify_password(password:str, hash:str):
    return password_context.verify(password, hash)