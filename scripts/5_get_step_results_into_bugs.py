from pathlib import Path

from tqdm import tqdm

from bug_improving.types.bug import Bugs
from bug_improving.utils.file_util import FileUtil
from bug_improving.utils.path_util import PathUtil
from config import DATA_DIR


def get_s2r_result_by_bug_id(bug_id, step_results):
    for step_result in step_results:
        if step_result["bug_id"] == bug_id:
            return step_result
    return None


if __name__ == "__main__":

    filtered_bugs_filepath = PathUtil.get_filtered_bugs_filepath()
    step_filename = Path(DATA_DIR, "step", "all", "bug_id_ans_pairs.json")
    bugs = FileUtil.load_pickle(filtered_bugs_filepath)

    step_results = FileUtil.load_json(step_filename)
    for bug in tqdm(bugs, ascii=True):
        step_result = get_s2r_result_by_bug_id(bug.id, step_results)
        if step_result:
            bug.description.get_steps_to_reproduce_from_dict(step_result["ans"])
        else:
            bug.description.steps_to_reproduce = []

    FileUtil.dump_pickle(filtered_bugs_filepath, bugs)
