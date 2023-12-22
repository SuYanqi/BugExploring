"""json文件输入输出"""
import json
import os
import pickle
import shutil
from datetime import datetime

# datetime无法写入json文件，用这个处理一下
from pathlib import Path

from tqdm import tqdm

from bug_improving.utils.list_util import ListUtil


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        # convert the ISO8601 string to a datetime object
        converted = datetime.datetime.strptime(obj.value, "%Y%m%dT%H:%M:%S")
        if isinstance(converted, datetime.datetime):
            return converted.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(converted, datetime.date):
            return converted.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, converted)


class FileUtil:
    @staticmethod
    def load_json(filepath):
        """
        从文件中取数据
        :param filepath:
        :return:
        """
        with open(filepath, 'r') as load_f:
            data_list = json.load(load_f)
        return data_list

    @staticmethod
    def dump_json(filepath, data_list):
        with open(filepath, 'w') as f:
            json.dump(data_list, f)

    @staticmethod
    def load_pickle(filepath):
        """
        load 从数据文件中读取数据（object）
        :param filepath:
        :return:
        """
        with open(filepath, 'rb') as f:
            data = pickle.load(f)
        return data

    @staticmethod
    def dump_pickle(filepath, data):
        """
        dump 将数据（object）写入文件
        :param filepath:
        :param data:
        :return:
        """
        with open(filepath, 'wb') as f:
            pickle.dump(data, f)

    @staticmethod
    def get_file_names_in_directory(directory, file_type="*"):
        """
        get '.file_type' file_names (paths) in directory
        @param directory: the path of directory
        @type directory: Path("", "", "")
        @param file_type: file type, such as ftl, html, xhtml
        @type file_type: string
        @return: file_names
        @rtype: [string, string, ...]
        """
        # print(directory)
        file_names = []
        for file_name in directory.glob(f"*.{file_type}"):
            file_names.append(str(file_name))
        return file_names

    @staticmethod
    def get_file_names_in_traverse_directory(directory, file_type="*"):
        """
        get '.file_type' file_names (paths) in directory
        @param directory: the path of directory
        @type directory: Path("", "", "")
        @param file_type: file type, such as ftl, html, xhtml
        @type file_type: string
        @return: file_names
        @rtype: [string, string, ...]
        """
        # print(directory)
        file_names = set()
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(file_type):
                    file_names.add(os.path.join(root, file))
        return file_names

    @staticmethod
    def rename_filenames_with_the_same_filename(filepaths):
        # get (filepath, filename) pair
        filepath_filename_pair_list = []
        for index, filepath in enumerate(filepaths):
            parts = filepath.split('/')
            filepath_filename_pair_list.append([filepath, parts[-1]])
        filepath_filename_pair_list = ListUtil.merge_sets_with_intersection_in_list(filepath_filename_pair_list)
        new_filepaths = []
        for filepath_filename_pair in filepath_filename_pair_list:
            # print(filepath_filename_pair)
            filename = [x for x in filepath_filename_pair if "/" not in x][0]
            filepaths = [x for x in filepath_filename_pair if "/" in x]
            if len(filepaths) > 1:
                for index, filepath in enumerate(filepaths):
                    filepath = filepath.replace(filename, f"{filename}_{index}")
                    new_filepaths.append(filepath)
            else:
                new_filepaths.extend(filepaths)
        return new_filepaths
        # sorted_filepath_filename_pair_list = sorted(filepath_filename_pair_list, key=lambda x: x[1])
        # for filepath_filename_pair in sorted_filepath_filename_pair_list:

    @staticmethod
    def get_all_special_files_from_src_dir_to_dst_dir(src_dir, dst_dir, file_type="*"):
        """
        get '.file_type' file_names (paths) in directory
        @param dst_dir: the path of destination directory
        @type dst_dir: Path("", "", "")
        @param src_dir: the path of source directory
        @type src_dir: Path("", "", "")
        @param file_type: file type, such as ftl, html, xhtml
        @type file_type: string
        @return: None
        @rtype: None
        """
        # Create the destination directory if it doesn't exist
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        file_paths = FileUtil.get_file_names_in_traverse_directory(src_dir, file_type)
        # file_paths = list(file_paths)
        # file_paths.sort()
        # for file_path in file_paths:
        #     print(file_path)
        # print(len(file_paths))
        for file_path in tqdm(file_paths, ascii=True):
            filename = file_path.split('/')[-1].replace(f'.{file_type}', '')
            index = 1
            while os.path.exists(Path(dst_dir, f"{filename}.{file_type}")):
                if index == 1:
                    filename = filename + f"_{index}"
                else:
                    filename = filename.replace(f"_{index - 1}", f"_{index}")
                index = index + 1
            shutil.copy(file_path, Path(dst_dir, f"{filename}.{file_type}"))

            # filename = file_path.split('/')[-1]
            # shutil.copy2(file_path, Path(dst_dir, f"{filename}"))

    @staticmethod
    def load_txt(filepath):
        with open(filepath) as f:
            lines = f.readlines()
        return lines

    @staticmethod
    def dump_txt(filepath, items):

        with open(filepath, 'w') as f:
            f.write(items)

    @staticmethod
    def dump_list_to_txt(filepath, items):
        """
        write items (list) into filepath (txt file): one item a line
        Args:
            filepath (): .txt file
            items (): list [, , , ...]

        Returns: write list into txt file: one item a line

        """
        with open(filepath, 'w') as tfile:
            tfile.write('\n'.join(items))
