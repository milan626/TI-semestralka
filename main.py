from enum import Enum


# Definice výčtových typů
class STAV(Enum):
    VRATA_DOLE = 0
    VRATA_DOLE_A_SVETLO = 1
    VRATA_V_POHYBU_NAHORU = 2
    VRATA_V_POHYBU_DOLU = 3
    VRATA_NAHORE = 4
    VRATA_NAHORE_A_SVETLO = 5
    VRATA_ZASTAVENE_V_POHYBU_NAHORU = 6
    VRATA_ZASTAVENE_V_POHYBU_DOLU = 7


class VSTUP(Enum):
    TLACITKO = 0
    HORNI_SPINAC = 1
    DOLNI_SPINAC = 2
    SVETELNY_PAPRSEK = 3
    KONEC_ODPOCTU = 4


pocet_stavu = len(STAV)
pocet_vstupu = len(VSTUP)

# Vytvoření dvourozměrného pole přechodové tabulky
prech_tab = [[None] * pocet_vstupu for _ in range(pocet_stavu)]

# Naplnění přechodové tabulky (příkladová data, nahraďte podle potřeby)
prech_tab[STAV.VRATA_DOLE.value][VSTUP.TLACITKO.value] = STAV.VRATA_V_POHYBU_NAHORU

prech_tab[STAV.VRATA_V_POHYBU_NAHORU.value][VSTUP.HORNI_SPINAC.value] = STAV.VRATA_NAHORE_A_SVETLO
prech_tab[STAV.VRATA_V_POHYBU_NAHORU.value][VSTUP.TLACITKO.value] = STAV.VRATA_ZASTAVENE_V_POHYBU_NAHORU

prech_tab[STAV.VRATA_NAHORE_A_SVETLO.value][VSTUP.KONEC_ODPOCTU.value] = STAV.VRATA_NAHORE
prech_tab[STAV.VRATA_NAHORE_A_SVETLO.value][VSTUP.TLACITKO.value] = STAV.VRATA_V_POHYBU_DOLU

prech_tab[STAV.VRATA_NAHORE.value][VSTUP.TLACITKO.value] = STAV.VRATA_V_POHYBU_DOLU

prech_tab[STAV.VRATA_V_POHYBU_DOLU.value][VSTUP.DOLNI_SPINAC.value] = STAV.VRATA_DOLE_A_SVETLO
prech_tab[STAV.VRATA_V_POHYBU_DOLU.value][VSTUP.TLACITKO.value] = STAV.VRATA_ZASTAVENE_V_POHYBU_DOLU
prech_tab[STAV.VRATA_V_POHYBU_DOLU.value][VSTUP.SVETELNY_PAPRSEK.value] = STAV.VRATA_V_POHYBU_NAHORU

prech_tab[STAV.VRATA_DOLE_A_SVETLO.value][VSTUP.KONEC_ODPOCTU.value] = STAV.VRATA_DOLE

prech_tab[STAV.VRATA_ZASTAVENE_V_POHYBU_DOLU.value][VSTUP.TLACITKO.value] = STAV.VRATA_V_POHYBU_NAHORU
prech_tab[STAV.VRATA_ZASTAVENE_V_POHYBU_NAHORU.value][VSTUP.TLACITKO.value] = STAV.VRATA_V_POHYBU_DOLU








# prech_tab[STAV.DRUHY_STAV][VSTUP.VSTUP_1] = STAV.DRUHY_STAV
# prech_tab[STAV.DRUHY_STAV][VSTUP.VSTUP_2] = STAV.PRVNI_STAV

# Výpis přechodové tabulky pro kontrolu
for i in range(pocet_stavu):
    for j in range(pocet_vstupu):
        print(f"prech_tab[{STAV(i)}][{VSTUP(j)}] = {prech_tab[i][j]}")


# # Přechodová tabulka pro Mealyho automat
# transition_table = {
#     State.A: {Input.Zero: State.B, Input.One: State.A},
#     State.B: {Input.Zero: State.B, Input.One: State.A}
# }
#
# # Výstupní tabulka pro Mealyho automat
# output_table = {
#     State.A: {Input.Zero: 1, Input.One: 0},
#     State.B: {Input.Zero: 0, Input.One: 1}
# }

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
