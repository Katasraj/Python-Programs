from locust import User, task, constant


class MyFirstTest(User):
    weight = 2                  # Probability of picking up the class
    wait_time = constant(1)

    @task
    def launch1(self):
        print("Launching URL_1: ")

    @task
    def search1(self):
        print("Searching_1")

class MySecondTest(User):
    weight = 2
    wait_time = constant(1)

    @task
    def launch2(self):
        print("Launching URL_2: ")

    @task
    def search2(self):
        print("Searching_2")



