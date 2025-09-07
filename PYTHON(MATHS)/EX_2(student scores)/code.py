scores = list(map(int, input("Enter scores separated by space: ").split()))

n = len(scores)

total = 0
for score in scores:
    total += score
mean = total / n

for i in range(n):
    for j in range(0, n - i - 1):
        if scores[j] > scores[j + 1]:
            scores[j], scores[j + 1] = scores[j + 1], scores[j]

if n % 2 == 0:
    median = (scores[n // 2 - 1] + scores[n // 2]) / 2
else:
    median = scores[n // 2]

maximum = scores[0]
minimum = scores[0]
for score in scores:
    if score > maximum:
        maximum = score
    if score < minimum:
        minimum = score

sum_sq_diff = 0
for score in scores:
    sum_sq_diff += (score - mean) ** 2
variance = sum_sq_diff / n
std_dev = variance ** 0.5

def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

grades = [assign_grade(score) for score in scores]

print("\n--- Statistical Results ---")
print(f"Mean: {mean:.2f}")
print(f"Median: {median}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
print(f"Standard Deviation: {std_dev:.2f}")

print("\n--- Grade Classification ---")
for i in range(n):
    print(f"Student {i+1}: Score = {scores[i]}, Grade = {grades[i]}")
