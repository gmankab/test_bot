def install_dependencies():
    from sys import executable
    from subprocess import check_call, DEVNULL
    from pkg_resources import working_set

    required = {'deep_translator', 'pandas', 'aiogram'}
    installed = {pkg.key for pkg in working_set}
    missing = required - installed

    if missing:
        python = executable
        check_call([python, '-m', 'pip', 'install', *missing], stdout=DEVNULL)


install_dependencies()


def fuck_pycharm_import_warning_install_dependencies():
    pass
