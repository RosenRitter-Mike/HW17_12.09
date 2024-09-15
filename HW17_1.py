import pprint

import sqlite_lib as sl


# 1.
def print_course(courses: list) -> None:
    for course in courses:
        # for cur in course:
        #     if not cur:
        #         cur = "N/A";
        course = [cur if cur else "N/A" for cur in course]

        print(f"{course[0]:4} | {course[1]:30} | {course[2]:12} | {course[3]:12} | {course[4]:30}  ")


# a.
def curses_with_lector() -> None:
    sl.connect('hw17_db');

    result: list[tuple] = sl.run_query_select('''
            SELECT co.course_id, co.course_name, lec.first_name, lec.last_name, lec.email FROM courses co
            JOIN lecturers lec USING(lecturer_id);
        ''');

    print_course(result);


# mini_test
# curses_with_lector();

# b.
def curses_with_no_lector() -> None:
    sl.connect('hw17_db');

    result: list[tuple] = sl.run_query_select('''
            SELECT co.course_id, co.course_name, lec.first_name, lec.last_name, lec.email FROM courses co
            LEFT JOIN lecturers lec USING(lecturer_id)
            WHERE first_name IS NULL ;
        ''');

    print_course(result);


# mini_test
# curses_with_no_lector();

# c.
def all_curses() -> None:
    sl.connect('hw17_db');

    result: list[tuple] = sl.run_query_select('''
            SELECT co.course_id, co.course_name, lec.first_name, lec.last_name, lec.email FROM courses co
            LEFT JOIN lecturers lec USING(lecturer_id)
        ''');

    print_course(result);


# mini_test
# all_curses();

# d.
def curses_with_lector_2() -> None:
    sl.connect('hw17_db');

    result: list[tuple] = sl.run_query_select('''
            SELECT co.course_name, lec.first_name, lec.last_name FROM courses co
            JOIN lecturers lec USING(lecturer_id);
        ''');

    pprint.pprint(result);


# mini_test
# curses_with_lector_2()

# e.
def lector_with_no_course() -> None:
    sl.connect('hw17_db');

    result: list[tuple] = sl.run_query_select('''
            SELECT co.course_id, co.course_name, lec.first_name, lec.last_name, lec.email FROM lecturers lec
            LEFT JOIN courses co USING(lecturer_id)
            WHERE course_name IS NULL ;
        ''');

    print_course(result);


# mini_test
# lector_with_no_course();

# f.
def all_lectors() -> None:
    sl.connect('hw17_db');

    result: list[tuple] = sl.run_query_select('''
            SELECT co.course_id, co.course_name, lec.first_name, lec.last_name, lec.email FROM lecturers lec
            LEFT JOIN courses co USING(lecturer_id)
        ''');

    print_course(result);


# mini_test
# all_lectors();

# g.
def all_in_all() -> None:
    sl.connect('hw17_db');

    ''' SELECT * FROM lecturers lec
        FULL OUTER JOIN courses co USING(lecturer_id) '''

    result: list[tuple] = sl.run_query_select('''
            SELECT * FROM lecturers l 
            LEFT OUTER JOIN courses c ON l.lecturer_id = c.lecturer_id
            UNION
            SELECT * FROM courses c 
            lEFT OUTER JOIN lecturers l ON l.lecturer_id = c.lecturer_id 
        ''');

    print_course(result);


# MINI_TEST
all_in_all();


# h.
def all_lect() -> None:
    sl.connect('hw17_db');

    result: list[tuple] = sl.run_query_select('''
            SELECT l.*, c.course_id, c.course_name FROM lecturers l 
            CROSS JOIN courses c 
        ''');

    print_course(result);


# MINI_TEST
# all_lect();
