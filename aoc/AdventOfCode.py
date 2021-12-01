from typing import Union
from requests import Session
from dotenv import dotenv_values
from os import path
from requests.cookies import cookiejar_from_dict
from importlib import import_module


class AdventOfCode:

    def __init__(self, root_dir: str, year: int) -> None:
        # Setup environment
        environment_file = path.join(root_dir, ".env")
        if not path.exists(environment_file):
            with open(environment_file, 'w') as file:
                file.write("SESSION_TOKEN=<Insert session token here!>")
            print(f"An empty environment file has been created in {environment_file}")
            exit()
        environment = dotenv_values(environment_file)

        # Initialize client
        client = Session()
        client.headers = {
            "User-Agent" : "AdventOfCode/1.0"
        }
        client.cookies = cookiejar_from_dict({
            "session" : environment["SESSION_TOKEN"]
        })

        # Init variables
        self.__client = client
        self.__root_dir = root_dir
        self.__year = year
        
    def run_challenges(self):
        for i in range(1, 25):
            challenge_file = path.join(self.__root_dir, "days", f"day{i}.py")
            if path.exists(challenge_file):
                print(f"Day {i}")

                daily_inputs = self.get_inputs(i)

                module = import_module(f"days.day{i}")
                first_task = getattr(module, "firstPart")
                second_task = getattr(module, "secondPart")

                first_result = first_task(daily_inputs)
                second_result = None

                if first_result != None:
                    second_result = second_task(daily_inputs, first_result)

                print(f"\tFirst result: {str(first_result)}")
                print(f"\tSecond result: {str(second_result)}")
            else:
                print(f"No file for day {i}")

    def get_inputs(self, day: int) -> str:
        url = f"https://adventofcode.com/{self.__year}/day/{day}/input"
        response = self.__client.get(url)
        return response.content.decode("utf-8", "strict")
