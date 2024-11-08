import numpy as np
import matplotlib.pyplot as plt

def ln2_series(N):
    return sum((-1) ** (n + 1) / n for n in range(1, N + 1))

def rearranged_series(p, q, max_terms=100):
    positive_terms = []
    negative_terms = []
    for n in range(1, max_terms + 1):
        term = (-1) ** (n + 1) / n
        if n % 2 == 1:
            positive_terms.append(term)
        else:
            negative_terms.append(term)

    rearranged_sum = 0
    pos_index, neg_index = 0, 0
    while pos_index < len(positive_terms) or neg_index < len(negative_terms):
        for _ in range(p):
            if pos_index < len(positive_terms):
                rearranged_sum += positive_terms[pos_index]
                pos_index += 1
        for _ in range(q):
            if neg_index < len(negative_terms):
                rearranged_sum += negative_terms[neg_index]
                neg_index += 1
    return rearranged_sum

N_values = np.arange(1, 101)
original_sums = [ln2_series(N) for N in N_values]

pq_cases = [
    (15, 30),
    (30, 10),
    (100, 50)
]

rearranged_sums_cases = {}

for p, q in pq_cases:
    rearranged_sums = [rearranged_series(p=p, q=q, max_terms=N) for N in N_values]
    rearranged_sums_cases[(p, q)] = rearranged_sums

plt.figure(figsize=(12, 8))
plt.plot(N_values, original_sums, label='Original Series for ln(2)', color='blue')
for (p, q), sums in rearranged_sums_cases.items():
    plt.plot(N_values, sums, label=f'Rearranged Series (p={p}, q={q})', linestyle='--')
plt.axhline(np.log(2), color='black', linestyle=':', label='True ln(2) ≈ 0.693147')
plt.xlabel('Number of terms (N)')
plt.ylabel('Partial Sum')
plt.title('Convergence of the Series for ln(2) and Different Rearrangements')
plt.legend()
plt.grid(True)
plt.show()

ln2_true = np.log(2)
final_values = {f"Rearranged (p={p}, q={q})": rearranged_sums_cases[(p, q)][-1] for p, q in pq_cases}
original_final_sum = original_sums[-1]

print("Final Values:")
print(f"Original Series Sum: {original_final_sum}")
for label, value in final_values.items():
    print(f"{label}: {value}")
print(f"True ln(2): {ln2_true}")
