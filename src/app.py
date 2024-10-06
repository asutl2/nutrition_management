import pandas as pd
import streamlit as st

# CSVファイルの読み込み
df = pd.read_csv("dataset/foodstruct_nutritional_facts.csv")

# Streamlitのアプリケーションタイトル
st.title("Food Nutritional Facts")

# サイドバーにフィルターを追加
st.sidebar.header("Filter Options")
# selected_columns = st.sidebar.multiselect(
#     "Select columns to display", options=df.columns.tolist(), default=df.columns.tolist()
# )

# # サイドバーに検索機能を追加
# search_query = st.sidebar.text_input("Search by food name")

# # データのフィルタリング
# if search_query:
#     df_filtered = df[df['food_name'].str.contains(search_query, case=False, na=False)]
# else:
#     df_filtered = df

# # フィルタリングされたカラムだけを表示
# df_filtered = df_filtered[selected_columns]

# # データの表示
# st.dataframe(df_filtered)

# # データのサマリー情報を追加
# st.write("### Nutritional Facts Summary")
# st.write(df_filtered.describe())
