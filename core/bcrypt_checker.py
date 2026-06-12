import bcrypt

def hash_password(password: str) -> bytes:
    """
    Gera um hash bcrypt a partir de uma senha em texto plano.
    O bcrypt.gensalt() cria um salt aleatório automaticamente.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def verify_password(password: str, hashed_password: bytes) -> bool:
    """
    Verifica se a senha em texto plano corresponde ao hash bcrypt.
    O bcrypt.checkpw extrai o salt do próprio hash para fazer a comparação.
    """
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
    except ValueError:
        return False
