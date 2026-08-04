# 🤖 AGENTIC AI

A powerful suite of autonomous AI agents built using the **[Agno Framework](https://github.com/agno-agi/agno)** and powered by high-performance **Groq LLMs** (such as `llama-3.3-70b-versatile` and `qwen/qwen3-32b`).

This repository demonstrates various agentic capabilities including real-time web search, financial analysis, long-term memory persistence with SQLite, multi-agent orchestration teams, and interactive video content extraction.

---

## 🌟 Key Features & Agent Modules

| Module | Agent Type | LLM Model | Tools / Database | Description |
| :--- | :--- | :--- | :--- | :--- |
| [`agent.py`](file:///d:/agentic-ai/AGENTICAI/agent.py) | **Travel Agent** | `llama-3.3-70b-versatile` | `DuckDuckGoTools` | Provides up-to-date travel advice and real-time web information. |
| [`finance.py`](file:///d:/agentic-ai/AGENTICAI/finance.py) | **Finance Analyst** | `qwen/qwen3-32b` | `YFinanceTools`, `DuckDuckGoTools` | Researches stock prices, analyst recommendations, and fundamentals formatted in Markdown tables. |
| [`memory.py`](file:///d:/agentic-ai/AGENTICAI/memory.py) | **Memory Agent** | `llama-3.3-70b-versatile` | `SqliteDb` (`agno.db`) | Stores and recalls user-specific memories across conversation sessions. |
| [`team.py`](file:///d:/agentic-ai/AGENTICAI/team.py) | **Translation Team** | `qwen/qwen3-32b` | `Team` Orchestration | Multi-agent team (English, Chinese, Hindi) that collaborates to respond in multiple languages. |
| [`youtube_analyzer.py`](file:///d:/agentic-ai/AGENTICAI/youtube_analyzer.py) | **YouTube Analyzer** | `llama-3.3-70b-versatile` | `YouTubeTools` | Extracts video overviews, key learnings, main topics, and timestamps. |
| [`ui.py`](file:///d:/agentic-ai/AGENTICAI/ui.py) | **Streamlit App** | `llama-3.3-70b-versatile` | Streamlit + `YouTubeTools` | Web interface to analyze YouTube videos interactively. |

---

## 🚀 Getting Started

### 1. Prerequisites
- Python **3.10+** installed on your system.
- A **Groq API Key**. Get one at [console.groq.com](https://console.groq.com/).

### 2. Installation

Clone the repository and install the required dependencies:

```bash
# Clone the repository
git clone https://github.com/Ronakjain935/AGENTICAI.git
cd AGENTICAI

# Install required packages
pip install -r requirements.txt
```

### 3. Environment Configuration

Create a `.env` file in the project root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 💻 Usage

### Run Individual Scripts

- **Travel Agent**
  ```bash
  python agent.py
  ```

- **Financial Analyst Agent**
  ```bash
  python finance.py
  ```

- **Persistent Memory Agent**
  ```bash
  python memory.py
  ```

- **Multi-Agent Translation Team**
  ```bash
  python team.py
  ```

- **YouTube Video Analyzer CLI**
  ```bash
  python youtube_analyzer.py
  ```

### Run Streamlit Web Application

Launch the interactive web UI for analyzing YouTube videos:

```bash
streamlit run ui.py
```

---

## 📦 Project Structure

```
AGENTICAI/
├── agent.py               # Travel Agent with web search tool
├── finance.py             # Stock & Financial Analyst Agent
├── memory.py              # User memory agent with SQLite persistence
├── team.py                # Multi-language agent team orchestration
├── youtube_analyzer.py    # Core YouTube video analyzer agent
├── ui.py                  # Streamlit web application interface
├── requirements.txt       # Python package dependencies
├── requirement.yxy        # Alias requirement file
└── README.md              # Project documentation
```

---

## 🛠️ Built With

- **[Agno](https://github.com/agno-agi/agno)** - Multi-agent AI framework
- **[Groq](https://groq.com/)** - High-speed AI inference engine
- **[Streamlit](https://streamlit.io/)** - Interactive web app framework
- **[YFinance](https://pypi.org/project/yfinance/)** & **[DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/)** - Financial & Web Search tools
