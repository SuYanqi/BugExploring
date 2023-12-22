import copy
import json

from bug_improving.event_extraction.placeholder import Placeholder
from bug_improving.types.bug import Bugs
from bug_improving.utils.llm_util import LLMUtil


class ScenarioModifier:
    def __init__(self):
        pass

    @staticmethod
    def convert_instances_into_qa_pairs(bugs):
        qa_pairs = []
        if Placeholder.SCENARIO_MODIFIER_INSTANCES:
            for instance_dict in Placeholder.SCENARIO_MODIFIER_INSTANCES:
                # print(instance_dict['bug_id'])
                bug = bugs.get_bug_by_id(int(instance_dict['bug_id']))
                question = ScenarioModifier.question_for_modified_scenario(bug)
                answer = ScenarioModifier.answer_for_modified_scenario(instance_dict['output'])
                qa_pairs.append((question, answer))
        return qa_pairs

    @staticmethod
    def get_session_prompt():
        session_prompt = f"I am a scenario modifier. " \
                         f"I can generate the variants of the given {Placeholder.SCENARIO} based on the specific rules."
        return session_prompt

    @staticmethod
    def get_initial_messages(bugs=None):
        session_prompt = ScenarioModifier.get_session_prompt()
        qa_pairs = None
        if bugs:
            qa_pairs = ScenarioModifier.convert_instances_into_qa_pairs(bugs)
        messages = LLMUtil.get_messages_for_turbo(session_prompt, qa_pairs)
        return messages

    @staticmethod
    def question_for_modified_scenario(bug):
        question = f"{Placeholder.SCENARIO}:\n{bug.get_scenario()}\n" \
                   f"Please generate the variants based on the given rules:\n\t" \
                   f"a. {Placeholder.GENERALIZATION[0]}: {Placeholder.GENERALIZATION[1]}\n\t" \
                   f"b. {Placeholder.PRECONDITIONS_VARIANTS[0]}: {Placeholder.PRECONDITIONS_VARIANTS[1]}\n\t" \
                   f"c. {Placeholder.STEP_VARIANTS[0]}: {Placeholder.STEP_VARIANTS[1]}"
        return question

    @staticmethod
    def answer_for_modified_scenario(outputs):
        return f"{outputs}"

    @staticmethod
    def modify_scenario(bug=None, bugs=None):
        # if messages is None:
        messages = ScenarioModifier.get_initial_messages(bugs)
        # extract summary
        question = ScenarioModifier.question_for_modified_scenario(bug)
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


