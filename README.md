# Trading-Projection
This is a super simple python file that calculates your account size over a time period from trading. Please read all the way to the end.

To make it work, you will need to hard code in 8 values. You can change these at any time to see different paths your account could take. 
The values are: 
- win_rate (the percent of all your trades that you win)
- break_even_rate (the percent of all your trades that you break even)
- win_percent (your average percent gain on wins)
- loss_percent (your average percent loss on losses)
- trades_per_week (the number of trades you take each week)
- account_size (the size of your account)
- trading_with (this is the percent of your account size that you enter each trade with)
- weeks (how many weeks you want to see simulated)

After you enter all this information and run the program, on the terminal will be a weekly view of your account size changes that includes each trade's outcome.
At the end, you will see a summary showing your wins, break evens, losses, and account size growth.

While this is a pretty cool tool, PLEASE keep a couple of things in mind
- This is by no means guaranteed. It requires consistency above all things. That is one of the things that makes a great trader, having a consistent strategy over a long period.
- Because of the way the program determines the outcome of your next trade, you will see varation if you run the program more than once with the same values. However, running the program about 5 or so times will give you a good picture of where the end account sizes will fall around. 
- Lastly, this program assumes a 100% reinvestment rate. 

Thank you for giving this a look! If you appreciate the work or have any comments/suggestions, I'd be happy to hear!
