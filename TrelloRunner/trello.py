""""""

from typing import Optional, Dict
from TrelloRunner.common import *
from TrelloRunner import config
import requests


class Trello:
    base_url = "https://api.trello.com/1/"

    def __init__(self, auth: AuthData) -> None:
        """"""
        self.auth = auth
        self.is_authenticated = self.test_authenticated()

    def test_authenticated(self) -> bool:
        resp = self._authenticated_api_call("GET", f"/members/me/tokens")
        return resp.ok

    def _authenticated_api_call(self, method: str, endpoint: str, data: Dict = {}, params: Dict = {}) -> requests.Response:
        # Insert auth data into params variable
        auth_params = {"key": self.auth.key, "token": self.auth.token}
        params = dict(params, **auth_params)

        # Make the call
        resp = Trello._make_api_call(method=method, endpoint=endpoint, params=params, data=data)
        return resp

    @staticmethod
    def _make_api_call(method: str, endpoint: str, **kwargs) -> requests.Response:
        """Helper function to send an API call to trello. Simply wraps an endpoint in the base url.

        :param method: GET, POST, PUT, DELETE
        :param endpoint: The api resource location minus base url
        :param kwargs: Any params to pass to the request
        :return: A requests response object
        """

        resp = requests.request(method=method, url=Trello.base_url+endpoint, **kwargs)

        return resp

