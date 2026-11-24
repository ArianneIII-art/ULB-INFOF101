# # Created
# Author: Arianneiii-art
# Date: November 23, 2026
# License: AGPLV3

# To be funnier, i did not iclude the documentation, 
# see the main.py file for the comment and documentation since this file is simply an reimplementation only using oneliner,
# but the logic is the same. This implementation also lack the load from file because do a merge request if you want it

class Player:
    def __init__(self, last_name: str, first_name: str, nationality: str) -> None:
        self.last_name, self.first_name, self.nationality, self.teams, self.played_matches = last_name, first_name, nationality, [], dict()
    
    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def add_match(self, team1: str, team2: str, number_of_goal: int|str) -> None:
        self.played_matches[(team1, team2)] = int(number_of_goal)
    
    def total_goals(self) -> int:
        return sum(self.played_matches.values())
    
    def total_matches(self) -> int:
        return len(self.played_matches)
    
    def __str__(self) -> str:
        return f"Player «{self.first_name} {self.last_name}, {self.teams}, {self.total_goals()} buts en {self.total_matches()} matchs»"
    
    def read_matches_from_file(self, file_path: str) -> None:
        with open(file_path) as f: [self.add_match(*line.split(',')) for line in f]
