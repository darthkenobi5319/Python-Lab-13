import helpers

#
# Each of the following functions have an arbitrary return value. Your
# job is to edit the functions to return the correct value. You'll
# know it's correct because when you run test.py, a message ending
# with "ok" will be printed for each:
#
#   test_a_rsum (__main__.RecursionTest) ... ok
#
# for example.
#

def rsum(values):
    if not values:
        return 0
    else:
        return helpers.head(values)+rsum(helpers.tail(values))
    

def exponentiate(base, power):
    if not power:        
        return 1
    else:
        return base * exponentiate(base, power-1)

def get_nth(list_of, n):
    if n == 0:
        return helpers.head(list_of)
    else:
        return get_nth(helpers.tail(list_of),n-1)

def reverse(list_of):
    if not list_of:
        return list_of
    else:
        return reverse(helpers.tail(list_of)) + [helpers.head(list_of)]
    
def is_older(date_1, date_2):
    if not date_1:
        return False
    elif helpers.head(date_1) < helpers.head(date_2):
        return True
    elif helpers.head(date_1) == helpers.head(date_2):
        return is_older(helpers.tail(date_1),helpers.tail(date_2))
    else:
        return False

# def number_before_reaching_sum(total, numbers):
#     return -1

# def what_month(day):
#     return 0

# def elfish(word, elf):
#     return False

# def coin_game_strategies(coins):
#     return -1

# def coin_game_winner(coins, player_1, player_2):
#     return ''