class ScenarioLinker:
    def __init__(self):
        pass

    @staticmethod
    def convert_instances_into_qa_pairs(bugs):
        """
        @todo: Placeholder.SCENARIO_LEVEL_INSTANCES
        @param bugs:
        @type bugs:
        @return:
        @rtype:
        """
        qa_pairs = []
        if Placeholder.SCENARIO_LEVEL_INSTANCES:
            for instance_dict in Placeholder.SCENARIO_LEVEL_INSTANCES:
                bug1 = bugs.get_bug_by_id(int(instance_dict['bug_id_pair'][0]))
                bug2 = bugs.get_bug_by_id(int(instance_dict['bug_id_pair'][1]))
                question = ScenarioLinker.question_for_linked_scenario((bug1, bug2))
                output = copy.deepcopy(instance_dict['output'])
                answer = ScenarioLinker.answer_for_linked_scenario((bug1, bug2), output)
                qa_pairs.append((question, answer))
        return qa_pairs

    @staticmethod
    def get_session_prompt():
        session_prompt = f"I am a scenario generator. " \
                         f"I can generate new scenarios based on the given scenarios. " \
            # f"Note that all these scenarios are executed on the Firefox browser."

        return session_prompt

    @staticmethod
    def get_initial_messages(bugs=None):
        session_prompt = ScenarioLinker.get_session_prompt()
        qa_pairs = None
        if bugs:
            qa_pairs = ScenarioLinker.convert_instances_into_qa_pairs(bugs)
        messages = LLMUtil.get_messages_for_turbo(session_prompt, qa_pairs)
        return messages

    @staticmethod
    def get_chunk_combination(bug_pair):
        s2r_1 = []
        s2r_1.extend(bug_pair[0].description.steps_to_reproduce)
        s2r_1.extend(bug_pair[1].description.steps_to_reproduce)
        s2r_2 = []
        s2r_2.extend(bug_pair[1].description.steps_to_reproduce)
        s2r_2.extend(bug_pair[0].description.steps_to_reproduce)
        return [s2r_1, s2r_2]

    @staticmethod
    def get_steps_for_chunk_combination(chunk, with_step_cluster=True):
        steps = []
        for step in chunk:
            if with_step_cluster:
                steps.append({
                    Placeholder.STEP: step.text,
                    Placeholder.STEP_CLUSTER: step.cluster_index
                })
            else:
                steps.append(step.text)
        return steps

    @staticmethod
    def question_for_linked_scenario(bug_pair):
        scenario1 = f"Bug{bug_pair[0].id}_{Placeholder.SCENARIO}"
        scenario2 = f"Bug{bug_pair[1].id}_{Placeholder.SCENARIO}"
        question = f"{scenario1}:\n{bug_pair[0].get_scenario()}"
        question = question + "\n\n" + f"{scenario2}:\n{bug_pair[1].get_scenario()}"
        # question = f"Scenario1:\n{bug_pair[0].description.text}"
        # question = question + "\n\n" + f"Scenario2:\n{bug_pair[1].description.text}"
        # question = question + "\n\n" + "First, please analyse the given scenarios and display the chains-of-thought.\n" \
        #                                "Second, please generate a new Scenario " \
        #                                "by appending the scenario from Scenario2 to Scenario1."
        chunk_combinations = ScenarioLinker.get_chunk_combination(bug_pair)
        question = question + "\n\n" + f"{scenario1} and {scenario2} can generate {len(chunk_combinations)} potential new {Placeholder.STEPS_TO_REPRODUCE} " \
                                       f"by linking {scenario1} and {scenario2} " \
                                       f"(i.e., {scenario1} + {scenario2} and {scenario2} + {scenario1}), as follows:\n"
        for index, chunk in enumerate(chunk_combinations):
            if index == 0:
                generated_method = f"{scenario1} + {scenario2}"
            else:
                generated_method = f"{scenario2} + {scenario1}"
            question = question + "\n\n" + f"{Placeholder.STEPS_TO_REPRODUCE}{index}: \n\t" \
                                           f"{Placeholder.GENERATED_METHOD}: " \
                                           f"{generated_method}\n\t" \
                                           f"{Placeholder.STEPS_TO_REPRODUCE}: " \
                                           f"{ScenarioLinker.get_steps_for_chunk_combination(chunk)}"
        question = question + f"\n\nValidate the feasibility of the potential {Placeholder.STEPS_TO_REPRODUCE}, details as follows:\n" \
                              f"""
For each potential set of steps to reproduce:
    if StepsToReproduce is feasible:
        if StepsInConnectingPart are redundant:
            Remove one of the redundant steps
        else:
            if StepsInConnectingPart involve opening Firefox:
                if No ClosingFirefoxStep before the OpeningFirefoxStep:
                    Remove OpeningFirefoxStep
        Generate a complete Scenario for feasible StepsToReproduce
    else:
        Remove the infeasible StepsToReproduce
""" \
            # f"For feasible {Placeholder.STEPS_TO_REPRODUCE}, generate a complete {Placeholder.SCENARIO}.\n" \
        # f"It is important to note that all of these scenarios are executed exclusively on the Firefox browser. " \
        # f"With the exception of closing Firefox, all other operations are performed while keeping Firefox open. "
        # question = question + "\n\n" + f"Please generate new scenarios " \
        #                                f"by linking {Placeholder.SCENARIO}1 and {Placeholder.SCENARIO}2 " \
        #                                f"(i.e., {Placeholder.SCENARIO}1 + {Placeholder.SCENARIO}2 and {Placeholder.SCENARIO}2 + {Placeholder.SCENARIO}1)." \
        # f"Note that during the scenario generation: \n\t" \
        # f"a. please remove the redundant steps. \n\t" \
        # f"b. if the new scenario is meaningless and cannot be executed, then dismiss it." \
        # f"\nPlease answer in the format of a JSON string." \
        # "Please answer in the format of a List: [{},]"
        # "(If the generated scenario doesn't make sense, then the generated scenario is None.)"
        # question = question + "\n" + "The generated scenario:\n"
        return question

    @staticmethod
    def get_step_dicts(bug_pair, s2r):
        steps = []
        bugs = Bugs([bug_pair[0], bug_pair[1]])
        # print(s2r)
        for bug_id, step_id_0, step_id_1 in s2r:
            bug = bugs.get_bug_by_id(bug_id)
            steps.extend(bug.description.steps_to_reproduce[step_id_0: step_id_1 + 1])

        step_dicts = []
        for step in steps:
            step_dicts.append(step.convert_step_into_step_dict())
        return step_dicts

    @staticmethod
    def answer_for_linked_scenario(bug_pair, outputs):
        """
        @param bug_pair:
        @type bug_pair:
        @param outputs:
        @type outputs:
        @param chains:
        @type chains:
        @return:
        @rtype:
        """
        # print(outputs[Placeholder.SCENARIOS])
        for output in outputs[Placeholder.SCENARIOS]:
            # print(output)
            # print(output[Placeholder.STEPS_TO_REPRODUCE])
            output[Placeholder.STEPS_TO_REPRODUCE] = ScenarioLinker. \
                get_step_dicts(bug_pair, output[Placeholder.STEPS_TO_REPRODUCE])
            # print(output[Placeholder.STEPS_TO_REPRODUCE])
        return json.dumps(outputs)

    @staticmethod
    def link_scenario(bug_pair=None, bugs=None, model_name=LLMUtil.GPT4_MODEL_NAME, temperature=0.2):
        messages = ScenarioLinker.get_initial_messages(bugs)
        # extract summary
        question = ScenarioLinker.question_for_linked_scenario(bug_pair)
        messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_USER, question, messages)
        # print(self.summary_question)
        # input()
        answer = LLMUtil.ask_turbo(messages, model_name, temperature)
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


