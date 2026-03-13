# Stub so "import otter" works in XeusLite (browser). Real grading runs on Binder/CodeSpaces.
# See: https://github.com/ucbds-infra/otter-grader

class Notebook:
    """Minimal stub for otter.Notebook so notebooks don't crash in the browser."""

    def __init__(self, path):
        self._path = path

    def check(self, question_id=None):
        pass  # No-op in browser

    def check_all(self):
        pass  # No-op in browser

    def export(self, *args, **kwargs):
        print("Export is not available in the browser. Use Binder or CodeSpaces to export.")
