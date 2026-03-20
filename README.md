# FinexaAI 🤖📈
### AI-Powered Financial Analysis & Editorial Assistant

> **Economic Times Hackathon 2026 — Problem #6: AI for the Indian Investor**  
> Built by **Team gaurisharmabts** — Gauri Sharma & Harshil Jain  
> Jaypee Institute of Information Technology, Noida

---

## 🧠 What is FinexaAI?

India has 14 crore+ demat account holders — yet most investors react to tips instead of data, miss regulatory filings, and spend hours reading reports manually. **FinexaAI** is a unified, production-ready AI platform that solves this.

It brings together **5 AI-powered modules** — document intelligence, editorial assistance, broker news automation, live market data, and corporate filings monitoring — all in one place.

> *Turning India's market data into actionable intelligence.*

---

## ✨ Features

### 📄 Module 1 — Financial Data Analysis (PDF Intelligence)
- Upload any financial PDF — annual reports, earnings presentations, 10-K/10-Q filings, broker notes
- Gemini AI reads and extracts **27 Key Financial Parameters** automatically
- Outputs structured summaries with plain-language explanations of each metric
- Tracks trends (YoY, QoQ), flags risks, and highlights key takeaways
- Full **Analysis History** — revisit any previously uploaded document
- One-click **Download Report** for sharing with your team
- Saves analysts **3–4 hours per report**

### ✍️ Module 2 — AI Editorial Assistant
- Paste a draft article and get instant **content improvement suggestions**
- Built-in **Style Guide** — editorial rules for tone, headline length, citations, and article structure
- **Draft Generator** — provide a market summary and get a complete, publish-ready financial article in under 3 minutes
- Supports **Context tab** for attaching reference documents and filings
- **3–5x faster** content production vs. manual writing

### 📰 Module 3 — Broker Report Articles
- Automatically crawls trusted financial news sources — Yahoo Finance, Bloomberg, MarketWatch, Reuters, SEC EDGAR
- Extracts, summarises, and **scores each article for sentiment** (positive / neutral / negative) using FinBERT
- Curated, hands-free news feed updated throughout the day
- Filter by keyword, source, or topic — read full articles directly from the platform

### 📊 Module 4 — Daily Market Summary Dashboard
- Live **Major Market Indices** — Indian and US markets
- **Top Gainers & Top Losers** with real-time price and percentage changes
- **Sector Performance Heatmap** — Financials, Healthcare, Energy, Consumer, Industrials, Real Estate, and more
- Personal **Watchlist** — track any stock (NSE/BSE/NYSE) with live price updates
- Export snapshot for reporting

### 🔔 Module 5 — Corporate Filings Alerts
- 24/7 monitoring of **SEBI, NSE, BSE (India)** and **SEC EDGAR (US)**
- Instant **email alerts** the moment a filing drops for a company on your watchlist
- View live **SEC filings** (10-K, 8-K, 6-K, 497 forms) with direct links to source documents
- View live **SEBI filings** — prospectuses, bulk deals, insider trades, and disclosures
- **Send Filings Digest** to your entire team with one click
- Never miss a regulatory disclosure again

---

## 🏗️ Architecture

The platform follows a **multi-source pipeline** — raw data flows through five distinct layers:

**Data Sources → Ingestion Layer → AI Core → Storage Layer → Outputs**

| Layer | What it does |
|---|---|
| **Data Sources** | User PDFs, Broker News Sites, SEBI/BSE/NSE portals, SEC EDGAR, Market APIs |
| **Ingestion Layer** | PyPDF/Unstructured for PDFs, Playwright/BeautifulSoup for web crawling, XBRL Parser for filings, FastAPI Async orchestration, Cron Scheduler for automated polling |
| **AI Core** | LangGraph Agentic Workflow + Gemini API — Scraping Agent, Sentiment (FinBERT), Vector Retrieval (ChromaDB), Summarisation Agent, Editorial Agent, Alert Agent |
| **Storage Layer** | ChromaDB (Vector/RAG), MongoDB (News & Reports), Watchlist Manager, Email Service, SQL/NoSQL (Market Time-Series) |
| **Outputs** | PDF Financial Analysis, AI Editorial Assistant, Broker Report Summarisation, Market Dashboard, Filings Monitor + Email Alerts |
| **Frontend** | React.js · Plotly.js Charts · WebSocket Live Feeds · Editorial UI · Watchlist Manager |

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Frontend** | React.js, Plotly.js | UI, charts, live feeds |
| **Backend** | FastAPI (Async) | API server, concurrent request handling |
| **Orchestration** | LangGraph + LangChain | Agentic multi-step workflow management |
| **AI Models** | Gemini API | Long-context document reasoning |
| **Sentiment** | FinBERT | Domain-trained financial sentiment classification |
| **Vector DB** | ChromaDB | Semantic retrieval, RAG pipeline |
| **Document DB** | MongoDB | News, reports, editorial storage |
| **PDF Parsing** | PyPDF, Unstructured | Financial document extraction |
| **Web Scraping** | Playwright, BeautifulSoup | News and filings crawling |
| **Filing Parser** | XBRL Parser | Regulatory filing parsing |
| **Scheduling** | Cron Scheduler | Automated polling of 4 regulatory APIs |