class ScenarioCombiner:
    def __init__(self):
        pass

    # @staticmethod
    # def convert_instances_into_qa_pairs(bugs, with_step_cluster):
    #     """
    #     @param with_step_cluster:
    #     @type with_step_cluster:
    #     @todo: Placeholder.STEP_LEVEL_INSTANCES
    #     @param bugs:
    #     @type bugs:
    #     @return:
    #     @rtype:
    #     """
    #     qa_pairs = []
    #     if Placeholder.STEP_LEVEL_INSTANCES:
    #         for instance_dict in Placeholder.STEP_LEVEL_INSTANCES:
    #             bug1 = bugs.get_bug_by_id(int(instance_dict['bug_id_pair'][0]))
    #             bug2 = bugs.get_bug_by_id(int(instance_dict['bug_id_pair'][1]))
    #             question = ScenarioCombiner.question_for_combined_scenario((bug1, bug2), with_step_cluster)
    #             answer = ScenarioCombiner.answer_for_combined_scenario(instance_dict['output'])
    #             qa_pairs.append((question, answer))
    #     return qa_pairs
    #
    # @staticmethod
    # def get_session_prompt():
    #     session_prompt = f"I am a scenario generator. " \
    #                      f"I can generate new scenarios based on the given scenarios."
    #     return session_prompt
    #
    # @staticmethod
    # def get_initial_messages(bugs=None, with_step_cluster=True):
    #     session_prompt = ScenarioCombiner.get_session_prompt()
    #     qa_pairs = None
    #     if bugs:
    #         qa_pairs = ScenarioCombiner.convert_instances_into_qa_pairs(bugs, with_step_cluster)
    #     messages = LLMUtil.get_messages_for_turbo(session_prompt, qa_pairs)
    #     return messages
    #
    # @staticmethod
    # def question_for_combined_scenario(bug_pair, with_step_cluster=True):
    #     question = f"{Placeholder.SCENARIO}1:\n{bug_pair[0].get_scenario(with_step_cluster)}"
    #     question = question + "\n\n" + f"{Placeholder.SCENARIO}2:\n{bug_pair[1].get_scenario(with_step_cluster)}"
    #     # question = f"Scenario1:\n{bug_pair[0].description.text}"
    #     # question = question + "\n\n" + f"Scenario2:\n{bug_pair[1].description.text}"
    #     # question = question + "\n\n" + "First, please analyse the given scenarios and display the chains-of-thought.\n" \
    #     #                                "Second, please generate a new Scenario " \
    #     #                                "by appending the scenario from Scenario2 to Scenario1."
    #     question = question + "\n\n" + f"Please generate new scenarios " \
    #                                    f"by combining {Placeholder.SCENARIO}1 and {Placeholder.SCENARIO}2 " \
    #                                    f"based on the shared steps (i.e., steps with the same {Placeholder.STEP_CLUSTER}). " \
    #                                    f"In detail, we generate new {Placeholder.SCENARIOS} as follows:\n" \
    #                                    f"For each shared step (i.e., {Placeholder.SHARED_STEP}):\n\t" \
    #                                    f"a) get the steps before {Placeholder.SHARED_STEP} in {Placeholder.SCENARIO}1, namely {Placeholder.SCENARIO1_STEPS};\n\t" \
    #                                    f"b) get the steps after {Placeholder.SHARED_STEP} in {Placeholder.SCENARIO}2, namely {Placeholder.SCENARIO2_STEPS};\n\t" \
    #                                    f"c) concatenate the steps {Placeholder.SCENARIO1_STEPS}, {Placeholder.SHARED_STEP} and {Placeholder.SCENARIO2_STEPS} as the {Placeholder.STEPS_TO_REPRODUCE} of the new {Placeholder.SCENARIO};\n\t" \
    #                                    f"d) By swapping the position of {Placeholder.SCENARIO}1 and {Placeholder.SCENARIO}2 and repeating the step a) - c), we get another new {Placeholder.SCENARIO}.\n" \
    #                                    f"Note that during the scenario generation: \n\t" \
    #                                    f"a. if the new {Placeholder.SCENARIO} is meaningless and cannot be executed, then dismiss it.\n\t" \
    #                                    f"b. please do not generate the same {Placeholder.SCENARIOS} as the given {Placeholder.SCENARIOS}.\n\t" \
    #                                    f"c. please do not generate duplicate {Placeholder.SCENARIOS}.\n\t"
    #     # f"based on the steps with the same cluster.\n" \
    #     return question
    #
    # @staticmethod
    # def answer_for_combined_scenario(outputs):
    #     """
    #     @param outputs:
    #     @type outputs:
    #     @param chains:
    #     @type chains:
    #     @return:
    #     @rtype:
    #     """
    #     # if chains:
    #     #     return f"Chains-of-Thought: {chains}\n\n" \
    #     #            f"Outputs: {outputs}"
    #     return f"{outputs}"
    #
    # @staticmethod
    # def combine_scenario(bug_pair=None, bugs=None, with_step_cluster=True, model_name=LLMUtil.TURBO_MODEL_NAME):
    #     messages = ScenarioCombiner.get_initial_messages(bugs, with_step_cluster)
    #     # extract summary
    #     question = ScenarioCombiner.question_for_combined_scenario(bug_pair, with_step_cluster)
    #     messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_USER, question, messages)
    #     # print(self.summary_question)
    #     # input()
    #     answer = LLMUtil.ask_turbo(messages, model_name)
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

    @staticmethod
    def convert_instances_into_qa_pairs(bugs, with_step_cluster):
        """
        @param with_step_cluster:
        @type with_step_cluster:
        @todo: Placeholder.STEP_LEVEL_INSTANCES
        @param bugs:
        @type bugs:
        @return:
        @rtype:
        """
        qa_pairs = []
        if Placeholder.STEP_LEVEL_INSTANCES:
            for instance_dict in Placeholder.STEP_LEVEL_INSTANCES:
                bug1 = bugs.get_bug_by_id(int(instance_dict['bug_id_pair'][0]))
                bug2 = bugs.get_bug_by_id(int(instance_dict['bug_id_pair'][1]))
                question = ScenarioCombiner.question_for_combined_scenario((bug1, bug2), with_step_cluster)
                output = copy.deepcopy(instance_dict['output'])
                answer = ScenarioCombiner.answer_for_combined_scenario((bug1, bug2), output)
                qa_pairs.append((question, answer))
        return qa_pairs

    @staticmethod
    def get_session_prompt():
        session_prompt = f"I am a scenario generator. " \
                         f"I can generate new scenarios based on the given scenarios."
        return session_prompt

    @staticmethod
    def get_initial_messages(bugs=None, with_step_cluster=True):
        session_prompt = ScenarioCombiner.get_session_prompt()
        qa_pairs = None
        if bugs:
            qa_pairs = ScenarioCombiner.convert_instances_into_qa_pairs(bugs, with_step_cluster)
        messages = LLMUtil.get_messages_for_turbo(session_prompt, qa_pairs)
        return messages

    @staticmethod
    def question_for_combined_scenario(bug_pair, with_step_cluster=True):
        scenario1 = f"Bug{bug_pair[0].id}_{Placeholder.SCENARIO}"
        scenario2 = f"Bug{bug_pair[1].id}_{Placeholder.SCENARIO}"
        question = f"{scenario1}:\n{bug_pair[0].get_scenario(with_step_cluster)}"
        question = question + "\n\n" + \
                   f"{scenario2}:\n{bug_pair[1].get_scenario(with_step_cluster)}"

        chunk_combinations = ScenarioCombiner.get_chunk_combination(bug_pair)
        if len(chunk_combinations) == 0:
            return None
        question = question + "\n\n" + f"{scenario1} and {scenario2} can generate " \
                                       f"{len(chunk_combinations)} potential new {Placeholder.STEPS_TO_REPRODUCE}, " \
                                       f"as follows:"
        for index, chunk in enumerate(chunk_combinations):
            question = question + "\n\n" + f"{Placeholder.STEPS_TO_REPRODUCE}{index}: \n\t" \
                                           f"{Placeholder.GENERATED_METHOD}: " \
                                           f"{ScenarioCombiner.get_explanation_for_chunk_combination(chunk)}\n\t" \
                                           f"{Placeholder.STEPS_TO_REPRODUCE}: " \
                                           f"{ScenarioCombiner.get_steps_for_chunk_combination(chunk)}"
            # question = question + json.dumps(
            #     {Placeholder.STEPS_TO_REPRODUCE: ScenarioCombiner.get_steps_for_chunk_combination(chunk)})
        question = question + f"\n\nValidate the feasibility of each potential {Placeholder.STEPS_TO_REPRODUCE}. " \
                              f"For each feasible {Placeholder.STEPS_TO_REPRODUCE}, " \
                              f"generate a complete {Placeholder.SCENARIO}."
        return question

    @staticmethod
    def get_step_dicts(bug_pair, s2r):
        steps = []
        bugs = Bugs([bug_pair[0], bug_pair[1]])
        for bug_id, step_id_0, step_id_1 in s2r:
            bug = bugs.get_bug_by_id(bug_id)
            steps.extend(bug.description.steps_to_reproduce[step_id_0: step_id_1 + 1])

        step_dicts = []
        for step in steps:
            step_dicts.append(step.convert_step_into_step_dict())
        return step_dicts

    @staticmethod
    def answer_for_combined_scenario(bug_pair, outputs):
        """
        @param bug_pair:
        @type bug_pair:
        @param outputs:
        @type outputs:
        @param chains:
        @type chains:
        @return:
        @rtype:
        """
        for output in outputs[Placeholder.SCENARIOS]:
            output[Placeholder.STEPS_TO_REPRODUCE] = ScenarioCombiner. \
                get_step_dicts(bug_pair, output[Placeholder.STEPS_TO_REPRODUCE])
        return json.dumps(outputs)

    @staticmethod
    def combine_scenario(bug_pair=None, bugs=None, with_step_cluster=True, model_name=LLMUtil.GPT4_MODEL_NAME):
        """
        @todo: if no chunk_combination, don't be into GPT4
        @param bug_pair:
        @type bug_pair:
        @param bugs:
        @type bugs:
        @param with_step_cluster:
        @type with_step_cluster:
        @param model_name:
        @type model_name:
        @return:
        @rtype:
        """
        messages = ScenarioCombiner.get_initial_messages(bugs, with_step_cluster)
        # extract summary
        question = ScenarioCombiner.question_for_combined_scenario(bug_pair, with_step_cluster)
        if question:
            messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_USER, question, messages)
            # print(self.summary_question)
            # input()
            answer = LLMUtil.ask_turbo(messages, model_name)
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
        return str({Placeholder.CHAINS_OF_THOUGHT: [], Placeholder.SCENARIOS: []}), None

    @staticmethod
    def get_shared_step_cluster_indexes(bug_pair):
        """
        @todo: remove non-operation shared step
        @param bug_pair:
        @type bug_pair:
        @return:
        @rtype:
        """
        step_cluster_indexes_0 = bug_pair[0].description.get_step_cluster_index_set()
        step_cluster_indexes_1 = bug_pair[1].description.get_step_cluster_index_set()
        shared_step_cluster_indexes = step_cluster_indexes_0.intersection(step_cluster_indexes_1)
        return shared_step_cluster_indexes

    # @staticmethod
    # def get_cluster_list_from_chunk(chunk):
    #     shared_step = chunk[0]
    #     pre_steps = chunk[1]
    #     next_steps = chunk[2]
    #     pre_step_cluster_indexes = []
    #     next_step_cluster_indexes = []
    #     for pre_step in pre_steps:
    #         pre_step_cluster_indexes.append(pre_step.cluster_index)
    #     for next_step in next_steps:
    #         next_step_cluster_indexes.append(next_step.cluster_index)
    #
    #     return shared_step.cluster_index, pre_step_cluster_indexes, next_step_cluster_indexes

    @staticmethod
    def get_cluster_list_from_step_id(bug, step_id):
        # print(type(step_id))
        pre_step_cluster_indexes = []
        next_step_cluster_indexes = []
        for pre_step in bug.description.steps_to_reproduce[0: step_id]:
            pre_step_cluster_indexes.append(pre_step.cluster_index)
        for next_step in bug.description.steps_to_reproduce[step_id + 1:]:
            next_step_cluster_indexes.append(next_step.cluster_index)
        # print(step_id)
        # print(pre_step_cluster_indexes)
        # print(next_step_cluster_indexes)
        return pre_step_cluster_indexes, next_step_cluster_indexes

    @staticmethod
    def get_cluster_list_from_chunk(chunk):
        cluster_list = []
        bug_0, shared_step_id_0, bug_1, shared_step_id_1 = chunk
        for step in bug_0.description.steps_to_reproduce[0:shared_step_id_0]:
            cluster_list.append(step.cluster_index)
        # cluster_list.append(bug_0.description.steps_to_reproduce[shared_step_id_0].cluster_index)
        for step in bug_1.description.steps_to_reproduce[shared_step_id_1:]:
            cluster_list.append(step.cluster_index)
        return cluster_list

    @staticmethod
    def check_chunk_existing_or_not(chunk, chunk_list, bug_0, bug_1):
        chunk_cluster_list = ScenarioCombiner.get_cluster_list_from_chunk(chunk)
        chunk_list_cluster_list = []
        for chunk in chunk_list:
            chunk_list_cluster_list.append(ScenarioCombiner.get_cluster_list_from_chunk(chunk))
        chunk_list_cluster_list.append(bug_0.description.get_step_cluster_index_list())
        chunk_list_cluster_list.append(bug_1.description.get_step_cluster_index_list())
        # print(chunk_cluster_list)
        # print(chunk_list_cluster_list)
        if chunk_cluster_list in chunk_list_cluster_list:
            return True
        return False

    @staticmethod
    def filter_chunk_combination(chunk, all_chunks):
        """
        @param bug_0:
        @type bug_0:
        @param shared_step_ids_0:
        @type shared_step_ids_0:
        @param bug_1:
        @type bug_1:
        @param shared_step_ids_1:
        @type shared_step_ids_1:
        @return: chunk_combination
        @rtype: (bug_0, shared_step_id_0, bug_1, shared_step_id_1)
        """
        bug_0, shared_step_ids_0, bug_1, shared_step_ids_1 = chunk
        # all_chunks = []
        for shared_step_id_0 in shared_step_ids_0:
            for shared_step_id_1 in shared_step_ids_1:
                pre_cluster_indexes_0, next_cluster_indexes_0 = ScenarioCombiner. \
                    get_cluster_list_from_step_id(bug_0, shared_step_id_0)
                # print(shared_step_id_0)
                # print(pre_cluster_indexes_0)
                # print(next_cluster_indexes_0)
                pre_cluster_indexes_1, next_cluster_indexes_1 = ScenarioCombiner. \
                    get_cluster_list_from_step_id(bug_1, shared_step_id_1)
                if pre_cluster_indexes_0 != pre_cluster_indexes_1 and next_cluster_indexes_0 != next_cluster_indexes_1:
                    chunk_0 = (bug_0, shared_step_id_0, bug_1, shared_step_id_1)
                    chunk_1 = (bug_1, shared_step_id_1, bug_0, shared_step_id_0)

                    if not ScenarioCombiner.check_chunk_existing_or_not(chunk_0, all_chunks, bug_0, bug_1):
                        all_chunks.append(chunk_0)
                    if not ScenarioCombiner.check_chunk_existing_or_not(chunk_1, all_chunks, bug_0, bug_1):
                        all_chunks.append(chunk_1)
        return all_chunks

    @staticmethod
    def get_chunk_combination(bug_pair):
        all_chunk_combination = []
        shared_step_cluster_indexes = ScenarioCombiner.get_shared_step_cluster_indexes(bug_pair)
        # print(shared_step_cluster_indexes)
        for shared_step_cluster_index in shared_step_cluster_indexes:
            # chunks_0 = bug_pair[0].description.chunk_steps_by_cluster_index(shared_step_cluster_index)
            # chunks_1 = bug_pair[1].description.chunk_steps_by_cluster_index(shared_step_cluster_index)
            shared_step_ids_0 = bug_pair[0].description.get_step_ids_by_cluster_index(shared_step_cluster_index)
            shared_step_ids_1 = bug_pair[1].description.get_step_ids_by_cluster_index(shared_step_cluster_index)
            # print(shared_step_ids_0)
            # print(shared_step_ids_1)
            chunk = (bug_pair[0], shared_step_ids_0, bug_pair[1], shared_step_ids_1)
            all_chunk_combination = ScenarioCombiner.filter_chunk_combination(chunk, all_chunk_combination)
            # all_chunk_combination.extend(chunk_combination)
        return all_chunk_combination

    @staticmethod
    def get_explanation_for_chunk_combination(chunk):
        bug_0, shared_step_index_0, bug_1, shared_step_index_1 = chunk
        if shared_step_index_0 != 0 and shared_step_index_1 != len(bug_1.description.steps_to_reproduce) - 1:
            explanation = f"The shared {Placeholder.STEP} is " \
                          f"'{bug_0.description.steps_to_reproduce[shared_step_index_0].text}'. " \
                          f"The new potential scenario is generated by " \
                          f"combining {Placeholder.STEP} 1 - {shared_step_index_0} from Bug{bug_0.id} and " \
                          f"the shared {Placeholder.STEP} and " \
                          f"{Placeholder.STEP} {shared_step_index_1 + 2} - {len(bug_1.description.steps_to_reproduce)} " \
                          f"from Bug{bug_1.id}."
        elif shared_step_index_0 == 0 and shared_step_index_1 != len(bug_1.description.steps_to_reproduce) - 1:
            explanation = f"The shared {Placeholder.STEP} is " \
                          f"'{bug_0.description.steps_to_reproduce[shared_step_index_0].text}'. " \
                          f"The new potential scenario is generated by " \
                          f"combining the shared {Placeholder.STEP} and " \
                          f"{Placeholder.STEP} {shared_step_index_1 + 2} - {len(bug_1.description.steps_to_reproduce)} " \
                          f"from Bug{bug_1.id}."
        elif shared_step_index_0 != 0 and shared_step_index_1 == len(bug_1.description.steps_to_reproduce) - 1:
            explanation = f"The shared {Placeholder.STEP} is " \
                          f"'{bug_0.description.steps_to_reproduce[shared_step_index_0].text}'. " \
                          f"The new potential scenario is generated by " \
                          f"combining {Placeholder.STEP} 1 - {shared_step_index_0} from Bug{bug_0.id} and " \
                          f"the shared {Placeholder.STEP}."
        elif shared_step_index_0 == 0 and shared_step_index_1 == len(bug_1.description.steps_to_reproduce) - 1:
            explanation = f"The shared {Placeholder.STEP} is " \
                          f"'{bug_0.description.steps_to_reproduce[shared_step_index_0].text}'. " \
                          f"The new potential scenario is generated by the shared {Placeholder.STEP}."
        else:
            explanation = ""

        return json.dumps(explanation)

    @staticmethod
    def get_steps_for_chunk_combination(chunk):
        bug_0, shared_step_index_0, bug_1, shared_step_index_1 = chunk
        steps = []
        for step in bug_0.description.steps_to_reproduce[0:shared_step_index_0]:
            steps.append(step.text)

        # steps.extend(bug_0.description.steps_to_reproduce[0:shared_step_index_0])
        steps.append(bug_0.description.steps_to_reproduce[shared_step_index_0].text)
        for step in bug_1.description.steps_to_reproduce[shared_step_index_1 + 1:]:
            steps.append(step.text)
        # steps.extend(bug_1.description.steps_to_reproduce[shared_step_index_1+1:])
        return json.dumps(steps)


