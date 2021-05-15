# Bayesian-Inference-On-The-Given-Data
## Objective
To estimate probability distributions or parameters of a given network. For this, we will make use of a dataset
containing samples comprising of values observed for different variables.

# Input Format
• Line 1: n : no. of variable or nodes (N1, N2, ...., Nn) \
• Line 2 to Line n + 1: Comma separated list of all possible values of variables N1 to Nn. \
• Line n + 2 to Line 2n + 1: n × n matrix of 1’s and 0’s representing conditional dependencies, e.g. a
value 1 at location (3,2) shows that N2 is conditionally dependent on N3 \
• Line 2n + 2: m : no. of samples. \
• Line 2n + 3 to Line 2n + 2 + m: Comma separated values observed for all variables (N1, N2, ...., Nn)
for each sample. 

**Sample Input**
2 \
yes, no \
yes, no \
0 0 \
0 0 \
8    
yes,no         \
yes,no         \
no,yes         \
no,no         \
yes,yes         \
yes,no         \
no,no         \
no,no         

## Output format
Print n lines where Line 1 will contain probability distribution of variable N1, Line 2 will contain probability distribution of variable N2 and so on.
For the above Sample Input, \
**Sample Output** \
0.2 0.8         \
0.4 0.6         \
0.2 0.4 0.3 0.5 0.8 0.6 0.7 0.5         


## Contributors
Dharamvir Ramroop Yadav (MT19CPS012) 
Subham (MT19AMD007)
