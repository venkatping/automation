#!/usr/local/bin/python3
x="python"
#i need output in this way p-y-t-h-o-n
y="-".join(x)
print(y)
z="\n".join(x)
print(z)
m="\t".join(x)
print(m)
my_str="python"
my_str2="scripting"
my_str3="Tutorials"
print(my_str.center(20))
print(f"{my_str.center(20)}\n{my_str2.center(20)}\n{my_str3.center(20)}")

#zfill means zero fill, it will fill spaces with 0, now iam taking 10 and python word consists of 6 letters and remaining letters will be fill-up with 0
print(my_str.zfill(10))
