import logging
from pathlib import Path

import nltk
from tqdm import tqdm

from bug_improving.types.bug import Bugs, Bug
from bug_improving.utils.file_util import FileUtil
from bug_improving.utils.nlp_util import NLPUtil
from bug_improving.utils.path_util import PathUtil
from config import DATA_DIR

if __name__ == "__main__":
    """
    从原始数据集中 creation_time = '2016-01-01T00:00:00Z'
                 1. if bug.description.text
                 2. most bug desc don't consist of log
                 3. 保留status = "CLOSED, RESOLVED, VERIFIED"
    """

    bugs = FileUtil.load_json(PathUtil.get_bugs_filepath())

    bug_list = []
    logging.warning(f"filter {len(bugs)} bugs by desc.text")
    for bug in tqdm(bugs, ascii=True):
        # add Notes section in description.from_text(bug.description.text)
        bug = Bug.from_dict(bug)
        if bug.description.text:
            bug_list.append(bug)
    bugs = Bugs(bug_list)
    logging.warning(f"{bugs.get_length()} bugs left")

    logging.warning(f"filter {len(bugs)} bugs by most bug desc don't consist of log")
    bug_list = []
    for bug in tqdm(bugs, ascii=True):
        if not bug.is_most_desc_as_log():
            bug_list.append(bug)
    bugs = Bugs(bug_list)
    logging.warning(f"{bugs.get_length()} bugs left")
    logging.warning(f"filter {len(bugs)} bugs by status")
    bug_list = []
    for bug in tqdm(bugs, ascii=True):
        if bug.status == 'CLOSED' or bug.status == 'RESOLVED' or bug.status == 'VERIFIED':
            bug_list.append(bug)
    bugs = Bugs(bug_list)
    logging.warning(f"{bugs.get_length()} bugs left")

    bugs.overall_bugs()
    filtered_bugs_filepath = PathUtil.get_filtered_bugs_filepath()
    FileUtil.dump_pickle(filtered_bugs_filepath, bugs)
