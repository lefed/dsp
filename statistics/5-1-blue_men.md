[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

**Exercise:** In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.

In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use `scipy.stats.norm.cdf`.

>> Answer solution code below with In/Out Notation based on ipython notebook:

scipy.stats contains objects that represent analytic distributions

In [27]:

import scipy.stats

_For example scipy.stats.norm represents a normal distribution._

In [28]:

mu = 178

sigma = 7.7

dist = scipy.stats.norm(loc=mu, scale=sigma)

type(dist)

Out[28]:

scipy.stats._distn_infrastructure.rv_frozen

_A "frozen random variable" can compute its mean and standard deviation._

In [29]:

dist.mean(), dist.std()

Out[29]:

(178.0, 7.7000000000000002)

_It can also evaluate its CDF. How many people are more than one standard deviation below the mean? About 16%_

In [30]:

dist.cdf(mu-sigma)

Out[30]:

0.15865525393145741

_How many people are between 5'10" and 6'1"?_

In [31]:

#Solution
​
low = dist.cdf(177.8)    # 5'10"

high = dist.cdf(185.4)   # 6'1"

low, high, high-low

Out[31]:

(0.48963902786483265, 0.83173371081078573, 0.34209468294595308)

