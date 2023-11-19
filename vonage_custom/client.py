import base64
import httpx

from configs import API_KEY, API_SECRET


class ClientV2:
    def __init__(self):
        self.base_url = "https://api.nexmo.com/v2"
        self._api_key = API_KEY
        self._secret_key = API_SECRET
        self.signature = self._sign()

    def _sign(self):
        key = self._api_key + ":" + self._secret_key
        signature = base64.b64encode(key.encode("utf-8")).decode("ascii")
        return f"Basic {signature}"

    async def _post(self, url, params):
        headers = {"Authorization": self._sign()}
        async with httpx.AsyncClient(verify=False) as client:  # TODO: verify=True fix
            response = await client.post(url, json=params, headers=headers)
        return response

    async def send_message(self, data):
        url = f"{self.base_url}/verify/"
        response = await self._post(url, data)
        return response

    async def verify_message(self, request_id, code):
        url = f"{self.base_url}/verify/{request_id}"
        data = {"code": code}
        response = await self._post(url, data)
        return response
