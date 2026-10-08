import sympy as sp

# Definisci il simbolo x specificando che è reale
x = sp.Symbol('x', real=True)

equazione = sp.Eq(x**3, sp.exp(x))

# Risolvi l'equazione per x
soluzioni = sp.solve(equazione, x)

print("Soluzione nell'intervallo principale:", soluzioni)
