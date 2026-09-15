import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Chemical Kinetics Simulator", page_icon="⚗️", layout="centered")

st.title("⚗️ Reaction Kinetics Simulator")
st.markdown("محاكاة تفاعلية لحركية التفاعلات الكيميائية ومتابعة تطور تقدم التفاعل ($x$) وزمن نصف التفاعل ($t_{1/2}$).")

st.sidebar.header("إعدادات التفاعل")
C0 = st.sidebar.slider("التركيز الابتدائي للمتفاعل $C_0$ (mol/L):", 0.1, 2.0, 1.0, 0.1)
k = st.sidebar.slider("ثابت السرعة $k$:", 0.01, 0.5, 0.1, 0.01)
order = st.sidebar.selectbox("مرتبة التفاعل:", ["من المرتبة الأولى", "من المرتبة الثانية"])

# حساب الزمن والتقدم
t_max = 50 / k
t = np.linspace(0, t_max, 200)

if order == "من المرتبة الأولى":
    # C(t) = C0 * exp(-k*t)
    C = C0 * np.exp(-k * t)
    x = C0 - C
    t_half = np.log(2) / k
else:
    # C(t) = C0 / (1 + C0 * k * t)
    C = C0 / (1 + C0 * k * t)
    x = C0 - C
    t_half = 1 / (k * C0)

# العرض النتائج في الواجهة
col1, col2 = st.columns(2)
with col1:
    st.metric(label="زمن نصف التفاعل ($t_{1/2}$)", value=f"{t_half:.2f} ثانية")
with col2:
    st.metric(label="التركيز الباقي حالياً عند النهاية", value=f"{C[-1]:.3f} mol/L")

st.subheader("📈 التمثيل البياني لتطور التركيز والتقدم")

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t, C, label="تركيز المتفاعل $C(t)$", color="crimson", linewidth=2.5)
ax.plot(t, x, label="تقدم التفاعل $x(t)$", color="teal", linewidth=2.5, linestyle="--")
ax.axvline(t_half, color="gray", linestyle=":", label=f"t1/2 = {t_half:.2f}s")
ax.set_xlabel("الزمن ($t$)")
ax.set_ylabel("التركيز / التقدم")
ax.legend()
ax.grid(True, alpha=0.3)

st.pyplot(fig)

st.markdown("---")
st.caption("موقع مخصص لمشروع البكالوريا في الهندسة الكيميائية - تم تطويره بواسطة Streamlit و Python.")
