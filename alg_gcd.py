"""
gcd
"""

def gcd(a:int,b:int):
    assert a!=0 or b!=0,"Not defined"
    if 0==a:
        return b
    elif 0==b:
        return a
    if a<b:
        return gcd(b,a)
    r = a % b
    while r !=0:
        return gcd(b,r)
    return b

# print(gcd(0,0))
# GPT,当b不等于0的时候，就一直进行迭代，卧槽，真几把帅！
# 这里利用了while 所接的布尔表达式是一个真的时候一直执行循环
# 满足条件的时候，持续执行长除法，直到b为0返回a的值，对应就是r=0，返回r_{0}的值
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
