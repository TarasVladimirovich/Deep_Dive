from os import getenv
from pathlib import Path

import yaml


class TopologyInstantiator:

    def __init__(self, *, env=None, path=None):
        self.env = env
        self._path = path
        self._topology = None

    @property
    def topology(self):
        if self._topology is None:
            topology = AttrDict()
            path = self._path if self._path is not None else getenv(self.env)
            topology.update(load_yaml(path))
            self._topology = topology
        return self._topology

    @property
    def controller_ip(self):
        return self.topology.inventory.controller.ip


class AttrDict(dict):
    """Recursively provides access to all dictionary items via attributes."""

    def _getitem(self, key):
        result = super(AttrDict, self).__getitem__(key)
        if isinstance(result, dict):
            return AttrDict(result)
        if isinstance(result, list):
            return [AttrDict(i) for i in result]
        else:
            return result

    __getitem__ = __getattr__ = _getitem


def load_yaml(path: Path):
    """Parse a yaml file and return it as a Python object."""
    with open(path) as f:
        return yaml.safe_load(f)


topology = TopologyInstantiator(path='topology_example.yaml')



print(topology.topology)

d = {}