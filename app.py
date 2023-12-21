# pylint: disable = missing-module-docstring

import duckdb
import streamlit as st

import duckdb

con = duckdb.connect(database = "data/exercices_sql_tables.duckdb", read_only=False)

# ANSWER_STR = """
# SELECT * FROM beverages
# CROSS JOIN food_items
# """
#
# solution_df = duckdb.sql(ANSWER_STR).df()

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review?",
        ("cross_joins", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="Select a theme...",
    )
    st.write("You selected:", theme)

    exercice = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exercice)


st.header("enter your code")
query = st.text_area(label="votre code SQL ici", key="user_input")
# if query:
#     result = duckdb.sql(query).df()
#     st.dataframe(result)
#
#     # if len(result.columns) != len(     #comparaison du nombre de colonnes avec celui attendu
#     #    solution_df.columns
#     # ):      # replace with try result = result(solution_df.columns)
#     #    st.write("Some columns are missing depuis if")
#
#     try:
#         result = result[solution_df.columns]
#         st.dataframe(result.compare(solution_df))
#         # comparaison deux dataframes, avec la méthode compare de pandas, mais cela ne fonctionne
#         # que sur des dataframes ayant le même nombre de colonnes et dans le même ordre
#     except KeyError as e:
#         st.write("Some columns are missing depuis except keyerror")
#
#     n_line_difference = (
#         result.shape[0] - solution_df.shape[0]
#     )  # comparaison du nombre de lignes avec celui attendu
#     if n_line_difference != 0:
#         st.write(
#             f"result has a {n_line_difference} lines difference with the solution_df"
#         )
#
#
# tab2, tab3 = st.tabs(["Tables", "Solutions"])
#
# with tab2:
#     st.write("table : beverages")
#     st.dataframe(beverages)
#     st.write("table : food_items")
#     st.dataframe(food_items)
#     st.write("expected")
#     st.dataframe(solution_df)
#
# with tab3:
#     st.write(ANSWER_STR)
