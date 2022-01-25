import configparser
import os


class Config(configparser.ConfigParser):
    """
    artefacts configuration
    """

    config_filename = 'pyproject.toml'
    config_abspath = os.path.abspath(os.getcwd())
    config_filepath = os.path.join(config_abspath, config_filename)

    @classmethod
    def load(cls):
        conf = cls()
        conf.read(cls.config_filepath)
        return conf

    def __init__(self):
        super().__init__(default_section='artefacts')


