import math

count = 0
for a in range(0, 5):
    for b in range(0, 5):
        for c in range(0, 5):
            for d in range(0, 5):
                for e in range(0, 5):
                    for f in range(0, 5):
                        for g in range(0, 5):
                            for h in range(0, 5):
                                for i in range(0, 5):
                                    for j in range(0, 5):
                                        for k in range(0, 5):
                                            for l in range(0, 5):
                                                for m in range(0, 5):
                                                    for n in range(0, 5):
                                                        for o in range(0, 5):
                                                            for p in range(0, 5):
                                                                for q in range(0, 5):
                                                                    for r in range(0, 5):
                                                                        for s in range(0, 5):
                                                                            for t in range(0, 5):
                                                                                for u in range(0, 5):
                                                                                    for v in range(0, 5):
                                                                                        four_sum = a*1 + b*4 + c*9 + d*16 + e*25 + \
                                                                                         f*36 + g*49 + h*64 + i*81 + j*100 + \
                                                                                         k*121 + l*144 + m*169 + n*169 + o*225 + \
                                                                                         p*256 + q*289 + r*324 + s*361 + t*400 + \
                                                                                         u*441 + v*484
                                                                                        if x == 528 and (a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v) == 4:
                                                                                            print(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v)
