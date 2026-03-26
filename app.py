import streamlit as st
from crew_setup import sports_crew

st.set_page_config(
    page_title="AI Sports Planning Assistant",
    page_icon="⚽",
    layout="wide"
)

# -------------------------
# CUSTOM CSS
# -------------------------
st.markdown("""
<style>
.stApp{
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
}

.title{
text-align:center;
font-size:60px;
font-weight:700;
background: linear-gradient(90deg,#00c6ff,#0072ff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.subtitle{
text-align:center;
font-size:20px;
color:#d1d1d1;
margin-bottom:40px;
}

.agent-card{
background:#0b0b0b;
padding:25px;
border-radius:15px;
border:1px solid #333;
}

button[kind="primary"]{
background:linear-gradient(90deg,#00c6ff,#0072ff);
border:none;
border-radius:10px;
font-size:18px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------
st.markdown('<h1 class="title">🏆 AI Sports Planning Assistant</h1>', unsafe_allow_html=True)

st.markdown(
'<p class="subtitle">Multi-Agent AI system that generates training plans, analysis and match strategies</p>',
unsafe_allow_html=True
)

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.title("⚙️ Sports Settings")

sport = st.sidebar.selectbox(
    "Choose Sport",
    ["Cricket","Football","Basketball","Tennis","Fitness Training"]
)

difficulty = st.sidebar.selectbox(
    "Skill Level",
    ["Beginner","Intermediate","Professional"]
)

st.sidebar.markdown("---")

st.sidebar.info("""
This AI uses **multiple agents**

🧠 Planning Agent  
📊 Performance Analyst  
🧭 Strategy Agent  
📄 Report Generator
""")

# -------------------------
# USER INPUT
# -------------------------
st.markdown("### 💬 Ask the AI Sports Coach")

user_input = st.text_input(
    "Example: cricket batting training plan",
    placeholder="Describe your sports training request..."
)

generate = st.button("🚀 Generate AI Sports Plan")

# -------------------------
# WORKFLOW DISPLAY
# -------------------------
st.markdown("### 🤖 Agent Workflow")

st.write("""
User Query  
⬇  
🧠 Planning Agent  
⬇  
📊 Performance Analyst  
⬇  
🧭 Strategy Agent  
⬇  
📄 Report Generator
""")

# -------------------------
# AI RESPONSE
# -------------------------
if generate and user_input:

    with st.spinner("🤖 AI Agents are working together..."):

        prompt = f"""
Sport: {sport}
Skill Level: {difficulty}

User Request:
{user_input}

Generate:
1. Training Plan
2. Performance Analysis
3. Match Strategy
4. Final Sports Report
"""

        crew_result = sports_crew.kickoff(
            inputs={"sport_topic": prompt}
        )

        # SAFE extraction of outputs
        planning_output = ""
        analysis_output = ""
        strategy_output = ""
        report_output = ""

        try:
            tasks = crew_result.tasks_output

            if len(tasks) > 0:
                planning_output = tasks[0].raw

            if len(tasks) > 1:
                analysis_output = tasks[1].raw

            if len(tasks) > 2:
                strategy_output = tasks[2].raw

            if len(tasks) > 3:
                report_output = tasks[3].raw

        except:
            report_output = str(crew_result)

    st.markdown("---")
    st.header("📊 Multi-Agent AI Outputs")

    tab1, tab2, tab3, tab4 = st.tabs([
        "🧠 Planning Agent",
        "📊 Performance Analyst",
        "🧭 Strategy Agent",
        "📄 Final Report"
    ])

    with tab1:
        st.subheader("Training Plan")
        st.markdown(
            f'<div class="agent-card">{planning_output}</div>',
            unsafe_allow_html=True
        )

    with tab2:
        st.subheader("Performance Analysis")
        st.markdown(
            f'<div class="agent-card">{analysis_output}</div>',
            unsafe_allow_html=True
        )

    with tab3:
        st.subheader("Winning Strategy")
        st.markdown(
            f'<div class="agent-card">{strategy_output}</div>',
            unsafe_allow_html=True
        )

    with tab4:
        st.subheader("Final AI Sports Report")
        st.markdown(
            f'<div class="agent-card">{report_output}</div>',
            unsafe_allow_html=True
        )

    # -------------------------
    # DOWNLOAD BUTTON
    # -------------------------
    st.download_button(
        label="📥 Download AI Report",
        data=str(report_output),
        file_name="sports_plan.txt",
        mime="text/plain"
    )

# -------------------------
# FOOTER
# -------------------------
st.markdown("---")

st.markdown("""
<center>

⚡ Built with **CrewAI + OpenRouter + Streamlit**

AI Multi-Agent Sports Strategy System

</center>
""", unsafe_allow_html=True)