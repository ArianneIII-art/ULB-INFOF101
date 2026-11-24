# # Created
# Author: Arianneiii-art
# Date: November 23, 2026
# License: AGPLV3

class Player:
    """Représentation via un un objet du jouer de la coupe du monde"""
    
    def __init__(self, last_name: str, first_name: str, nationality: str) -> None:
        """
        Constructeur de la classe Player

        last_name: str, first_name: str, nationality: str
        are exactly what they say they are.

        played_matches and teams are also initialise in the constructor but set to empty structure.

        teams: list[str] (la liste des équipes (nationale ou club) avec lesquelles le joueur joue ou a joué dans le passé.)

        played_matches: dict[tuple[str, str] : int] (le nombre de buts du joueur pour chaque match joué. Les clés de ce dictionnaire seront des tuples de deux équipes, et les valeurs les nombres de buts.)
        """
        self.last_name: str = last_name
        self.first_name: str = first_name
        self.nationality: str = nationality
        self.teams: list[str] = []
        self.played_matches: dict[tuple[str, str] : int] = dict()
    
    def get_name(self) -> str:
        """
        Retourne le nom complet du joueur sous le format string
        """
        return f"{self.first_name} {self.last_name}"
    
    def add_match(self, team1: str, team2: str, number_of_goal: int) -> None:
        """
        add a match to the played_matches dictionary
        team1 and team2 are the two teams who participeate in the match
        number_of_goal is the number of goal scored by the player

        team1 and team2 does not equal to team2, team1.
        This mean that if you need to modify a match for any reason, you need to know he order you input the two team to be sure you modify the correct match
        """
        self.played_matches[(team1, team2)] = number_of_goal
    
    def total_goals(self) -> int:
        """
        Return the sum of the goal scored by the player using played_matches
        The sum is return as an integer
        """
        return sum(self.played_matches.values())
    
    def total_matches(self) -> int:
        """
        Return the number of match played by the player using played_matches
        The return value is an integer
        """
        return len(self.played_matches)
    
    def __str__(self) -> str:
        """
        return a given string who create a simple recap of the current state of the class
        """
        return f"Player «{self.first_name} {self.last_name}, {self.teams}, {self.total_goals()} buts en {self.total_matches()} matchs»"
    
    def read_matches_from_file(self, file_path: str) -> None:
        """
        Read from a file the match who happend and inject the data inside the add_match
        
        file_path: take a file path to the file who containt the data

        expected format for the file:
        team1,team2,numberofgoal

        short exemple of what a file would look like:
        France,Brazil,2
        France,Maroc,0
        France,Argentine,2
        """
        with open(file_path) as f:
            for line in f:
                tmp = line.split(',')
                tmp[2] = int(tmp[2])
                self.add_match(*tmp)
    
    def write_matches_to_file(self, file_path: str, mode: str ="a") -> None:
        """
        Write to a file the match who happend from the data inside the add_match variable
        
        file_path: take a file path to the file who containt the data

        mode: by default append the data but can be change to trunk the file before the write

        format for the file:
        team1,team2,numberofgoal
        """
        if not(mode == "a" or mode == "w"):
            raise ValueError("The mode need to be a (append) or w (overwrite the file)")

        with open(file_path, mode) as f:
            for i in self.played_matches:
                f.write(f"{i[0]},{i[1]},{self.played_matches[i]}\n")


# simple test not automated. Need human check!!!
if __name__ == "__main__":
    cr = Player ( "Ronaldo" , "Christiano" , "Portuguese" )
    cr.teams.append("France")
    cr.teams.append("Psg")
    print(cr.get_name())
    print(cr)
    cr.add_match("France","Russia",2)
    cr.add_match("France","Belgium",13)
    print(cr)
    cr.read_matches_from_file("/home/main/Project/INOFF101/devoir/coupe/match.csv")
    print(cr)
    cr.write_matches_to_file("/home/main/Project/INOFF101/devoir/coupe/res.csv", mode="w")