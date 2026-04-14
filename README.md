#  Sports Planning Assistant Agent (Multi-Agent AI System)

##  Overview

The **Sports Planning Assistant Agent** is a multi-agent AI system designed to generate intelligent sports training plans, performance analysis, match strategies, and final reports.

This project leverages **CrewAI**, **OpenRouter API**, and **Streamlit** to simulate a collaborative team of AI agents working together to assist athletes and coaches.

---

##  Features

*  Multi-Agent Architecture (Planner, Analyst, Strategy, Reporter)
* Automated Training Plan Generation
*  Performance Analysis with actionable insights
*  Match-winning Strategy Recommendations
*  Final Comprehensive Sports Report
* Interactive UI using Streamlit

---

## System Architecture

### Agents:

* **Planning Agent** → Creates structured training plans
* **Performance Analyst** → Evaluates and improves plans
* **Strategy Agent** → Generates match strategies
* **Report Agent** → Combines all outputs into final report

---

## Tech Stack

* **Python**
* **CrewAI**
* **OpenRouter API (LLM Integration)**
* **Streamlit (Frontend UI)**
* **dotenv (Environment Management)**

---

## Project Structure

```
AI-AGENT-SPORTS/
│── agents.py              # Agent definitions
│── tasks.py               # Task workflows
│── crew_setup.py          # Crew configuration
│── app.py                 # Streamlit UI
│── main.py                # Entry point
│── requirements.txt       # Dependencies
│── .gitignore             # Ignored files
│── High-Level-Design.pdf
│── low-level-design.pdf
│── Project-final-report.pdf
```

---

## Setup Instructions

### 1️ Clone Repository

```
git clone https://github.com/AyushiParsai/AI-AGENT-SPORTS.git
cd AI-AGENT-SPORTS
```

---

### 2️Install Dependencies

```
pip install -r requirements.txt
```

---

### Setup Environment Variables

Create a `.env` file:

```
OPENROUTER_API_KEY=your_api_key_here
```

---

### Run the Application

```
streamlit run app.py
```

---

## Example Use Case

Input:

```
Sport: Cricket  
Skill Level: Beginner  
Request: Generate training plan  
```

Output:

* Training Plan
* Performance Analysis
* Match Strategy
* Final Report

---

## Screenshots

*(Add your UI screenshots here for better presentation)*

---

##  Future Enhancements

* Real-time performance tracking
* Integration with wearable sports devices
* Advanced analytics dashboard
* Multi-sport support

---

## Security Note

Sensitive data like API keys are stored in `.env` and excluded using `.gitignore`.


