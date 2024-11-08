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
    i = 0
    while i < len(positive_terms) or i < len(negative_terms):
        for j in range(p):
            if i < len(positive_terms):
                rearranged_sum += positive_terms[i]
                i += 1
        for j in range(q):
            if i < len(negative_terms):
                rearranged_sum += negative_terms[i]
                i += 1
    return rearranged_sum


N_values = np.arange(1, 101)
original_sums = [ln2_series(N) for N in N_values]

rearranged_sums = [rearranged_series(p=5, q=5, max_terms=N) for N in N_values]

plt.figure(figsize=(10, 6))
plt.plot(N_values, original_sums, label='Original Series for ln(2)', color='blue')
plt.plot(N_values, rearranged_sums, label='Rearranged Series (p=5, q=5)', color='red', linestyle='--')
plt.axhline(np.log(2), color='black', linestyle=':', label='True ln(2) ≈ 0.693147')
plt.xlabel('Number of terms (N)')
plt.ylabel('Partial Sum')
plt.title('Convergence of the Series for ln(2) and its Rearrangement')
plt.legend()
plt.grid(True)
plt.show()

ln2_true = np.log(2)
original_sums[-1], rearranged_sums[-1], ln2_true
