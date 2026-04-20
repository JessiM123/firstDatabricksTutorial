import base64
def encode_base64(value):
    creds_bytes = value.encode('ascii')
    base64_bytes = base64.b64encode(creds_bytes)
    return base64_bytes.decode('ascii')