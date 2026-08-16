from rag.models.chunk import Chunk

SAMPLE_CHUNKS: list[Chunk] = [
    Chunk(
        id="handbook_p2_c1",
        text=(
            "Full-time employees accrue paid time off at a rate of 1.5 days per "
            "month worked, up to a maximum of 18 days per calendar year. Accrued "
            "days carry over into the following year only; any unused balance is "
            "forfeited at the end of that second year."
        ),
        filename="handbook.pdf",
        page=2
    ),

    Chunk(
        id="handbook_p3_c1",
        text=(
            "Employees may request up to twelve weeks of parental leave following "
            "the birth, adoption, or foster placement of a child. Requests should "
            "normally be submitted to Human Resources at least thirty days before "
            "the expected start date when advance notice is possible."
        ),
        filename="handbook.pdf",
        page=3
    ),

    Chunk(
        id="handbook_p3_c2",
        text=(
            "Employees returning from approved parental leave will normally return "
            "to the same position or to a substantially similar position with the "
            "same base salary. Employees should contact their manager one week "
            "before returning to confirm their expected return date."
        ),
        filename="handbook.pdf",
        page=3
    ),

    Chunk(
        id="handbook_p4_c1",
        text=(
            "Full-time employees receive five paid sick days each calendar year. "
            "Sick leave may be used for the employee's own illness, medical "
            "appointments, or to care for an immediate family member who is ill."
        ),
        filename="handbook.pdf",
        page=4
    ),

    Chunk(
        id="handbook_p5_c1",
        text=(
            "Employees called for jury duty may take up to ten working days of "
            "paid jury-duty leave. Employees must provide a copy of the official "
            "jury summons to Human Resources before the leave begins."
        ),
        filename="handbook.pdf",
        page=5
    ),

    # Negation pair
    Chunk(
        id="handbook_p6_c1",
        text=(
            "Travel expenses for required company training are covered by the "
            "company. Eligible expenses include standard transportation, hotel "
            "accommodations, and reasonable meal costs when approved in advance."
        ),
        filename="handbook.pdf",
        page=6
    ),

    Chunk(
        id="handbook_p6_c2",
        text=(
            "Travel expenses for required company training are not covered by "
            "the company. Employees are responsible for their own "
            "transportation, hotel accommodations, and meal costs."
        ),
        filename="handbook.pdf",
        page=6,
    ),

    Chunk(
        id="benefits_p2_c1",
        text=(
            "Employees whose roles are designated as remote-eligible may work from "
            "home up to three days per week. The remaining workdays must normally "
            "be completed from the employee's assigned office unless a manager "
            "approves a temporary exception."
        ),
        filename="benefits_guide.pdf",
        page=2
    ),

    Chunk(
        id="benefits_p3_c1",
        text=(
            "Remote employees may receive a home-office stipend of up to $500 once "
            "every two years. The stipend may be used for approved equipment such "
            "as a desk, office chair, external monitor, keyboard, or webcam."
        ),
        filename="benefits_guide.pdf",
        page=3
    ),

    # Near-duplicate pair
    Chunk(
        id="benefits_p3_c2",
        text=(
            "Employees approved for remote work can request reimbursement of up to "
            "$500 for home-office equipment during each two-year period. Eligible "
            "purchases include desks, chairs, monitors, keyboards, and webcams."
        ),
        filename="benefits_guide.pdf",
        page=3
    ),

    Chunk(
        id="benefits_p4_c1",
        text=(
            "The company provides employees with a monthly internet reimbursement "
            "of up to $40 when their position requires regular remote work. "
            "Employees must submit an internet bill through the expense system "
            "before reimbursement will be issued."
        ),
        filename="benefits_guide.pdf",
        page=4
    ),

    Chunk(
        id="benefits_p5_c1",
        text=(
            "Employees may enroll in the company's health insurance plan during "
            "their first thirty days of employment or during the annual open "
            "enrollment period. Coverage options include medical, vision, and "
            "dental plans for eligible employees and dependents."
        ),
        filename="benefits_guide.pdf",
        page=5
    ),

    Chunk(
        id="security_p2_c1",
        text=(
            "Employees must wear their company identification badge while inside "
            "secured office areas. Lost or stolen badges must be reported to the "
            "security team immediately so that building access can be disabled."
        ),
        filename="security_policy.pdf",
        page=2
    ),

    Chunk(
        id="security_p3_c1",
        text=(
            "Company account passwords must contain at least twelve characters and "
            "must not be shared with another employee. Passwords should not contain "
            "the employee's name, email address, or easily guessed personal "
            "information."
        ),
        filename="security_policy.pdf",
        page=3
    ),

    Chunk(
        id="security_p4_c1",
        text=(
            "Multi-factor authentication is required for access to company email, "
            "source-code repositories, and administrative systems. Employees should "
            "never approve an authentication request they did not personally initiate."
        ),
        filename="security_policy.pdf",
        page=4
    ),
]

# Planted unanswerable question (for Lesson 9):
# "How much paid time off do part-time employees get?"
# Sounds like it should be in the handbook. It isn't anywhere.