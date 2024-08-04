import requests
import operator
import json

from configuration import Configuration
from utils import polarionRequest

class WorkItem():
    def __init__(self, projectID) -> None:
        self.workItems = []

        if projectID == None:
            endPoint = "/all/workitems"
        else:
            endPoint = f"/projects/{projectID}/workitems"

        response = polarionRequest(endPoint)
        
        if response.status_code != 200:
            print(f"Request at endpoint '{endPoint}' failed: {response.status_code}")
            exit

        data = json.loads(response.text)

        for workItem in data["data"]:
            self.workItems.append(workItem)

        config = Configuration()
        data = json.loads(response.text)
        total = int(data["meta"]["totalCount"])

        pageCount = 0

        while pageCount < int(total/100):

            if "next" in data["links"]:
                url = data["links"]["next"]
            else:
                url = data["links"]["last"]
        
            response = requests.get(url=url,
                headers=config.header
            )

            data = json.loads(response.text)
            pageCount += 1

            for workItem in data["data"]:
                self.workItems.append(workItem)
        
        self.workItems.sort(key=operator.itemgetter("id"))


    def getWorkItemDetails(self, workItemID: str) -> map:
        for workItem in self.workItems:
            id = workItem["id"].split("/")[1]
            if id == workItemID:
                return workItem["attributes"]


if __name__ == "__main__":
    workItems = WorkItem(projectID=None)

    # for workItem in workItems.workItems:
    #     print(workItem["id"])