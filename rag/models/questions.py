from pydantic import BaseModel, ConfigDict
from typing import Literal

class EvalCase(BaseModel):
    model_config = ConfigDict(frozen=True)

    question: str
    kind: Literal["factual", "cross_context", "ambiguous", "unanswerable"]
    expected_sources: list[tuple[str, int]]
    note: str


TEST_QUESTIONS: list[EvalCase] = [
    # --- factual ---
    EvalCase(
        question="What score do I need to pass this course?",
        kind="factual",
        expected_sources=[("course_syllabus.pdf", 2)],
        note="Baseline smoke test. p2 has the 60 percent failing threshold. "
             "Watch for p4 (minimum C for major credit) crowding in — that is a "
             "different question and should not count as the answer.",
    ),
    EvalCase(
        question="How many days do I have to request a regrade?",
        kind="factual",
        expected_sources=[("course_syllabus.pdf", 3)],
        note="Corpus-specific number (seven calendar days). Four chunks contain "
             "'days'; only one answers. Retrieved cleanly in Lesson 4 at 0.727 "
             "vs 0.417 second place — this is the control case.",
    ),
    EvalCase(
        question="What items am I allowed to bring into an examination?",
        kind="factual",
        expected_sources=[("academic_policy.pdf", 3)],
        note="Control for academic_policy.pdf — proves the third document is "
             "retrievable at all, so a miss on the plagiarism case below is "
             "isolated to that page rather than the whole file.",
    ),
    EvalCase(
        question="What happens if I am caught plagiarizing?",
        kind="factual",
        expected_sources=[("academic_policy.pdf", 2)],
        note="EXPECTED TO MISS. The content is in the PDF but p2 is image-only "
             "and extracted to an empty string, so no chunk exists. This is an "
             "extraction failure that will present as a retrieval failure — "
             "diagnosis exercise, ladder step 2.",
    ),

    # --- cross_context ---
    EvalCase(
        question="I missed a class because I was sick. What counts as documented, "
                 "and how long do I have to make up the work?",
        kind="cross_context",
        expected_sources=[("student_handbook.pdf", 2), ("student_handbook.pdf", 3)],
        note="Two halves in one file: p2 defines an excused absence and the "
             "ten-day documentation window, p3 gives the two-week make-up window. "
             "Neither page alone answers it.",
    ),
    EvalCase(
        question="My assignment is four days late. How much credit do I lose, and "
                 "which document governs that?",
        kind="cross_context",
        expected_sources=[("course_syllabus.pdf", 3), ("student_handbook.pdf", 1)],
        note="Hard by design. p3 has the ten-percent-per-day penalty; handbook p1 "
             "has the precedence rule (syllabus wins when stricter). The "
             "near-duplicate late-work chunk in handbook p4 will compete for a "
             "top-3 slot and may push p1 out.",
    ),

    # --- ambiguous ---
    EvalCase(
        question="Can I work with other students on take-home assignments?",
        kind="ambiguous",
        expected_sources=[("academic_policy.pdf", 4)],
        note="Negation pair, both chunks on p4. Retrieval passes trivially — the "
             "entire test is at generation: naming the contradiction is correct, "
             "any confident single answer is a FAIL on 'appropriate' regardless "
             "of which side it picks.",
    ),

    # --- unanswerable ---
    EvalCase(
        question="What is the policy for requesting an incomplete grade?",
        kind="unanswerable",
        expected_sources=[],
        note="Planted gap from Lesson 2. Refused cleanly in Lesson 6. Nearby "
             "excused-absence material makes stretching plausible, so this is a "
             "real refusal test, not a freebie.",
    ),
    EvalCase(
        question="What is the maximum number of credit hours I can take per semester?",
        kind="unanswerable",
        expected_sources=[],
        note="Leak test. Sounds like handbook content and the model has strong "
             "priors (commonly 18). Any specific number in the answer means "
             "pretrained knowledge got through the grounding instruction.",
    ),
]