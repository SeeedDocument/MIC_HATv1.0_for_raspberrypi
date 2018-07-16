import json
import uuid
import wave
import io
import os
import types
import requests

from monotonic import monotonic

class BaiduVoiceApi:

    def __init__(self,appkey=os.getenv('APP_KEY', ''),secretkey=os.getenv('SECRET_KEY', '')):

        self.client_id = appkey

        self.client_secret = secretkey

        self.access_token = None

        self.expire_time = None

        self.session = requests.Session()

    def auth(self):

        if self.expire_time is None or monotonic() > self.expire_time:

            credential_url = "https://openapi.baidu.com/oauth/2.0/token"

            headers = {"Content-Type": "application/json"}

            params = {
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret":self.client_secret
            }

            start_time = monotonic()

            response = self.session.post(credential_url, headers=headers, params=params)

            if response.status_code != 200:
                raise IOError("http request error with status code {}".format(response.status_code))

            access_token = response.json()

            self.access_token = access_token['access_token']

            expiry_seconds = 7200

            self.expire_time = start_time + expiry_seconds

    def server_api(self,audio_data):

        self.auth()

        if isinstance(audio_data, types.GeneratorType):
            def generate(audio):
                yield self.get_wav_header()
                for a in audio:
                    yield a

            data = generate(audio_data)
        else:
            data = self.to_wav(audio_data)

        headers = {
            "Content-Type": "audio/wav;rate=16000",
        }

        url = "http://vop.baidu.com/server_api?lan=zh&cuid=HG:er:rt:7f:eD&token=" + self.access_token
        response = self.session.post(url,headers=headers, data=data)

        if response.status_code != 200:
            raise IOError("http request error with status code {}".format(response.status_code))

        result = response.content

        return result

    @staticmethod
    def to_wav(raw_data):
        # generate the WAV file contents
        with io.BytesIO() as wav_file:
            wav_writer = wave.open(wav_file, "wb")
            try:  # note that we can't use context manager, since that was only added in Python 3.4
                wav_writer.setframerate(16000)
                wav_writer.setsampwidth(2)
                wav_writer.setnchannels(1)
                wav_writer.writeframes(raw_data)
                wav_data = wav_file.getvalue()
            finally:  # make sure resources are cleaned up
                wav_writer.close()
        return wav_data


    @staticmethod
    def get_wav_header():
        # generate the WAV header
        with io.BytesIO() as f:
            w = wave.open(f, "wb")
            try:
                w.setframerate(16000)
                w.setsampwidth(2)
                w.setnchannels(1)
                w.writeframes('')
                header = f.getvalue()
            finally:
                w.close()
        return header

    def main():
        import timeit
        import logging
        logging.basicConfig(level=logging.DEBUG)
        Baidu = BaiduVoiceApi()

    if __name__ == '__main__':
        main()
