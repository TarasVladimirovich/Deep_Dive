import yaml
import pprint

def load_yaml(path):
    """Parse a yaml file and return it as a Python object."""
    with open(path) as f:
        return yaml.safe_load(f)


q = load_yaml('my.yml')

pprint.pprint(q)
