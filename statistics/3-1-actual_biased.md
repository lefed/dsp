[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

**Exercise:** Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample.

Use the NSFG respondent variable `numkdhh` to construct the actual distribution for the number of children under 18 in the respondents' households.

Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household.

Plot the actual and biased distributions, and compute their means.

>>Answer with ipython In/Out syntax below


resp = nsfg.ReadFemResp()

resp = nsfg.ReadFemResp()

In [37]:

#Solution
​
pmf = thinkstats2.Pmf(resp.numkdhh, label='numkdhh')

In [38]:

#Solution
​
thinkplot.Pmf(pmf)

thinkplot.Config(xlabel='Number of children', ylabel='PMF')

In [39]:

#Solution
​
biased = BiasPmf(pmf, label='biased')

In [40]:

#Solution
​
thinkplot.PrePlot(2)

thinkplot.Pmfs([pmf, biased])

thinkplot.Config(xlabel='Number of children', ylabel='PMF')

In [41]:

#Solution
​
pmf.Mean()

Out[41]:

1.0242051550438309

In [42]:

#Solution
​
biased.Mean()

Out[42]:

2.4036791006642821
