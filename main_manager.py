import random


class Mangler:
    def __init__(self, proj_name):
        self.proj_name = proj_name
        self.working_branches = []
        self.accepted_branch_types = ['feature', 'bug']

    def __repr__(self):
        return f"Mangler('{self.proj_name}')"

    def new_branch_name(self, branch_type):
        if branch_type in self.accepted_branch_types:
            if branch_type == 'feature':
                pass
            elif branch_type == 'bug':
                pass
        else:
            return False
