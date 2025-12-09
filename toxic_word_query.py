
def toxic_word_query():
    import streamlit as st
    import os
    from dotenv import load_dotenv
    import pandas as pd

    load_dotenv()

    db_url = os.getenv('DB_URL')

    st.title("Word Safety Data Audit")

    table_map = {
    "Toxic Quarantine": "quarantined_toxic_data",
    "Clean Training Data": "clean_training_data"
    }

    col1, col2 = st.columns(2)

    with col1:
        selected_label = st.selectbox("Select dataset to audit", list(table_map.keys()))
        table_name = table_map[selected_label]
    
    with col2:
        search_term = st.text_input("Search for a keyword: e.g. stupid, politics")

    if search_term:
        toxic_query = pd.read_sql(
            f"SELECT * FROM {table_name} WHERE text ILIKE '%%{search_term}%%' LIMIT 50",
            db_url
        )

        if not toxic_query.empty:
            st.error(f"Found records in {table_name}")
            st.dataframe(toxic_query)

        else:
            st.info(f"No records found in {table_name}")

if __name__ == '__main__':
    toxic_word_query()