import sys
import re


class version_compare:
    """Compare the current compiling version Python against a benchmark to determine which code to use"""

    def __init__(self):
        self._current_version = sys.version.split(' ')[0]

    def current_version_greater_than_or_equal_than(self, compare_version):
        def normalize(version_info):
            return [
                int(version_component)
                for version_component
                in re.sub(
                    r'(\.0+)*$', '', version_info).split(".")
            ]

        return normalize(self._current_version) >= normalize(compare_version)
