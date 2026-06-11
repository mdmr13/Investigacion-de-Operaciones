import pulp

# 1. Definir el problema (Maximización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Servidor_Basico", lowBound=0, upBound=30, cat='Integer')
x2 = pulp.LpVariable("Servidor_Avanzado", lowBound=0, upBound=50, cat='Integer')

# 3. Función Objetivo
model += 30 * x1 + 50 * x2, "Ganancia_Total"

# 4. Restricciones
model += x1 + 2 * x2 <= 16, "RAM_Demand"
model += 3 * x1 + 2 * x2 <= 24, "Procesador_Demand"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Contratar Servidor_Basico: {x1.varValue}")
print(f"Contratar Servidor_Avanzado: {x2.varValue}")
print(f"Ganancia_Total: ${pulp.value(model.objective)}")

#source .venv/bin/activate