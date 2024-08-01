import requests
import operator
import json

from configuration import Configuration

class WorkItem():
    def __init__(self, projectID) -> None:
        self.config = Configuration()
        self.workItems = []

        if projectID == None:
            self.url = f"{self.config.schema}://{self.config.polarionHost}/{self.config.polarionAPIPrefix}/all/workitems"
        else:
            self.url = f"{self.config.schema}://{self.config.polarionHost}/{self.config.polarionAPIPrefix}/projects/{projectID}/workitems"

        self.response = requests.get(url=self.url,
                params=self.config.dataFilter,
                headers={
                    "accept": "application/json",
                    "content-type": "application/json",
                    "authorization": f"Bearer {self.config.apiToken}"
                }
        )

        if self.response.status_code != 200:
            print(f"Request '{self.url}' failed: {self.response.status_code}")
            exit
    
        workItems = json.loads(self.response.text)["data"]

        for workItem in workItems:
            self.workItems.append(workItem)
        
        self.workItems.sort(key=operator.itemgetter("id"))


    def getWorkItemDetails(self, workItemID: str) -> map:
        for workItem in self.workItems:
            id = workItem["id"].split("/")[1]
            if id == workItemID:
                return workItem["attributes"]


if __name__ == "__main__":
    workItems = WorkItem(projectID="drivepilot")

    for workItem in workItems.workItems:
        print(workItem["id"])