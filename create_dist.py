#!/usr/bin/env python3
import os
import zipfile

skip_dirs = ['node_modules', 'api_docs', 'dev_tools', 'old_examples',
             'jsdoc', 'automated_tests', 'tests', 'utils', '.git',
             '.vscode']
skip_files = ['known_problems.md', 'make.bat', '404.html',
              'package.json', 'README.md', 'tasklist.todo', 'index_en.html',
              'index_fr.html', 'serve_reeborg.py', 'unit_test.bat']

def zipdir(new_dir, path, ziph=None):
    # ziph is zipfile handle
    os.chdir("..")
    for root, dirs, files in os.walk(path):
        skip = False
        for skip_dir in skip_dirs:
            if skip_dir in root:
                skip = True
                break
        if skip:
            continue
        for file in files:
            if not file.startswith(".") and file not in skip_files:
                ziph.write(os.path.join(root, file))
            else:
                continue


if __name__ == '__main__':
    zipf = zipfile.ZipFile('reeborg.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('..', 'reeborg', zipf)
    zipf.close()
