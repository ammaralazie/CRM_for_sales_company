import uuid

def slugid():
    x=str(uuid.uuid4)[:9].replace('_','').lower()
    return x

def order_Number():
    return str(uuid.uuid4)[:9].replace('_','').lower()