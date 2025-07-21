from api_requests.request_generator import RequestGenerator


class UsersRequestGenerator(RequestGenerator):
    def __init__(self, base_url: str = "https://reqres.in/api"):
        super().__init__(base_url)

    def get_users(self, page):
        return self.get(f"/users?page={page}")

    def get_user_by_id(self, user_id: int):
        return self.get_by_id(f"/users/{user_id}")

    def create_user(self, data: dict):
        return self.post("/users", data)

    def update_user(self, user_id: int, data: dict):
        return self.put(f"/users/{user_id}", data)

    def patch_user(self, user_id: int, data: dict):
        return self.patch(f"/users/{user_id}", data)

    # DELETE
    def delete_user(self, user_id: int):
        return self.delete(f"/users/{user_id}")
