import random


def win_trade(win_percent, account_size, trading_with):
    account_size *= (1 + (win_percent * trading_with))
    return round(account_size, 2)


def lose_trade(loss_percent, account_size, trading_with):
    account_size *= (1 - (loss_percent * trading_with))
    return round(account_size, 2)

# Enter in your win rate and break even rate. This will be an estimated percent of the trades that you win and break
# even on. Your loss rate is calculated from these two. Make sure you enter it with the following format:
# If you win 50% of your trades, enter 50.


win_rate = 50
break_even_rate = 20
loss_rate = 100 - win_rate - break_even_rate


# This section is for your win percent and loss percent. If on average, your wins are 5% each, enter 5.
# Do not change the part that has '/ 100'. Do the same for your loss percent


win_percent = 5 / 100
loss_percent = 1 / 100


# Here you will enter the number of trades you take per week. If you trade 3 times a day, multiply by 5 to get 15
# The next value is your account size in your currency. Ignore the following line
# The last line 'trading_with' is the percent of your account size that you enter a trade with. So if you have
# a $10,000 account, and you only trade with $2,500 of that, you are trading with 2,500/10,000 or 25% of your account
# Enter that value in this format 25% --> 0.25

trades_per_week = 10
account_size = 25000
original_account_size = account_size
trading_with = 0.25
weeks = 12

win_count = 0
break_even_count = 0
loss_count = 0
for i in range(1, weeks + 1):
    print("-" * 50)
    print(f"Week {i}:")
    for j in range(trades_per_week):
        rand_num = random.randint(1, 100)
        if rand_num <= win_rate:  # Win
            account_size = win_trade(win_percent, account_size, trading_with)
            print(f"Won: ${account_size}")
            win_count += 1
        elif rand_num <= (win_rate + break_even_rate):  # Break even
            print("Broke even.")
            break_even_count += 1
        else:  # Lose
            account_size = lose_trade(loss_percent, account_size, trading_with)
            print(f"Lost: ${account_size}")
            loss_count += 1

print(f"""
Summary
Wins: {win_count}
Break evens: {break_even_count}
Losses: {loss_count}
Account size growth: ${original_account_size} to ${account_size}
""")