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

class VYSTUP(Enum):
    MOTOR_NAHORU = "Motor spuštěn a vrata jedou nahoru. "
    MOTOR_STOP = "Motor zastaven a vrata stojí. "
    MOTOR_DOLU = "Motor spuštěn a vrata jedou dolu. "
    CASOVAC_START = "Časovač pro světla spuštěn. "
    CASOVAC_STOP = "Časovač pro světla zastaven. "
    ROZSVIT = "Světla rozsvícena. "
    ZHASNI = "Světla zhasnuta. "

def Inic_tab():
    global prech_tab
    global vyst_tab

    pocet_stavu = len(STAV)
    pocet_vstupu = len(VSTUP)

    # Vytvoření dvourozměrného pole přechodové tabulky
    prech_tab = [[None] * pocet_vstupu for _ in range(pocet_stavu)]
    vyst_tab = [[None] * pocet_vstupu for _ in range(pocet_stavu)]

    # Přechodové tabulka
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
    prech_tab[STAV.VRATA_DOLE_A_SVETLO.value][VSTUP.TLACITKO.value] = STAV.VRATA_V_POHYBU_NAHORU

    prech_tab[STAV.VRATA_ZASTAVENE_V_POHYBU_DOLU.value][VSTUP.TLACITKO.value] = STAV.VRATA_V_POHYBU_NAHORU
    prech_tab[STAV.VRATA_ZASTAVENE_V_POHYBU_NAHORU.value][VSTUP.TLACITKO.value] = STAV.VRATA_V_POHYBU_DOLU



    # Vystupní tabulka
    vyst_tab[STAV.VRATA_DOLE.value][VSTUP.TLACITKO.value] = (VYSTUP.MOTOR_NAHORU.value + VYSTUP.ROZSVIT.value)

    vyst_tab[STAV.VRATA_V_POHYBU_NAHORU.value][VSTUP.HORNI_SPINAC.value] = (VYSTUP.MOTOR_STOP.value + VYSTUP.CASOVAC_START.value)
    vyst_tab[STAV.VRATA_V_POHYBU_NAHORU.value][VSTUP.TLACITKO.value] = (VYSTUP.MOTOR_STOP.value)

    vyst_tab[STAV.VRATA_NAHORE_A_SVETLO.value][VSTUP.KONEC_ODPOCTU.value] = (VYSTUP.ZHASNI.value)
    vyst_tab[STAV.VRATA_NAHORE_A_SVETLO.value][VSTUP.TLACITKO.value] = (VYSTUP.MOTOR_DOLU.value + VYSTUP.CASOVAC_STOP.value)

    vyst_tab[STAV.VRATA_NAHORE.value][VSTUP.TLACITKO.value] = (VYSTUP.MOTOR_DOLU.value + VYSTUP.ROZSVIT.value)

    vyst_tab[STAV.VRATA_V_POHYBU_DOLU.value][VSTUP.DOLNI_SPINAC.value] = (VYSTUP.MOTOR_STOP.value + VYSTUP.CASOVAC_START.value)
    vyst_tab[STAV.VRATA_V_POHYBU_DOLU.value][VSTUP.TLACITKO.value] = (VYSTUP.MOTOR_STOP.value)
    vyst_tab[STAV.VRATA_V_POHYBU_DOLU.value][VSTUP.SVETELNY_PAPRSEK.value] = (VYSTUP.MOTOR_NAHORU.value)

    vyst_tab[STAV.VRATA_DOLE_A_SVETLO.value][VSTUP.KONEC_ODPOCTU.value] = (VYSTUP.ZHASNI.value)
    vyst_tab[STAV.VRATA_DOLE_A_SVETLO.value][VSTUP.TLACITKO.value] = (VYSTUP.MOTOR_NAHORU.value + VYSTUP.CASOVAC_STOP.value)

    vyst_tab[STAV.VRATA_ZASTAVENE_V_POHYBU_DOLU.value][VSTUP.TLACITKO.value] = (VYSTUP.MOTOR_NAHORU.value)
    vyst_tab[STAV.VRATA_ZASTAVENE_V_POHYBU_NAHORU.value][VSTUP.TLACITKO.value] = (VYSTUP.MOTOR_DOLU.value)

def Inic_stav():
    global stav
    stav = STAV.VRATA_DOLE

    print("Aktuální stav: ", end='')
    print(stav)

def Vstup_znaku():
    global vstup

    # slovník s číselníkem
    ciselnik_vstupu = {index: vstup_type for index, vstup_type in enumerate(VSTUP)}
    pocet_vstupu = len(ciselnik_vstupu)
    ciselnik_vstupu[pocet_vstupu] = "Ukončit program."

    for index, vstup_type in ciselnik_vstupu.items():
        print(f"{index} = {vstup_type}")

    vybrany_index = int(input("Vyberte vstup: "))

    if vybrany_index == pocet_vstupu:
        exit()

    vstup = ciselnik_vstupu.get(vybrany_index)

def Transf_akce():
    global stav
    stav = prech_tab[stav.value][vstup.value]
    print("Nový stav: ", end='')
    print(stav)
    print()


def Vyst_akce():
    print("▄▄▄▄▄▄▄")
    print("" + vyst_tab[stav.value][vstup.value])
    print("▀▀▀▀▀▀▀")

def main():
    Inic_stav()
    Inic_tab()
    while True:
        Vstup_znaku()
        Vyst_akce()
        Transf_akce()


# prech_tab[STAV.DRUHY_STAV][VSTUP.VSTUP_1] = STAV.DRUHY_STAV
# prech_tab[STAV.DRUHY_STAV][VSTUP.VSTUP_2] = STAV.PRVNI_STAV

# # Výpis přechodové tabulky pro kontrolu
# for i in range(pocet_stavu):
#     for j in range(pocet_vstupu):
#         print(f"prech_tab[{STAV(i)}][{VSTUP(j)}] = {prech_tab[i][j]}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
