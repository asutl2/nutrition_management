import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# CSVファイルの読み込み
df = pd.read_csv("dataset/foodstruct_nutritional_facts.csv")

# Streamlitのアプリケーションタイトル
st.title("Food Nutritional Facts")

# サイドバーにナビゲーションバーを追加
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["ホーム", "何食べた？"])

# ナビゲーションに応じたコンテンツの表示
if page == "ホーム":
    st.write("### ホームページへようこそ")
    st.write(
        "ここでは食品の栄養データにアクセスできます。サイドバーからオプションを選んでください。"
    )

elif page == "何食べた？":
    st.write("### 何食べた？ページ")
    st.write("ここでは最近食べた食品の栄養情報を表示します。")

    # 1. カテゴリー名を選択
    categories = df["Category Name"].unique()
    selected_category = st.selectbox("What type of food did you eat?", categories)

    # 2. 選択したカテゴリーに属する食べ物を選択
    filtered_foods = df[df["Category Name"] == selected_category]["Food Name"].unique()
    selected_foods = st.multiselect(
        f"Select specific foods from the category '{selected_category}'",
        filtered_foods,
    )

    # 選ばれた食べ物の情報を表示
    st.write("You selected the foods: ", selected_foods)

    # 選択された食品の情報をデータフレームから取得
    if selected_foods:
        food_info = df[df["Food Name"].isin(selected_foods)]
        st.write("Nutritional Information:", food_info.iloc[:, 2:])

        # 栄養情報の集計
        df_macronutrients = food_info[['Calories', 'Protein']]

        # 合計値を計算
        total_calories = df_macronutrients['Calories'].sum()
        total_protein = df_macronutrients['Protein'].sum()

        # グラフ描画の準備
        labels = ['カロリー', 'タンパク質']
        men_values = [2600, 60]  # 男性の推奨摂取量
        women_values = [2000, 50]  # 女性の推奨摂取量
        current_values = [total_calories, total_protein]  # 合計摂取量

        x = range(len(labels))

        # グラフ描画
        fig, ax = plt.subplots(figsize=(8, 5))  # サイズを指定 (幅, 高さ)

        ax.bar(x, current_values, width=0.2, label='現在の摂取量', align='center')
        ax.bar([i + 0.2 for i in x], men_values, width=0.2, label='男性推奨摂取量', align='center')
        ax.bar([i + 0.4 for i in x], women_values, width=0.2, label='女性推奨摂取量', align='center')

        ax.set_xticks([i + 0.2 for i in x])
        ax.set_xticklabels(labels)
        ax.set_ylabel('摂取量')
        ax.legend()
        ax.set_title('今日の栄養素')

        # Streamlitでグラフ表示
        st.pyplot(fig)
