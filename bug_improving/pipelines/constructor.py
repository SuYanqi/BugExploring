import copy
import json

from tqdm import tqdm

from bug_improving.event_extraction.placeholder import Placeholder
from bug_improving.utils.llm_util import LLMUtil


class StepSplitter:
    def __init__(self):
        pass

    # split STR into Steps **********************************************************
    @staticmethod
    def convert_instances_into_qa_pairs(bugs, with_step_type=False):
        qa_pairs = []
        if with_step_type:
            instances = Placeholder.STEP_SPLITTER_INSTANCES_WITH_TYPE
        else:
            instances = Placeholder.STEP_SPLITTER_INSTANCES
        if instances:
            for instance_dict in instances:
                bug = bugs.get_bug_by_id(int(instance_dict['bug_id']))
                question = StepSplitter.question_for_step_splitting(bug)
                answer = StepSplitter.answer_for_step_splitting(instance_dict['output'])
                qa_pairs.append((question, answer))
        return qa_pairs

    @staticmethod
    def get_session_prompt(with_step_type=False):
        session_prompt = f"I am a step splitter. " \
                         f"I can split 'Steps To Reproduce' section into steps, " \
                         f"which each step is an individual UI operation."
        if with_step_type:
            session_prompt = session_prompt + \
                             f'\nMeanwhile, I can classify each step into ' \
                             f'{Placeholder.OPERATION} or {Placeholder.NON_OPERATION}.'
        return session_prompt

    @staticmethod
    def get_initial_messages(bugs=None, with_step_type=False):
        session_prompt = StepSplitter.get_session_prompt(with_step_type)
        qa_pairs = None
        if bugs:
            qa_pairs = StepSplitter.convert_instances_into_qa_pairs(bugs, with_step_type)
        messages = LLMUtil.get_messages_for_turbo(session_prompt, qa_pairs)
        return messages

    @staticmethod
    def question_for_step_splitting(bug=None):
        return f"{Placeholder.STEPS_TO_REPRODUCE}: {bug.description.steps_to_reproduce}\n\n" \
               f"Please split {Placeholder.STEPS_TO_REPRODUCE} into steps, " \
               f"especially splitting the step with multiple UI operations into steps with one UI operation). " \
            # f"Please answer in the format of a List: ['',]" \
        # f"Please be careful not to exceed the given scope of the content."

    @staticmethod
    def answer_for_step_splitting(outputs, chains=None):
        if chains:
            return f"Chains-of-Thought: {chains}\n\n" \
                   f"Outputs: {outputs}"
        return json.dumps(outputs)

    @staticmethod
    def split_s2r(bug=None, bugs=None, with_step_type=False):
        # if messages is None:
        messages = StepSplitter.get_initial_messages(bugs, with_step_type)
        # extract summary
        question = StepSplitter.question_for_step_splitting(bug)
        messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_USER, question, messages)
        # print(self.summary_question)
        # input()
        answer = LLMUtil.ask_turbo(messages)
        messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_ASSISTANT, answer, messages)

        # LLMUtil.show_messages(messages)
        # desc_question, desc_answer = LLMUtil.question_answer(self.desc_question)
        # print(summary_question)
        # print(summary_answer)
        # print(desc_question)
        # print(desc_answer)
        # answer = Answer.from_answer(summary_pair, summary_answer, desc_answer)
        # raw_answer = RawAnswer(summary_pair,
        #                        QA(self.summary_question, summary_answer),
        #                        QA(self.desc_question, desc_answer))

        return answer, messages


