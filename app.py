import streamlit as st
import pandas as pd
from agent import generate_sql
from database import execute_query

st.set_page_config(page_title="AI SQL Agent Pro", page_icon="🤖", layout="wide")

st.markdown("""<style>
.stApp{background:#0e1117;color:white;}
section[data-testid="stSidebar"]{background:#161b22;}
h1{font-size:3rem!important;}
textarea,input{font-size:1.1rem!important;}
button{border-radius:12px!important;height:3rem!important;}
</style>""",unsafe_allow_html=True)

if 'history' not in st.session_state: st.session_state.history=[]

with st.sidebar:

    st.title("🤖 Agentic-AI-SQL-Assistant")

    st.markdown("---")

    st.markdown("### 🚀 Technologies")

    st.markdown("""
    - 🐍 Python
    - 🖥️ Streamlit
    - 🧠 Qwen3
    - 🔗 OpenRouter API
    - 🗄️ SQLite
    - 📊 Pandas
    """)

    st.markdown("---")

    st.caption(
        "AI-powered assistant that converts natural language into SQL queries."
    )

    page = st.selectbox(

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
    st.title('💬 AI Chat')
    q=st.text_area('Ask anything',height=120,placeholder='Show customers from Sofia')
    if st.button('🚀 Run') and q:
        p=st.progress(0)
        with st.spinner('🤖 AI is thinking...'):
            p.progress(30)
            sql=generate_sql(q)
            p.progress(70)
            rows,cols=execute_query(sql)
            p.progress(100)
        st.session_state.history.insert(0,(q,sql))
        st.subheader('Generated SQL')
        st.code(sql,language='sql')
        st.subheader('Results')
        if rows: st.dataframe(pd.DataFrame(rows,columns=cols),use_container_width=True)
        else: st.warning('No results found.')
        p.empty()
    if st.session_state.history:
        st.subheader('History')
        for q,sql in st.session_state.history[:5]:
            with st.expander(q): st.code(sql,'sql')

elif page=="🏠 Dashboard":
    st.title('🏠 Dashboard')
    c,_=execute_query('SELECT COUNT(*) c FROM customers')
    p,_=execute_query('SELECT COUNT(*) c FROM products')
    o,_=execute_query('SELECT COUNT(*) c FROM orders')
    a,b,d=st.columns(3)
    a.metric('Customers',c[0][0]); b.metric('Products',p[0][0]); d.metric('Orders',o[0][0])

elif page=="👥 Customers":
    st.title('👥 Customers')
    r,c=execute_query('SELECT * FROM customers')
    st.dataframe(pd.DataFrame(r,columns=c),use_container_width=True)

elif page=="📦 Products":
    st.title('📦 Products')
    r,c=execute_query('SELECT * FROM products')
    st.dataframe(pd.DataFrame(r,columns=c),use_container_width=True)

elif page=="🛒 Orders":
    st.title('🛒 Orders')
    r,c=execute_query('SELECT * FROM orders')
    st.dataframe(pd.DataFrame(r,columns=c),use_container_width=True)

elif page=="📈 Statistics":
    st.title('📈 Statistics')
    r,_=execute_query('SELECT city,COUNT(*) FROM customers GROUP BY city')
    df=pd.DataFrame(r,columns=['City','Customers']).set_index('City')
    st.bar_chart(df)
