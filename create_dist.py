#!/usr/bin/env python3
import os
import zipfile

skip_dirs = ['node_modules', 'doc_js', 'dev_tools', 'old_docs', 
             'qunit_test', 'test', 'utils', '.git']
skip_files = ['known_problems.md', 'LICENSE.md', 'make.bat',
              'package.json', 'README.md', 'reeborg_qunit_test.html',
              'repaired_robot.py', 'run_qunit_test.py',
              'serve_reeborg.py']

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
