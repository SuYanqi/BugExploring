class Placeholder:
    URL = "PLH_URL_"
    CONCEPT = "CONCEPT_"

    # TAG_STEPS_TO_REPRODUCE = ["<STEPS_TO_REPRODUCE>", "</STEPS_TO_REPRODUCE>"]

    # the Tag is from html
    CATEGORY_TAG_DICT = {'RadioButton': ["radio"], "Checkbox": ["checkbox"], "Button": ["button"],
                         'Dropdown': ["menuitem", "option"],
                         'Panel': ["richlistitem", "appmenuitem"],
                         'TextField': ["textbox", "input"],
                         'Hyperlink': ["a", "link"],
                         'Text': ["title", "description", "subtitle", "header", "treecol", "message", "text",
                                  "heading",
                                  # "instruction", "intro",
                                  "label"],
                         # 'Icon': ["icon", "img"],  # new added
                         "Page": [],
                         "Key": [],
                         "App": [],
                         "Others": [],
                         }

    # APP_ALIAS = ['Firefox', 'browser', 'Nightly', 'Firefox browser', 'the Latest Nightly browser', 'Latest Nightly']

    ACTION_DICT = {'click': {'alias': ['click on'], },
                   'right click': {'alias': [], },
                   'check': {'alias': [], },
                   'uncheck': {'alias': [], },
                   # 'toggle': {'alias': [], },
                   'tick': {'alias': [], },
                   'untick': {'alias': [], },
                   'enable': {'alias': [], },
                   'disable': {'alias': [], },
                   'go to': {'alias': ['navigate to', 'access', 'visit']},
                   'open': {'alias': ['start', 'launch']},
                   'close': {'alias': []},
                   'quit': {'alias': []},
                   'restart': {'alias': []},
                   'refresh': {'alias': []},
                   'select': {'alias': ['choose']},
                   'hold': {'alias': []},
                   'release': {'alias': []},
                   'drag': {'alias': []},
                   'hover': {'alias': ['hover the cursor above', 'hover over']},
                   'press': {'alias': []},
                   # 'scroll': {'alias': ['scroll to']},
                   'scroll up': {'alias': ['scroll up to', 'scroll up until']},
                   'scroll down': {'alias': ['scroll down to', 'scroll down until']},
                   'observe': {'alias': ['inspect', 'see']},
                   'freeze': {'alias': []},
                   'return to': {'alias': ['go back to', 'switch back to', 'focus back to']},
                   'switch': {'alias': ['switch to']},
                   'type': {'alias': ['enter', 'fill']},
                   'change': {'alias': []},
                   'resize': {'alias': []},
                   }

    CATEGORY_ACTION_RELATION_DICT = {
        'RadioButton': {'check': {'equivalent': ['click', 'tick', 'enable'],
                                  'opposite': ['uncheck', 'untick', 'disable']},
                        'uncheck': {'equivalent': ['untick', 'disable'],
                                    'opposite': ['check', 'click', 'tick', 'enable']},
                        },
        "Checkbox": {'check': {'equivalent': ['click', 'tick', 'enable'],
                               'opposite': ['uncheck', 'untick', 'disable']},
                     'uncheck': {'equivalent': ['untick', 'disable'],
                                 'opposite': ['check', 'click', 'tick', 'enable']},
                     },
        "Button": {'click': {'equivalent': [],
                             'opposite': []},
                   'hold': {'equivalent': [],
                            'opposite': ['release']},
                   'release': {'equivalent': [],
                               'opposite': ['hold']},
                   'hover': {'equivalent': [],
                             'opposite': []},
                   'scroll up': {'equivalent': [],
                                 'opposite': ['scroll down']},
                   'scroll down': {'equivalent': [],
                                   'opposite': ['scroll up']},
                   'observe': {'equivalent': ['check'],
                               'opposite': []},
                   },
        'Dropdown': {'click': {'equivalent': [],
                               'opposite': []},
                     'select': {'equivalent': [],
                                'opposite': []},
                     # 'hold': {'equivalent': [],
                     #          'opposite': ['release']},
                     # 'release': {'equivalent': [],
                     #             'opposite': ['hold']},
                     'hover': {'equivalent': [],
                               'opposite': []},
                     # 'scroll up': {'equivalent': [],
                     #               'opposite': ['scroll down']},
                     # 'scroll down': {'equivalent': [],
                     #                 'opposite': ['scroll up']},
                     'observe': {'equivalent': ['check'],
                                 'opposite': []},
                     },
        'Panel': {'click': {'equivalent': [],
                            'opposite': []},
                  'select': {'equivalent': [],
                             'opposite': []},
                  'observe': {'equivalent': ['check'],
                              'opposite': []},
                  },
        'TextField': {'click': {'equivalent': [],
                                'opposite': []},
                      'right click': {'equivalent': [],
                                      'opposite': []},
                      'type': {'equivalent': [],
                               'opposite': []},
                      },
        'Hyperlink': {'click': {'equivalent': [],
                                'opposite': []},
                      'right click': {'equivalent': [],
                                      'opposite': []},
                      'hover': {'equivalent': [],
                                'opposite': []},
                      'observe': {'equivalent': ['check'],
                                  'opposite': []},
                      },
        'Text': {'observe': {'equivalent': ['check'],
                             'opposite': []},
                 'scroll up': {'equivalent': [],
                               'opposite': ['scroll down']},
                 'scroll down': {'equivalent': [],
                                 'opposite': ['scroll up']},
                 'go to': {'equivalent': ['switch'],
                           'opposite': []},
                 },
        "Page": {'go to': {'equivalent': ['open'],
                           'opposite': ['close']},
                 'close': {'equivalent': [],
                           'opposite': ['open', 'go to']},
                 'observe': {'equivalent': ['check'],
                             'opposite': []},
                 'refresh': {'equivalent': [],
                             'opposite': []},
                 'return to': {'equivalent': [],
                               'opposite': []},
                 'switch': {'equivalent': [],
                            'opposite': []},
                 'resize': {'equivalent': [],
                            'opposite': []},
                 },
        "Key": {'press': {'equivalent': ['type'],
                          'opposite': []},
                },
        "App": {
            # 'click': {'equivalent': ['open'],
            #           'opposite': ['close']},
            'open': {'equivalent': ['click'],  # click?
                     'opposite': ['close', 'quit']},
            'close': {'equivalent': ['quit'],
                      'opposite': ['open', 'click']},
            'restart': {'equivalent': [],
                        'opposite': ['close', 'quit']},
            'freeze': {'equivalent': [],
                       'opposite': []},
        },
        "Others": {},
    }

    # "label", "placeholder", "aria-label", "tooltiptext", "labelnotsyncing", "labelsyncing"
    # ATTRIBUTE_IDS = ["label", "placeholder", "tooltiptext"]
    ATTRIBUTE_IDS = ["label", "placeholder", "tooltiptext", "title"]

    """
    external knowledge:
        Category-> Key: Keyboard shortcuts: https://support.mozilla.org/en-US/kb/keyboard-shortcuts-perform-firefox-tasks-quickly    
         
    """
    EXTERNAL_KNOWLEDGE_DICT = {
        # keyboard shortcuts
        'Key': {
            # Current Page
            "Tab": {'alias': [],
                    'related_concepts': ["Shift+Tab", ], },  # Focus Next Link or Input Field
            "Shift+Tab": {'alias': [],
                          'related_concepts': ["Tab", ], },  # Focus Previous Link or Input Field
            "Command+P": {'alias': ["Command-P", ],
                          'related_concepts': [], },  # Print
            "Command+S": {'alias': [],
                          'related_concepts': [], },  # Save Page As
        },

        # maybe don't need this category
        'App': {
            "Firefox": {'alias': ['Firefox', 'browser', 'Nightly', 'Firefox browser', 'the Latest Nightly browser',
                                  'Latest Nightly'],
                        'related_concepts': [], },
        }

    }

    VARIANTS = 'VARIANTS'
    ORIGINAL = "ORIGINAL"
    VARIANT = 'VARIANT'
    STEP_IDS = 'STEP_IDS'
    # PRECONDITIONS_VARIANTS = 'PRECONDITIONS_VARIANTS'
    # STEP_VARIANTS = 'STEP_VARIANTS'
    # GENERALIZATION = 'GENERALIZATION'

    SUMMARY = 'SUMMARY'
    PRECONDITIONS = 'PRECONDITIONS'
    STEPS_TO_REPRODUCE = 'STEPS_TO_REPRODUCE'
    EXPECTED_RESULTS = 'EXPECTED_RESULTS'
    ACTUAL_RESULTS = 'ACTUAL_RESULTS'
    NOTES = 'NOTES'
    AFFECTED_VERSIONS = 'AFFECTED_VERSIONS'
    AFFECTED_PLATFORMS = 'AFFECTED_PLATFORMS'
    OTHERS = 'OTHERS'

    STEP = 'STEP'
    STEP_CLUSTER = 'STEP_CLUSTER'
    STEP_TYPE = 'STEP_TYPE'
    # SPECIFIC_OPERATION = 'SPECIFIC_OPERATION'
    # GENERIC_OPERATION = 'GENERIC_OPERATION'
    OPERATION = 'OPERATION'
    NON_OPERATION = 'NON_OPERATION'

    SHARED_STEP = 'SHARED_STEP'
    SCENARIO1_STEPS = 'SCENARIO1_STEPS'
    SCENARIO2_STEPS = 'SCENARIO2_STEPS'

    GENERATED_METHOD = 'GENERATED_METHOD'

    CHAINS_OF_THOUGHT = 'CHAINS_OF_THOUGHT'
    SCENARIO = 'SCENARIO'
    SCENARIOS = 'SCENARIOS'
    SCENARIO_LEVEL = 'SCENARIO_LEVEL'
    STEP_LEVEL = 'STEP_LEVEL'

    PRECONDITIONS_VARIANTS = (
        'PRECONDITIONS_VARIANTS',
        'negate the preconditions to test the execution of the scenario under opposite conditions.'
        # 'first, we check if there are any reverse preconditions. '
        # f'If reverse preconditions exist, we negate them and evaluate '
        # f'whether the negated preconditions enable the expected execution of '
        # f'the {STEPS_TO_REPRODUCE}. '
        # f'If they do not, no PRECONDITIONS_VARIANTS are generated.\n'
    )
    STEP_VARIANTS = (
        'STEP_VARIANTS',
        'replace the original steps with alternative steps that can achieve the same outcome.')
    GENERALIZATION = (
        'GENERALIZATION',
        'extract a GUI-agnostic oracle from the scenario that can be used to test similar cases.'
        # f'first, we try to derive the oracle from '
        # f'{EXPECTED_RESULTS} and {ACTUAL_RESULTS} directly to ensure higher generality '
        # f'due to the oracle not relying on specific steps or operations. '
        # f'However, if the oracle cannot be directly extracted from {EXPECTED_RESULTS} and '
        # f'{ACTUAL_RESULTS}, we need to rely on steps or operations to define the '
        # f'oracle to strike a balance between accuracy and generality. '
        # f'Note that we strive to generalize the steps and operations used as much as '
        # f'possible to ensure the maximum generality of the Oracle.\n'
    )

    # PREREQUISITES = "Preconditions"
    # STEPS_TO_REPRODUCE = "Steps To Reproduce"
    # EXPECTED_RESULTS = "Expected Results"
    # ACTUAL_RESULTS = "Actual Results"
    # NOTES = "Notes"

    # SCENARIO_LEVEL_INSTANCES = [
    #     {
    #         # (1678633, 1587737): redundant steps
    #         "bug_id_pair": (1678633, 1587737),
    #         "chains":
    #             # "1. Scenario1 is on
    #             # "2. Scenario2 is on
    #             # "3. logistic problem detection
    #             # "4. redundant steps detection
    #             #       "After executing Scenario1, the browser is still open, and the about:logins page is displayed. "
    #             #       "Therefore, the steps related to starting the browser and navigating to about:logins "
    #             #       "from Scenario2 are redundant and can be removed. ",
    #                   "After executing Scenario1, the browser is still open, and the about:logins page is displayed. "
    #                   "Therefore, the steps related to starting the browser and navigating to about:logins "
    #                   "from Scenario2 are redundant and can be removed. ",
    #         "output": "1. Navigate to the \"about:logins\" page."
    #                   "2. Go to the “about:preferences#sync” page using a new tab."
    #                   "3. Click on the “Sign Out...” button."
    #                   "4. check the “Delete data from this device” checkbox from the pop-up."
    #                   "5. Click on the “Sign Out” button from the pop-up."
    #                   "6. switch back to the “about:logins” tab."
    #                   "7. Observe the Login Item area."
    #                   "8. Click on the “Sign in to Sync” button."
    #                   "9. Enter the credentials from the prerequisites and log in."
    #                   "10. Go back to the “about:logins” page."
    #                   "11. observe the “Login List”."
    #     },
    #     {
    #         # (1678633, 1575516): redundant steps, logistic problem
    #         "bug_id_pair": (1678633, 1575516),
    #         "chains": "After executing Scenario1, the browser is still open, and the about:logins page is displayed. "
    #                   "Therefore, the steps related to starting the browser and navigating to about:logins "
    #                   "from Scenario2 are redundant and can be removed. "
    #                   "Additionally, Scenario1 has already signed out and deleted the data from this device. "
    #                   "So, there is no login item in about:logins page. "
    #                   "It is impossible to execute Scenario2 since it need to have at least one saved login.",
    #         "output": None
    #     },
    # ]

    # SCENARIO_MODIFIER_INSTANCES = [
    #     {
    #         "bug_id": 1571444,
    #         "output": {
    #             CHAINS_OF_THOUGHT: [
    #                 f'For this given scenario, the oracle directly extracted from '
    #                 f'{EXPECTED_RESULTS} and {ACTUAL_RESULTS} is "A no matching result message should '
    #                 f'be displayed but not", which is incomplete and meaningless without the operation '
    #                 f'"Perform a search that returns 0 results.". Therefore, the oracle is '
    #                 f'"A no matching result message should be displayed instead of no message'
    #                 f'if performing a search returns 0 results."',
    #                 f'The {PRECONDITIONS} is "Have a Firefox profile with multiple saved logins.". '
    #                 f'The variant of this {PRECONDITIONS} is '
    #                 f'"Have a Firefox profile without saved logins.". '
    #                 f'The {STEPS_TO_REPRODUCE} are '
    #                 f'on performing searching logins that returns 0 results on "about:logins" page. '
    #                 f'With this {PRECONDITIONS} variant, '
    #                 f'this {STEPS_TO_REPRODUCE} still can be executed. '
    #                 f'Therefore, this {PRECONDITIONS} variant is valid.',
    #                 f'For {STEP_VARIANTS[0]}, '
    #                 f'"about:logins?filter=<search input>" can also execute login searching '
    #                 f'on "about:logins" page. Therefore, {STEP}2 and {STEP}3 can be replaced by this. '
    #                 f'To meet the requirement of performing searching logins that returns 0 results, '
    #                 f'generate a random string to replace <search input>.',
    #             ],
    #             VARIANTS: {
    #                 GENERALIZATION[0]: 'A no matching result message should be displayed instead of no message '
    #                                    f'if performing a search returns 0 results.',
    #                 PRECONDITIONS_VARIANTS[0]: [
    #                     {
    #                         ORIGINAL: "Have a Firefox profile with multiple saved logins.",
    #                         VARIANT: "Have a Firefox profile without saved logins."
    #                     }, ],
    #                 STEP_VARIANTS[0]:
    #                     [
    #                         {
    #                             STEP_IDS: [1, 2],
    #                             VARIANT: 'Navigate to "about:logins?filter=kdskdsfjhskdjfhlksdaflkadsfasdkjlfsd".'
    #                         },
    #                     ],
    #
    #             }
    #             # SCENARIOS: [
    #             #     {
    #             #         PRECONDITIONS: ["Have a Firefox profile without saved logins."],
    #             #         STEPS_TO_REPRODUCE: ['Open the latest Nightly browser with the profile from prerequisites.',
    #             #                              'Navigate to "about:logins" page.',
    #             #                              'Perform a search that returns 0 results.',
    #             #                              'Observe the login list.'],
    #             #         EXPECTED_RESULTS: ['A "No matching logins" message is displayed.'],
    #             #         ACTUAL_RESULTS: ['No message is displayed, the list is blank.']
    #             #     },
    #             #     {
    #             #         PRECONDITIONS: ["Have a Firefox profile with multiple saved logins."],
    #             #         STEPS_TO_REPRODUCE: ['Open the latest Nightly browser with the profile from prerequisites.',
    #             #                              'Navigate to "about:logins?filter=kdskdsfjhskdjfhlksdaflkadsfasdkjlfsd".',
    #             #                              'Observe the login list.'],
    #             #         EXPECTED_RESULTS: ['A "No matching logins" message is displayed.'],
    #             #         ACTUAL_RESULTS: ['No message is displayed, the list is blank.']
    #             #     },
    #             # ]
    #         },
    #     },
    #     {
    #         "bug_id": 1679131,
    #         "output": {
    #             CHAINS_OF_THOUGHT: [f'For {GENERALIZATION[0]}, the oracle described in '
    #                                 f'{EXPECTED_RESULTS} and {ACTUAL_RESULTS} is "When dragging icons, '
    #                                 f'icons shouldn\'t be draggable and should remain in place.". '
    #                                 f'We can check every icon element instead of only the icons in the '
    #                                 f'{STEPS_TO_REPRODUCE}. Therefore, the oracle is the above one.',
    #                                 f'For {PRECONDITIONS_VARIANTS[0]}, '
    #                                 f'the {PRECONDITIONS} is None, so the {PRECONDITIONS} variant is None.',
    #                                 f'For {STEP_VARIANTS[0]}, '
    #                                 f'Since no alternative steps for removing all logins, '
    #                                 f'generate no new {STEP_VARIANTS[0]}.',
    #                                 ],
    #             VARIANTS: [
    #                 {
    #                     GENERALIZATION[
    #                         0]: "When dragging icons, icons shouldn\'t be draggable and should remain in place.",
    #                     PRECONDITIONS_VARIANTS[0]: None,
    #                     STEP_VARIANTS[0]: None,
    #                 },
    #             ]
    #         },
    #     },
    #     {
    #         "bug_id": 1505751,
    #         "output": {
    #             CHAINS_OF_THOUGHT: [f'For {GENERALIZATION[0]}, the oracle described in {EXPECTED_RESULTS} '
    #                                 f'and {ACTUAL_RESULTS} is "dropdown menu should be closed but remain open.", '
    #                                 f'which is incomplete and meaningless. '
    #                                 f'Therefore, the oracle should contain some necessary context, namely '
    #                                 f'"When navigating a dropdown menu using the Tab key to focus, '
    #                                 f'the Down key selects options, and the Enter key confirms the selection. '
    #                                 f'After confirming, the dropdown menu should be closed instead of remaining open.',
    #                                 f'For {PRECONDITIONS_VARIANTS[0]}, '
    #                                 f'the {PRECONDITIONS} is None, so the {PRECONDITIONS} variant is None. ',
    #                                 f'For {STEP_VARIANTS[0]}, '
    #                                 f'{STEP}3 uses Tab key to navigate to the specific element, since "Shift+Tab" '
    #                                 f'also can be used for navigation. Thus, use Shift+Tab key to replace Tab key as an '
    #                                 f'alternative {STEP}. '
    #                                 f'Besides, for {STEP}4, we can also use the "Up" key to show and select the '
    #                                 f'options of the dropdown menu. '
    #                                 f'Thus, there is an alternative {STEP} for {STEP}4.',
    #                                 ],
    #             VARIANTS: [
    #                 {
    #                     GENERALIZATION[0]: "When navigating a dropdown menu using the Tab key to focus, "
    #                                        "the Down key selects options, and the Enter key confirms the selection. "
    #                                        "After confirming, "
    #                                        "the dropdown menu should be closed instead of remaining open.",
    #                     PRECONDITIONS_VARIANTS[0]: None,
    #                     STEP_VARIANTS[0]: [
    #                         {
    #                             STEP_IDS: [2],
    #                             VARIANT: 'Use the "Shift+Tab" key to focus the language drop-down from '
    #                                      '"Choose the languages used '
    #                                      'to display menus, messages, and notifications" section'
    #                         },
    #                         {
    #                             STEP_IDS: [3],
    #                             VARIANT: 'Use the "Up Arrow" key.'
    #                         },
    #                     ],
    #                 },
    #             ]
    #         },
    #     },
    # ]

    SCENARIO_MODIFIER_INSTANCES = [
        {
            "bug_id": 1571444,
            "output": {
                CHAINS_OF_THOUGHT: [
                    f'For this given scenario, it is about '
                    f'"when performing a search among saved logins in "about:logins" page returns 0 results, '
                    f'a no matching logins message should be displayed but not.". For generate a generalized oracle, we '
                    f'can generalize this scenario into "When performing a search returns 0 results, a no matching '
                    f'result message should be displayed but not.".',
                    f'The {PRECONDITIONS} is "Have a Firefox profile with multiple saved logins.". '
                    f'The variant of this {PRECONDITIONS} is '
                    f'"Have a Firefox profile without saved logins.". '
                    f'The {STEPS_TO_REPRODUCE} are '
                    f'on performing searching logins that returns 0 results on "about:logins" page. '
                    f'With this {PRECONDITIONS} variant, '
                    f'this search operation still can be executed. '
                    f'Therefore, this {PRECONDITIONS} variant is valid.',
                    f'For {STEP_VARIANTS[0]}, '
                    f'"about:logins?filter=<search input>" can also execute login searching '
                    f'on "about:logins" page, which has the same effect as {STEP}2 and {STEP}3. '
                    f'Therefore, {STEP}2 and {STEP}3 can be replaced by this. '
                    f'To meet the requirement of performing searching logins that returns 0 results, '
                    f'generate a random string to replace <search input>.',
                ],
                VARIANTS: {
                    GENERALIZATION[0]: 'A no matching result message should be displayed instead of no message '
                                       f'if performing a search returns 0 results.',
                    PRECONDITIONS_VARIANTS[0]: [
                        {
                            ORIGINAL: "Have a Firefox profile with multiple saved logins.",
                            VARIANT: "Have a Firefox profile without saved logins."
                        }, ],
                    STEP_VARIANTS[0]:
                        [
                            {
                                STEP_IDS: [1, 2],
                                VARIANT: 'Navigate to "about:logins?filter=kdskdsfjhskdjfhlksdaflkadsfasdkjlfsd".'
                            },
                        ],

                }
            },
        },
        {
            "bug_id": 1679131,
            "output": {
                CHAINS_OF_THOUGHT: [
                    f'For {GENERALIZATION[0]}, the scenario is about "After clicking Remove all button, '
                    f'grab and drag elements around. Elements should remain in place, '
                    f'but modal-remove-icon and [x] button are draggale.". The generalized oracle is '
                    f'about "When dragging icons, icons shouldn\'t be draggable and '
                    f'should remain in place.". '
                    f'With this oracle, it inspires us to check any icon element appearing '
                    f'in the software instead of the mentioned ones. ',
                    f'For {PRECONDITIONS_VARIANTS[0]}, '
                    f'the {PRECONDITIONS} is None, so the {PRECONDITIONS} variant is None.',
                    f'For {STEP_VARIANTS[0]}, '
                    f'Since no alternative steps for removing all logins, '
                    f'generate no new {STEP_VARIANTS[0]}.',
                ],
                VARIANTS: [
                    {
                        GENERALIZATION[
                            0]: "When dragging icons, icons shouldn\'t be draggable and should remain in place.",
                        PRECONDITIONS_VARIANTS[0]: None,
                        STEP_VARIANTS[0]: None,
                    },
                ]
            },
        },
        {
            "bug_id": 1505751,
            "output": {
                CHAINS_OF_THOUGHT: [
                    f'For {GENERALIZATION[0]}, the scenario is about using keys to the oracle described in {EXPECTED_RESULTS} '
                    f'and {ACTUAL_RESULTS} is "dropdown menu should be closed but remain open.", '
                    f'which is incomplete and meaningless. '
                    f'Therefore, the oracle should contain some necessary context, namely '
                    f'"When navigating a dropdown menu using the Tab key to focus, '
                    f'the Down key selects options, and the Enter key confirms the selection. '
                    f'After confirming, the dropdown menu should be closed instead of remaining open.',
                    f'For {PRECONDITIONS_VARIANTS[0]}, '
                    f'the {PRECONDITIONS} is None, so the {PRECONDITIONS} variant is None. ',
                    f'For {STEP_VARIANTS[0]}, '
                    f'{STEP}3 uses Tab key to navigate to the specific element, since "Shift+Tab" '
                    f'also can be used for navigation. Thus, use Shift+Tab key to replace Tab key as an '
                    f'alternative {STEP}. '
                    f'Besides, for {STEP}4, we can also use the "Up" key to show and select the '
                    f'options of the dropdown menu. '
                    f'Thus, there is an alternative {STEP} for {STEP}4.',
                ],
                VARIANTS: [
                    {
                        GENERALIZATION[0]: "When navigating a dropdown menu using the Tab key to focus, "
                                           "the Down key selects options, and the Enter key confirms the selection. "
                                           "After confirming, "
                                           "the dropdown menu should be closed instead of remaining open.",
                        PRECONDITIONS_VARIANTS[0]: None,
                        STEP_VARIANTS[0]: [
                            {
                                STEP_IDS: [2],
                                VARIANT: 'Use the "Shift+Tab" key to focus the language drop-down from '
                                         '"Choose the languages used '
                                         'to display menus, messages, and notifications" section'
                            },
                            {
                                STEP_IDS: [3],
                                VARIANT: 'Use the "Up Arrow" key.'
                            },
                        ],
                    },
                ]
            },
        },
    ]

    # SCENARIO_MODIFIER_INSTANCES = [
    #     {
    #         "bug_id": 1571444,
    #         "output": {
    #             CHAINS_OF_THOUGHT: [f'For {NEGATION_VARIATION}, '
    #                                 f'the {PRECONDITIONS} is "Have a Firefox profile with multiple saved logins.". '
    #                                 f'The {NEGATION_VARIATION} of this {PRECONDITIONS} is '
    #                                 f'"Have a Firefox profile without saved logins.". '
    #                                 f'The {STEPS_TO_REPRODUCE} are '
    #                                 f'on performing searching logins that returns 0 results on "about:logins" page. '
    #                                 f'With this {PRECONDITIONS} variant, '
    #                                 f'this {STEPS_TO_REPRODUCE} still can be executed. '
    #                                 f'Therefore, generate a new {SCENARIO} by using this {PRECONDITIONS} variant.',
    #                                 f'For {ALTERNATIVE_VARIATION}, '
    #                                 f'"about:logins?filter=<search input>" can also execute login searching '
    #                                 f'on "about:logins" page. '
    #                                 f'To meet the requirement of performing searching logins that returns 0 results, '
    #                                 f'generate a random string to replace <search input>. '
    #                                 f'Therefore, generate a new {SCENARIO} by using this alternative {STEP}.',
    #                                 f'For {EQUIVALENCE_VARIATION}, the issue described in '
    #                                 f'{EXPECTED_RESULTS} and {ACTUAL_RESULTS} cannot exist independently of'
    #                                 f' {STEPS_TO_REPRODUCE}. '
    #                                 f'Therefore, the generalized description without specific '
    #                                 f'components for this {SCENARIO} contains the summary of {STEPS_TO_REPRODUCE}, '
    #                                 f'{EXPECTED_RESULTS} and {ACTUAL_RESULTS}, namely '
    #                                 f'"When perform searching that returns no results, '
    #                                 f'the message of no searching '
    #                                 f'results should be displayed instead of no message.'
    #                                 ],
    #             VARIATION: {
    #                 NEGATION_VARIATION: {SCENARIOS: [
    #                     {
    #                         PRECONDITIONS: ["Have a Firefox profile without saved logins."],
    #                         STEPS_TO_REPRODUCE: ['Open the latest Nightly browser with the profile from prerequisites.',
    #                                              'Navigate to "about:logins" page.',
    #                                              'Perform a search that returns 0 results.',
    #                                              'Observe the login list.'],
    #                         EXPECTED_RESULTS: ['A "No matching logins" message is displayed.'],
    #                         ACTUAL_RESULTS: ['No message is displayed, the list is blank.']
    #                     },
    #                 ]},
    #                 ALTERNATIVE_VARIATION: {SCENARIOS: [
    #                     {
    #                         PRECONDITIONS: ["Have a Firefox profile with multiple saved logins."],
    #                         STEPS_TO_REPRODUCE: ['Open the latest Nightly browser with the profile from prerequisites.',
    #                                              'Navigate to "about:logins?filter=kdskdsfjhskdjfhlksdaflkadsfasdkjlfsd".',
    #                                              'Observe the login list.'],
    #                         EXPECTED_RESULTS: ['A "No matching logins" message is displayed.'],
    #                         ACTUAL_RESULTS: ['No message is displayed, the list is blank.']
    #                     },
    #                 ]},
    #                 EQUIVALENCE_VARIATION: "When perform searching that returns no results, "
    #                                        "the message of no searching "
    #                                        "results should be displayed instead of no message"
    #             }
    #             # SCENARIOS: [
    #             #     {
    #             #         PRECONDITIONS: ["Have a Firefox profile without saved logins."],
    #             #         STEPS_TO_REPRODUCE: ['Open the latest Nightly browser with the profile from prerequisites.',
    #             #                              'Navigate to "about:logins" page.',
    #             #                              'Perform a search that returns 0 results.',
    #             #                              'Observe the login list.'],
    #             #         EXPECTED_RESULTS: ['A "No matching logins" message is displayed.'],
    #             #         ACTUAL_RESULTS: ['No message is displayed, the list is blank.']
    #             #     },
    #             #     {
    #             #         PRECONDITIONS: ["Have a Firefox profile with multiple saved logins."],
    #             #         STEPS_TO_REPRODUCE: ['Open the latest Nightly browser with the profile from prerequisites.',
    #             #                              'Navigate to "about:logins?filter=kdskdsfjhskdjfhlksdaflkadsfasdkjlfsd".',
    #             #                              'Observe the login list.'],
    #             #         EXPECTED_RESULTS: ['A "No matching logins" message is displayed.'],
    #             #         ACTUAL_RESULTS: ['No message is displayed, the list is blank.']
    #             #     },
    #             # ]
    #         },
    #     },
    #     {
    #         "bug_id": 1679131,
    #         "output": {
    #             CHAINS_OF_THOUGHT: [f'For {NEGATION_VARIATION}, '
    #                                 f'the {PRECONDITIONS} is None, so the {PRECONDITIONS} variant is None. '
    #                                 f'Therefore, generate no new {SCENARIO} by using this {PRECONDITIONS} variant.',
    #                                 f'For {ALTERNATIVE_VARIATION}, '
    #                                 f'Since no alternative steps for removing all logins, '
    #                                 f'generate no new {SCENARIO}.',
    #                                 f'For {EQUIVALENCE_VARIATION}, the generalized issue described in '
    #                                 f'{EXPECTED_RESULTS} and {ACTUAL_RESULTS} is "When dragging icon elements, '
    #                                 f'they shouldn\'t be draggale" and should remain in place.". '
    #                                 f'We can check every icon element instead of only the icons in the '
    #                                 f'{STEPS_TO_REPRODUCE}. Therefore, the generalized description is the above one.'
    #                                 ],
    #             VARIATION: [
    #                 {
    #                     NEGATION_VARIATION: None,
    #                     ALTERNATIVE_VARIATION: None,
    #                     EQUIVALENCE_VARIATION: "When dragging icon elements, "
    #                                            "they shouldn\'t be draggable and should remain in place."
    #                 },
    #             ]
    #         },
    #     },
    #     {
    #         "bug_id": 1505751,
    #         "output": {
    #             CHAINS_OF_THOUGHT: [f'For {NEGATION_VARIATION}, '
    #                                 f'the {PRECONDITIONS} is None, so the {PRECONDITIONS} variant is None. '
    #                                 f'Therefore, generate no new {SCENARIO} by using this {PRECONDITIONS} variant.',
    #                                 f'For {ALTERNATIVE_VARIATION}, '
    #                                 f'{STEP}3 uses Tab key to navigate to the specific element, since "Shift+Tab" '
    #                                 f'also can be used for navigation. Thus, use Shift+Tab key to replace Tab key as an '
    #                                 f'alternative operation. '
    #                                 f'Besides, for {STEP}4, we can also use the "Up" key to show and select the '
    #                                 f'options of the dropdown menu. '
    #                                 f'Thus, there is an alternative operation for {STEP}4.',
    #                                 f'For {EQUIVALENCE_VARIATION}, the issue described in {EXPECTED_RESULTS} '
    #                                 f'and {ACTUAL_RESULTS} can be generalized without {STEPS_TO_REPRODUCE}. Therefore, '
    #                                 f'The generalized description contains {STEPS_TO_REPRODUCE}, {EXPECTED_RESULTS} '
    #                                 f'and {ACTUAL_RESULTS}, namely "After using Tab key to focus the dropdown menu, '
    #                                 f'use the down key to select the options under dropdown menu and use Enter key to '
    #                                 f'confirm the selected option, the drop down menu should be closed instead of open.'
    #                                 f'".'
    #                                 ],
    #             VARIATION: [
    #                 {
    #                     NEGATION_VARIATION: None,
    #                     ALTERNATIVE_VARIATION: None,
    #                     EQUIVALENCE_VARIATION: "After using Tab key to focus the dropdown menu, "
    #                                            "use the Down key to select the options under dropdown menu and "
    #                                            "use Enter key to confirm the selected option, "
    #                                            "the drop down menu should be closed instead of open."
    #                 },
    #             ]
    #         },
    #     },
    # ]

    SCENARIO_LEVEL_INSTANCES = [
        # {
        #     # (1678633, 1587737): redundant steps
        #     "bug_id_pair": (1678633, 1587737),
        #     "output": {
        #         # CHAINS_OF_THOUGHT: {
        #         #     SCENARIO_LEVEL: f"Generate new {SCENARIOS} by {SCENARIO}1 + {SCENARIO}2 and {SCENARIO}2 + {SCENARIO}1. "
        #         #                     f"{SCENARIO}1 is on "
        #         #                     f"First, for {SCENARIO}1 + {SCENARIO}2, "
        #         # },
        #         SCENARIOS: [
        #             {
        #                 PRECONDITIONS: ['You are signed in with a valid FxA account that contains at least one login saved.'],
        #                 STEPS_TO_REPRODUCE: ['Navigate to the "about:logins" page.',
        #                                      'Click the "Choose..." button under the "Language" section.',
        #                                      'Drag to resize the popup box (try to enlarge it).',
        #                                      'Click "Select a language to add" so that language list options will pops up.'],
        #                 EXPECTED_RESULTS: ['Box corner should follow the mouse.',
        #                                    'And the popup should not shift up. There should not be gap.'],
        #                 ACTUAL_RESULTS: ['The size of the box does not follow the mouse. '
        #                                  'It seem it enlarges about half of the mouse pointer movement.',
        #                                  'Language list popup shift up. '
        #                                  'So, there is gap between select button and options popup.']
        #             },
        #         ]
        #     }
        #     #     [{
        #     #     "chains":
        #     #     # "1. Scenario1 is on
        #     #     # "2. Scenario2 is on
        #     #     # "3. logistic problem detection
        #     #     # "4. redundant steps detection
        #     #     #       "After executing Scenario1, the browser is still open, and the about:logins page is displayed. "
        #     #     #       "Therefore, the steps related to starting the browser and navigating to about:logins "
        #     #     #       "from Scenario2 are redundant and can be removed. ",
        #     #         "After executing Scenario1, the browser is still open, and the about:logins page is displayed. "
        #     #         "Therefore, the steps related to starting the browser and navigating to about:logins "
        #     #         "from Scenario2 are redundant and can be removed. ",
        #     #     "scenario": "1. Navigate to the \"about:logins\" page."
        #     #     "2. Go to the “about:preferences#sync” page using a new tab."
        #     #     "3. Click on the “Sign Out...” button."
        #     #     "4. check the “Delete data from this device” checkbox from the pop-up."
        #     #     "5. Click on the “Sign Out” button from the pop-up."
        #     #     "6. switch back to the “about:logins” tab."
        #     #     "7. Observe the Login Item area."
        #     #     "8. Click on the “Sign in to Sync” button."
        #     #     "9. Enter the credentials from the prerequisites and log in."
        #     #     "10. Go back to the “about:logins” page."
        #     #     "11. observe the “Login List”."
        #     # }]
        # },
        # {
        #     # (1678633, 1575516): redundant steps, logistic problem
        #     "bug_id_pair": (1678633, 1575516),
        #     "output": {
        #         # CHAINS_OF_THOUGHT: {
        #         #     SCENARIO_LEVEL: f"Generate new {SCENARIOS} by {SCENARIO}1 + {SCENARIO}2 and {SCENARIO}2 + {SCENARIO}1.\n"
        #         #                     f"{SCENARIO}1 is on signing out from Firefox Sync and delete all logins.\n"
        #         #                     f"{SCENARIO}2 is on logging into its website using the credentials from the login during editing a saved login.\n"
        #         #                     f"First, for {SCENARIO}1 + {SCENARIO}2, "
        #         #                     # f"the new scenario is logging into its website using the credentials from the login during editing a saved login after signing out from Firefox Sync and delete all logins"
        #         #                     f"Since {SCENARIO}1 deletes all logins, it is impossible for {SCENARIO}2 to edit the saved login. "
        #         #                     f"So, no new {SCENARIO} can be generated by {SCENARIO}1 + {SCENARIO}2.\n"
        #         #                     f"Second, for {SCENARIO}2 + {SCENARIO}1, {SCENARIO}2 is logging into its website using the credentials from the login during editing a saved login and then {SCENARIO}1 signing out from Firefox Sync and delete all logins. "
        #         #                     f"This new {SCENARIO} can be executed.\n"
        #         #                     f"Therefore, a new {SCENARIO} is generated."
        #         # },
        #         SCENARIOS: [
        #             {
        #                 PRECONDITIONS: ['You are signed in with a valid FxA account that contains at least one login saved.'],
        #                 STEPS_TO_REPRODUCE: ['Open the latest Nightly browser with the profile from prerequisites.',
        #                                      'Navigate to "about:logins" page.',
        #                                      'Click one of the saved logins.',
        #                                      'Click on the “Edit” button.',
        #                                      'Edit the username.',
        #                                      'Edit the password.',
        #                                      'Click on the website address.',
        #                                      'logging in.',
        #                                      'Focus back to the “about:logins” page.',
        #                                      'Go to the “about:preferences#sync” page using a new tab.',
        #                                      'Click on the “Sign Out...” button.',
        #                                      'Check the “Delete data from this device” checkbox from the pop-up.',
        #                                      'Click on the “Sign Out” button from the pop-up.',
        #                                      'switch back to the “about:logins” tab.',
        #                                      'Observe the Login Item area.'],
        #                 EXPECTED_RESULTS: [],
        #                 ACTUAL_RESULTS: []
        #             },
        #
        #         ]
        #     },
        # "chains": "After executing Scenario1, the browser is still open, and the about:logins page is displayed. "
        #           "Therefore, the steps related to starting the browser and navigating to about:logins "
        #           "from Scenario2 are redundant and can be removed. "
        #           "Additionally, Scenario1 has already signed out and deleted the data from this device. "
        #           "So, there is no login item in about:logins page. "
        #           "It is impossible to execute Scenario2 since it need to have at least one saved login.",
        # "output": None
        {
            # (1678633, 1575516): redundant steps, logistic problem
            "bug_id_pair": (1678633, 1575516),
            "output": {
                CHAINS_OF_THOUGHT:
                    f"Bug1678633_SCENARIO is to sign out from Firefox Sync, delete all data, return to the 'about:logins' page, and observe the Login Item area.\n"
                    f"Bug1575516_SCENARIO is to edit a saved login on 'about:logins' page and log into the website of the selected login.\n"
                    f"For Bug1678633_SCENARIO + Bug1575516_SCENARIO, "      
                    f"since Bug1678633_SCENARIO deletes all data, no saved login is available for Bug1575516_SCENARIO to edit. "
                    f"Therefore, Bug1678633_SCENARIO + Bug1575516_SCENARIO is infeasible.\n"
                    f"For Bug1575516_SCENARIO + Bug1678633_SCENARIO, the execution of Bug1575516_SCENARIO (edit a saved login and log into it) will not prevent Bug1678633_SCENARIO (sign out and delete all data) from being executed. "
                    f"Hence, Bug1575516_SCENARIO + Bug1678633_SCENARIO is feasible. "
                    f"Then, we consider whether the steps in the connecting part (i.e., the last step in Bug1575516_SCENARIO and the first step in Bug1678633_SCENARIO) are redundant or unnecessary. "
                    f"The last step of Bug1575516_SCENARIO is [Focus back to the 'about:logins' page]. The first "
                    f"step of Bug1678633_SCENARIO is [Navigate to the 'about:logins' page.]. "
                    f"Both of them are going to about:logins page, so remove the first step of Bug1678633_SCENARIO."
                ,
                SCENARIOS: [
                    {
                        PRECONDITIONS: [
                            'Have at least one saved login'],
                        # STEPS_TO_REPRODUCE: ['Open the latest Nightly browser with the profile from prerequisites.',
                        #                      'Navigate to "about:logins" page.',
                        #                      'Click one of the saved logins.',
                        #                      'Click on the “Edit” button.',
                        #                      'Edit the username.',
                        #                      'Edit the password.',
                        #                      'Click on the website address.',
                        #                      'logging in.',
                        #                      'Focus back to the “about:logins” page.',
                        #                      'Observe the behavior.',
                        #                      'Go to the “about:preferences#sync” page using a new tab.',
                        #                      'Click on the “Sign Out...” button.',
                        #                      'Check the “Delete data from this device” checkbox from the pop-up.',
                        #                      'Click on the “Sign Out” button from the pop-up.',
                        #                      'switch back to the “about:logins” tab.',
                        #                      'Observe the Login Item area.'],
                        STEPS_TO_REPRODUCE: [(1575516, 0, 8), (1678633, 1, 6)],
                        EXPECTED_RESULTS: ['The “Discard Unsaved Changes?” pop-up is displayed.',
                                           'The password and the username are not updated.',
                                           'All logins are successfully removed and the "No FxA sync" state of the about:logins page is displayed.'],
                        ACTUAL_RESULTS: [
                            'All logins are successfully removed and no state is displayed for the “about:logins” page.']
                    },

                ]
            },
        },
        # {
        #     # (1678633, 1575516): redundant steps    can have a better example, e.g., (1688817, 1460406)
        #     "bug_id_pair": (1642616, 1593060),
        #     "output": {
        #         SCENARIOS: [
        #             {
        #                 PRECONDITIONS: [],
        #                 # STEPS_TO_REPRODUCE: ['Open Options (about:preferences).',
        #                 #                      'Click the "Choose..." button under the "Language" section.',
        #                 #                      'Drag to resize the popup box (try to enlarge it).',
        #                 #                      'Click "Select a language to add" so that language list options will pops up.'],
        #                 STEPS_TO_REPRODUCE: [(1642616, 0, 2), (1593060, 2, 2)],
        #                 EXPECTED_RESULTS: ['Box corner should follow the mouse.',
        #                                    'And the popup should not shift up. There should not be gap.'],
        #                 ACTUAL_RESULTS: ['The size of the box does not follow the mouse. '
        #                                  'It seem it enlarges about half of the mouse pointer movement.',
        #                                  'Language list popup shift up. '
        #                                  'So, there is gap between select button and options popup.']
        #             },
        #             {
        #                 PRECONDITIONS: [],
        #                 # STEPS_TO_REPRODUCE: ['Open Options.',
        #                 #                      'Click [Choose...] button of Language section.',
        #                 #                      'Click "Select a language to add" so that language list options will pops up.',
        #                 #                      'Drag to resize the popup box (try to enlarge it).'],
        #                 STEPS_TO_REPRODUCE: [(1593060, 0, 2), (1642616, 2, 2)],
        #                 EXPECTED_RESULTS: ['And the popup should not shift up. There should not be gap.',
        #                                    'Box corner should follow the mouse.'],
        #                 ACTUAL_RESULTS: ['Language list popup shift up. '
        #                                  'So, there is gap between select button and options popup.',
        #                                  'The size of the box does not follow the mouse. '
        #                                  'It seem it enlarges about half of the mouse pointer movement.']
        #             },
        #
        #         ]
        #     },
        # },
        # {
        #     # (1688817, 1460406): redundant steps
        #     "bug_id_pair": (1688817, 1460406),
        #     "output": {
        #         CHAINS_OF_THOUGHT:
        #         # f"Generate two new {SCENARIOS}: {SCENARIO}1 + {SCENARIO}2 and {SCENARIO}2 + {SCENARIO}1.\n"
        #         # f"{SCENARIO}1 is on signing out from Firefox Sync and delete all logins.\n"
        #         # f"{SCENARIO}2 is on logging into its website using the credentials from the login during editing a saved login.\n"
        #             f"For {SCENARIO}1 + {SCENARIO}2, "
        #             f"Both {SCENARIO}1 and {SCENARIO}2 are operations on 'Privacy & Security', "
        #             f"which can be executed sequentially. "
        #             f"So, {SCENARIO}1 + {SCENARIO}2 is feasible. "
        #             f"Then, we refine the new {SCENARIO} by "
        #             f"removing redundant or unnecessary steps. "
        #             f"Since the first step of {SCENARIO}2 is to 'Upgrade to Firefox 60.0.', "
        #             f"Firefox might be reopened after upgrading. "
        #             f"Although {SCENARIO}1 has already been to 'Privacy & Security', "
        #             f"it is necessary to navigate to it again. "
        #             f"So no steps need to be removed"
        #             f"So, {SCENARIO}1 + {SCENARIO}2 is feasible.\n"
        #             f"For {SCENARIO}2 + {SCENARIO}1, "
        #             f"Both {SCENARIO}2 and {SCENARIO}1 are operations on 'Privacy & Security', "
        #             f"which can be executed sequentially. "
        #             f"So, {SCENARIO}2 + {SCENARIO}1 is feasible. Then, we refine the new {SCENARIO} by "
        #             f"removing redundant or unnecessary steps. "
        #             f"After executing the {SCENARIO}2, it "
        #             f"step of {SCENARIO}1 (Navigate to the 'about:logins' page.) is redundant and can be removed."
        #         ,
        #         SCENARIOS: [
        #             {
        #                 PRECONDITIONS: [],
        #                 # STEPS_TO_REPRODUCE: ['Open Options (about:preferences).',
        #                 #                      'Click the "Choose..." button under the "Language" section.',
        #                 #                      'Drag to resize the popup box (try to enlarge it).',
        #                 #                      'Click "Select a language to add" so that language list options will pops up.'],
        #                 STEPS_TO_REPRODUCE: [(1688817, 0, 2), (1460406, 0, 3)],
        #                 EXPECTED_RESULTS: ['There should be a Status tab where tracking options can be managed',
        #                                    'The calculation of site data and cache size should finish The options to manage Cookie data should be available'],
        #                 ACTUAL_RESULTS: ['There is no Status tab on the Manage Cookies and Site Data table',
        #                                  'The calculation of site data and cache size never finishes',
        #                                  'The options to manage Cookie data are greyed out']
        #             },
        #             {
        #                 PRECONDITIONS: [],
        #                 # STEPS_TO_REPRODUCE: ['Open Options.',
        #                 #                      'Click [Choose...] button of Language section.',
        #                 #                      'Click "Select a language to add" so that language list options will pops up.',
        #                 #                      'Drag to resize the popup box (try to enlarge it).'],
        #                 STEPS_TO_REPRODUCE: [(1460406, 0, 3), (1688817, 2, 2)],
        #                 EXPECTED_RESULTS: [
        #                     'The calculation of site data and cache size should finish The options to manage Cookie data should be available',
        #                     'There should be a Status tab where tracking options can be managed'],
        #                 ACTUAL_RESULTS: ['The calculation of site data and cache size never finishes',
        #                                  'The options to manage Cookie data are greyed out',
        #                                  'There is no Status tab on the Manage Cookies and Site Data table']
        #             },
        #
        #         ]
        #     },
        # },
        {
            # (1238444, 1313079): redundant steps
            "bug_id_pair": (1238444, 1313079),
            "output": {
                CHAINS_OF_THOUGHT:
                    f"Bug1238444_SCENARIO is to open the pdf link, change zoom on pdf and scroll down the pdf.\n"
                    f"Bug1313079_SCENARIO is to open a website, scroll down the website, click the specific button and scroll up the webpage.\n"
                    f"For Bug1238444_SCENARIO + Bug1313079_SCENARIO, "
                    f"The execution of Bug1238444_SCENARIO will not prevent Bug1313079_SCENARIO from being executed. "
                    f"So, Bug1238444_SCENARIO + Bug1313079_SCENARIO is feasible. "
                    f"Then, we consider whether the steps in the connecting part (i.e., the last step in Bug1238444_SCENARIO and the first step in Bug1313079_SCENARIO) are redundant or unnecessary. "
                    f"The last step of Bug1238444_SCENARIO involves scrolling down the page, "
                    f"whereas the first step of Bug1313079_SCENARIO is to navigate to 'https://testpilot.firefox.com/', "
                    f"which performs a different operation altogether. "
                    f"Next, check if the first step of Bug1313079_SCENARIO on opening Firefox. "
                    f"Note that all of these scenarios are executed on the Firefox browser. "
                    f"Except for the specific step to close Firefox, all other operations are performed while keeping Firefox open. "
                    f"Therefore, without any closing operation, there is no need to perform the opening Firefox operation in the middle of a scenario."
                    f"The first step of Bug1313079_SCENARIO is not about opening Firefox. "
                    f"So both of them in the connecting part are necessary, no steps need to be removed.\n"
                    f"For Bug1313079_SCENARIO + Bug1238444_SCENARIO, the execution of Bug1313079_SCENARIO will not prevent Bug1238444_SCENARIO from being executed. "
                    f"So, Bug1313079_SCENARIO + Bug1238444_SCENARIO is feasible. "
                    f"Then, we consider whether the steps in the connecting part (i.e., the last step in Bug1313079_SCENARIO and the first step in Bug1238444_SCENARIO) are redundant or unnecessary. "
                    f"The last step of Bug1313079_SCENARIO involves scrolling up the webpage, "
                    f"whereas the first step of Bug1238444_SCENARIO is to open Firefox, "
                    f"which performs a different operation altogether. "
                    f"Next, check if the first step of Bug1238444_SCENARIO on opening Firefox. "
                    f"Note that all of these scenarios are executed on the Firefox browser. "
                    f"Except for the specific step to close Firefox, all other operations are performed while keeping Firefox open. "
                    f"Therefore, without any closing operation, there is no need to perform the opening Firefox operation in the middle of a scenario."
                    f"The first step of Bug1238444_SCENARIO is about opening Firefox. "
                    f"After executing Bug1313079_SCENARIO, Firefox remains open as the last step involves scrolling up the webpage instead of closing Firefox. "
                    f"Therefore, there is no need to open Firefox again as the first step in Bug1238444_SCENARIO. "
                    f"The first step of Bug1238444_SCENARIO is unnecessary and should be removed."
                ,
                SCENARIOS: [
                    {
                        PRECONDITIONS: ['Firefox Nightly 52.0a1 with e10s enabled'],
                        # STEPS_TO_REPRODUCE: ['Open Options (about:preferences).',
                        #                      'Click the "Choose..." button under the "Language" section.',
                        #                      'Drag to resize the popup box (try to enlarge it).',
                        #                      'Click "Select a language to add" so that language list options will pops up.'],
                        STEPS_TO_REPRODUCE: [(1238444, 0, 4), (1313079, 0, 3)],
                        EXPECTED_RESULTS: ['PDF should be read smoothly in the browser without any system crashes or '
                                           'graphical issues',
                                           'The \'Please fill out this field.\' tooltip should be dismissed on scroll event'],
                        ACTUAL_RESULTS: ['After following the steps, the whole system becomes unresponsive',
                                         'After a while, the system prompts the user to log in again, resulting in the loss of all work and open programs',
                                         'There might also be visible graphic issues such as colored lines and jammed images',
                                         'The \'Please fill out this field.\' tooltip is still displayed when '
                                         'scrolling the webpage']
                    },
                    {
                        PRECONDITIONS: ['Firefox Nightly 52.0a1 with e10s enabled'],
                        # STEPS_TO_REPRODUCE: ['Open Options.',
                        #                      'Click [Choose...] button of Language section.',
                        #                      'Click "Select a language to add" so that language list options will pops up.',
                        #                      'Drag to resize the popup box (try to enlarge it).'],
                        STEPS_TO_REPRODUCE: [(1313079, 0, 3), (1238444, 1, 4)],
                        EXPECTED_RESULTS: [
                            'The \'Please fill out this field.\' tooltip should be dismissed on scroll event',
                            'PDF should be read smoothly in the browser without any system crashes or graphical issues'],
                        ACTUAL_RESULTS: ['The \'Please fill out this field.\' tooltip is still displayed when '
                                         'scrolling the webpage',
                                         'After following the steps, the whole system becomes unresponsive',
                                         'After a while, the system prompts the user to log in again, resulting in the loss of all work and open programs',
                                         'There might also be visible graphic issues such as colored lines and jammed images',
                                         ]
                    },

                ]
            },
        },
        # {
        #     # (1260727, 1769007): redundant steps
        #     "bug_id_pair": (1260727, 1769007),
        #     "output": {
        #         CHAINS_OF_THOUGHT:
        #             f"For Bug1260727_SCENARIO + Bug1769007_SCENARIO, "
        #             f"Bug1260727_SCENARIO is to install a webextension and click the webextension icon from the toolbar. "
        #             f"Bug1769007_SCENARIO is to pin some tabs, move the window, close and open Firefox again. "
        #             f"The execution of Bug1260727_SCENARIO will not prevent Bug1769007_SCENARIO from being executed. "
        #             f"So, Bug1260727_SCENARIO + Bug1769007_SCENARIO is feasible. "
        #             f"Then, we consider whether the steps in the connecting part "
        #             f"(i.e., the last step in Bug1260727_SCENARIO and the first step in Bug1769007_SCENARIO) are redundant. "
        #             f"The last step of Bug1260727_SCENARIO involves clicking on the webextension icon from the toolbar, "
        #             f"whereas the first step of Bug1769007_SCENARIO is to open Firefox. "
        #             f"It is important to note that all of these scenarios are executed exclusively on the Firefox browser. "
        #             f"With the exception of closing Firefox, all other operations are performed while keeping Firefox open. "
        #             f"After executing Bug1260727_SCENARIO, Firefox remains open as the last step involves clicking on the webextension icon from the toolbar instead of closing Firefox. "
        #             f"Therefore, there is no need to open Firefox again as the first step in Bug1769007_SCENARIO. "
        #             f"The first step of Bug1769007_SCENARIO is unnecessary and should be removed.\n"
        #             f"For Bug1769007_SCENARIO + Bug1260727_SCENARIO, the execution of Bug1769007_SCENARIO will not prevent Bug1260727_SCENARIO from being executed. "
        #             f"So, Bug1769007_SCENARIO + Bug1260727_SCENARIO is feasible. "
        #             f"Then, we consider whether the steps in the connecting part (i.e., the last step in Bug1769007_SCENARIO and the first step in Bug1260727_SCENARIO) are redundant. "
        #             f"The last step of Bug1769007_SCENARIO involves opening Firefox again. "
        #             f"The first step of Bug1260727_SCENARIO is to launch Firefox. "
        #             f"Both of them are going to open Firefox, so remove the first step of Bug1260727_SCENARIO."
        #         ,
        #         SCENARIOS: [
        #             {
        #                 PRECONDITIONS: ['Clean profile in Firefox'],
        #                 # STEPS_TO_REPRODUCE: ['Open Options (about:preferences).',
        #                 #                      'Click the "Choose..." button under the "Language" section.',
        #                 #                      'Drag to resize the popup box (try to enlarge it).',
        #                 #                      'Click "Select a language to add" so that language list options will pops up.'],
        #                 STEPS_TO_REPRODUCE: [(1260727, 0, 3), (1769007, 1, 4)],
        #                 EXPECTED_RESULTS: ["No scrollbar should be displayed in the webextension's panel",
        #                                    'The pinned tabs should be left-aligned'],
        #                 ACTUAL_RESULTS: ['An unnecessary scrollbar appears at the bottom of the panel',
        #                                  "There is a 'ghost' tab at the start of the pinned tabs, making it look like there is a missing pinned tab icon"]
        #             },
        #             {
        #                 PRECONDITIONS: [],
        #                 # STEPS_TO_REPRODUCE: ['Open Options.',
        #                 #                      'Click [Choose...] button of Language section.',
        #                 #                      'Click "Select a language to add" so that language list options will pops up.',
        #                 #                      'Drag to resize the popup box (try to enlarge it).'],
        #                 STEPS_TO_REPRODUCE: [(1769007, 0, 4), (1260727, 1, 3)],
        #                 EXPECTED_RESULTS: [
        #                     'The pinned tabs should be left-aligned',
        #                     "No scrollbar should be displayed in the webextension's panel"],
        #                 ACTUAL_RESULTS: ["There is a 'ghost' tab at the start of the pinned tabs, making it look like there is a missing pinned tab icon",
        #                                  'An unnecessary scrollbar appears at the bottom of the panel',
        #                                  ]
        #             },
        #
        #         ]
        #     },
        # },
    ]

    # STEP_LEVEL_INSTANCES = [
    #     # {
    #     #     # (1678633, 1575516): redundant steps, logistic problem
    #     #     "bug_id_pair": (1678633, 1575516),
    #     #     "output": {
    #     #         # CHAINS_OF_THOUGHT: {
    #     #         #     SCENARIO_LEVEL: f"Generate new {SCENARIOS} by {SCENARIO}1 + {SCENARIO}2 and {SCENARIO}2 + {SCENARIO}1.\n"
    #     #         #                     f"{SCENARIO}1 is on signing out from Firefox Sync and delete all logins.\n"
    #     #         #                     f"{SCENARIO}2 is on logging into its website using the credentials from the login during editing a saved login.\n"
    #     #         #                     f"First, for {SCENARIO}1 + {SCENARIO}2, "
    #     #         #                     # f"the new scenario is logging into its website using the credentials from the login during editing a saved login after signing out from Firefox Sync and delete all logins"
    #     #         #                     f"Since {SCENARIO}1 deletes all logins, it is impossible for {SCENARIO}2 to edit the saved login. "
    #     #         #                     f"So, no new {SCENARIO} can be generated by {SCENARIO}1 + {SCENARIO}2.\n"
    #     #         #                     f"Second, for {SCENARIO}2 + {SCENARIO}1, {SCENARIO}2 is logging into its website using the credentials from the login during editing a saved login and then {SCENARIO}1 signing out from Firefox Sync and delete all logins. "
    #     #         #                     f"This new {SCENARIO} can be executed.\n"
    #     #         #                     f"Therefore, a new {SCENARIO} is generated."
    #     #         # },
    #     #         SCENARIOS: [
    #     #             {
    #     #                 PRECONDITIONS: [
    #     #                     'You are signed in with a valid FxA account that contains at least one login saved.'],
    #     #                 STEPS_TO_REPRODUCE: ['Open the latest Nightly browser with the profile from prerequisites.',
    #     #                                      'Navigate to "about:logins" page.',
    #     #                                      'Click one of the saved logins.',
    #     #                                      'Click on the “Edit” button.',
    #     #                                      'Edit the username.',
    #     #                                      'Edit the password.',
    #     #                                      'Click on the website address.',
    #     #                                      'logging in.',
    #     #                                      'Focus back to the “about:logins” page.',
    #     #                                      'Observe the behavior.',
    #     #                                      'Go to the “about:preferences#sync” page using a new tab.',
    #     #                                      'Click on the “Sign Out...” button.',
    #     #                                      'Check the “Delete data from this device” checkbox from the pop-up.',
    #     #                                      'Click on the “Sign Out” button from the pop-up.',
    #     #                                      'switch back to the “about:logins” tab.',
    #     #                                      'Observe the Login Item area.'],
    #     #                 EXPECTED_RESULTS: ['The “Discard Unsaved Changes?” pop-up is displayed.',
    #     #                                    'The password and the username are not updated.',
    #     #                                    'All logins are successfully removed and the "No FxA sync" state of the about:logins page is displayed.'],
    #     #                 ACTUAL_RESULTS: ['All logins are successfully removed and no state is displayed for the “about:logins” page.']
    #     #             },
    #     #
    #     #         ]
    #     #     },
    #     # },
    #     {
    #         # (1678633, 1575516): no new scenarios generated
    #         "bug_id_pair": (1642616, 1593060),
    #         "output": {
    #             # CHAINS_OF_THOUGHT:
    #             SCENARIOS: [
    #
    #             ]
    #         },
    #     },
    #     {
    #         # for step-level generation instance：3 shared steps: with redundant scenario and new scenario
    #         "bug_id_pair": (1659081, 1659497),
    #         "output": {
    #             # CHAINS_OF_THOUGHT:
    #             SCENARIOS: [
    #                 {
    #                     PRECONDITIONS: None,
    #                     STEPS_TO_REPRODUCE: ['Launch Firefox.',
    #                                          'Enable the new print UI via print.tab_modal.enabled.',
    #                                          'Hit CTRL + P.',
    #                                          'Print to paper.'],
    #                     EXPECTED_RESULTS: ['The content is printed.'],
    #                     ACTUAL_RESULTS: ['The Printing loading dialog is displayed for a moment, then nothing happens, no actually printing is done.']
    #                 },
    #                 {
    #                     PRECONDITIONS: None,
    #                     STEPS_TO_REPRODUCE: ['Launch Firefox.',
    #                                          'Make sure the print UI via print.tab_modal.enabled is set on true.',
    #                                          'Open about:support.'
    #                                          'Hit CTRL + P.',
    #                                          'Input a negative number or a string inside the Copies field.',
    #                                          'Click outside the field'],
    #                     EXPECTED_RESULTS: ['A red border is displayed around the Copies field.', ],
    #                     ACTUAL_RESULTS: ['The invalid input is accepted.']
    #                 },
    #
    #             ]
    #         },
    #     },
    # ]

    STEP_LEVEL_INSTANCES = [
        {
            # (1524153, 1572109): shared step generated one un-executed scenario and one executed scenario
            "bug_id_pair": (1524153, 1572109),
            "output": {
                CHAINS_OF_THOUGHT: [f'For {STEPS_TO_REPRODUCE}0, '
                                    f'"Create New Login" button '
                                    f'from {STEP} "Press the Tab key until the Create New Login button is focused." '
                                    f'is specific on "about:logins" page. '
                                    f"{STEPS_TO_REPRODUCE}0 happening on 'about:config' page doesn't have this button, "
                                    f'so {STEPS_TO_REPRODUCE}0 is not feasible.',
                                    f'For {STEPS_TO_REPRODUCE}1, after clicking the "Edit" button on "about:logins" page, it has '
                                    f'text field for editing, '
                                    f'so "Type something in text filed." and "Try to cancel to edit." can be executed. '
                                    f'Therefore, {STEPS_TO_REPRODUCE}1 is feasible'],
                SCENARIOS: [
                    {
                        PRECONDITIONS: ["Have a Firefox profile with at least one saved login."],
                        # STEPS_TO_REPRODUCE: ['Open the latest Nightly browser with the profile from prerequisites.',
                        #                      'Navigate to "about:logins" page.',
                        #                      'Select a saved login.',
                        #                      'Click the "Edit" button.',
                        #                      'Type something in text filed.',
                        #                      'Try to cancel to edit.'],
                        STEPS_TO_REPRODUCE: [(1572109, 0, 3), (1524153, 2, 3)],
                        EXPECTED_RESULTS: ['The value will be restored to the previous value.'],
                        ACTUAL_RESULTS: ['Unable to cancel.']
                    },
                ]
            },
        },
        {
            # (1524153, 1572109): shared step generated one un-executed scenario and one executed scenario
            "bug_id_pair": (1483786, 1571414),
            "output": {
                CHAINS_OF_THOUGHT: [f'For {STEPS_TO_REPRODUCE}0, '
                                    f'since {STEP} 1 - 2 are to open the browser and open a new tab, '
                                    f'without opening the browser console. '
                                    f'The “message_id” of the telemetry ping from the browser console '
                                    f'cannot be observed. '
                                    f'Therefore, {STEPS_TO_REPRODUCE}0 is not feasible.',
                                    f'For {STEPS_TO_REPRODUCE}1, {STEP} 1 - 4 are about '
                                    f'"open the browser, the browser console and a new tab.". '
                                    f'Then, resize the browser and execute some operations on the new tab '
                                    f'by dragging the new tab and releasing the mouse button. '
                                    f'All these operations are context-independent and '
                                    f'can be executed based on the preceding operations. '
                                    f'Therefore, {STEPS_TO_REPRODUCE}1 is feasible'],
                SCENARIOS: [
                    {
                        PRECONDITIONS: [
                            "Have a new Firefox profile with the browser.ping-centre.log pref set to true."],
                        # STEPS_TO_REPRODUCE: ['Open the browser.',
                        #                      'Open the browser console.',
                        #                      'Focus the browser.',
                        #                      'Open a new tab.',
                        #                      'Resize the Browser to half screen.',
                        #                      'Drag the new tab in the empty area of the screen.',
                        #                      'Release the mouse button.',
                        #                      'Observe the behavior.'],
                        STEPS_TO_REPRODUCE: [(1571414, 0, 3), (1483786, 2, 5)],
                        EXPECTED_RESULTS: ['The new tab is opened in a new window and moved in that area.',
                                           'Observe the “message_id” of the telemetry ping from the browser console and '
                                           'the "EXTENDED_TRIPLETS_1” value is displayed for the “message_id” argument.'],
                        ACTUAL_RESULTS: ['The new tab is opened in a new window over the current one.',
                                         'Observe the “message_id” of the telemetry ping from the browser console and '
                                         'The "TRAILHEAD_1” value is displayed for the “message_id” argument.']
                    },
                ]
            },
        },
    ]

    STEP_SPLITTER_INSTANCES_WITH_TYPE = [
        {
            "bug_id": 1556965,
            "output": [
                {STEP: "Launch Firefox", STEP_TYPE: OPERATION},
                {STEP: "Enable the prefs", STEP_TYPE: OPERATION},
                {STEP: "Go to 'about:logins'", STEP_TYPE: OPERATION},
                {STEP: "Create new entries until the list becomes scrollable", STEP_TYPE: OPERATION},
                {STEP: "Scroll the entries list", STEP_TYPE: OPERATION},
                {STEP: "Observe the Header", STEP_TYPE: NON_OPERATION},
            ]
        },
        {
            "bug_id": 1730692,
            "output": [
                {STEP: "Set prerequisite preferences.", STEP_TYPE: OPERATION},
                {STEP: "Restart the browser.", STEP_TYPE: OPERATION},
                {STEP: "Dismiss the Make Firefox default message if it is displayed to trigger the Suggestions modal.",
                 STEP_TYPE: OPERATION},
                {STEP: "Open 'System Settings'.", STEP_TYPE: OPERATION},
                {STEP: "Select 'Ease of Access'.", STEP_TYPE: OPERATION},
                {STEP: "Click on 'Display' option.", STEP_TYPE: OPERATION},
                {STEP: "Set the 'Make text bigger' slider to a larger value (e.g. 135% ).",
                 STEP_TYPE: OPERATION},
                {STEP: "Observe the modal.", STEP_TYPE: NON_OPERATION},
            ]
        },
    ]

    STEP_SPLITTER_INSTANCES = [
        # {
        #     "bug_id": 1758767,
        #     "chains": "",
        #     "output": None
        # },
        # {
        #     "bug_id": 1730692,
        #     "chains": "1st step is 'Restart the browser after setting prerequisite preferences.' "
        #               "Due to the conjunction word 'after', this step can be separated into two sub-steps, "
        #               "'Set prerequisite preferences' and 'Restart the browser'.\n"
        #               "",
        #     "output": f"Set prerequisite preferences\nRestart the browser\n"
        #               f"Dismiss the Make Firefox default message if it is displayed to trigger the Suggestions modal\n"
        #               f"Open System Settings\n"
        #               f"Open Ease of Access\n"
        #               f"Open Display\n"
        #               f"Set the “Make text bigger” slider to a larger value (e.g. 135% )\n"
        #               f"Observe the modal"
        # }

        {
            "bug_id": 1556965,
            "output": [
                "Launch Firefox",
                "Enable the prefs",
                "Go to about:logins",
                "Create new entries until the list becomes scrollable",
                "Scroll the entries list",
                "Observe the Header"
            ]
        },
        {
            "bug_id": 1730692,
            "output": [
                "Set prerequisite preferences.",
                "Restart the browser.",
                "Dismiss the Make Firefox default message if it is displayed to trigger the Suggestions modal.",
                "Open System Settings.",
                "Select Ease of Access.",
                "Click on Display option.",
                "Set the “Make text bigger” slider to a larger value (e.g. 135% ).",
                "Observe the modal."
            ]
        },
    ]

    SEC_STEP_SPLITTER_INSTANCES = [
        # {
        #     "bug_id": 1572475,
        #     # "chains": "1st step is 'Restart the browser after setting prerequisite preferences.' "
        #     #           "Due to the conjunction word 'after', this step can be separated into two sub-steps, "
        #     #           "'Set prerequisite preferences' and 'Restart the browser'.\n"
        #     #           "",
        #     "output": {
        #           "PRECONDITIONS": [
        #             "Have a Firefox profile with at least one saved login."
        #           ],
        #           "STEPS_TO_REPRODUCE": [
        #             "Open the latest Nightly browser.",
        #             "Navigate to \"about:logins\" page.",
        #             "Select a saved login.",
        #             "Click the \"Edit\" button.",
        #             "Edit the username so that you have at least 50 characters.",
        #             "Click the “Save Changes” button.",
        #             "Observe the way the Sidebar behaves."
        #           ],
        #           "EXPECTED_RESULTS": [
        #             "The width of the Sidebar remains the same."
        #           ],
        #           "ACTUAL_RESULTS": [
        #             "The width of the Sidebar expands."
        #           ],
        #           "NOTES": [
        #             "The Sidebar is displayed as expanded also when navigating to the “about:logins” page when there are no logins saved at all. This is because the text is displayed on 2 different rows instead of 3, as per the UI specifications.",
        #             "The Sidebar also resizes when searching for logins, depending on the usernames’ number of characters.",
        #             "Attached a screen recording with the issue."
        #           ],
        #           "AFFECTED_VERSIONS": [
        #             "Nightly 70.0a1 (Build ID: 20190808093310)"
        #           ],
        #           "AFFECTED_PLATFORMS": [
        #             "All Windows",
        #             "All Mac",
        #             "All Linux"
        #           ],
        #           "OTHERS": [
        #             "Created attachment 9084051",
        #             "sidebar expands.gif"
        #           ]
        #     }
        # },
        {
            "bug_id": 1556965,
            "output": {
                "PRECONDITIONS": [
                    "browser.in-content.dark-mode is True",
                    "signon.management.page.enabled is True"
                ],
                "STEPS_TO_REPRODUCE": [
                    "Launch Firefox",
                    "Enable the prefs",
                    "Go to about:logins",
                    "Create new entries until the list becomes scrollable",
                    "Scroll the entries list",
                    "Observe the Header"
                ],
                "EXPECTED_RESULTS": [
                    "The header should have a better opacity set."
                ],
                "ACTUAL_RESULTS": [
                    "See attached screenshot."
                ],
                "NOTES": [
                    ""
                ],
                "AFFECTED_VERSIONS": [
                    "Latest Nightly 69.0a1 (2019-06-04) (64-bit)",
                    "Latest Beta 68.0b7 (64-bit)"
                ],
                "AFFECTED_PLATFORMS": [
                    "Windows 10 x64",
                    "Mac OS 10.14"
                ],
                "OTHERS": [
                    ""
                ]
            }
        },
        {
            "bug_id": 1730692,
            "output": {
                "PRECONDITIONS": ['Have Firefox installed and opened.',
                                  'Have the following preferences set:\n    - `browser.urlbar.quicksuggest.enabled` =    `true`\n- `browser.urlbar.quicksuggest.scenario`  =  `online`\n- `browser.urlbar.quicksuggest.shouldShowOnboardingDialog` =  ` true`\n- `browser.urlbar.suggest.quicksuggest` =  `false`\n- `browser.urlbar.suggest.quicksuggest.sponsored`  =  `false`'],
                "STEPS_TO_REPRODUCE": [
                    "Set prerequisite preferences.",
                    "Restart the browser.",
                    "Dismiss the Make Firefox default message if it is displayed to trigger the Suggestions modal.",
                    "Open System Settings.",
                    "Select Ease of Access.",
                    "Click on Display option.",
                    "Set the “Make text bigger” slider to a larger value (e.g. 135% ).",
                    "Observe the modal."
                ],
                "EXPECTED_RESULTS": [
                    "The text and buttons of the modal are still readable/clickable with a larger system text."
                ],
                "ACTUAL_RESULTS": [
                    "The text and buttons are cut off when a larger system text is set and are unreachable."
                ],
                "NOTES": [
                    "The issue does not seem reproducible for the accessibility options of the tested Linux Mint and macOS devices (“Scale” and “Large text”).",
                    "Attached is a screen recording of the issue."
                ],
                "AFFECTED_VERSIONS": [
                    "Firefox Beta 93.0b4 (Build ID: 20210912185727)",
                    "Firefox Nightly 94.0a1 (Build ID: 20210913213224)"
                ],
                "AFFECTED_PLATFORMS": [
                    "Windows 10"
                ],
                "OTHERS": [
                    'Created attachment 9241126',
                    'larger system text.gif'
                ]
            }
        },
    ]

    SEC_SPLITTER_INSTANCES = [
        # {
        #     "bug_id": 1556965,
        #     "output": {
        #         "PRECONDITIONS": [
        #             "browser.in-content.dark-mode is True",
        #             "signon.management.page.enabled is True"
        #         ],
        #         "STEPS_TO_REPRODUCE": [
        #             "Launch Firefox",
        #             "Enable the prefs",
        #             "Go to about:logins",
        #             "Create new entries until the list becomes scrollable",
        #             "Scroll the entries list",
        #             "Observe the Header"
        #         ],
        #         "EXPECTED_RESULTS": [
        #             "The header should have a better opacity set."
        #         ],
        #         "ACTUAL_RESULTS": [
        #             "See attached screenshot."
        #         ],
        #         "NOTES": [
        #             ""
        #         ],
        #         "AFFECTED_VERSIONS": [
        #             "Latest Nightly 69.0a1 (2019-06-04) (64-bit)",
        #             "Latest Beta 68.0b7 (64-bit)"
        #         ],
        #         "AFFECTED_PLATFORMS": [
        #             "Windows 10 x64",
        #             "Mac OS 10.14"
        #         ],
        #         "OTHERS": [
        #             ""
        #         ]
        #     }
        # },
        {
            # only steps to reproduce
            "bug_id": 1537640,
            "output": {
                "PRECONDITIONS": [],
                "STEPS_TO_REPRODUCE": [
                    "Go to the URL bar",
                    "Type 'http://192.' or 'https://192.'"
                ],
                "EXPECTED_RESULTS": [
                    "URL bar should retain the typed value without any substitution or modification"
                ],
                "ACTUAL_RESULTS": [
                    "After typing 'http://192.' or 'https://192.' in the URL bar, "
                    "Firefox automatically substitutes '0.0.0' after the '. "
                    "So to get to internal addresses like 192.168.1.1, I have to manually delete these values."
                ],
                "NOTES": [
                    "This behavior started after upgrading to Firefox 66"
                ],
                "AFFECTED_VERSIONS": [
                    "Firefox version 66"
                ],
                "AFFECTED_PLATFORMS": [
                    "Windows NT 10.0"
                ],
                "OTHERS": [
                    "User Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
                ]
            }
        },
        {
            # only steps to reproduce, preconditions in S2R, no expected results
            "bug_id": 1578873,
            "output": {
                "PRECONDITIONS": [
                    "No previously saved logins",
                ],
                "STEPS_TO_REPRODUCE": [
                    "Open about:logins",
                    "Start tabbing through page elements"
                ],
                "EXPECTED_RESULTS": [
                    "Tabbing should proceed smoothly through all page elements"
                ],
                "ACTUAL_RESULTS": [
                    "Tabbing gets stuck on the \"Create New Login\" button when there are zero saved logins",
                    "The \"Lockwise Support\" link can only be accessed via keyboard by tabbing backwards"
                ],
                "NOTES": [],
                "AFFECTED_VERSIONS": [
                    "Nightly build on 9/4"
                ],
                "AFFECTED_PLATFORMS": [
                ],
                "OTHERS": [
                    "Attachment: focusIsStuckOnButton.png"
                ]
            }
        },
        {
            # all in one paragraph
            "bug_id": 1552289,
            "output": {
                "PRECONDITIONS": [
                    "Top Sites and Pocket are both turned off",
                ],
                "STEPS_TO_REPRODUCE": [
                    "Open DiscoveryStream",
                    "Check if the search-only view is shown"
                ],
                "EXPECTED_RESULTS": [
                    "The search-only view should be shown"
                ],
                "ACTUAL_RESULTS": [
                    "The search-only view is not shown"
                ],
                "NOTES": [
                    "The search-only view is expecting highlights to be off, but that section doesn't exist in the settings for discovery stream."],
                "AFFECTED_VERSIONS": [
                ],
                "AFFECTED_PLATFORMS": [
                ],
                "OTHERS": [
                ]
            }
        },

    ]

    # SCENARIO_MODIFIER_INSTANCES = []
