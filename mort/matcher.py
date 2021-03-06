import json
from typing import Dict, List

from mort.file_utils import get_absolute_path
from mort.local_conf import TARGET_LIST_FILE_PATH


def target_matches(pattern: Dict, target: Dict) -> bool:
    """
    Whether the `target` target_matches the `pattern`, which means that

    * all the keys in `pattern` should also exists in `target`
    * the value for the patterns can also be found in the target.

    All target_matches are case insensitive.

    :param target: A `target` unit
    :param pattern: The matching pattern
    :return: True if the target target_matches the pattern
    """
    if not set(pattern.keys()).issubset(set(target.keys())):
        return False
    for (key, substr) in pattern.items():
        if not target[key] or substr.lower() not in target[key].lower():
            return False
    return True


def get_targets(pattern: Dict) -> List[Dict]:
    """
    Return all the targets that target_matches the pattern from the local target list.

    :param pattern: A matching pattern
    :param from_file: Location to the target list file we are loading all the targets from
    :return: List of all targets
    """
    return [target for target in
            json.loads(open(get_absolute_path(TARGET_LIST_FILE_PATH)).read()) if target_matches(pattern, target)]
