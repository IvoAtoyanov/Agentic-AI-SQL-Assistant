import streamlit as st

import pandas as pd

from agent import generate_sql

from database import execute_query


st.set_page_config(

page_title="Agentic-AI-SQL-Assistant",

page_icon="🤖",

layout="wide"

)



st.markdown("""

<style>

.stApp{

background:#0e1117;

color:white;

}


section[data-testid="stSidebar"]{

background:#161b22;

}


h1{

font-size:50px !important;

}


textarea{

font-size:20px !important;

}


button{

height:55px;

border-radius:15px;

}


</style>

""",

unsafe_allow_html=True)



if "history" not in st.session_state:

    st.session_state.history=[]



with st.sidebar:


    st.title(

    "🤖 Agentic-AI-SQL-Assistant"

    )


    st.markdown("---")


    st.markdown(

    "### 🚀 Technologies"

    )


    st.markdown("""

- 🐍 Python

- 🖥️ Streamlit

- 🧠 Qwen3

- 🔗 OpenRouter API

- 🗄️ SQLite

- 📊 Pandas

""")


    st.markdown("---")


    page=st.selectbox(

    "Navigate",

    [

    "💬 AI Chat",

    "🏠 Dashboard",

    "👥 Customers",

    "📦 Products",

    "🛒 Orders",

    "📈 Statistics"

    ]

    )



if page=="💬 AI Chat":


    st.title(

    "💬 AI Chat"

    )


    q=st.text_area(

    "Ask anything",

    height=120,

    placeholder="Show customers from Sofia"

    )



    if st.button(

    "🚀 Run"

    ) and q:



        with st.spinner(

        "🤖 AI is thinking..."

        ):



            sql=generate_sql(

            q

            )



            rows,cols=execute_query(

            sql

            )



        st.session_state.history.insert(

        0,

        (q,sql)

        )



        st.subheader(

        "Generated SQL"

        )


        st.code(

        sql,

        language="sql"

        )



        st.subheader(

        "Results"

        )



        if rows:


            df=pd.DataFrame(

            rows,

            columns=cols

            )


            st.dataframe(

            df,

            use_container_width=True

            )


        else:


            st.warning(

            "No results."

            )



elif page=="🏠 Dashboard":


    st.title("🏠 Dashboard")


    c,_=execute_query(

    "SELECT COUNT(*) FROM customers"

    )


    p,_=execute_query(

    "SELECT COUNT(*) FROM products"

    )


    o,_=execute_query(

    "SELECT COUNT(*) FROM orders"

    )



    a,b,c2=st.columns(3)



    a.metric(

    "Customers",

    c[0][0]

    )


    b.metric(

    "Products",

    p[0][0]

    )


    c2.metric(

    "Orders",

    o[0][0]

    )



elif page=="👥 Customers":


    r,c=execute_query(

    "SELECT * FROM customers"

    )


    st.dataframe(

    pd.DataFrame(

    r,

    columns=c

    ),

    use_container_width=True

    )



elif page=="📦 Products":


    r,c=execute_query(

    "SELECT * FROM products"

    )


    st.dataframe(

    pd.DataFrame(

    r,

    columns=c

    ),

    use_container_width=True

    )



elif page=="🛒 Orders":


    r,c=execute_query(

    "SELECT * FROM orders"

    )


    st.dataframe(

    pd.DataFrame(

    r,

    columns=c

    ),

    use_container_width=True

    )



elif page=="📈 Statistics":


    r,_=execute_query(

    """

    SELECT

    city,

    COUNT(*)

    FROM customers

    GROUP BY city

    """

    )



    df=pd.DataFrame(

    r,

    columns=[

    "City",

    "Customers"

    ]

    )



    st.bar_chart(

    df.set_index(

    "City"

    )

    )
