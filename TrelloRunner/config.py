from .common import *
import yaml


def get_auth(filename: str) -> AuthData:
    with open(filename, 'r') as f:
        conf = yaml.load(f)

    return AuthData(conf.get("key"), conf.get("token"))