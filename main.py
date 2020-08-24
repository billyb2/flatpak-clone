#!/bin/python3

import sys
from clone import clone

helping = [False, None]
cloning = [False, None]
data = False

args = sys.argv[1:]


def help_banner(reason):
    print("Usage: flatpak-clone [-h] [-v] {clone, restore, info} {all, apps} {options}")

    if reason == 'h':
        print("Backup and restore flatpak\n\n"
              "To view the specifics for a command, run\n"
              "flatpak-clone -h {clone, restore, info}")

    elif reason == 'clone':
        print("Backup and restore flatpak\n\n"
              "clone finds all installed apps + their data, and copies it into a tarball.\n"
              "You can choose whether you want to copy the app's data as well, though this is set to true "
              "by default. You can also specify if you want to backup all flatpak apps, or specific "
              "ones.\n To find the specific names of apps, check ~/.var/app "
              "Usage: flatpak-clone clone {all, (specific app names)} {output_location} \n"
              "Example: flatpak-clone clone io.mrarm.mcpelauncher ~/Backups\n"
              "Example: flatpak-clone clone all /tmp/HolaMundo")

    elif reason == 'no_arg':
        print("flatpak-clone: error: No Arguments")

    elif reason == 'num_of_args':
        print("flatpak-clone: error: Invalid number of arguments (clone needs at least 2)")

    elif reason == 'inv_arg':
        print("flatpak-clone: error: Invalid argument")


def set_args():
    global cloning
    global helping

    for arg in args:
        if arg == 'clone':
            cloning = [True, args.index(arg)]

        elif arg == '-h' or arg == '--help':
            helping = [True, args.index(arg)]

        elif arg == '-d' or arg == '--data':
            data = True


def main():
    set_args()

    if len(args) == 0:
        help_banner('no_arg')
        return

    if helping[1] is not None:
        if cloning[1] is not None:
            if helping[1] >= cloning[1]:
                help_banner('inv_arg')
                return

    if helping[0]:
        if cloning[0]:
            help_banner('clone')
            return

        help_banner('h')
        return

    if cloning[0]:
        if len(args) < 2:
            help_banner('num_of_args')
            return

        print("Compressing app data (this could take a while)...")
        if args[cloning[1] + 1] == 'all':
            try:
                clone.clone('all', args[cloning[1] + 2], data)

            except IndexError:
                print("No output folder specified, using " + clone.home)
                clone.clone('all', clone.home + "/", data)

        else:
            apps = []
            for arg in args[cloning[1] + 1:]:
                apps.append(arg)

            clone.clone

        print("Cloned!")

    else:
        help_banner('inv_arg')
        return


if __name__ == '__main__':
    main()
