class Player:
    def __init__(self, player_id, name):
        self.player_id = player_id
        self.name = name
        self.runs = 0
        self.wickets = 0

    def update_runs(self, runs):
        self.runs += runs

    def update_wickets(self, wickets):
        self.wickets += wickets

    def display_stats(self):
        print(f"{self.name:<15} Runs: {self.runs:<5} Wickets: {self.wickets}")


class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.players = []

    def add_player(self, player):
        self.players.append(player)


class Scoreboard:
    def __init__(self, match):
        self.match = match

    def match_summary(self):
        total_runs = sum(player.runs for player in self.match.players)
        total_wickets = sum(player.wickets for player in self.match.players)

        print("\n========== MATCH SUMMARY ==========")
        print(f"Match : {self.match.team1} vs {self.match.team2}")
        print(f"Total Runs    : {total_runs}")
        print(f"Total Wickets : {total_wickets}")

        print("\nPlayer Statistics")
        print("-" * 40)

        for player in self.match.players:
            player.display_stats()

        print("=" * 40)


# Main Program

match = Match("India", "Australia")

n = int(input("Enter number of players: "))

for i in range(n):
    print(f"\nEnter Details of Player {i+1}")

    pid = input("Player ID: ")
    name = input("Player Name: ")

    player = Player(pid, name)

    runs = int(input("Runs Scored: "))
    wickets = int(input("Wickets Taken: "))

    player.update_runs(runs)
    player.update_wickets(wickets)

    match.add_player(player)

scoreboard = Scoreboard(match)
scoreboard.match_summary()