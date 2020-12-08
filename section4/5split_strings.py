#!/usr/local/bin/python3
"""
x="python"
y="   python"
z="   python    "
print(y.strip())
print(z.strip())
m="python   "
print(m.strip()) #strip will remove spaces from either sides
"""
#stripping of words/sentences
"""
x="python"
print(x.strip('p')) #since p is the starting word, it will remove p
print(x.strip('n')) #since n is the ending word, it will remove n
print(x.strip('o')) #since o is not on the starting/ending side, it will not remove
x="python scripting is easy" 
print(x.strip('easy')) #it will remove easy
x="python scripting is easy python"
print(x.strip('python')) #it will remove python in both sides
print(x.lstrip('python')) #it will remove python in left side
print(x.rstrip('python')) #it will remove python in right side
x="python./i"
print(x.strip('./i'))
x="pythonyy"
print(x.strip('p').strip('y'))
x="pythonyy"
print(x.strip('p').lstrip('y').rstrip('y'))
"""
#splitting of words/sentences
x="python is easy"
print(x.split()) #wherever space is there it will split
x="python is easy"
print(x.split('is')) #wherever is is there it will split and remove is
x="python is easy and it is scripting"
print(x.split('is')) #is will be removed and teh ouput is ['python, easy and it, scripting]