class SecSplitter:
    def __init__(self):
        pass

    @staticmethod
    def convert_instances_into_qa_pairs(bugs):
        qa_pairs = []
        if Placeholder.SEC_SPLITTER_INSTANCES:
            for instance_dict in Placeholder.SEC_SPLITTER_INSTANCES:
                bug = bugs.get_bug_by_id(int(instance_dict['bug_id']))
                question = SecSplitter.question_for_sec_splitting(bug)
                answer = SecSplitter.answer_for_sec_splitting(instance_dict['output'])
                qa_pairs.append((question, answer))
        return qa_pairs

    @staticmethod
    def get_session_prompt():
        session_prompt = f"I am a text splitter. " \
                         f"I can split the text into the specific parts."
        return session_prompt

    @staticmethod
    def get_initial_messages(bugs=None):
        session_prompt = SecSplitter.get_session_prompt()
        qa_pairs = None
        if bugs:
            qa_pairs = SecSplitter.convert_instances_into_qa_pairs(bugs)
        messages = LLMUtil.get_messages_for_turbo(session_prompt, qa_pairs)
        return messages

    @staticmethod
    def question_for_sec_splitting(bug):
        return f"Bug Summary: {bug.summary}\n" \
               f"Bug Description:\n{bug.description.text}\n\n" \
               f"Please split the bug description into the specific sections " \
               "and answer in the format of a JSON string: " \
               "{" \
               f'"{Placeholder.PRECONDITIONS}":["",],' \
               f'"{Placeholder.STEPS_TO_REPRODUCE}":["",],' \
               f'"{Placeholder.EXPECTED_RESULTS}":["",],' \
               f'"{Placeholder.ACTUAL_RESULTS}":["",],' \
               f'"{Placeholder.NOTES}":["",],' \
               f'"{Placeholder.AFFECTED_VERSIONS}":["",],' \
               f'"{Placeholder.AFFECTED_PLATFORMS}":["",],' \
               f'"{Placeholder.OTHERS}":["",]' \
               "}"

    @staticmethod
    def answer_for_sec_splitting(outputs):
        return json.dumps(outputs)

    @staticmethod
    def split_section(bug, bugs=None):
        messages = SecSplitter.get_initial_messages(bugs)
        # extract summary
        question = SecSplitter.question_for_sec_splitting(bug)
        messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_USER, question, messages)
        # print(self.summary_question)
        # input()
        answer = LLMUtil.ask_turbo(messages)
        messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_ASSISTANT, answer, messages)

        # LLMUtil.show_messages(messages)
        # desc_question, desc_answer = LLMUtil.question_answer(self.desc_question)
        # answer = Answer.from_answer(summary_pair, summary_answer, desc_answer)
        # raw_answer = RawAnswer(summary_pair,
        #                        QA(self.summary_question, summary_answer),
        #                        QA(self.desc_question, desc_answer))

        return answer, messages

    @staticmethod
    def get_messages_list_for_bugs(bugs, with_instances=False):
        initial_messages = SecSplitter.get_initial_messages(with_instances)
        # print(initial_messages)
        messages_list = []
        for bug in tqdm(bugs, ascii=True):
            question = SecSplitter.question_for_sec_splitting(bug)
            # print(question)
            # for initial_message in initial_messages:
            #     print(initial_message)
            # print("******************")
            # print(initial_messages)
            messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_USER, question,
                                                                   copy.deepcopy(initial_messages))
            # for message in messages:
            #     print(message)
            messages_list.append(messages)
            # print("############################")
        return messages_list


