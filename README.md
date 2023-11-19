# SMS 2FA Service

### To run app in docker: 
``make run``

### To run locally:

1. In a separate venv `pip install -r requirements.txt`
2. `cd app`
3. `uvicorn main:app --reload --log-config=./logging.yaml`


## Things that might be done, but I don't have time for:

1. Add better typing to routers. Each should have right `response_model`. Some models have been written in `vonage_custom/models.py`.
2. Versioning
3. Logging middleware
4. Separate logic in `routers/sms_handler.py` for sending request to Vonage and receiving response. Make views smaller.
5. Add custom HTTP exceptions
6. Tests.

## Setup project

If you use PyCharm, mark `app` as Source Root for better compatibility.
