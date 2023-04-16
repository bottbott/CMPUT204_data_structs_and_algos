
## Recurrence Relations
# Merge Sort
'''math
\begin{equation}
  T(n) =
    \begin{cases}
      c & \text{if n = 1}\\
      2T(\frac{n}{2})+cn & \text{if n >= 2}\\
    \end{cases}       
\end{equation}
'''

# Quick Sort
'''math
\begin{equation}
  T(n) =
    \begin{cases}
      0 & \text{if n <= 1}\\
      T(n_1)+cn + T(n-1-n_1) +(n-1) & \text{if n >= 2}\\
    \end{cases}       
\end{equation}
'''

# Karatsuba's Algorithm - Large Integer Multiplication
'''math
T(n) = 3T(\frac{n}{2}) + O(n)
'''

# Strassen's Algorithm
'''math
T(n) = 7T(\frac{n}{2}+O(n^2))
'''

# Fractional Knapsack
'''math
\begin{align}
  &OPT(W,<w_1,b_1>,...,<w_n,b_n>) = \\
  &max_j(\frac{b_j}{w_j}x_j + ) \\
  &OPT(W-x_j,<w_1,b_1>,...,<w_{j-1},b{j-1}>,<w_{j+1},b{j+1}>,...,<w_n,b_n>))
\end{align}
'''

# Integral Knapsack
'''math
\begin{align}
  &OPT(W;w_1,...,w_n;v_1,...,v_n) = \\ &max(OPT(W;w_1,...,w_(n-1); v_1,...,v_(n-1)), \\ &(if W >= w_n) v_n + OPT(W-w_n,w_1,...,w_(n-1); v_1,...,v_(n-1)))
\end{align}
'''

# Rod Cutting
'''math
r_n=\underset{i\in\{1,2,...,n\}}{max} (p_i+r_{n-i})
'''

# Longest Common Subsequence
'''math
\begin{align}
  LCS(x_1...x_n, y_1...y_n) &= \\
  max(&LCS(x_1...x_{n-1},y_1...y_{m})), \\
  &LCS(x_1...x_n,y_1...y_{m-1}), \\
  &(if x_n=y_m) 1 + LCS(x_1...x_{n-1}, y_1...y_{m-1})
  \end{align}
'''

# Matrix Chain Multiplication
R(i,j) = \underset{i \leq k \leq j}{min} (R(i,k) + R(k+1,j)+d_{i-1}d_k d_j)

# Bellman Ford
'''math
d^{i+1}[v] = min(d^{(i)}[v], \underset{\forall \;Nbrs\;u\;of\;v}{min} (d^{(i)}[u] + w(u,v)))
'''