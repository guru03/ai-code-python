# common_utils/sorting.py
from natsort import natsorted

def natural_sort(queryset, field=None, fields=None, reverse=False):
    objs = list(queryset)

    # normalize to a list of fields
    if fields is None:
        fields = [field] if field else ["serial_number"]

    def sort_key(obj):
        return tuple(getattr(obj, f) for f in fields)

    return natsorted(objs, key=sort_key, reverse=reverse)
