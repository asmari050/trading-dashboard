import streamlit as st
import pandas as pd
import numpy as np

# إعدادات الصفحة لتكون بعرض الشاشة وتصميم داكن
st.set_page_config(page_title="0DTE Dashboard", layout="wide", initial_sidebar_state="collapsed")

# تصميم CSS مخصص لجعل المظهر احترافي وداكن
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { background-color: #1f2937; padding: 15px; border-radius: 10px; border: 1px solid #374151; }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 لوحة تحكم تداول 0DTE - أبو عبد الرحمن")
st.write("تحليل لحظي لمؤشرات السوق (بيانات تجريبية)")

# توزيع المؤشرات في أعمدة (تتوافق تلقائياً مع الجوال)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="VOLD (NYSE)", value="1.2B", delta="15%", delta_color="normal")
with col2:
    st.metric(label="ADD (NYSE)", value="+850", delta="120", delta_color="normal")
with col3:
    st.metric(label="TRIN.NY", value="0.85", delta="-0.05", delta_color="inverse")
with col4:
    st.metric(label="SPX Price", value="5,240.50", delta="+12.20")

# قسم الرسوم البيانية
st.markdown("### 📈 حركة السيولة التراكمية (CVD)")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['CVD Buy', 'CVD Sell', 'VPIN'])
st.line_chart(chart_data)

st.success("النظام يعمل بنجاح وجاهز للربط مع API الخاص بك لاحقاً.")