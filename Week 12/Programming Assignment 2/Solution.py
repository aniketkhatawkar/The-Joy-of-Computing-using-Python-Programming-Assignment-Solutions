def state_after_iterations(n):
    happy = n
    sad = 0
    
    for _ in range(3):
        new_happy = 0.3 * happy + 0.5 * sad
        new_sad = 0.7 * happy + 0.5 * sad
        happy = new_happy
        sad = new_sad
    
    return int(round(happy)), int(round(sad))

n = int(input())

happy_count, sad_count = state_after_iterations(n)
print(happy_count, sad_count, end="")
