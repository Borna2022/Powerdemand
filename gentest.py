import random

# تعریف متغیرها و محدوده‌ها
E_range = (90, 100)
T_range = (70, 85)
R_range = (10, 15)
energy_limit = 100
time_limit = 1440

def evaluate_solution(T1, R1, T2, R2, E1, E2):
    # محاسبه تعداد محصولات تولیدی هر تجهیز
    num_products_t1 = time_limit // (T1 + R1)
    num_products_t2 = time_limit // (T2 + R2)
    # محاسبه کل مصرف انرژی هر تجهیز
    total_energy_t1 = num_products_t1 * E1
    total_energy_t2 = num_products_t2 * E2
    # بررسی محدودیت مصرف انرژی
    if total_energy_t1 + total_energy_t2 <= energy_limit:
        return num_products_t1, num_products_t2, total_energy_t1 + total_energy_t2
    return 0, 0, total_energy_t1 + total_energy_t2

def genetic_algorithm():
    population_size = 50
    generations = 100
    mutation_rate = 0.1
    population = [(random.uniform(*T_range), random.uniform(*R_range), random.uniform(*T_range), random.uniform(*R_range), random.uniform(*E_range), random.uniform(*E_range)) for _ in range(population_size)]

    for _ in range(generations):
        evaluated_population = [(ind, evaluate_solution(*ind)) for ind in population]
        evaluated_population = sorted(evaluated_population, key=lambda x: sum(x[1][:2]), reverse=True)
        next_generation = [ind for ind, _ in evaluated_population[:10]]

        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(next_generation[:10], 2)
            crossover_point = random.randint(1, 5)
            child = parent1[:crossover_point] + parent2[crossover_point:]
            if random.random() < mutation_rate:  # جهش
                child = (random.uniform(*T_range), random.uniform(*R_range), random.uniform(*T_range), random.uniform(*R_range), random.uniform(*E_range), random.uniform(*E_range))
            next_generation.append(child)

        population = next_generation

    best_solution = max(evaluated_population, key=lambda x: sum(x[1][:2]))
    return best_solution[0], best_solution[1]

best_individual, (num_products_t1, num_products_t2, total_energy) = genetic_algorithm()
print("Best solution (T1, R1, T2, R2, E1, E2):", best_individual)
print("Number of products produced by T1:", num_products_t1)
print("Number of products produced by T2:", num_products_t2)
print("Total energy consumed:", total_energy)
