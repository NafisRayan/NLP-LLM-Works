import random

def create_chromosome(n, t):
    """Creates a random chromosome representing the schedule."""
    return ''.join(random.choice('01') for _ in range(n * t))

def fitness_function(chromosome, n, t):
    """Calculates the fitness of a given chromosome based on overlap and consistency penalties."""
    overlap_penalty = 0
    consistency_penalty = 0

    courses = []
    i = 0
    while i < len(chromosome):
        courses.append(chromosome[i:i + n])
        i += n

    # Overlap penalty calculation
    for timeslot in courses:
        num_courses = sum(int(part) for part in timeslot)
        if num_courses > 1:
            overlap_penalty += num_courses - 1

    # Consistency penalty calculation
    for i in range(n):
        course_schedule_parts = [courses[j][i] for j in range(t)]
        num_scheduled_times = sum(int(part) for part in course_schedule_parts)
        if num_scheduled_times != 1:
            consistency_penalty += abs(num_scheduled_times - 1)

    return - (overlap_penalty + consistency_penalty)

def choose_parents(population_schedules, fitness_scores):
    """Selects two parents based on their fitness scores."""
    total_fitness = sum(fitness_scores)
    selection_probabilities = [fitness / total_fitness for fitness in fitness_scores]
    parents = random.choices(population_schedules, weights=selection_probabilities, k=2)
    return parents

def run_crossover(parentOne, parentTwo, n, t):
    """Performs single-point crossover between two parents."""
    crossover_index = random.randint(1, len(parentOne) - 1)
    child1 = parentOne[:crossover_index] + parentTwo[crossover_index:]
    child2 = parentTwo[:crossover_index] + parentOne[crossover_index:]
    return child1, child2

def run_mutate(chromosome, mutationRate):
    """Applies mutation to a chromosome based on the mutation rate."""
    mutatedChromosome = ''
    for part in chromosome:
        if random.random() < mutationRate:
            mutatedChromosome += '1' if part == '0' else '0'
        else:
            mutatedChromosome += part
    return mutatedChromosome

def run_genetic_algorithm(n, t, population_len, max_iterations, mutationRate):
    """Runs the genetic algorithm to find the best chromosome."""
    population_value = [create_chromosome(n, t) for _ in range(population_len)]

    for _ in range(max_iterations):
        fitness_scores = [fitness_function(chromosome, n, t) for chromosome in population_value]
        max_fitness = max(fitness_scores)
        if max_fitness == 0:
            break

        new_population_schedules = []
        for _ in range(population_len // 2):
            parents = choose_parents(population_value, fitness_scores)
            child1, child2 = run_crossover(parents[0], parents[1], n, t)
            mutated_child1 = run_mutate(child1, mutationRate)
            mutated_child2 = run_mutate(child2, mutationRate)
            new_population_schedules.extend([mutated_child1, mutated_child2])

        population_value = new_population_schedules

    best_chromosome = max(population_value, key=lambda x: fitness_function(x, n, t))
    return best_chromosome, fitness_function(best_chromosome, n, t)

def twoPoint_crossover(parentOne, parentTwo):
    """Performs a two-point crossover between two parents."""
    idx = sorted(random.sample(range(1, len(parentOne)), 2))
    child1 = parentOne[:idx[0]] + parentTwo[idx[0]:idx[1]] + parentOne[idx[1]:]
    child2 = parentTwo[:idx[0]] + parentOne[idx[0]:idx[1]] + parentTwo[idx[1]:]
    return child1, child2

# Input and execution for the genetic algorithm
n, t = map(int, input("Enter number of courses and timeslots: ").split())
courses = [input("Enter course details: ") for _ in range(n)]

best_chromosome, fitness_value = run_genetic_algorithm(n, t, 100, 100, 0.01)

print("Best Chromosome from Genetic Algorithm:", best_chromosome)
print("Best Fitness from Genetic Algorithm:", fitness_value)

# Input and execution for the two-point crossover
print("\nTwo-Point Crossover Example:")
n = 3
t = 3
population_schedules = [create_chromosome(n, t) for _ in range(10)]

parents = choose_parents(population_schedules, 2)

child1, child2 = twoPoint_crossover(parents[0], parents[1])

print("Parent 1:", parents[0])
print("Parent 2:", parents[1])
print("Offspring 1:", child1)
print("Offspring 2:", child2)
