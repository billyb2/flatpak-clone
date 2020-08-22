#!/bin/python3

import sys
from clone import clone

help_page = False
cloning = False

args = sys.argv[1:]


def help_banner(reason):
    print("Usage: flatpak-clone [-h] [-v] {clone, restore, info} {all, apps} {options}")

    if reason == 'h':
        if len(args) >= 2:
            for arg in args:
                if arg == 'clone':
                    print("Backup and restore flatpak\n\n"
                          "clone finds all installed apps + their data, and copies it into a tarball.\n"
                          "You can choose whether you want to copy the app's data as well, though this is set to true "
                          "by default. You can also specify if you want to backup all flatpak apps, or specific "
                          "ones.\n To find the specific names of apps, check ~/.var/app "
                          "Usage: flatpak-clone clone {all, (specific app names)} {output_location} \n"
                          "Example: flatpak-clone clone io.mrarm.mcpelauncher ~/Backups\n"
                          "Example: flatpak-clone clone all /tmp/HolaMundo")

        else:
            print("Backup and restore flatpak\n\n"
                  "To view the specifics for a command, run\n"
                  "flatpak-clone -h {clone, restore, info}")

    elif reason == 'no_arg':
        print("flatpak-clone: error: No Arguments")

    elif reason == 'num_of_args':
        print("flatpak-clone: error: Invalid number of arguments (clone needs at least 2)")

    elif reason == 'inv_arg':
        print("flatpak-clone: error: Invalid argument")


def main():
    if len(args) == 0:
        help_banner('no_arg')
        return

    if args[0] == 'clone':
        if len(args) < 2:
            help_banner('num_of_args')
            return

        print("Compressing app data (this could take a while)...")
        if args[1] == 'all':
            data = True

            clone.clone(args[1], args[2], data)

        else:
            apps = []
            for arg in args[1:]:
                apps.append(arg)

            print(apps)

        print("Cloned!")

    elif args[0] == '-h' or args[0] == '--help':
        help_banner('h')
        return

    else:
        help_banner('inv_arg')
        return

    if help_page:
        print("Hello world!")


if __name__ == '__main__':
    main()
