"""Hand-written sample chunks for Lessons 2-6.

Fake university documents. Designed to expose retrieval behaviour:
topic clusters, one near-duplicate pair, one negation pair, and one
planted unanswerable question (see bottom of file).

Order is fixed. Lesson 3 embeds this list positionally, so do not sort,
filter, or reorder.
"""

from rag.models.chunk import Chunk

SAMPLE_CHUNKS: list[Chunk] = [
    # --- Topic A: grading (course_syllabus.pdf) ---
    Chunk(
        id="syllabus_p2_c1",
        text=(
            "The final course grade is calculated from four components: weekly "
            "assignments account for 40 percent, the midterm examination for 25 "
            "percent, the final examination for 30 percent, and in-class "
            "participation for the remaining 5 percent."
        ),
        filename="course_syllabus.pdf",
        page=2,
    ),

    Chunk(
        id="syllabus_p2_c2",
        text=(
            "Letter grades are assigned on the following scale: A from 90 percent "
            "and above, B from 80 to 89 percent, C from 70 to 79 percent, and D "
            "from 60 to 69 percent. Any final score below 60 percent is recorded "
            "as a failing grade."
        ),
        filename="course_syllabus.pdf",
        page=2,
    ),

    # --- Near-duplicate pair, first half (see handbook_p4_c1) ---
    Chunk(
        id="syllabus_p3_c1",
        text=(
            "Assignments submitted after the posted deadline lose 10 percent of "
            "the available marks for each day they are late. Submissions are no "
            "longer accepted once an assignment is five days overdue, and a score "
            "of zero is recorded."
        ),
        filename="course_syllabus.pdf",
        page=3,
    ),

    Chunk(
        id="syllabus_p3_c2",
        text=(
            "Students who believe an assignment has been marked incorrectly may "
            "request a regrade within seven calendar days of receiving the mark. "
            "Requests must be submitted in writing and must explain which specific "
            "criterion the student believes was misapplied."
        ),
        filename="course_syllabus.pdf",
        page=3,
    ),

    Chunk(
        id="syllabus_p4_c1",
        text=(
            "A minimum final grade of C is required for this course to count "
            "toward the major requirements. Students who finish with a D may still "
            "receive elective credit, but must retake the course before enrolling "
            "in any dependent upper-level course."
        ),
        filename="course_syllabus.pdf",
        page=4,
    ),

    # --- Topic B: attendance (student_handbook.pdf) ---
    Chunk(
        id="handbook_p2_c1",
        text=(
            "Students are permitted a maximum of four unexcused absences per "
            "semester in any course meeting twice weekly. A fifth unexcused "
            "absence reduces the final course grade by one full letter, and a "
            "seventh results in administrative withdrawal from the course."
        ),
        filename="student_handbook.pdf",
        page=2,
    ),

    Chunk(
        id="handbook_p2_c2",
        text=(
            "An absence is considered excused when it results from documented "
            "illness, a religious observance, a university-sanctioned activity, or "
            "a family emergency. Supporting documentation must be submitted to the "
            "registrar within ten days of the missed session."
        ),
        filename="student_handbook.pdf",
        page=2,
    ),

    Chunk(
        id="handbook_p3_c1",
        text=(
            "The participation component of a course grade reflects both presence "
            "and contribution. Students who attend consistently but do not "
            "contribute to discussion should expect to receive roughly half of the "
            "available participation marks."
        ),
        filename="student_handbook.pdf",
        page=3,
    ),

    Chunk(
        id="handbook_p3_c2",
        text=(
            "Work missed because of an excused absence may be completed within two "
            "weeks of the student's return. Make-up examinations are scheduled by "
            "the department rather than the instructor and may differ in format "
            "from the original assessment."
        ),
        filename="student_handbook.pdf",
        page=3,
    ),

    # --- Near-duplicate pair, second half (see syllabus_p3_c1) ---
    Chunk(
        id="handbook_p4_c1",
        text=(
            "Late coursework is penalised at a rate of ten percent of the total "
            "possible marks per day past the due date. After the fifth day, the "
            "submission will not be graded and the student receives no credit for "
            "that piece of work."
        ),
        filename="student_handbook.pdf",
        page=4,
    ),

    # --- Topic C: academic integrity (academic_policy.pdf) ---
    Chunk(
        id="policy_p2_c1",
        text=(
            "Plagiarism is the presentation of another person's words, ideas, or "
            "data as one's own. A first confirmed offence results in a zero for "
            "the assessment and a formal note on the student's file; a second "
            "offence is referred to the academic conduct board."
        ),
        filename="academic_policy.pdf",
        page=2,
    ),

    Chunk(
        id="policy_p2_c2",
        text=(
            "All directly quoted material must appear in quotation marks with an "
            "accompanying citation, and paraphrased material must be cited even "
            "when no words are shared. Students may use any consistent citation "
            "style unless the instructor specifies one."
        ),
        filename="academic_policy.pdf",
        page=2,
    ),

    Chunk(
        id="policy_p3_c1",
        text=(
            "During examinations, students may bring only writing implements and "
            "an approved calculator. Mobile phones, smart watches, and notes of "
            "any kind must be left at the front of the room, and leaving the room "
            "mid-examination requires proctor approval."
        ),
        filename="academic_policy.pdf",
        page=3,
    ),

    # --- Negation pair: same subject, opposite polarity ---
    Chunk(
        id="policy_p4_c1",
        text=(
            "Collaboration on take-home assignments is permitted. Students may "
            "discuss approaches and work through problems together, provided each "
            "student writes and submits their own solution independently."
        ),
        filename="academic_policy.pdf",
        page=4,
    ),

    Chunk(
        id="policy_p4_c2",
        text=(
            "Collaboration on take-home assignments is not permitted. Students may "
            "not discuss approaches or work through problems together, and all "
            "submitted solutions must be produced entirely independently."
        ),
        filename="academic_policy.pdf",
        page=4,
    ),
]

# Planted unanswerable question (for Lesson 9):
# "What is the policy for requesting an incomplete grade?"
# Sounds like it belongs in the academic policy. It is nowhere in these documents.