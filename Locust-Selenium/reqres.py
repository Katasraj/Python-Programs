from locust import HttpUser,constant,task


class MyReqRes(HttpUser):

    host = "https://reqres.in"
    wait_time = constant(1)

    @task
    def get_Users(self):
        get_res = self.client.get("/api/users?page=2")
        print(get_res.text)
        print(get_res.status_code)
        print(get_res.headers)

    @task
    def create_User(self):
        post_res = self.client.post("/api/users",data='''{name: "morpheus", job: "leader"}''')
        print(post_res.text)
        print(post_res.status_code)
        print(post_res.headers)



