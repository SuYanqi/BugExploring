Dataset link: [https://drive.google.com/file/d/1gRkdAUZm6lTWfAJ9byqlR2wd_DQ0_sYl/view?usp=sharing](https://drive.google.com/file/d/1mlAM1-lZ95zKKPxlUb4Ah9drMFLr7lRV/view?usp=sharing)

Directory prepare
1. Construct the data directory under the root directory

Dataset prepare
1. Download dataset from Dataset link
2. put the bugs.json into the data directory

Construct the SysKG-UTF
1. run 1_filter_bugs.py
2. run 2_split_section.py
3. run 3_get_sec_results_into_bugs.py
4. run 4_split_s2r.py
5. run 5_get_step_results_into_bugs.py
6. run 6_fast_clustering_by_transformer.py

Generate test scenarios
1. run 7_generate_scenario.py

Bugs found
1. Bug 1-36 found during the user study by the experimental group
2. Bug 36-56 found during the user study by the control group
3. Bug 57-88 found during the tool development and test scenario variation

| No.      | Bug ID | Period |
| -------- | ------ | ------ |
| 1  | https://bugzilla.mozilla.org/show_bug.cgi?id=1844283 | user study |
| 2  | https://bugzilla.mozilla.org/show_bug.cgi?id=1844289 | user study |
| 3  | https://bugzilla.mozilla.org/show_bug.cgi?id=1844980 | user study |
| 4  | https://bugzilla.mozilla.org/show_bug.cgi?id=1844891 | user study |
| 5  | https://bugzilla.mozilla.org/show_bug.cgi?id=1844893 | user study |
| 6  | https://bugzilla.mozilla.org/show_bug.cgi?id=1844902 | user study |
| 7  | https://bugzilla.mozilla.org/show_bug.cgi?id=1844931 | user study |
| 8  | https://bugzilla.mozilla.org/show_bug.cgi?id=1844933 | user study |
| 9  | https://bugzilla.mozilla.org/show_bug.cgi?id=1844374 | user study |
| 10 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844390 | user study |
| 11 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844972 | user study |
| 12 | https://bugzilla.mozilla.org/show_bug.cgi?id=1831455 | user study |
| 13 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844998 | user study |
| 14 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844999 | user study |
| 15 | https://bugzilla.mozilla.org/show_bug.cgi?id=1845000 | user study |
| 16 | https://bugzilla.mozilla.org/show_bug.cgi?id=1845002 | user study |
| 17 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844935 | user study |
| 18 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844936 | user study |
| 19 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844621 | user study |
| 20 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844715 | user study |
| 21 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844720 | user study |
| 22 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844339 | user study |
| 23 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862130 | user study |
| 24 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862134 | user study |
| 25 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862893 | user study |
| 26 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862164 | user study |
| 27 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862175 | user study |
| 28 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862193 | user study |
| 29 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862355 | user study |
| 30 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862354 | user study |
| 31 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862559 | user study |
| 32 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862183 | user study |
| 33 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862974 | user study |
| 34 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862188 | user study |
| 35 | https://bugzilla.mozilla.org/show_bug.cgi?id=1863719 | user study |
| 36 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862351 | user study |
| 37 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844272 | user study |
| 38 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844276 | user study |
| 39 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844374 | user study |
| 40 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844973 | user study |
| 41 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844376 | user study |
| 42 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844378 | user study |
| 43 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844380 | user study |
| 44 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844383 | user study |
| 45 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844331 | user study |
| 46 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844384 | user study |
| 47 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844393 | user study |
| 48 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844975 | user study |
| 49 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844980 | user study |
| 50 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862576 | user study |
| 51 | https://bugzilla.mozilla.org/show_bug.cgi?id=1863004 | user study |
| 52 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862811 | user study |
| 53 | https://bugzilla.mozilla.org/show_bug.cgi?id=1863000 | user study |
| 54 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862366 | user study |
| 55 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862567 | user study |
| 56 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862568 | user study |
| 57 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844934 | others |
| 58 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844790 | others |
| 59 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844808 | others |
| 60 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844316 | others |
| 61 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844322 | others |
| 62 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844984 | others |
| 63 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844985 | others |
| 64 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844987 | others |
| 65 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844988 | others |
| 66 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844937 | others |
| 67 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844938 | others |
| 68 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844778 | others |
| 69 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844898 | others |
| 70 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844899 | others |
| 71 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844903 | others |
| 72 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844932 | others |
| 73 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844940 | others |
| 74 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844969 | others |
| 75 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844971 | others |
| 76 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844399 | others |
| 77 | https://bugzilla.mozilla.org/show_bug.cgi?id=1844997 | others |
| 78 | https://bugzilla.mozilla.org/show_bug.cgi?id=1845136 | others |
| 79 | https://bugzilla.mozilla.org/show_bug.cgi?id=1846182 | others |
| 80 | https://bugzilla.mozilla.org/show_bug.cgi?id=1846184 | others |
| 81 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862360 | others |
| 82 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862139 | others |
| 83 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862138 | others |
| 84 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862352 | others |
| 85 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862821 | others |
| 86 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862823 | others |
| 87 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862824 | others |
| 88 | https://bugzilla.mozilla.org/show_bug.cgi?id=1862931 | others |
