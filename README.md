# Image Caption AI Agent

This is a Streamlit-based web app that generates smart image captions using BLIP (Bootstrapped Language-Image Pretraining), and then stylizes them with OpenRouter AI to suit various tones like **funny**, **aesthetic**, **poetic**, etc.

> Upload an image → generate a smart caption → choose a style → get a stylized caption!

---

## Features

- 📷 Upload any image (JPG, PNG)
- 🧠 Automatically generate a base caption using BLIP
- 🎨 Stylize the caption using OpenRouter AI (choose from: *funny, aesthetic, poetic, emotional, sarcastic*)
- 🧼 Clean, stateful UI using Streamlit

---

## 📸 Dashboard

<img width="1366" height="617" alt="image" src="https://github.com/user-attachments/assets/f3e320f8-4d11-4f8e-9b7c-30f2cf1c3628" />

---
## Results
<img width="1208" height="606" alt="Screenshot (87)" src="https://github.com/user-attachments/assets/2a31eec4-7b48-4d1d-96d7-3130c3ab1200" />

---

## Setup & Installation

```bash
# Clone the repo
git clone https://github.com/Mansiq/Image-caption-Agent.git
cd Image-caption-Agent

python -m venv venv
venv\Scripts\activate    # Windows

source venv/bin/activate # macOS/Linux

# Install required packages
pip install -r requirements.txt
```

---

## Setup API Key

1. Create a file named `api_key.env` in the root directory.
2. Add this inside:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

---

## Run the App

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

---

## Example Styles

| Style     | Result Example                                  |
|-----------|--------------------------------------------------|
| Funny     | “This dog thinks he's the CEO of the couch.”     |
| Aesthetic | “Soft sunlight kisses the fur of a calm pup.”    |
| Poetic    | “Where dreams and paws find morning light.”      |

---

## Requirements

- Python 3.8+
- `streamlit`
- `transformers`
- `torch`
- `Pillow`
- `requests`
- `python-dotenv`

Install all with:

```bash
pip install -r requirements.txt
```

---

## Tech Stack

- BLIP: Image captioning (HuggingFace Transformers)
- OpenRouter: GPT-like models for stylization
- Streamlit: Web UI
- Dotenv: API key management

---

## Project Structure

```
Image-caption-Agent/
│
├── app.py              
├── model.py           
├── api_key.env        
├── requirements.txt    
├── .gitignore         
└── README.md        
 
```

---

