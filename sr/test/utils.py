def generate_data(data, exclude=[], update={}):
    _data = data.copy()
    if exclude:
        _data = {
            key: _data[key]
            for key in _data.keys()
            if key not in exclude
        }
    if update:
        _data.update(update)
    return _data
