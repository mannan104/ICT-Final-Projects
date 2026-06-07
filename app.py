import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="ICT for Structural Safety",
    page_icon="🏗️",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg,#0f172a,#1e293b,#0f766e);
}

.title {
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:white;
    padding:10px;
}

.subtitle {
    text-align:center;
    font-size:20px;
    color:#cbd5e1;
}

.card {
    background: rgba(255,255,255,0.08);
    padding:20px;
    border-radius:20px;
    backdrop-filter: blur(10px);
    border:1px solid rgba(255,255,255,0.1);
}

.team {
    background: linear-gradient(135deg,#06b6d4,#3b82f6);
    padding:15px;
    border-radius:15px;
    color:white;
    text-align:center;
    font-size:18px;
}

.metric-box {
    background:#0ea5e9;
    padding:15px;
    border-radius:15px;
    color:white;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.markdown(
    '<div class="title">🏗 ICT FOR STRUCTURAL SAFETY</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Live Beam Deflection Visualizer</div>',
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("⚙ Beam Parameters")

L = st.sidebar.slider(
    "Beam Length (m)",
    1.0,
    20.0,
    10.0
)

P = st.sidebar.slider(
    "Point Load (N)",
    100.0,
    10000.0,
    5000.0
)

E = st.sidebar.slider(
    "Young's Modulus (Pa)",
    1e9,
    3e11,
    2e11,
    format="%.2e"
)

I = st.sidebar.slider(
    "Moment of Inertia (m⁴)",
    0.000001,
    0.01,
    0.0005,
    format="%.6f"
)

# ---------------- THEORY ---------------- #
col1, col2 = st.columns([2,1])

with col1:
    st.markdown("""
    <div class="card">
    <h3 style='color:white;'>📘 Project Overview</h3>

    This application demonstrates how Information and Communication Technology (ICT)
    can be used for structural safety analysis.

    The visualizer calculates and displays the beam deflection in real time.
    Engineers can instantly observe the effect of changing beam length,
    load, material stiffness, and section properties.

    Deflection Formula:

    δ = PL³ / (48EI)

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3 style='color:white;'>✨ Features</h3>

    ✔ Real-Time Visualization

    ✔ Interactive Controls

    ✔ Structural Safety Monitoring

    ✔ Modern Dashboard

    ✔ Engineering Calculations

    </div>
    """, unsafe_allow_html=True)

st.markdown("")

# ---------------- CALCULATIONS ---------------- #
delta_max = (P * (L**3)) / (48 * E * I)

x = np.linspace(0, L, 500)

y = delta_max * np.sin(np.pi * x / L)

# ---------------- METRICS ---------------- #
m1, m2, m3 = st.columns(3)

with m1:
    st.metric("Beam Length", f"{L:.2f} m")

with m2:
    st.metric("Applied Load", f"{P:.0f} N")

with m3:
    st.metric("Maximum Deflection", f"{delta_max:.8f} m")

st.markdown("---")

# ---------------- GRAPH ---------------- #
fig, ax = plt.subplots(figsize=(12,5))

ax.plot(
    x,
    y,
    linewidth=4,
    color="#00E5FF"
)

ax.fill_between(
    x,
    y,
    color="#00E5FF",
    alpha=0.3
)

ax.set_title(
    "Live Beam Deflection Profile",
    fontsize=16,
    fontweight="bold"
)

ax.set_xlabel("Beam Length (m)")
ax.set_ylabel("Deflection (m)")
ax.grid(True, linestyle="--", alpha=0.5)

st.pyplot(fig)

# ---------------- SAFETY STATUS ---------------- #
st.markdown("## 🛡 Structural Safety Indicator")

if delta_max < 0.005:
    st.success("✅ SAFE STRUCTURE - Deflection is within acceptable limits.")

elif delta_max < 0.02:
    st.warning("⚠ MODERATE DEFLECTION - Monitoring Recommended.")

else:
    st.error("🚨 HIGH DEFLECTION - Structural Review Required.")

# ---------------- ANIMATION ---------------- #
st.markdown("## 🎯 Live Load Animation")

progress = st.progress(0)

for i in range(100):
    progress.progress(i + 1)

# ---------------- TEAM SECTION ---------------- #
st.markdown("---")
st.markdown("## 👨‍💻 Project Team")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="team">

    <h3>Team Members</h3>

    Abdul Mannan (55)

    Muhammad Bin Akarma (59)

    Muneeb Azhar (03)

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="team">

    <h3>Team Members</h3>

    Ahmed Ali (115)

    Hammad Fida (27)

    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div style='text-align:center;
font-size:18px;
color:white;
padding:15px;'>

🏗 Mechanical Engineering Project

ICT for Structural Safety: Live Beam Deflection Visualizer

Developed using Python, Streamlit, NumPy & Matplotlib

</div>
""", unsafe_allow_html=True)
