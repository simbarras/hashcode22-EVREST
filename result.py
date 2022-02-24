class Result:
    project: str
    collaborator: list

    def __init__(self, project: str):
        self.project = project
        self.collaborator = []

    def add_collaborator(self, collaborator: str):
        self.collaborator.append(collaborator)
