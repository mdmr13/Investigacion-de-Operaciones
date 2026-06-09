import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMinimize)

# 2. Variables
x1 = pulp.LpVariable("Estandar", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Premium", lowBound=0, cat='Integer')

# 3. Función objetivo
model += 20 * x1 + 60 * x2, "Costo_Total"

# 4. Restricciones
model += x1 + 3 * x2 >= 15, "Velocidad"
model += 2 * x1 + 2 * x2 >= 14, "Retencion"

# 5. Resolver
model.solve()

# 6. Resultados
print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Estandar: {x1.varValue}")
print(f"Premium: {x2.varValue}")
print(f"Costo_Total: ${pulp.value(model.objective)}")