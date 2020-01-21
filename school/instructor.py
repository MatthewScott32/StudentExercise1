class Instructor:
    def __init__(self, inst_first_name, inst_last_name, slack_handle, cohort, specialty):
        self.inst_first_name = inst_first_name
        self.inst_last_name = inst_last_name
        self.slack_handle = slack_handle
        self.cohort = cohort
        self.specialty = specialty

    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)