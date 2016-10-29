#! /usr/bin/python3

from os import getcwd, mkdir
from os.path import normpath, basename

import click, os
import colorama as C

version = '1.0.0'


def touch(fname: str) -> None:
    with open(fname, 'a'):
        os.utime(fname)


def banner():
    print(TF.strong('scaffold ') + TF.reset() + 'v'+version)


class TF(object):
    @staticmethod
    def strong(txt):
        return C.Style.BRIGHT + txt

    @staticmethod
    def green(txt):
        return C.Fore.GREEN + txt

    @staticmethod
    def reset():
        return C.Style.RESET_ALL


def apply_template(filename, **kwargs):
    script_path = os.path.dirname(os.path.realpath(__file__))
    template_name = os.path.join(script_path, 'templates', filename)
    if os.path.exists(template_name):
        with open(template_name) as t:
            template = t.read()
            with open(filename, 'w') as f:
                f.write(template.format(**kwargs))


class Scaffold(object):
    dirs = ['doc', 'src', 'include', 'env']
    files = ['.gitignore', '.editorconfig', 'CMakeLists.txt',
             'doc/mkdocs.yml', 'doc/index.md', 'include/version.h.in',
             'README.md']

    def init(self):
        self.project_name = basename(normpath(getcwd()))
        print('Initializing project', TF.green(self.project_name), TF.reset())
        print('Creating directories...')
        for d in self.dirs:
            mkdir(d)
        print('Creating files...')
        for f in self.files:
            touch(f)
            apply_template(f, project_name=self.project_name, project_id=self.project_name.upper())


@click.command()
@click.argument('command')
def run(command):
    C.init()
    banner()
    scf = Scaffold()
    if hasattr(scf, command):
        getattr(scf, command)()
    else:
        print('No such command.')


if __name__ == '__main__':
    run()
