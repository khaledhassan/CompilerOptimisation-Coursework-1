import random
import string

fromo2 = 10
fromo3 = 6
multi = 40
o2 = ["-fthread-jumps", "-falign-functions", "-falign-jumps", "-falign-loops", "-falign-labels", "-fcaller-saves", "-fcrossjumping", "-fcse-follow-jumps", "-fcse-skip-blocks", "-fdelete-null-pointer-checks", "-fexpensive-optimizations", "-fgcse", "-fgcse-lm", "-findirect-inlining", "-foptimize-sibling-calls", "-fpeephole2", "-fregmove", "-freorder-blocks", "-freorder-functions", "-frerun-cse-after-loop", "-fsched-interblock", "-fsched-spec", "-fstrict-aliasing", "-fstrict-overflow", "-ftree-switch-conversion", "-ftree-pre", "-ftree-vrp", "-fschedule-insns2"]
o2removed =  ["-fschedule-insns"]
o3 = "-finline-functions -funswitch-loops -fpredictive-commoning -fgcse-after-reload -ftree-vectorize -fipa-cp-clone -funroll-loops".split(" ")
unrolls = ["--param max-unroll-times=2", "--param max-unroll-times=4", "--param max-unroll-times=8", "--param max-unroll-times=16", "--param max-unroll-times=32"]

for x in range(multi):
	a = random.sample(o2, fromo2)
	b = o3
	for un in unrolls:
		finaloptlist = "-O1 "
		finaloptlist+=string.join(a, " ")+" "
		finaloptlist+=string.join(b, " ")
		finaloptlist+= " " + un
		print '\"' +  finaloptlist + '\" \\'

