#!/usr/bin/env python


colors = "black blue brown cyan green grey magenta orange pink purple red violet white yellow"
colors = colors.split()


for name in colors:
    lines = open(name + '.raw').readlines()
    half = int(len(lines) / 2)
    print(name, half)
    assert((half * 2) == len(lines))    

for name in colors:
    lines = open(name + '.raw').readlines()
    half = int(len(lines) / 2)

    names = lines[0:half]
    values = lines[half:]
    names = [v.strip() for v in names]
    values = [v.strip() for v in values]
    pairs = list(zip(names, values))
    output = open(name + '.csv', 'w')
    for p in pairs:
        output.write(p[0] + ',' + p[1] + '\n')
    output.flush()
    output.close()