class Generator:
    def __init__(self):
        pass

    @staticmethod
    def get_scenario_level_question(bug_pair):
        question = f"Scenario1:\n{bug_pair[0].get_steps_string()}"
        question = question + "\n\n" + f"Scenario2:\n{bug_pair[1].get_steps_string()}"
        # question = question + "\n\n" + "First, please analyse the given scenarios and display the chains-of-thought.\n" \
        #                                "Second, please generate a new Scenario " \
        #                                "by appending the scenario from Scenario2 to Scenario1."
        question = question + "\n\n" + "Please process the Chains-of-Thought and then generate a new Scenario " \
                                       "by appending the scenario from Scenario2 to Scenario1. " \
                                       "(If the generated scenario doesn't make sense, then the generated scenario is None.)"
        # question = question + "\n" + "The generated scenario:\n"
        return question

    @staticmethod
    def get_answer(output, chains=None):
        answer = ""
        if chains is not None:
            answer = answer + f"Chains-of-Thought: \n{chains}\n\n"
        answer = answer + f"Generated scenario: \n{output}"
        return answer

    @staticmethod
    def get_scenario_level_instances(bugs, with_chains=True):
        """
        [
        (1678633, 1587737): redundant steps
        (1678633, 1575516): redundant steps, logistic problem
        ]
        @return: [(Q(example input), A(chain-of-thought, example output))]
        @rtype:
        """
        instance_list = []
        for instance_dict in Placeholder.SCENARIO_LEVEL_INSTANCES:
            bug1 = bugs.get_bug_by_id(instance_dict["bug_id_pair"][0])
            bug2 = bugs.get_bug_by_id(instance_dict["bug_id_pair"][1])
            question = Generator.get_scenario_level_question((bug1, bug2))
            chains = instance_dict["chains"]
            output = instance_dict["output"]
            if with_chains:
                answer = Generator.get_answer(output, chains)
            else:
                answer = Generator.get_answer(output)
            instance_list.append((question, answer))
        return instance_list

    @staticmethod
    def get_step_level_instances():
        pass

    @staticmethod
    def generate_dramas():
        pass

    @staticmethod
    def generate_scenario_level_dramas(test_bug_pair, bugs, with_chains):
        session_prompt = "I am a generator. I can generate new scenarios based on the given scenarios."
        instances = Generator.get_scenario_level_instances(bugs, with_chains)
        messages = LLMUtil.get_messages_for_turbo(session_prompt, instances)
        question = Generator.get_scenario_level_question(test_bug_pair)
        messages = LLMUtil.add_role_content_dict_into_messages(LLMUtil.ROLE_USER, question, messages)
        LLMUtil.show_messages(messages)

    @staticmethod
    def generate_step_level_dramas():
        pass
