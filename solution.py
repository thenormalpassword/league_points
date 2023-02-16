def league_points(wins, draws, losses):
 
 wins = 3 * wins 
 draws = 1 * draws
 losses = 0 * losses
 
 total = ( wins + draws + losses )
 return total
 
if __name__ == "__main__":
 print(league_points(3, 4, 2))
