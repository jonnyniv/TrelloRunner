from TrelloRunner.common import AuthData
import yaml


def get_auth(filename: str) -> AuthData:
    """Retrieves the authentication data from the config file

    :param filename: A string containing the path to the config file
    :return: A named tuple containing the api key and token if supplied in a file
    """
    with open(filename, 'r') as f:
        conf = yaml.load(f)

    return AuthData(conf.get("key"), conf.get("token"))
