# FakeAPI
A REST API that returns fake test data in a customizable shape.

Data can be POST-ed in any shape, with `{ "fakeapi_item": true, "type": "$" }` blocks to be replaced by the specified `type`.

Use `count` to create an array of the specified type.

The bulk of this is powered by Faker.

## Examples

### Flat JSON
```bash
$ curl -X POST -H "Content-Type: application/json" -d '{
    "name": {
        "fakeapi_item": true,
        "type": "name"
    },
    "number": {
        "fakeapi_item": true,
        "type": "number",
        "min": 30, # Optional parameter
        "max": 300 # Optional parameter
    }
}'  "http://127.0.0.1:5000/data"
```

```json
{
  "name": "Stephen Thomas",
  "number": 105
}
```

### Nested JSON
```shell
$ curl -X POST -H "Content-Type: application/json" -d '{
    "nested_data": {
        "fake_name": {
            "fakeapi_item": true,
            "type": "name"
        },
        "fake_username": {
            "fakeapi_item": true,
            "type": "username"
        },
        "fake_password": {
            "fakeapi_item": true,
            "type": "password"
        },
        "more_nested_data": {
            "status": "OK",
            "metadata": {
                "test": true,
                "fake_data": {
                    "fake_number": {
                        "fakeapi_item": true,
                        "type": "number",
                        "min": 10,
                        "max": 60
                    },
                    "fake_email": {
                        "fakeapi_item": true,
                        "type": "email"
                    }
                }
            }
        }
    }
}'  "http://127.0.0.1:5000/data"
```

```json
{
  "nested_data": {
    "fake_name": "Kristen Williams",
    "fake_password": "uCfJMjPFNycu",
    "fake_username": "amywilson",
    "more_nested_data": {
      "metadata": {
        "fake_data": {
          "fake_email": "hector86@example.org",
          "fake_number": 23
        },
        "test": true
      },
      "status": "OK"
    }
  }
}
```

### Creating an array with `count`
```shell
$ curl -X POST -H "Content-Type: application/json" -d '{
    "names": {
        "fakeapi_item": true,
        "type": "name",
        "count": 3
    }
}'  "http://127.0.0.1:5000/data"
```

```json
{
  "names": [
    "Casey Reed",
    "Travis Butler III",
    "Kelly Greene"
  ]
}
```

## Types (and Parameters)
- **boolean** -> boolean
- **city** -> string
- **country** -> string
- **country_code** -> string
- **date** -> string
- **domain_name** -> string
  - **subdomains**: integer (default 0)
- **full_address** -> string
- **image_url** -> string
  - **height**: integer (default 480)
  - **width**: integer (default 640)
- **ipv4** -> string
- **length** -> integer (default 12)
- **max** -> integer (default 100)
- **min** -> integer (default 0)
- **name** -> string (eg "Tyler Sanders")
- **number** -> integer
- **password** -> string (eg "kyphIAcGZiPB")
  - **length**: integer (default 12)
- **slug** -> string
- **street_address** -> string (eg "34003 Mcdonald Inlet Apt. 374")
- **text** -> string
  - **sentences**: integer (default 1)
- **time** -> string
- **username** -> string (eg "tsanders")