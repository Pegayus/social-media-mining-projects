#Zachary's Karate Club Clustering
Download the adjacency matrix for Zachary's Karate Club from [here](http://networkdata.ics.uci.edu/data/karate/). You can read more about this dataset's problem in [here](http://dmml.asu.edu/smm/SMM.pdf), page 177. The correct community assignments are available in Table 1 (column: club after fission) in [the original paper](http://aris.ss.uci.edu/~lin/76.pdf). Both spectral clustering and modularity maximization methods are performed for k = 2. For modularity maximization, I have used [this](https://people.orie.cornell.edu/yudong.chen/cmm/) useful library in Matlab.

Output for both approaches:
1. Two communities
2. F-measure.
