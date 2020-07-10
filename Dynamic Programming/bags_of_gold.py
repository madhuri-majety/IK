"""
http://www.techiedelight.com/pots-gold-game-dynamic-programming/
https://www.geeksforgeeks.org/optimal-strategy-for-a-game-dp-31/

maxgold(st, end) -> max gold I can get if I play first and can choose from bags st .. end
Player A: maximizing their gold
Player B: Minimizing the gold for Player A

Formula:
maxgold(s,e) = max{(v[s] + min(maxgold(v[s+2], v[e]), maxgold(v[s+1],v[e-1]))),
                   (v[e] + min(maxgold(v[s+1], v[e-1]), maxgold(v[s], v[e-2]))}

"""

def bagsofgold(coins, s, e):
    # Base Conditions
    if s == e:
        return coins[s]
    if s+ 1 == e:
        return max(coins[s], coins[e])

    # Recursive case

    # If player chooses front pot s, opponent left to choose from s+1, e
    # 1. If opponent chooses front pot s+1, recurse for [s+2, e]
    # 2. If opponent chooses from pot e, recurse for [s+1, e-1]
    start = coins[s] + min(bagsofgold(coins, s + 2, e), bagsofgold(coins, s + 1, e - 1))

    # If player  chooses rear pot e, opponent is left to choose from s, e-1
    # 1. If Opponent chooses from pot s, recuse for [s+1, e-1]
    # 2. If opponent chooses from pot e-1, recurse for [s, e-2]
    end = coins[e] + min(bagsofgold(coins, s + 1, e - 1), bagsofgold(coins, s, e - 2))

    # Return max of two choices
    return max(start, end)


def main():
    #coins = [5,8,2,3]
    coins = [5,8,2,3,6,9]

    print(bagsofgold(coins, 0, len(coins)-1))

if __name__ == '__main__':
    main()
