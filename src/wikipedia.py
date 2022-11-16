import bz2
from glob import glob
import os
import re
import subprocess
import sys


def download_dump(file_path, url):
    cmd = ['curl', '-o', file_path, url]
    subprocess.call(cmd, stdout=sys.stdout)


def iter_docs(file_path, dir_path):
    """
    Parameters
    ----------
    file_path : string
        File path of wikipedia dump file
    dir_path : string
        Directory path where extracted text files are put
    """

    extracted_file_path_pattern = os.path.join(dir_path, '*', '*')
    extracted_file_paths = glob(extracted_file_path_pattern)
    if len(extracted_file_paths) == 0:
        cmd = ['wikiextractor', '--quiet', '-o', dir_path, file_path]
        subprocess.call(cmd, stdout=sys.stdout)
        extracted_file_paths = glob(extracted_file_path_pattern)

    re_doc_begin = re.compile(r'^<doc(\s.*)?>$')
    re_doc_end = re.compile(r'^</doc>$')
    re_nonstandard_namespace = re.compile(r'.*:.*')
    for fpath in extracted_file_paths:
        with open(fpath) as f:
            print(fpath)
            is_inside_doc = False
            does_skip_this_doc = False
            lines = []
            for line in f:
                line = line.rstrip()
                if not is_inside_doc:
                    m = re_doc_begin.match(line)
                    if m is not None:
                        is_inside_doc = True
                        title = f.__next__().rstrip()
                        if re_nonstandard_namespace.match(title):
                            does_skip_this_doc = True
                        continue
                else:
                    m = re_doc_end.match(line)
                    if m is not None:
                        if not does_skip_this_doc:
                            yield '\n'.join(lines)
                        is_inside_doc = False
                        does_skip_this_doc = False
                        lines = []
                        continue
                    if len(line) > 0:
                        lines.append(line)
