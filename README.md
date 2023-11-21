# SMS 2FA Service

## Setup project

Copy `.env.example`, name it `.env`, input your credentials from Vonage.

### To run app in docker:
```shell
make run
```

### To run locally:

- In a separate venv `pip install -r requirements.txt`

#### In terminal

```shell
sh entrypoint.sh
```

## Tests

### `/verify` sends SMS to selected number

```shell
curl -X POST http://127.0.0.1:8000/api/verify \
-H "Content-Type: application/json" \
-d '{"phone": "your number"}'
```

### `/check` confirms whether code sent to the phone is correct

```shell
curl -X POST http://127.0.0.1:8000/api/check \
-H "Content-Type: application/json" \
-d '{"to": "your number", "code": ""}
```

## Things that might be done, but I don't have time for:

1. Add better typing to routers. Each should have right `response_model`. Some models have been written in `vonage_custom/models.py`.
2. Versioning
3. Logging middleware
4. Separate logic in `routers/sms_handler.py` for sending request to Vonage and receiving response. Make views smaller.
5. Add custom HTTP exceptions
6. Tests.
7. All the `TODO:` comments.

## Misc

1. Run `pre-commit install` to automatically run checks before commit.
