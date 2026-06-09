import pulp

# 1. Definir el problema (Maxización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Personajes", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Escenarios", lowBound=0, cat='Integer')

# 3. Función Objetivo
model += 80 * x1 + 60 * x2, "Total"

# 4. Restricciones
model += 2 * x1 + x2 <= 12, "Tiempo_GPU"
model += x1 + 2 * x2 <= 14, "VRAM"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Personajes: {x1.varValue}")
print(f"Escenarios: {x2.varValue}")
print(f"Total: ${pulp.value(model.objective)}")

#source .venv/bin/activate