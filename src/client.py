# https://github.com/pylast/pylast/blob/main/tests/test_user.py

import os
import httpx
import asyncio
import requests
import pylast
from datetime import datetime, timedelta, date

class LastFmClient():
    def __init__(self):
        self.api_key = os.environ.get("API_KEY")
        self.api_secret = os.environ.get("API_SECRET")
        self.account = os.environ.get("API_ACCOUNT")
        self.password = os.environ.get("ACCOUNT_PASS")

    def get_client(self):

        hashed_pass = pylast.md5(self.password)

        client = pylast.LastFMNetwork(
            api_key=self.api_key,
            api_secret=self.api_secret,
            username=self.account,
            password_hash=hashed_pass,
        )

        user = client.get_user(self.account)

        from_date, to_date = user.get_weekly_chart_dates()[0]

        scrobble_list = user.get_weekly_track_charts(from_date, to_date)
        print(scrobble_list)
        # artist = client.search_for_artist('slayer')
        # artist_list = artist.get_next_page()
        # print(artist_list[0].info)
        # for band in artist_list:
            # print(band)
        # response = requests.get(self.auth_url)
        # print(self.auth_url)


LastFmClient().get_client()