# Handle errors
import json

def failedParseType():
    return json.dumps({
    "type": "error",
    "code": "404",
    "data": {
            "message": "Invalid type"
        }
    })

def ok():
    return json.dumps({
    "type": "ok",
    "code": "200",
    "data": {
            "message": "OK"
        }
    })

def failedJsonWrite():
    return json.dumps({
    "type": "error",
    "code": "500",
    "data": {
            "message": "Failed to write JSON config file"
        }
    })

