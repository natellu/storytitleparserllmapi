# Story Title Extractor

Python server that asks Ollama to find story title + chapter number from Reddit post titles.

## How to run:

1. Install requirements `pip install -r requirements.txt`
2. Install Ollama
3. pull a llm `ollama pull mistral:7b-instruct`
4. Start the server `uvicorn title_parser:app --host 0.0.0.0 --port 8000`
5. Send a post request to `http://localhost:8000/parse_title` with a body like `{"title": "Villains Don't Date Heroes! 68: Emergency Protocol"}`
6. Should return `{"story_title": "Villains Don't Date Heroes!", "chapter_number": 68}`
