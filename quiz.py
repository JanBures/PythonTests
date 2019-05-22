
def say(*args):

    head = "\n======= OUTPUT {}======="
    msg = ""
    for msg in args:
        print(msg)
    print("\n")


def inccounter(start):
    step=1
    cur = start
    while True:
        yield cur
        cur += step
        if cur >=100:
            break

for i in inccounter(5):
    say(i)


nums = [5, 4, 7, 55, -13, -22, 133]
nums.sort()

print(nums)

#filter only positive nums
positives = list(filter(lambda x:x>0, nums))
say("filtered by filter funct:",positives)

#map nums to function
doubles = list(map(lambda x:x*2, nums))
print("doubled by map funct:", doubles)

# generator of nums
tripow = lambda x: x**3
say(tripow(11))
