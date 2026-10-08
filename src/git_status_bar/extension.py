from __future__ import annotations

import typing

from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


class GitStatusBar(Extension):
    """Git branch, ahead/behind count, and dirty status in statusbar"""

    def __init__(self, api: "ExtensionsAPI") -> None:
        super().__init__(api)
        self.api = api
        self.api.logger.info("Git Status Bar extension initialised.")

    def install(self) -> None:
        """Run when extension is loaded."""
        self.api.logger.info("Git Status Bar installed successfully.")
