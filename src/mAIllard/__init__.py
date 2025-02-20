"""Python Package mAIllard"""

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version

__all__ = [
    "__version__",
]

# Official PEP 396
try:
    __version__ = version("fastmindapi")
except PackageNotFoundError:
    __version__ = "unknown version"