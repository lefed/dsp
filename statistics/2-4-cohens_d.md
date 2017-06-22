[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

**Exercise 2.4:**

_Using the variable 'totalwgt_lb', investigate whether first babies
are lighter or heavier than others. Compute Cohen’s d to quantify the
difference between the groups. How does it compare to the difference in
pregnancy length?_

>> Place Answer Below:


​In[30]:

#Solution

firsts.totalwgt_lb.mean(), others.totalwgt_lb.mean()

Out[30]:

(7.201094430437772, 7.325855614973262)

In [31]:

#Solution

​CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)

Out[31]:

-0.088672927072602006
