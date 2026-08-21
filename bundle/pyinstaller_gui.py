#!/usr/bin/env python3

# Allow direct execution
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyInstaller.__main__ import run as run_pyinstaller

from bundle.pyinstaller import (
    OS_NAME,
    announce,
    base_options,
    exe,
    parse_options,
    resolve_onedir,
    set_version_info,
)
from devscripts.utils import read_version

BASE_NAME = 'yt-dlp-gui'
BUNDLE_IDENTIFIER = 'org.yt-dlp.gui'


def main():
    opts, version = parse_options(), read_version()
    onedir = resolve_onedir(opts)

    name, final_file = exe(onedir, BASE_NAME)
    announce(BASE_NAME, version, final_file, opts)

    windowed = ['--windowed']
    if OS_NAME == 'darwin':
        windowed.append(f'--osx-bundle-identifier={BUNDLE_IDENTIFIER}')

    opts = [*base_options(name), *windowed, *opts, 'yt_dlp/gui/__main__.py']

    print(f'Running PyInstaller with {opts}')
    run_pyinstaller(opts)
    set_version_info(final_file, version, BASE_NAME, 'Graphical Interface')


if __name__ == '__main__':
    main()
