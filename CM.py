import streamlit as st
import pandas as pd 

st.write(''' 
# Convertisseur d'unité pour Mathilde
Cette application convertit les Litres pour ma copine qui n'aime pas les conversions ''')

def conv(option, v, option_2):
    
    p_l = {'yottalitre': 24, 'zettalitre': 21, 'exalitre': 18, 'pétalitre': 15, 'téralitre': 12, 'gigalitre': 9,
           'mégalitre': 6, 'kilolitre': 3, 'hectolitre': 2, 'décalitre': 1, 'litre': 0, 'décilitre': -1, 'centilitre': -2,
           'millilitre': -3, 'microlitre': -6, 'nanolitre': -9, 'picolitre': -12, 'femtolitre': -15, 'attolitre': -18,
           'zeptolitre': -21, 'yoctolitre': -24}

    p_c = {'yottalitre': -24, 'zettalitre': -21, 'exalitre': -18, 'pétalitre': -15, 'téralitre': -12, 'gigalitre': -9,
           'mégalitre': -6, 'kilolitre': -3, 'hectolitre': -2, 'décalitre': -1, 'litre': 0, 'décilitre': 1, 'centilitre': 2,
           'millilitre': 3, 'microlitre': 6, 'nanolitre': 9, 'picolitre': 12, 'femtolitre': 15, 'attolitre': 18,
           'zeptolitre': 21, 'yoctolitre': 24}

    for key, i in p_l.items():
        if option == key:
            l = v * 10 ** i
    
    for key, i in p_c.items():
        if option_2 == key:
            r = l * 10 ** i
    
    return r



option = st.selectbox(
    "Quelle est votre unité de départ ?",
    ('yottalitre','zettalitre','exalitre','pétalitre','téralitre','	gigalitre',
     'mégalitre','kilolitre','hectolitre','décalitre','litre','décilitre','centilitre',
     'millilitre','microlitre','nanolitre','picolitre','femtolitre','attolitre','zeptolitre','yoctolitre'))


v = st.number_input('Insérer un nombre')
if v >= 2:
    st.write(f'La valeur est {v} {option}s ')

else:
    st.write(f'La valeur est {v} {option} ')


option_2 = st.selectbox(
        "Convertir en quelle unité ? ",
        ('yottalitre', 'zettalitre', 'exalitre', 'pétalitre', 'téralitre', 'gigalitre',
         'mégalitre', 'kilolitre', 'hectolitre', 'décalitre', 'litre', 'décilitre', 'centilitre',
         'millilitre', 'microlitre', 'nanolitre', 'picolitre', 'femtolitre', 'attolitre', 'zeptolitre', 'yoctolitre'))

resultat = conv(option, v,option_2)


if st.button("Convertir"):
    if  resultat < 2 and v >= 2:
        st.write(f"{v} {option}s équivaut à {resultat} {option_2}")

    elif v < 2 and resultat >= 2: 
        st.write(f"{v} {option} équivaut à {resultat} {option_2}s")

    elif resultat < 2 and v < 2 : 
        st.write(f"{v} {option} équivaut à {resultat} {option_2}")

    else:
        st.write(f"{v} {option}s équivaut à {resultat} {option_2}s")




