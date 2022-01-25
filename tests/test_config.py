from artefacts.config import Config


def test_config_loads():
    conf = Config.load()
    assert conf['artefacts']['test'] == '1'
