import uuid

def get_code():
    code = str(uuid.uuid4)[:11].replace("-","")
    print(code)

get_code()