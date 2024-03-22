def max_guests_at_any_instance(T, E, L):
    max_guests = 0
    current_guests = 0

    for i in range(T):
        current_guests += E[i]  
        current_guests -= L[i]  
        max_guests = max(max_guests, current_guests)

    return max_guests

T = -4
E = [1, 5, 9, 10]
L = [0, 2, 3, 4]

print(max_guests_at_any_instance(T, E, L))  
