# 🧠 Codebase Q&A

<div align="center">
  <img src="docs/architecture.png" width="600">
</div>

## 🚀 Features
- [x] GitHub repo ingestion
- [ ] Code search with natural language

## 🛠️ Local Setup
```bash
git clone https://github.com/yourusername/codebase-qa
cd codebase-qa
pip install -r requirements.txt

# Run backend
uvicorn backend.main:app --reload

# Run frontend (in new terminal)
streamlit run frontend/app.py
