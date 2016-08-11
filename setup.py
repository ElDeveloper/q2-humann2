from setuptools import setup, find_packages
import re
import ast

# version parsing from __init__ pulled from Flask's setup.py
# https://github.com/mitsuhiko/flask/blob/master/setup.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('q2_humann2/__init__.py', 'rb') as f:
    hit = _version_re.search(f.read().decode('utf-8')).group(1)
    version = str(ast.literal_eval(hit))

setup(
    name="q2-humann2",
    version=version,
    packages=find_packages(),
    # pandas and q2-dummy-types are only required for the dummy methods and
    # visualizers provided as examples. Remove these dependencies when you're
    # ready to develop your plugin, and add your own dependencies (if there are
    # any).
    install_requires=['qiime >= 2.0.0', 'pandas', 'q2-dummy-types'],
    author="QIIME Development Team",
    author_email="yoshiki@ucsd.edu",
    description="HUMAnN is a pipeline for efficiently and accurately profiling the presence/absence and abundance of microbial pathways in a community from metagenomic or metatranscriptomic sequencing data (typically millions of short DNA/RNA reads).",
    entry_points={
        "qiime.plugins":
        ["q2-humann2=q2_humann2.plugin_setup:plugin"]
    }
)
