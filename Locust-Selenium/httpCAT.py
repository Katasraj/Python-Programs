from locust import TaskSet, constant, task, HttpUser
import random

class MyHTTPCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("GET Status of 200")

    @task
    def get_random_stats(self):
        status_codes = [100,101,102,200,201,202,203,204,205,206,207,208,226,300,301,302,303,304,305,306,307,308,
                        400,401,402,403,404,405,406,407,408,409,410,660]

        random_url = "/" + str(random.choice(status_codes))
        res = self.client.get(random_url)

        print("Random HTTP Status: ",res)


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MyHTTPCat]
    wait_time = constant(1)

