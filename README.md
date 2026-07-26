# 🎥 AI Video Assistant

An end-to-end AI-powered Video Assistant that transforms YouTube videos or local audio files into searchable knowledge using Whisper, LangChain, ChromaDB, and Large Language Models.

Instead of manually watching long videos, users can automatically generate:

- 📝 AI-generated summaries
- 📌 Action items
- ✅ Key decisions
- ❓ Open questions
- 💬 Chat with the video using Retrieval-Augmented Generation (RAG)

---

# 🚀 Features

### 🎥 Video Processing
- Accepts YouTube URLs
- Supports local audio files
- Automatically downloads and processes audio

### 🎙 Speech-to-Text
- Uses OpenAI Whisper
- Splits long audio into chunks
- Handles lengthy videos efficiently
- Supports transcription and translation

### 📄 AI Summarization
Generates:
- Concise summaries
- AI-generated titles
- Action Items
- Key Decisions
- Open Questions

### 🧠 Retrieval-Augmented Generation (RAG)

Instead of sending the entire transcript to the LLM, the assistant:

- Splits transcript into semantic chunks
- Generates embeddings
- Stores them in ChromaDB
- Retrieves only relevant chunks
- Produces context-aware answers

### 💬 Interactive Chat

Users can ask questions like:

- What is the video about?
- Who is the speaker?
- What decisions were made?
- What tasks were assigned?
- Summarize the ending.

The assistant retrieves only the most relevant transcript chunks before answering.

### 🌐 Streamlit Interface

Simple and interactive UI allowing users to:

- Upload YouTube URLs
- View summaries
- Explore extracted insights
- Chat with the processed video

---

# 🏗 Project Architecture

```
                +-------------------+
                |  YouTube URL      |
                +-------------------+
                          |
                          ▼
                yt-dlp + FFmpeg
                          |
                          ▼
                  WAV Audio File
                          |
                          ▼
               Audio Chunking
                          |
                          ▼
              Whisper Transcription
                          |
                          ▼
                 Full Transcript
                          |
          ┌───────────────┴───────────────┐
          ▼                               ▼
 AI Insight Generation             Vector Database
 (Summary, Title, etc.)          (Chroma + Embeddings)
          │                               │
          ▼                               ▼
     Streamlit UI                 Retriever + LLM
          │                               │
          └───────────────┬───────────────┘
                          ▼
                    User Questions
```

---

# 🛠 Tech Stack

## Programming Language

- Python 3.11+

---

## Frontend

- Streamlit

---

## AI Models

- Whisper (Speech Recognition)
- Mistral LLM (Text Generation)

---

## LLM Framework

- LangChain

---

## Vector Database

- ChromaDB

---

## Embedding Model

- HuggingFace Sentence Transformers

---

## Audio Processing

- yt-dlp
- FFmpeg
- Pydub

---

## Environment Management

- python-dotenv

---

# 📂 Project Structure

```
AI-Video-Assistant/

│
├── app.py                  # Streamlit UI
├── main.py                 # Complete AI Pipeline
├── requirements.txt
├── README.md
│
├── core/
│   ├── transcriber.py
│   ├── summarize.py
│   ├── extractor.py
│   ├── RAG_engine.py
│   ├── embeddings.py
│   ├── llm.py
│   └── prompts.py
│
├── utils/
│   ├── downloader.py
│   ├── audio_processor.py
│   └── cleanup.py
│
├── downloads/
│
├── vector_db/
│
└── .env
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/AI-Video-Assistant.git

cd AI-Video-Assistant
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install FFmpeg

Windows

Download from

https://ffmpeg.org/download.html

or

```bash
winget install -e --id Gyan.FFmpeg
```

Verify

```bash
ffmpeg -version
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
MISTRAL_API_KEY=your_api_key_here

WHISPER_MODEL=small
```

---

# ▶ Running the Project

Streamlit UI

```bash
streamlit run app.py
```

---

# 📖 How It Works

## Step 1

Download audio from YouTube.

↓

## Step 2

Convert audio to WAV format.

↓

## Step 3

Split long audio into chunks.

↓

## Step 4

Transcribe each chunk using Whisper.

↓

## Step 5

Merge transcripts into one document.

↓

## Step 6

Generate:

- Title
- Summary
- Action Items
- Key Decisions
- Open Questions

↓

## Step 7

Chunk transcript.

↓

## Step 8

Generate embeddings.

↓

## Step 9

Store embeddings inside ChromaDB.

↓

## Step 10

Retrieve relevant chunks for each user query.

↓

## Step 11

Generate final answer using Mistral.

---

# 💬 Example Questions

```
What is this video about?

Summarize the ending.

Who are the speakers?

What action items were discussed?

What decisions were made?

Explain the main topic.

List all open questions.
```

---

# 📸 Screenshots

(Add screenshots here)

```
Home Screen

Summary

Chat Interface

Generated Insights
```

---

# 🚧 Current Limitations

- Processes one video at a time.
- Requires internet for YouTube downloads.
- Long videos take additional transcription time.
- Accuracy depends on transcript quality.

---

# 🔮 Future Improvements

- Multiple video support
- PDF report generation
- Speaker diarization
- Timestamp-based citations
- Multi-language support
- Streaming transcription
- Cloud deployment
- Chat history persistence
- Better reranking models
- Docker support

---

# 📚 Learning Outcomes

This project demonstrates practical implementation of:

- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Embeddings
- Whisper Speech Recognition
- LangChain
- Prompt Engineering
- Semantic Search
- Streamlit Application Development
- AI Pipeline Design

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Samuel Raj G**

AI & Machine Learning Engineer

GitHub: https://github.com/samuelrajgarikimukku

LinkedIn: https://www.linkedin.com/in/samuelrajgofficial
