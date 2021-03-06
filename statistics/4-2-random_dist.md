[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

**Exercise:** The numbers generated by `numpy.random.random` are supposed to be uniform between 0 and 1; that is, every value in the range should have the same probability.

Generate 1000 numbers from `numpy.random.random` and plot their PMF.  What goes wrong?

Now plot the CDF. Is the distribution uniform?

>> Solution code w/ In/Out notation below:

#Solution
​
t = np.random.random(1000)

In [29]:

#Solution
​
pmf = thinkstats2.Pmf(t)

thinkplot.Pmf(pmf, linewidth=0.1)

thinkplot.Config(xlabel='Random variate', ylabel='PMF')

In [30]:

#Solution
​
cdf = thinkstats2.Cdf(t)

thinkplot.Cdf(cdf)

thinkplot.Config(xlabel='Random variate', ylabel='CDF')


