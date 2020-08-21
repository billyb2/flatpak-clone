#!/bin/python3
import os
from pathlib import Path
import tarfile as tar

home = str(Path.home())


def compress_data(apps, dir_to_compress, output_folder):
    def compress(file):
        with tar.open(output_folder + file + '.tar.xz', 'w:xz') as app_data_tar:
            app_data_tar.add(home + dir_to_compress + file, arcname=file)
            app_data_tar.close()

    if dir_to_compress[:-1] != '/':
        dir_to_compress += '/'

    if output_folder[:-1] != '/':
        output_folder += '/'

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    if apps == 'all':
        app_data_dirs = os.listdir(home + dir_to_compress)

        for app in app_data_dirs:
            compress(app)

    else:
        for app in apps:
            compress(app)

