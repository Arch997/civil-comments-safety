
def toxic_word_query(table_name: str):
    import streamlit as st
    import os
    from dotenv import load_dotenv
    import pandas as pd

    load_dotenv()

    db_url = os.getenv('DB_URL')

    st.title("AI Safety Data Audit")

    search_term = st.text_input("Search for a keyword: e.g. stupid, politics")


    toxic_query = pd.read_sql(
        f"SELECT * FROM {table_name} WHERE text ILIKE '%%{search_term}%%' LIMIT 50",
        db_url
    )

    if not toxic_query.empty:
        st.error("Found toxic entries in the db")
        st.dataframe(toxic_query)

    else:
        st.success("No toxic records found in quarantine")

if __name__ == '__main__':
    toxic_word_query('clean_training_data')