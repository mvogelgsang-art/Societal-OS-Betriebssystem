# sim/endgame.py – Härtetest: 0% Wachstum, 50 Jahre
ABGABE, FLAT_TAX, JAHRE = 0.10, 0.25, 50
EINWOHNER, EINKOMMEN = 80_000_000, 30_000
fonds = 0
for j in range(JAHRE):
    abgabe = EINWOHNER * EINKOMMEN * ABGABE
    fonds += abgabe + fonds * 0.03 * (1 + FLAT_TAX)
print("STABIL" if fonds > 0 else "KOLLAPS")
