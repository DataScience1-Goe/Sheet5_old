import matplotlib.pyplot as plt

def assignment(new_list, i, old_list, j):
    new_list[i] = old_list[j]
    return

def merge_sort(list_to_sort):
    # teste of list_to_sort mindestens 2 Einträge hat (sonst ist sie schon sortiert)
    if len(list_to_sort) > 1: 
	# splitte die Liste in linken Teil und rechten Teil
        mid = len(list_to_sort) // 2
        left = list_to_sort[:mid]
        right = list_to_sort[mid:]

	# Rekursiver Aufruf der Funktion um zunächst left und right sortiert zu haben
        merge_sort(left)
        merge_sort(right)

        l = 0; r = 0; i = 0

	# Iteration durch left und right
        while l < len(left) and r < len(right):
            # Schreibe immer den kleineren Wert von left und right in das ganze Array
            if left[l] <= right[r]:
                assignment(new_list=list_to_sort, i=i, old_list=left, j=l)
                l += 1
            else:
                assignment(new_list=list_to_sort, i=i, old_list=right, j=r)
                r += 1
            i += 1

	# Schreibe restliche Werte des linken Arrays in ganze Array
        while l < len(left):
            list_to_sort[i] = left[l]
            l += 1
            i += 1

	# Schreibe restliche Werte des rechten Arrays in ganze Array
        while r < len(right):
            list_to_sort[i] = right[r]
            r += 1
            i += 1
    return


# Plotte List ohne Sortieren
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()

# Plotte Liste mit Sortieren
merge_sort(my_list)
plt.plot(x, my_list)
plt.show()
