# DISCLAIMER: Modellrechnung. Output ≠ Realität. Parameter sind Annahmen.
# Zweck: Prüfbarkeit der Mechanik. Keine Prognose.
# Diese Modellrechnung zeigt nur, dass die beschriebene Rückkopplungslogik
# theoretisch in eine einfache Iteration überführbar ist. Sie sagt nichts darüber aus,
# ob die Parameter realistisch sind.

# sim/endgame.py – Härtetest: 0% Wachstum, 50 Jahre
ABGABE, FLAT_TAX, JAHRE = 0.10, 0.25, 50
EINWOHNER, EINKOMMEN = 80_000_000, 30_000
fonds = 0
for j in range(JAHRE):
    abgabe = EINWOHNER * EINKOMMEN * ABGABE
    fonds += abgabe + fonds * 0.03 * (1 + FLAT_TAX)
print("STABIL" if fonds > 0 else "KOLLAPS")

# Hinweis: Diese Modellrechnung dient nur zur Illustration der Mechanik.
# Keine empirische Prognose, keine Garantie auf Realitätsnähe.

P.S.: Ich bin dafür nicht der Fachmann!
