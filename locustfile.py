from locust import HttpUser, task, between

class WikipediaApiUser(HttpUser):
    wait_time = between(1, 3)  # Users wait between 1 and 3 seconds between tasks

    @task(3)  # This task will be executed 3 times more often than the search task
    def wiki(self):
        self.client.get(f"/wiki/apple")

    @task(1)  # Weight of 1, so it's executed less often than the wiki task
    def search(self):
        self.client.get(f"/search/apple")

