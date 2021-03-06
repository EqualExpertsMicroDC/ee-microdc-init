import yaml
from collections import OrderedDict


def check_config(expected_items, configyaml):
    for item in expected_items:
        if item not in configyaml:
            print('\nERR: \'{}\' missing from config\n'.format(item))
            return False

    return True


def readyaml(filename):
    try:
        file = open(filename)
        yamldict = ordered_load(file, yaml.SafeLoader)
        file.close()
        return yamldict
    except(IOError, ImportError):
        raise


def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)
