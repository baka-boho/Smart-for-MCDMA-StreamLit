import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("SMART method")
def make_grid(rows,cols):
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid

def SMART(les_poids, directions, les_utilities):
    print(les_poids)
    print(les_utilities)
    n = len(les_poids)  # Number of criteria
    m = len(les_utilities)  # Number of alternatives
    poids_normaliser = [w / sum(les_poids) for w in les_poids]
    utilities_normaliser = []
    for j in range(n):
        minCj = min([les_utilities[i][j] for i in range(m)])
        maxCj = max([les_utilities[i][j] for i in range(m)])
        if directions[j] == 'max':
            column = [(les_utilities[i][j] - minCj) / (maxCj - minCj) if maxCj > minCj else 0 for i in range(m)]
        else:
            column = [( maxCj - les_utilities[i][j] ) / (maxCj - minCj) if maxCj > minCj else 0 for i in range(m)]
        utilities_normaliser.append(column)
    utilities_normaliser = list(zip(*utilities_normaliser))
    sum_ponderation = [
        sum(poids_normaliser[j] * utilities_normaliser[i][j] for j in range(n)) for i in range(m)
    ]
    return sum_ponderation, sum_ponderation.index(max(sum_ponderation)) + 1



Crits=st.number_input(label='$Crit Count$',max_value=10,min_value=3,key='CritCount')
Alts=st.number_input(label='$Alt Count$',max_value=10,min_value=3,key='AltCount')


C=[0 for j in range(Crits)]
Dir=['max' for j in range(Crits)]
U=[[0 for j in range(Crits)] for i in range(Alts)]

st.header("Input Criteria Weights") 

Crit_Grid = st.columns([1 for i in range(Crits)])

st.header("Input Alternatives Utilities") 
Alt_Grid = [st.columns([1 for i in range(Crits)]) for j in range(Alts)]
for i in range(Alts):
    print("\n")
    for j in range(Crits):
        print(i,j)
        with Alt_Grid[i][j]:
            U[i][j] = st.text_input(f'Utility $A_{{ {i+1},{j+1} }}$', key=f'U{i}{j}')

for j in range(len(Crit_Grid)):
    with Crit_Grid[j]:
        Dir[j] = st.selectbox(f'Direction for $C_{{{j+1}}}$', options=['max', 'min'], index=0, key=f'Dir{j}')
        C[j] = st.text_input(f'Weight for $C_{{{j+1}}}$', key=f'C{j}')



def compute():
    les_poids = [float(x) for x in C]
    les_utilities = [[float(x) for x in row] for row in U]
    directions = Dir

    sum_ponderation, best_alternative = SMART(les_poids,directions, les_utilities)
    sum_ponderation_with_keys = {"Alternative "+str(i+1): sum_ponderation[i] for i in range(len(sum_ponderation))}
    st.write("Les sommes pondérées avec clés sont :")
    df = pd.DataFrame.from_dict(sum_ponderation_with_keys, orient='index', columns=['Score'])
    df_style = df.style.apply(lambda x: ['background-color: lightgreen; color: black' if x.name == f'Alternative {best_alternative}' else '' for i in x], axis=1)
    st.table(df_style.set_table_styles(
        [{'selector': 'th', 'props': [('text-align', 'center')]},
         {'selector': 'td', 'props': [('text-align', 'center')]}]
    ))
    st.write("L'alternative donnée par la méthode SMART est :", best_alternative)

if st.button("Apply SMART"):
    compute()
def Example():

    les_poids = [0.4, 0.3, 0.2, 0.1]
    les_utilities = [
        [10000, 8, 7, 500],
        [12000, 9, 8, 550],
        [9500, 7, 6, 600],
        [11000, 8, 7, 480],
        [10500, 6, 8, 520],
        [11500, 8, 7, 530],
        [9000, 7, 9, 490],
        [10200, 9, 6, 570]
    ]
    directions = ['min', 'max', 'max', 'min']
    st.session_state['CritCount'] = len(les_poids)
    st.session_state['AltCount'] = len(les_utilities)
    for i in range(len(les_poids)):
        st.session_state[f'C{i}'] = str(les_poids[i])
        st.session_state[f'Dir{i}'] = directions[i]
    for j in range(len(les_poids)):
        for i in range(len(les_utilities)):
            st.session_state[f'U{i}{j}'] = str(les_utilities[i][j])

st.button("Example", on_click=Example)

# C:\Users\HP\AppData\Roaming\Python\Python313\Scripts\streamlit.exe run smart.py
