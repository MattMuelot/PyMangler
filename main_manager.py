import random as r
from string import ascii_letters


class Mangler:
    def __init__(self, proj_name):
        self.proj_name = proj_name
        self.feature_branches = []
        self.bug_branches = []
        self.accepted_branch_types = ['feature', 'bug']

    def __repr__(self):
        return f"Mangler('{self.proj_name}')"

    def new_branch_name(self, branch_type):
        while True:
            if branch_type in self.accepted_branch_types:
                if branch_type == 'feature':
                    b_id = r.sample(ascii_letters, 2)
                    new_branch = f'feature-{b_id[0]}{b_id[1]}{r.randint(10, 99)}{r.choice(ascii_letters)}'
                    if new_branch in self.feature_branches:
                        continue
                    else:
                        self.feature_branches.append(new_branch)
                        return new_branch
                elif branch_type == 'bug':
                    b_id = r.sample(ascii_letters, 2)
                    new_branch = f'bug-{b_id[0]}{b_id[1]}{r.randint(10, 99)}{r.choice(ascii_letters)}'
                    if new_branch in self.bug_branches:
                        continue
                    else:
                        self.bug_branches.append(new_branch)
                        return new_branch
            else:
                return False

    def get_features(self):
        return self.feature_branches

    def get_bugs(self):
        return self.bug_branches

    def purge_project(self):
        for f in self.feature_branches:
            self.feature_branches.remove(f)

        for i in self.bug_branches:
            self.bug_branches.remove(i)

    def delete_branch_by_name(self, branch_name):
        if 'feature' in branch_name:
            if branch_name in self.feature_branches:
                self.feature_branches.remove(branch_name)
            else:
                pass
        elif 'bug' in branch_name:
            if branch_name in self.bug_branches:
                self.bug_branches.remove(branch_name)
            else:
                pass
