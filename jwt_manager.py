from jwt import encode, decode

def created_token(data, secreto="1234567890"):
    token = encode(playload=data, key=secreto, algorithm="HS256")
    return token

def validate_token(token):
    data = decode(token, "1234567890", algorithms={"HS256"})
    return data 