import os
from google.cloud import bigquery
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'sunpower-375201-74be4a55360d.json'


client = bigquery.Client()

sqlquery = """
SELECT * FROM `sunpower-375201.sunpower_agg.sunpower_full_funnel` WHERE Date = "2023-10-17" 
"""

query_job = client.query(sqlquery).to_dataframe()

st.dataframe(query_job)

col1, col2, col3 = st.columns(3)
col1.metric("Clicks", query_job.Clicks.sum())
col2.metric("Impressions", query_job.Impressions.sum())
col3.metric("Cost", round(query_job.Cost.sum()))


# Create scatter plot of cost and clicks
fig, ax = plt.subplots()
sns.scatterplot(data=query_job, x="Cost", y="Clicks", ax=ax)
ax.set_title("Cost vs Clicks")
ax.set_xlabel("Cost")
ax.set_ylabel("Clicks")
st.pyplot(fig)
