# FakeAPI
A REST API that returns fake test data in a customizable shape.

Data can be POST-ed in any shape, with `{ "fakeapi_item": true }` blocks to be replaced by the specified `type`.

## Examples

**Flat JSON:** 
```
$ curl -X POST -H "Content-Type: application/json" -d '{
    "name": {
        "fakeapi_item": true,
        "type": "name"
    },
    "number": {
        "fakeapi_item": true,
        "type": "number",
        "min": 30,
        "max": 300
    }
}'  "http://127.0.0.1:5000/data"


{
  "name": "Stephen Thomas",
  "number": 105
}
```

**Nested JSON:**
```
$ curl -X POST -H "Content-Type: application/json" -d '{
    "data": {
        "name": {
            "fakeapi_item": true,
            "type": "name"
        },
        "username": {
            "fakeapi_item": true,
            "type": "username"
        },
        "password": {
            "fakeapi_item": true,
            "type": "password"
        },
        "immutable_data": {
            "status": "OK",
            "metadata": {
                "test": true,
                "mutable": {
                    "number": {
                        "fakeapi_item": true,
                        "type": "number",
                        "min": 10,
                        "max": 60
                    },
                    "email": {
                        "fakeapi_item": true,
                        "type": "email"
                    }
                }
            }
        }
    }
}'  "http://127.0.0.1:5000/data"


{
  "data": {
    "immutable_data": {
      "metadata": {
        "mutable": {
          "email": "tylersanders@gmail.com",
          "number": 57
        },
        "test": true
      },
      "status": "OK"
    },
    "name": "Tyler Sanders",
    "password": "kyphIAcGZiPB",
    "username": "tylersanders"
  }
}
```