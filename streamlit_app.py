# 🎰 Aviator Analyzer - Powered by Kali GPT

> 🔍 Predict crash values in the Aviator game using ARIMA & LSTM models — for **educational and research purposes only**.

![Streamlit UI Screenshot](https://huggingface.co/spaces/your-username/aviator-analyzer/raw/main/screenshot.png)

---

## 🚀 Live Demo

👉 Try it now: [Launch on Hugging Face Spaces](https://huggingface.co/spaces/your-username/aviator-analyzer)

---

## 📦 Features

✅ Upload your own game crash data in `.csv` format  
✅ Use auto-generated dummy data  
✅ Visualize game history with interactive plots  
✅ Predict next crash multiplier using:
- 🔮 ARIMA (Auto-Regressive Integrated Moving Average)
- 🤖 LSTM (Long Short-Term Memory Neural Network)

✅ Download predictions as a text file  
✅ Entirely offline, no API dependencies

---

## 🧠 Technologies Used

| Tech | Role |
|------|------|
| `Streamlit` | Web Interface |
| `Pandas` / `NumPy` | Data Handling |
| `Matplotlib` | Visualization |
| `statsmodels` | ARIMA Modeling |
| `TensorFlow / Keras` | LSTM Prediction |
| `scikit-learn` | Data Scaling |

---

## 🗃️ How to Use

### 📥 1. Upload Game Data

Upload a `.csv` file with the following format:

```csv
value
1.75
2.30
1.05
...
