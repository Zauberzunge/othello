# Datenquelle: https://www.statworx.com/de/blog/einfuehrung-in-reinforcement-learning-wenn-maschinen-wie-menschen-lernen/

import numpy as np

# Anzahl der Felder
fields = 8

# Funktion
def q_learning(R, gamma, alpha, episodes):
    """ Funktion für Q-Learning """

    # Anzahl der Zeilen und Spalten der R-Matrix
    n, p = R.shape

    # Erstellung einer Q-Matrix (0-Werte)
    Q = np.zeros(shape=[n, p])

    # Loop Episoden
    for i in range(episodes):
        # Zufälliger Startpunkt der Berechnung
        state = np.random.randint(0, n, 1) # Zufallszahl zwischen 0 und 8 als eindimensionales Array, z.B. [3]

        # Iteration
        for j in range(100):
            # Mögliche Belohnung (Rewards) im aktuellen Status
            rewards = R[state]

            # Mögliche Züge der KI im aktuellen Status
            possible_moves = np.where(rewards[0] > 99)[0]

            # Zufällige Zug der KI
            # funktioniert nur, wenn in dem Array auch ein Wert > 99 vorkommt, sonst gibt es eine Exception
            # deshalb try: except:
            try:
                next_state = np.random.choice(possible_moves, 1) # zufälligen Zug als eindimensionales Array ermitteln
            except:
                pass

            # Update der Q-Values berechnen
            try:
                Q[state, next_state] = (1 - alpha) * Q[state, next_state] + alpha * (
                        R[state, next_state] + gamma * np.max(Q[next_state, :]))
            except:
                Q[state, 0] = (1 - alpha) * Q[state, 0] + alpha * (
                        R[state, 0] + gamma * np.max(Q[0, :]))

            # Abbrechen der Episode wenn Ziel erreicht
            try:
                if R[state, next_state] == 608:
                    break
            except:
                pass

    # Q-matrix zurückgeben
    return Q


# Belohnungs-Matrix in der Ausgangsstellung
# diese Matrix gilt nur dann, wenn die KI den ersten Zug macht
# -200 -> Feld ist nicht besetzt
R = np.zeros(shape=[fields, fields]) # erzeugt eine leere Matrix
# Matrix wird befüllt
R[0, :] = [-200, -200, -200, -200, -200, -200, -200, -200]
R[1, :] = [-200, -200, -200, -200, -200, -200, -200, -200]
R[2, :] = [-200, -200, -200, -200, -200, -200, -200, -200]
R[3, :] = [-200, -200, -200, -200, -200, -200, -200, -200]
R[4, :] = [-200, -200, -200, -200, -200, -200, -200, -200]
R[5, :] = [-200, -200, -200, -200, -200, -200, -200, -200]
R[6, :] = [-200, -200, -200, -200, -200, -200, -200, -200]
R[7, :] = [-200, -200, -200, -200, -200, -200, -200, -200]







