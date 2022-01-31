from artefacts.core import Manifest


def models():
    result = []
    manifest = Manifest.load()
    for k,v in manifest.nodes.items():
        if v.resource_type == 'model':
            result.append(v)
    else:
        return result


def tests():
    result = []
    manifest = Manifest.load()
    for k,v in manifest.nodes.items():
        if v.resource_type == 'test':
            result.append(v)
    else:
        return result
