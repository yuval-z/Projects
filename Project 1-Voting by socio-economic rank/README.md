This is a simple project regarding linear regression. In this project I use the voting data for each point of settlement in the 2021 Israeli elections, and use a normalized least squares formula to calculate the effect each party in the election has on the socio-economic rank of that city.
The data used has the samples (the number of votes for each party in each city) and the lables (the socio-economic ranks for each city according to the Central Bureau Of Statistics).
The Output is:
1. The factors for each political party-in other words, what would the projected socio-economic rank of a city with 100% votes for a political party be.
2. A confusion matrix with the projected and actual socio-economic ranks. You can see that for approximately 40% of cities the prediction was precise and for approximately 90% the margin of error was smaller or equal to 1.
3. The 10 points of settlement with the most accurate and least accurate predictions.