class Splitter:
    def __init__(self):
        pass

    # @staticmethod
    # def split_desc(bug, bugs):
    #     sec_ans, messages = Splitter.split_section(bug, bugs)
    #     stp_ans, messages = Splitter.split_s2r(messages)
    #     LLMUtil.show_messages(messages)

    # ****************************************************************************
    # split DESC into SEC **********************************************************
    # @staticmethod
    # def convert_sec_instances_into_qa_pairs(bugs):
    #     qa_pairs = []
    #     if Placeholder.SEC_SPLITTER_INSTANCES:
    #         for instance_dict in Placeholder.SEC_SPLITTER_INSTANCES:
    #             bug = bugs.get_bug_by_id(int(instance_dict['bug_id']))
    #             question = Splitter.question_for_sec_splitting(bug)
    #             answer = Splitter.answer_for_sec_splitting(instance_dict['output'])
    #             qa_pairs.append((question, answer))
    #     return qa_pairs
    #
    # @staticmethod
    # def get_sec_splitting_session_prompt():
    #     session_prompt = f"I am a text splitter. " \
    #                      f"I can split the text into the specific parts."
    #     return session_prompt
    #
    # @staticmethod
    # def get_sec_splitting_initial_messages(bugs=None):
    #     session_prompt = Splitter.get_sec_splitting_session_prompt()
    #     qa_pairs = None
    #     if bugs:
    #         qa_pairs = Splitter.convert_sec_instances_into_qa_pairs(bugs)
    #     messages = LLMUtil.get_messages_for_turbo(session_prompt, qa_pairs)
    #     return messages
    #
    # @staticmethod
    # def question_for_sec_splitting(bug):
    #     return f"Bug Description:\n{bug.description.text}\n\n" \
    #            f"Please split the bug description into the specific sections " \
    #            "and answer in the format of a JSON string: " \
    #            "{" \
    #            f"'{Placeholder.PRECONDITIONS}':['',]," \
    #            f"'{Placeholder.STEPS_TO_REPRODUCE}':['',]," \
    #            f"'{Placeholder.EXPECTED_RESULTS}':['',]," \
    #            f"'{Placeholder.ACTUAL_RESULTS}':['',]," \
    #            f"'{Placeholder.NOTES}':['',]," \
    #            f"'{Placeholder.AFFECTED_VERSIONS}':['',]," \
    #            f"'{Placeholder.AFFECTED_PLATFORMS}':['',]," \
    #            f"'{Placeholder.OTHERS}':['',]" \
    #            "}"
    #
    # @staticmethod
    # def answer_for_sec_splitting(outputs):
    #     return f"{outputs}"
    #
    # @staticmethod
    # def split_section(bug, bugs=None):
    #     messages = Splitter.get_sec_splitting_initial_messages(bugs)
    #     # extract summary
    #     question = Splitter.question_for_sec_splitting(bug)
    #     messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_USER, question, messages)
    #     # print(self.summary_question)
    #     # input()
    #     answer = LLMUtil.ask_turbo(messages)
    #     messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_ASSISTANT, answer, messages)
    #
    #     # LLMUtil.show_messages(messages)
    #     # desc_question, desc_answer = LLMUtil.question_answer(self.desc_question)
    #     # answer = Answer.from_answer(summary_pair, summary_answer, desc_answer)
    #     # raw_answer = RawAnswer(summary_pair,
    #     #                        QA(self.summary_question, summary_answer),
    #     #                        QA(self.desc_question, desc_answer))
    #
    #     return answer, messages

    # ****************************************************************************
    # # split STR into Steps **********************************************************
    # @staticmethod
    # def convert_step_splitting_instances_into_qa_pairs(bugs):
    #     qa_pairs = []
    #     if Placeholder.STEP_SPLITTER_INSTANCES:
    #         for instance_dict in Placeholder.STEP_SPLITTER_INSTANCES:
    #             bug = bugs.get_bug_by_id(int(instance_dict['bug_id']))
    #             question = Splitter.question_for_step_splitting(bug)
    #             answer = Splitter.answer_for_step_splitting(instance_dict['output'])
    #             qa_pairs.append((question, answer))
    #     return qa_pairs
    #
    # @staticmethod
    # def get_step_splitting_session_prompt():
    #     session_prompt = f"I am a step splitter. " \
    #                      f"I can split 'Steps To Reproduce' section into steps, " \
    #                      f"which each step is an individual UI operation."
    #     return session_prompt
    #
    # @staticmethod
    # def get_step_splitting_initial_messages(bugs=None):
    #     session_prompt = Splitter.get_step_splitting_session_prompt()
    #     qa_pairs = None
    #     if bugs:
    #         qa_pairs = Splitter.convert_step_splitting_instances_into_qa_pairs(bugs)
    #     messages = LLMUtil.get_messages_for_turbo(session_prompt, qa_pairs)
    #     return messages
    #
    # @staticmethod
    # def question_for_step_splitting(bug=None):
    #     return f"{Placeholder.STEPS_TO_REPRODUCE}: {bug.description.steps_to_reproduce}\n\n" \
    #            f"Please split {Placeholder.STEPS_TO_REPRODUCE} into steps, " \
    #            f"especially splitting the step with multiple UI operations into steps with one UI operation). " \
    #            f"Please answer in the format of a List: ['',]" \
    #         # f"Please be careful not to exceed the given scope of the content."
    #
    # @staticmethod
    # def answer_for_step_splitting(outputs, chains=None):
    #     if chains:
    #         return f"Chains-of-Thought: {chains}\n\n" \
    #                f"Outputs: {outputs}"
    #     return f"{outputs}"
    #
    # @staticmethod
    # def split_s2r(messages=None, bug=None, bugs=None):
    #     if messages is None:
    #         messages = Splitter.get_step_splitting_initial_messages(bugs)
    #     # extract summary
    #     question = Splitter.question_for_step_splitting(bug)
    #     messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_USER, question, messages)
    #     # print(self.summary_question)
    #     # input()
    #     answer = LLMUtil.ask_turbo(messages)
    #     messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_ASSISTANT, answer, messages)
    #
    #     LLMUtil.show_messages(messages)
    #     # desc_question, desc_answer = LLMUtil.question_answer(self.desc_question)
    #     # print(summary_question)
    #     # print(summary_answer)
    #     # print(desc_question)
    #     # print(desc_answer)
    #     # answer = Answer.from_answer(summary_pair, summary_answer, desc_answer)
    #     # raw_answer = RawAnswer(summary_pair,
    #     #                        QA(self.summary_question, summary_answer),
    #     #                        QA(self.desc_question, desc_answer))
    #
    #     return answer, messages

    # ****************************************************************************
    # split DESC into SEC and STEPS **********************************************************

    @staticmethod
    def convert_sec_step_instances_into_qa_pairs(bugs):
        qa_pairs = []
        if Placeholder.SEC_STEP_SPLITTER_INSTANCES:
            for instance_dict in Placeholder.SEC_STEP_SPLITTER_INSTANCES:
                bug = bugs.get_bug_by_id(int(instance_dict['bug_id']))
                question = Splitter.question_for_sec_step_splitting(bug)
                answer = Splitter.answer_for_sec_step_splitting(instance_dict['output'])
                qa_pairs.append((question, answer))
        return qa_pairs

    @staticmethod
    def get_sec_step_splitting_session_prompt():
        session_prompt = f"I am a text splitter. " \
                         f"I can split the text into the specific sections. "
        return session_prompt

    @staticmethod
    def get_sec_step_splitting_initial_messages(bugs=None):
        session_prompt = Splitter.get_sec_step_splitting_session_prompt()
        qa_pairs = None
        if bugs:
            qa_pairs = Splitter.convert_sec_step_instances_into_qa_pairs(bugs)
        messages = LLMUtil.get_messages_for_turbo(session_prompt, qa_pairs)
        return messages

    @staticmethod
    def question_for_sec_step_splitting(bug):
        return f"Bug Description:\n{bug.description.text}\n\n" \
               f"Please split the bug description into the specific sections " \
               "and answer in the format of a JSON string: " \
               "{" \
               f"'{Placeholder.PRECONDITIONS}':['',]," \
               f"'{Placeholder.STEPS_TO_REPRODUCE}':['',]," \
               f"'{Placeholder.EXPECTED_RESULTS}':['',]," \
               f"'{Placeholder.ACTUAL_RESULTS}':['',]," \
               f"'{Placeholder.NOTES}':['',]," \
               f"'{Placeholder.AFFECTED_VERSIONS}':['',]," \
               f"'{Placeholder.AFFECTED_PLATFORMS}':['',]," \
               f"'{Placeholder.OTHERS}':['',]" \
               "}\n" \
               f"!!! Note that when splitting {Placeholder.STEPS_TO_REPRODUCE} section into steps, " \
               f"if one step has more than one GUI operations, please further split it into steps, " \
               f"which each of them has only one GUI operation!!!" \
 \
               @ staticmethod

    def answer_for_sec_step_splitting(outputs):
        return f"{outputs}"

    @staticmethod
    def split_section_steps(bug, bugs=None):
        messages = Splitter.get_sec_step_splitting_initial_messages(bugs)
        # extract summary
        question = Splitter.question_for_sec_step_splitting(bug)
        messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_USER, question, messages)
        # print(self.summary_question)
        # input()
        answer = LLMUtil.ask_turbo(messages)
        messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_ASSISTANT, answer, messages)

        LLMUtil.show_messages(messages)
        # desc_question, desc_answer = LLMUtil.question_answer(self.desc_question)
        # print(summary_question)
        # print(summary_answer)
        # print(desc_question)
        # print(desc_answer)
        # answer = Answer.from_answer(summary_pair, summary_answer, desc_answer)
        # raw_answer = RawAnswer(summary_pair,
        #                        QA(self.summary_question, summary_answer),
        #                        QA(self.desc_question, desc_answer))

        return answer


