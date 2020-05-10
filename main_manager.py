import random


class Mangler:
    def __init__(self, proj_name):
        self.proj_name = proj_name
        self.working_branches = []
        self.accepted_branch_types = ['feature', 'bug']

    def __repr__(self):
        return f"Mangler('{self.proj_name}')"

    def new_branch_name(self, branch_type):
        # TODO: Add loop so method restarts if branch already exists
        if branch_type in self.accepted_branch_types:
            if branch_type == 'feature':
                new_branch = f'feature-{random.randint(1, 1000)}'
                if new_branch in self.working_branches:
                    return False
                else:
                    self.working_branches.append(new_branch)
            elif branch_type == 'bug':
                new_branch = f'bug-{random.randint(1, 10000)}'
                if new_branch in self.working_branches:
                    return False
                else:
                    self.working_branches.append(new_branch)
        else:
            return False

    def remove_branch_by_name(self, branch_name):
        if branch_name in self.working_branches:
            self.working_branches.remove(branch_name)
        else:
            return False
