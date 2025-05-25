import streamlit as st
import pandas as pd

# Load the CSV file
df = pd.read_csv("pokemon.csv")

# Set column names based on your dataset
TYPE_COLUMN = "type1"
NAME_COLUMN = "name"
HP_COLUMN = "hp"
ATTACK_COLUMN = "attack"
DEFENSE_COLUMN = "defense"
SPEED_COLUMN = "speed"

# Sidebar filter for Type
st.sidebar.title("Filter")
types = sorted(df[TYPE_COLUMN].dropna().unique())
selected_type = st.sidebar.selectbox("Choose Pokémon Type", ["All"] + types)

# Filter based on Type
if selected_type != "All":
    filtered_df = df[df[TYPE_COLUMN] == selected_type]
else:
    filtered_df = df

# App Title
st.title("Pokémon Stat Viewer")
st.write("Explore Pokémon base stats by primary type.")

# Show stat table
st.subheader("Pokémon Stats Table")
st.dataframe(filtered_df[[NAME_COLUMN, TYPE_COLUMN, HP_COLUMN, ATTACK_COLUMN, DEFENSE_COLUMN, SPEED_COLUMN]])

# Bar Chart for Attack
st.subheader("Attack Stat Chart")
attack_chart = filtered_df[[NAME_COLUMN, ATTACK_COLUMN]].set_index(NAME_COLUMN)
st.bar_chart(attack_chart)
