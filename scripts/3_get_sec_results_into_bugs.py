from pathlib import Path

from tqdm import tqdm

from bug_improving.event_extraction.placeholder import Placeholder
from bug_improving.types.bug import Bugs
from bug_improving.types.description import Description
from bug_improving.utils.file_util import FileUtil
from bug_improving.utils.path_util import PathUtil
from config import DATA_DIR


def get_sec_result_by_bug_id(bug_id, sec_results):
    for sec_result in sec_results:
        if sec_result["bug_id"] == bug_id:
            return sec_result
    return None


if __name__ == "__main__":

    foldername = "all"
    # bugs = FileUtil.load_pickle(PathUtil.get_filtered_bugs_filepath(f"{foldername}_bugs"))
    bugs = FileUtil.load_pickle(PathUtil.get_filtered_bugs_filepath())

    sec_results = FileUtil.load_json(Path(DATA_DIR, "section", foldername, "bug_id_ans_pairs.json"))

    for bug in tqdm(bugs, ascii=True):
        sec_result = get_sec_result_by_bug_id(bug.id, sec_results)
        if sec_result:
            bug.description.get_sections_from_dict(sec_result["ans"])
        else:
            bug.description = Description(bug, bug.description.text)

    # for sec_result in tqdm(sec_results, ascii=True):
    #     bug = bugs.get_bug_by_id(sec_result["bug_id"])
    #     bug.description.get_sections_from_dict(sec_result["ans"])

    filtered_bugs_filepath = PathUtil.get_filtered_bugs_filepath()
    FileUtil.dump_pickle(filtered_bugs_filepath, bugs)
