class TryThisThen(object):
    """
    Will this get documented? It will if I add module.bar to hack.rst.
    """
    pass


def safe_json(obj):
    """
    >>> L = safe_json(set(["a", "b", "c"]))
    >>> isinstance(L, list)
    True
    >>> set(L) == set(["a", "b", "c"])
    True
    """
    # Python sets are not JSONable. Convert them to lists.
    if isinstance(obj, set):
        return [safe_json(x) for x in obj]
    elif isinstance(obj, dict):
        return dict([(key, safe_json(obj.get(key))) for key in obj])
    else:
        return obj