class Linker:
    def __init__(self):
        pass

    @staticmethod
    def convert_instances_into_qa_pairs(bugs):
        qa_pairs = []
        if Placeholder.STEP_SPLITTER_INSTANCES:
            for instance_dict in Placeholder.STEP_SPLITTER_INSTANCES:
                bug = bugs.get_bug_by_id(int(instance_dict['bug_id']))
                question = Splitter.question_for_step_splitting(bug)
                answer = Splitter.answer_for_step_splitting(instance_dict['output'])
                qa_pairs.append((question, answer))
        return qa_pairs

    @staticmethod
    def get_session_prompt():
        session_prompt = f"I am a step splitter. " \
                         f"I can split 'Steps To Reproduce' section into steps, " \
                         f"which each step is an individual UI operation."
        return session_prompt

    @staticmethod
    def get_step_splitting_initial_messages(bugs=None):
        session_prompt = Splitter.get_step_splitting_session_prompt()
        qa_pairs = None
        if bugs:
            qa_pairs = Splitter.convert_step_splitting_instances_into_qa_pairs(bugs)
        messages = LLMUtil.get_messages_for_turbo(session_prompt, qa_pairs)
        return messages

    @staticmethod
    def question_for_step_splitting(bug=None):
        return f"{Placeholder.STEPS_TO_REPRODUCE}: {bug.description.steps_to_reproduce}\n\n" \
               f"Please split {Placeholder.STEPS_TO_REPRODUCE} into steps, " \
               f"especially splitting the step with multiple UI operations into steps with one UI operation). " \
               f"Please answer in the format of a List: ['',]" \
            # f"Please be careful not to exceed the given scope of the content."

    @staticmethod
    def answer_for_step_splitting(outputs, chains=None):
        if chains:
            return f"Chains-of-Thought: {chains}\n\n" \
                   f"Outputs: {outputs}"
        return f"{outputs}"

    @staticmethod
    def split_s2r(messages=None, bug=None, bugs=None):
        if messages is None:
            messages = Splitter.get_step_splitting_initial_messages(bugs)
        # extract summary
        question = Splitter.question_for_step_splitting(bug)
        messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_USER, question, messages)
        # print(self.summary_question)
        # input()
        answer = LLMUtil.ask_turbo(messages)
        messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_ASSISTANT, answer, messages)

        LLMUtil.show_messages(messages)
        # desc_question, desc_answer = LLMUtil.question_answer(self.desc_question)
        # print(summary_question)
        # print(summary_answer)
        # print(desc_question)
        # print(desc_answer)
        # answer = Answer.from_answer(summary_pair, summary_answer, desc_answer)
        # raw_answer = RawAnswer(summary_pair,
        #                        QA(self.summary_question, summary_answer),
        #                        QA(self.desc_question, desc_answer))

        return answer, messages


