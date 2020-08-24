#!/bin/python3
import os
from pathlib import Path
import tarfile as tar
import shutil

home = str(Path.home())


def compress_data(apps, dir_to_compress, output_folder):
    if dir_to_compress[-1] != '/':
        dir_to_compress += '/'

    if output_folder[-1] != '/':
        output_folder += '/'

    print(dir_to_compress)
    print(output_folder)

    def compress(file):
        with tar.open(output_folder + file + '.tar.xz', 'w:xz') as app_data_tar:
            app_data_tar.add(home + dir_to_compress + file, arcname=file)
            app_data_tar.close()

    if apps == 'all':
        app_data_dirs = os.listdir(home + dir_to_compress)

        for app in app_data_dirs:
            compress(app)

    else:
        for app in apps:
            compress(app)


def clone(apps, output_dir, data):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    apps_dir = os.listdir(home + '/.var/app/')

    # Compresses save data
    if data:
        print("Compressing app data (this could take a while, grab a cup of coffee)")
        compress_data(apps, '/.var/app/', output_dir)

    # Finds apps and version numbers
    with open(output_dir + 'apps.fpbck', 'w') as f:
        for app in apps_dir[:-1]:
            print("Writing " + app + " name")
            f.write(app + "\n")
        print("Finished writing")

    with tar.open(output_dir + 'flatpak_backup.tar.xz', 'w:xz') as flatpak_tar:
        for i in os.listdir(output_dir):
            if i + ".tar.xz" in apps_dir or i == 'apps.fpbck':
                print("Adding " + i + " to tar")
                flatpak_tar.add(output_dir + i, arcname=i)

        flatpak_tar.close()

    for i in os.listdir(output_dir):
        if i != 'flatpak_backup.tar.xz':
            if i == 'apps.fpbck' or i + ".tar.xz" in apps_dir:
                if os.path.isfile(output_dir + i):
                    os.remove(output_dir + i)
                else:
                    shutil.rmtree(output_dir + i)
