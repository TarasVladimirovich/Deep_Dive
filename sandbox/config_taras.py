from pathlib import Path

import yaml

CONFIG_DIR = Path(__file__).parent  # type: Path
CONFIG_FILE = 'config.yaml'
CONFIG_LOCAL_FILE = 'config_local.yaml'
DEVICES_DIR = Path(__file__).parents[1] / 'devices'
DEVICES_FILES = 'devices*.yaml'


class AttrDict(dict):
    """Recursively provides access to all dictionary items via attributes."""

    def _getitem(self, key):
        result = super(AttrDict, self).__getitem__(key)
        if isinstance(result, dict):
            return AttrDict(result)
        else:
            return result

    __getitem__ = __getattr__ = _getitem


def load_yaml(path: Path):
    """Parse a yaml file and return it as a Python object."""
    with open(path) as f:
        return yaml.safe_load(f)


def get_config():
    config = AttrDict()
    config.update(load_yaml(CONFIG_DIR / CONFIG_FILE))
    config['devices'] = {k: v for d in DEVICES_DIR.rglob(DEVICES_FILES)
                         for k, v in load_yaml(d).items()}
    config['devices_features'] = 'DEVICE_FEATURES'

    # Load local config if exists.
    config_local = CONFIG_DIR / CONFIG_LOCAL_FILE
    if config_local.exists():
        config.update(load_yaml(config_local))

    return config
