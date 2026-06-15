from openai import OpenAI

import streamlit as st

import re



SCHEMA="""


customers(

id INTEGER,

name TEXT,

city TEXT,

age INTEGER

)


products(

id INTEGER,

name TEXT,

price REAL

)


orders(

id INTEGER,

customer_id INTEGER,

product_id INTEGER,

quantity INTEGER

)


"""



def generate_sql(question):


    client=OpenAI(

    base_url="https://openrouter.ai/api/v1",

    api_key=st.secrets["OPENROUTER_API_KEY"]

    )



    prompt=f"""

You are an AI SQL Agent.


Database schema:


{SCHEMA}


Rules:


1.Return ONLY SQL

2.SQLite syntax only

3.No markdown

4.No explanations

5.Return ONE query only



Question:


{question}



SQL:


"""



    response=client.chat.completions.create(


    model="qwen/qwen3:free",


    messages=[

    {

    "role":"user",

    "content":prompt

    }

    ],


    timeout=60


    )



    answer=response.choices[0].message.content



    match=re.search(


    r"SELECT[\s\S]*?;",


    answer,


    re.IGNORECASE


    )



    if match:


        return match.group(0)



    return answer.strip()
