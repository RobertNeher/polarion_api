import operator
import json

from utils import polarionRequest

class Space():
    def __init__(self, projectID: str) -> None:
        self.spaces = []

        response = polarionRequest(f"/projects/{projectID}/spaces")

        if response == None:
            print(f"Request at end point '/projects/{projectID}/spaces' failed: {response.status_code}")
            exit

        spaces = json.loads(self.response.text)

        for space in spaces:
            self.spaces.append(space)
        
        self.spaces.sort(key=operator.itemgetter("id"))


if __name__ == "__main__":
    spaces = Space(projectID="drivepilot")