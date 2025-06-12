a='{0} institute, rajkot, INDIA'
aa=a.format('hardik')
print(aa)

b='{0} institute, {1}, {2}'
bb=b.format('hardik', 'rajkot', 'INDIA')
print(bb)

c='{0} institute, {1}, {2}, welcome to {0}'
cc=c.format('hardik', 'rajkot', 'INDIA')
print(cc)

d='{{{0}}} institute'
dd=d.format('hardik')
print(dd)

e='the price for {0} is {1}'
ee=e.format('redmi', '12000')
print(ee)

f='{0:25} institute, of engineering'
print(f.format('dharmik'))

g='{0:>25} institute, of engineering'
print(g.format('dharmik'))

h='{0:^25} institute, of engineering'
print(h.format('dharmik'))

i='{0:-^25} institute, of engineering'
print(i.format('dharmik'))

j='{0:.3} institute, of engineering'
print(j.format('dharmik'))

k='amount = {0}'
print(k.format(123456))

l='amount = {0:0=10}'
print(l.format(123456))

m='amount = {0:010}'
print(m.format(123456))

n='amount = {0: }'
print(n.format(123456))

l='amount = {0:0=10}'
print(l.format(123456))












