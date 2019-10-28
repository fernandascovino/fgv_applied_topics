# Complex networks
---

## Class contents

### Spectral theory

##### Adjacency matrix ($A$)


##### Incidence matrix ($B$)

##### Laplacian matrix
It's defined as: 
$$L = D - A$$

Where D is the degree matrix.
### Random networks

#### Erdos-Rényl model

Choose a probability $p$ and a number of nodes $N$, where $p$ gives the connection probability between any two nodes.

Derived from that, we have the average links of the network as $\langle k \rangle  = (N-1)p$. 

What's the number of edges? $\sum k = 2L \rightarrow L = \frac{\langle k \rangle N}{2} = \frac{(N-1)N}{2}p$. The number of edges of a node follows a binomial distribution with maximum number of edges (total of choises) as $\frac{(N-1)N}{2}$ and probability $p = \frac{\langle k \rangle }{N-1}$.

$$k_{N} = Bin(N, \frac{\langle k_{N} \rangle }{N-1})$$

Usually, with a large N (our is $\frac{(N-1)N}{2}$), we can approximate binomial distribution as Gaussin or a Poisson. In our case, examining the mean $\langle k_{N} \rangle $ and variance $Var(k_{N})$ of the distribuition, we can see that, as it grows, $ \langle k_{N} \rangle  \approx Var(k_{N}) \approx \langle k_{N} \rangle $

- What is the maximum degree we should observate in a random graph? 

We can think of that as what is $k(max)$ such that the probability of $k < k_{max}$ is less than $\frac{1}{N}$, i.e., the probability of all the nodes degreee being less than $k_{max}$ is greater than one being greater than $k_max$. 

$$N[1 - P(k_{max})] \approx 1 \rightarrow P(k_{max}) \approx \frac{1}{N}$$ Therefore, random networks usually don't have outliers.

#### Cluster size distribution

- What's the minimum of links we should have to generate a connected component?

Connected components appears once we have enough links so that exists subgraphs in our network. The critical point is when $\langle k\rangle = 1$. Derived from that, we have 4 cases: subcritical, critical, supercritical and connected ($\langle k\rangle > ln(N)$)

#### Distance in random graphs

- Milgram's small worlds and Karinthy's six degrees of separation

> What does short (or small) mean, i.e. short compared to what? How do we explain the existence of these short distances?

- Maximum distance:

Given a network with average degree $\langle k_{N} \rangle$, we can think that a node have on average $\langle k \rangle$ nodes at distance one ($d=1$), $\langle k \rangle^2$ nodes at distance one ($d=2$), and so on.
$$ d_{max} = \frac{log(N)}{log \langle k_{N} \rangle}$$

### Finite scale-free networks
(i. e. *Law power networks*)

#### Power law distribution
- It's possible to find extreme values more often: we have a "heavy" tail. We have:

$$ p_k ∼ k^{−γ} $$

Where $γ$ is the degree exponent. We can separate the equation with $p_{in}$ and $p_{out}$ distributions also, each one with its on $γ$.
$$ p(k) = C e^{−λk} $$

#### Hubs

- What is the maximum degree we should observate in such networks?

In general: "ther larger a network, the larger is the degree of aits biggest hub".

$$k_{max} = k_{min} N^{\frac{1}{γ−1}}$$


#### Scale-free property

- Why "scale-free"? As the network growns, it's patterns remains the same: the caracteristcs of the network are scale-free.

#### Ultra-small property
- Comparing to random networks, which have a "tree-like" topology i.e. nodes degrees are almost the same, 

- When we have $γ$ = 2, it means in general that all nodes will be connect with one hub, therefore the distance between them has no relation to the size of the network.

$$k_{max} \approx N$$

- When we have $2 < γ < 3$, "the average distance increases as $ln(ln(N))$, a significantly slower growth than the $ln(N)$ derived for random networks. We call networks in this regime ultra-small, as the hubs radically reduce the path length." This is the ultra-small network.

#### Notes reference:

(1) ["Network Science by Albert-László Barabási*](http://networksciencebook.com/)