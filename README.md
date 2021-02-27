# N Queens declarative solution

A fun program I made using pycosat and sat_utils as provided from one of Raymond Hettinger's talks. (GitHub link [here](https://github.com/rhettinger/rhettinger.github.io)) (Website link [here](https://rhettinger.github.io/einstein.html))

I added two functions to sat_utils, one_or_less and zero_or_more. 

Set the size of board to n * n and number of queens to n by changing the n variable.

display_resulting_states when set to True will display all of the board states that were generated. Setting it to False will display a count of all solutions found and display the time in seconds it took to run.

Solutions generated do not account for rotations, i.e. a board that can be rotated to be another board will be considered distinct from the other board.

I have verified for a small n (<=4) that the program produces expected output. I also compared the number of solutions found to those on the wikipedia page for the 8 Queens puzzle ([found here](https://en.wikipedia.org/wiki/Eight_queens_puzzle#Counting_solutions)). It appears to be accurate for those I tested (n=8, n=12). 

## Performance

Testing performance on my personal computer, with a single run for n=12, it took 43.64 seconds to find all 14200 solutions with display_resulting_states set to False. Also note that I start the timer after setup has been completed, with solve_all being called immediately after the start time is captured.

With the same constraint that timing excludes setup, here are some other single-run results:

- For n=4, approx. 1ms, solutions: 2
- For n=5, approx. 1ms, solutions: 10
- For n=6, approx. 1ms, solutions: 4
- For n=7, approx. 3ms, solutions: 40
- For n=8, approx. 8ms, solutions: 92

...

- For n=12, approx. 43.64s, solutions: 14200
