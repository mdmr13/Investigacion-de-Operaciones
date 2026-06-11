import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Ilustraciones", lowBound=0, upBound=30, cat='Integer')
x2 = pulp.LpVariable("Iconos", lowBound=0, upBound=50, cat='Integer')

# 3. Función Objetivo
model += 40 * x1 + 20 * x2, "Ganancia"

# 4. Restricciones
model += 2 * x1 + x2 <= 12, "T_Diseno"
model += x1 + x2 <= 9, "T_Renderizado"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Ilustraciones: {x1.varValue}")
print(f"Iconos: {x2.varValue}")
print(f"Ganancia: ${pulp.value(model.objective)}")

#source .venv/bin/activate