# class Constructor:
#     def __init__(self):
#         pass
#
    # @staticmethod
    # def process_desc(bug, bugs):
    #     sec_ans, messages = Constructor.split_section(bug, bugs)
    #     stp_ans, messages = Constructor.split_s2r(messages)
    #     LLMUtil.show_messages(messages)
    #
    # # split DESC into SEC
    # @staticmethod
    # def convert_sec_instances_into_qa_pairs(bugs):
    #     qa_pairs = []
    #     if Placeholder.SEC_SPLITTER_INSTANCES:
    #         for instance_dict in Placeholder.SEC_SPLITTER_INSTANCES:
    #             bug = bugs.get_bug_by_id(int(instance_dict['bug_id']))
    #             question = Constructor.question_for_sec_splitting(bug)
    #             answer = Constructor.answer_for_sec_splitting(instance_dict['output'])
    #             qa_pairs.append((question, answer))
    #     return qa_pairs
    #
    # @staticmethod
    # def get_sec_splitting_session_prompt():
    #     session_prompt = f"I am a text splitter. " \
    #                      f"I can split the text into the specific parts." \
    #         # f"(i.e., {Placeholder.PRECONDITIONS}, " \
    #     # f"{Placeholder.STEPS_TO_REPRODUCE}, " \
    #     # f"{Placeholder.EXPECTED_RESULTS}, {Placeholder.ACTUAL_RESULTS}, " \
    #     # f"{Placeholder.NOTES}, " \
    #     # f"{Placeholder.AFFECTED_VERSIONS}, {Placeholder.AFFECTED_PLATFORMS}, " \
    #     # f"{Placeholder.OTHERS})."
    #     return session_prompt
    #
    # @staticmethod
    # def get_sec_splitting_initial_messages(bugs=None):
    #     session_prompt = Constructor.get_sec_splitting_session_prompt()
    #     qa_pairs = None
    #     if bugs:
    #         qa_pairs = Constructor.convert_sec_instances_into_qa_pairs(bugs)
    #     messages = LLMUtil.get_messages_for_turbo(session_prompt, qa_pairs)
    #     return messages
    #
    # @staticmethod
    # def question_for_sec_splitting(bug):
    #     return f"Bug Description:\n{bug.description.text}\n\n" \
    #            f"Please split the bug description into the specific sections " \
    #            "and answer in the format of a JSON string: " \
    #            "{" \
    #            f"'{Placeholder.PRECONDITIONS}':['',]," \
    #            f"'{Placeholder.STEPS_TO_REPRODUCE}':['',]," \
    #            f"'{Placeholder.EXPECTED_RESULTS}':['',]," \
    #            f"'{Placeholder.ACTUAL_RESULTS}':['',]," \
    #            f"'{Placeholder.NOTES}':['',]," \
    #            f"'{Placeholder.AFFECTED_VERSIONS}':['',]," \
    #            f"'{Placeholder.AFFECTED_PLATFORMS}':['',]," \
    #            f"'{Placeholder.OTHERS}':['',]" \
    #            "}" \
    #         # f"(i.e., {Placeholder.PRECONDITIONS}, " \
    #     # f"{Placeholder.STEPS_TO_REPRODUCE}, " \
    #     # f"{Placeholder.EXPECTED_RESULTS}, {Placeholder.ACTUAL_RESULTS}, " \
    #     # f"{Placeholder.NOTES}, " \
    #     # f"{Placeholder.AFFECTED_VERSIONS}, {Placeholder.AFFECTED_PLATFORMS}, " \
    #     # f"{Placeholder.OTHERS}).\n\n" \
    #     # f"2. Please be careful not to generate information, which exceed the given scope of the content."
    #
    # @staticmethod
    # def answer_for_sec_splitting(outputs):
    #     return f"{outputs}"
    #
    # @staticmethod
    # def split_section(bug, bugs=None):
    #     messages = Constructor.get_sec_splitting_initial_messages(bugs)
    #     # extract summary
    #     question = Constructor.question_for_sec_splitting(bug)
    #     messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_USER, question, messages)
    #     # print(self.summary_question)
    #     # input()
    #     answer = LLMUtil.ask_turbo(messages)
    #     messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_ASSISTANT, answer, messages)
    #
    #     # LLMUtil.show_messages(messages)
    #     # desc_question, desc_answer = LLMUtil.question_answer(self.desc_question)
    #     # answer = Answer.from_answer(summary_pair, summary_answer, desc_answer)
    #     # raw_answer = RawAnswer(summary_pair,
    #     #                        QA(self.summary_question, summary_answer),
    #     #                        QA(self.desc_question, desc_answer))
    #
    #     return answer, messages
    #
    # # split STR into Steps
    # @staticmethod
    # def convert_step_splitting_instances_into_qa_pairs(bugs):
    #     qa_pairs = []
    #     if Placeholder.STEP_SPLITTER_INSTANCES:
    #         for instance_dict in Placeholder.STEP_SPLITTER_INSTANCES:
    #             bug = bugs.get_bug_by_id(int(instance_dict['bug_id']))
    #             question = Constructor.question_for_step_splitting(bug)
    #             answer = Constructor.answer_for_step_splitting(instance_dict['output'])
    #             qa_pairs.append((question, answer))
    #     return qa_pairs
    #
    # @staticmethod
    # def get_step_splitting_session_prompt():
    #     session_prompt = f"I am a step splitter. " \
    #                      f"I can split 'Steps To Reproduce' section into steps, " \
    #                      f"which each step is an individual UI operation."
    #     return session_prompt
    #
    # @staticmethod
    # def get_step_splitting_initial_messages(bugs=None):
    #     session_prompt = Constructor.get_step_splitting_session_prompt()
    #     qa_pairs = None
    #     if bugs:
    #         qa_pairs = Constructor.convert_step_splitting_instances_into_qa_pairs(bugs)
    #     messages = LLMUtil.get_messages_for_turbo(session_prompt, qa_pairs)
    #     return messages
    #
    # @staticmethod
    # def question_for_step_splitting(bug=None):
    #     return f"{Placeholder.STEPS_TO_REPRODUCE}: {bug.description.steps_to_reproduce}\n\n" \
    #            f"Please split {Placeholder.STEPS_TO_REPRODUCE} into steps, " \
    #            f"especially splitting the step with multiple UI operations into steps with one UI operation). " \
    #            f"Please answer in the format of a List: ['',]" \
    #         # f"Please be careful not to exceed the given scope of the content."
    #
    # @staticmethod
    # def answer_for_step_splitting(outputs, chains=None):
    #     if chains:
    #         return f"Chains-of-Thought: {chains}\n\n" \
    #                f"Outputs: {outputs}"
    #     return f"{outputs}"
    #
    # @staticmethod
    # def split_s2r(messages=None, bug=None, bugs=None):
    #     if messages is None:
    #         messages = Constructor.get_step_splitting_initial_messages(bugs)
    #     # extract summary
    #     question = Constructor.question_for_step_splitting(bug)
    #     messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_USER, question, messages)
    #     # print(self.summary_question)
    #     # input()
    #     answer = LLMUtil.ask_turbo(messages)
    #     messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_ASSISTANT, answer, messages)
    #
    #     LLMUtil.show_messages(messages)
    #     # desc_question, desc_answer = LLMUtil.question_answer(self.desc_question)
    #     # print(summary_question)
    #     # print(summary_answer)
    #     # print(desc_question)
    #     # print(desc_answer)
    #     # answer = Answer.from_answer(summary_pair, summary_answer, desc_answer)
    #     # raw_answer = RawAnswer(summary_pair,
    #     #                        QA(self.summary_question, summary_answer),
    #     #                        QA(self.desc_question, desc_answer))
    #
    #     return answer, messages
    #
    # # ****************************************************************************
    # # split DESC into SEC and STEPS
    #
    # @staticmethod
    # def convert_sec_step_instances_into_qa_pairs(bugs):
    #     qa_pairs = []
    #     if Placeholder.SEC_STEP_SPLITTER_INSTANCES:
    #         for instance_dict in Placeholder.SEC_STEP_SPLITTER_INSTANCES:
    #             bug = bugs.get_bug_by_id(int(instance_dict['bug_id']))
    #             question = Constructor.question_for_sec_step_splitting(bug)
    #             answer = Constructor.answer_for_sec_step_splitting(instance_dict['output'])
    #             qa_pairs.append((question, answer))
    #     return qa_pairs
    #
    # @staticmethod
    # def get_sec_step_splitting_session_prompt():
    #     session_prompt = f"I am a text splitter. " \
    #                      f"I can split the text into the specific sections. " \
    #         # f"(i.e., {Placeholder.PRECONDITIONS}, " \
    #     # f"{Placeholder.STEPS_TO_REPRODUCE}, " \
    #     # f"{Placeholder.EXPECTED_RESULTS}, {Placeholder.ACTUAL_RESULTS}, " \
    #     # f"{Placeholder.NOTES}, " \
    #     # f"{Placeholder.AFFECTED_VERSIONS}, {Placeholder.AFFECTED_PLATFORMS}, " \
    #     # f"{Placeholder.OTHERS})" \
    #     # f"Meanwhile, I can split the {Placeholder.STEPS_TO_REPRODUCE} section into steps, " \
    #     # f"which each step contains an individual action."
    #     return session_prompt
    #
    # @staticmethod
    # def get_sec_step_splitting_initial_messages(bugs=None):
    #     session_prompt = Constructor.get_sec_step_splitting_session_prompt()
    #     qa_pairs = None
    #     if bugs:
    #         qa_pairs = Constructor.convert_sec_step_instances_into_qa_pairs(bugs)
    #     messages = LLMUtil.get_messages_for_turbo(session_prompt, qa_pairs)
    #     return messages
    #
    # @staticmethod
    # def question_for_sec_step_splitting(bug):
    #     return f"Bug Description:\n{bug.description.text}\n\n" \
    #            f"Please split the bug description into the specific sections " \
    #            "and answer in the format of a JSON string: " \
    #            "{" \
    #            f"'{Placeholder.PRECONDITIONS}':['',]," \
    #            f"'{Placeholder.STEPS_TO_REPRODUCE}':['',]," \
    #            f"'{Placeholder.EXPECTED_RESULTS}':['',]," \
    #            f"'{Placeholder.ACTUAL_RESULTS}':['',]," \
    #            f"'{Placeholder.NOTES}':['',]," \
    #            f"'{Placeholder.AFFECTED_VERSIONS}':['',]," \
    #            f"'{Placeholder.AFFECTED_PLATFORMS}':['',]," \
    #            f"'{Placeholder.OTHERS}':['',]" \
    #            "}\n" \
    #            f"!!! Note that when splitting {Placeholder.STEPS_TO_REPRODUCE} section into steps, " \
    #            f"if one step has more than one GUI operations, please further split it into steps, " \
    #            f"which each of them has only one GUI operation!!!" \
    #         # f"(i.e., each step contains only one individual action.). " \
    #     # f"Note that if the bug description does not contain a specific section, " \
    #     # f"then that section return None.\n\n" \
    #     # f"The splitted output are as follows:" \
    #     # f"{Placeholder.PRECONDITIONS}:\n" \
    #     # f"{Placeholder.STEPS_TO_REPRODUCE}:\n" \
    #     # f"{Placeholder.EXPECTED_RESULTS}:\n" \
    #     # f"{Placeholder.ACTUAL_RESULTS}:\n" \
    #     # f"{Placeholder.NOTES}:\n" \
    #     # f"{Placeholder.AFFECTED_VERSIONS}:\n" \
    #     # f"{Placeholder.AFFECTED_PLATFORMS}:\n" \
    #     # f"{Placeholder.OTHERS}:" \
    #     # f"2. Please be careful not to generate information, which exceed the given scope of the content."
    #
    # @staticmethod
    # def answer_for_sec_step_splitting(outputs):
    #     return f"{outputs}"
    #
    # @staticmethod
    # def split_section_steps(bug, bugs=None):
    #     messages = Constructor.get_sec_step_splitting_initial_messages(bugs)
    #     # extract summary
    #     question = Constructor.question_for_sec_step_splitting(bug)
    #     messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_USER, question, messages)
    #     # print(self.summary_question)
    #     # input()
    #     answer = LLMUtil.ask_turbo(messages)
    #     messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_ASSISTANT, answer, messages)
    #
    #     LLMUtil.show_messages(messages)
    #     # desc_question, desc_answer = LLMUtil.question_answer(self.desc_question)
    #     # print(summary_question)
    #     # print(summary_answer)
    #     # print(desc_question)
    #     # print(desc_answer)
    #     # answer = Answer.from_answer(summary_pair, summary_answer, desc_answer)
    #     # raw_answer = RawAnswer(summary_pair,
    #     #                        QA(self.summary_question, summary_answer),
    #     #                        QA(self.desc_question, desc_answer))
    #
    #     return answer
    #
    # # ****************************************************************************
    # # split STR into atomic steps
    #
    # # @staticmethod
    # # def convert_step_splitting_instances_into_qa_pairs(bugs):
    # #     qa_pairs = []
    # #     if Placeholder.STEP_SPLITTER_INSTANCES:
    # #         for instance_dict in Placeholder.STEP_SPLITTER_INSTANCES:
    # #             bug = bugs.get_bug_by_id(int(instance_dict['bug_id']))
    # #             question = Constructor.question_for_step_splitting(bug)
    # #             answer = Constructor.answer_for_step_splitting(instance_dict['chains'], instance_dict['output'])
    # #             qa_pairs.append((question, answer))
    # #     return qa_pairs
    # #
    # # @staticmethod
    # # def get_step_splitting_session_prompt():
    # #     session_prompt = f"I am a step splitter. " \
    # #                      f"I can split 'Steps To Reproduce' section into steps, " \
    # #                      f"which each step is the individual action."
    # #     return session_prompt
    # #
    # # @staticmethod
    # # def get_step_splitting_initial_messages(bugs=None):
    # #     session_prompt = Constructor.get_step_splitting_session_prompt()
    # #     qa_pairs = None
    # #     if bugs:
    # #         qa_pairs = Constructor.convert_step_splitting_instances_into_qa_pairs(bugs)
    # #     messages = LLMUtil.get_messages_for_turbo(session_prompt, qa_pairs)
    # #     return messages
    # #
    # # @staticmethod
    # # def question_for_step_splitting(bug):
    # #     return f"Steps-To-Reproduce:\n{bug.description.steps_to_reproduce}\n\n" \
    # #            f"Please split 'Steps To Reproduce' section into steps, " \
    # #            f"which each step is the individual action." \
    # #            f"Please be careful not to exceed the given scope of the content."
    # #
    # # @staticmethod
    # # def answer_for_step_splitting(chains, outputs):
    # #     return f"Chains-of-Thought: {chains}\n\n" \
    # #            f"Outputs: {outputs}"
    # #
    # # @staticmethod
    # # def split_str_into_steps(bug, bugs=None):
    # #     messages = Constructor.get_step_splitting_initial_messages(bugs)
    # #     # extract summary
    # #     question = Constructor.question_for_step_splitting(bug)
    # #     messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_USER, question, messages)
    # #     # print(self.summary_question)
    # #     # input()
    # #     answer = LLMUtil.ask_turbo(messages)
    # #     messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_ASSISTANT, answer, messages)
    # #
    # #     LLMUtil.show_messages(messages)
    # #     # desc_question, desc_answer = LLMUtil.question_answer(self.desc_question)
    # #     # print(summary_question)
    # #     # print(summary_answer)
    # #     # print(desc_question)
    # #     # print(desc_answer)
    # #     # answer = Answer.from_answer(summary_pair, summary_answer, desc_answer)
    # #     # raw_answer = RawAnswer(summary_pair,
    # #     #                        QA(self.summary_question, summary_answer),
    # #     #                        QA(self.desc_question, desc_answer))
    # #
    # #     return answer
