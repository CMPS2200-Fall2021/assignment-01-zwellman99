

# CMPS 2200 Assignment 1

**Name: Zachary Wellman**
**Partner: Rafi Deykin**


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository.



1. **Asymptotic notation**

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not?
.  
.  True
.  
.  2^(n+1) ≤ 2^n * c
.  
.  2^(n+1)/2^n ≤ c
.  
.  As 2^(n+1) approaches infinity, so does 2^n but faster. Meaning that c is
.  greater than the algorithmic cost model.
.  
.
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  
.  False
.  
.  2^2^n ≤ 2^n * c
.  
.  2^2^n / 2^n ≤ c
.  
.  2^2^n grows faster than 2^n, making this statement false.
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  
.  False
.  
.  n^1.01 ≤ c * O(log^2n)
.  
.  1/logn * n^1.01 ≤ c * O(logn)
.  
.  As n^1.01 --> infinity, 1/logn --> 0, no value of c could ever make log(n) > n
.  
  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  
.  True
.  
.  n^1.01 ≥ c * log^2n
.  
.  n^1.01 * 1/log n ≥ c * log n
.  
.  As n^1.01 --> infinity, 1/log n --> 0, no value of c could ever make log(n) < n
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  
.  False
.  
.  √n ≤ O((log n)^3) * c
.
.  √n / (log n)^3 ≤ c
.  
.  As (log n)^3 --> infinity, √n approaches infinity and no value of c is greater
.  than infinity over infinity.
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  
.  True
.  
.  √n ≥ (log n)^3 * c
.  
.  √n / (log n)^3 ≥ c
.  
.  As (log n)^3 --> infinity, √n approaches infinity and no value of c is less
.  than infinity over infinity.
.  

  - 1g. Consider the definition of "Little o" notation:

$g(n) \in o(f(n))$ means that for **every** positive constant $c$, there exists a constant $n_0$ such that $g(n) \le c \cdot f(n)$ for all $n \ge n_0$. There is an analogous definition for "little omega" $\omega(f(n))$. The distinction between $o(f(n))$ and $O(f(n))$ is that the former requires the condition to be met for **every** $c$, not just for some $c$. For example, $10x \in o(x^2)$, but $10x^2 \notin o(x^2)$.  

.  

**Prove** that $o(g(n)) \cap \omega(g(n))$ is the empty set.  

.  o(g(n)) --> g(n) < c * f(n) = c > f(n) / g(n)
.  
.  w(f(n)) --> g(n) > c * f(n) = c < f(n) / g(n)
.  
.  This wouldn't work because for every c, this introduction wouldn't hold true.
.  
.  o(g(n)) intersects w(g(n)) = {0}
.  
.  
.  
.  
.  



2. **SPARC to Python**

Consider the following SPARC code:  
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$

  - 2a. Translate this to Python code -- fill in the `def foo` method in `main.py`  


  - 2b. What does this function do, in your own words?  

.  This function takes in a value, checks to see if it is less than or equal to
.  1. If it is, it returns the value inputed. Otherwise, the function takes in
.  the value and sums up the two previous values. An example would be 4, the
.  output would be 3 because:
.  F(3)+F(2) = F(2)+F(1)+F(1)+F(0)
.  F(2)+F(1)+F(1)+F(0) = F(1)+F(0)+1+1+0
.  F(1)+F(0)+1+1+0 = 1+0+1+1+0
.  1+0+1+1+0 = 3



3. **Parallelism and recursion**

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  

  - 3a. First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. What is the Work and Span of this implementation?  

.  Work = O(n)
.  
.  Span = O(n)
.  
.  
.  
.  
.  
.  


  - 3c. Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. What is the Work and Span of this sequential algorithm?  
.  
.  
.  
.  Work = O(n log n)
.  
.  Span = O(log n)
.  
.  
.  
.  
.  


  - 3e. Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  
.  Work = O(n log n)
.  
.  Span = O(n)
.  
.  
.  
.  
