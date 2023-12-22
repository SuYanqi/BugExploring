"""
This is a simple application for sentence embeddings: clustering
Sentences are mapped to sentence embeddings and then agglomerative clustering with a threshold is applied.
"""

from sentence_transformers import SentenceTransformer

from bug_improving.utils.file_util import FileUtil
from bug_improving.utils.path_util import PathUtil

if __name__ == "__main__":
    # https://www.sbert.net/examples/applications/clustering/README.html#agglomerative-clustering
    # https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering

    # embedder = SentenceTransformer('all-MiniLM-L6-v2')
    embedder = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # maybe this model is better
    bugs_filepath = PathUtil.get_filtered_bugs_filepath()
    bugs = FileUtil.load_pickle(bugs_filepath)

    bugs.merge_steps_by_fast_clustering(embedder)
    FileUtil.dump_pickle(bugs_filepath, bugs)

