from fastapi import FastAPI
from pydantic import BaseModel
import ollama

app = FastAPI()

class TitleRequest(BaseModel):
    title: str

@app.post("/parse_title")
async def parse_title(req: TitleRequest):
    prompt = f"""
You are a title parser for Reddit posts. Your task is to extract the story title and the chapter number from post titles like this:

Examples:
1. "The Distinguished Mr. Rose - Chapter 40" → {{"story_title": "The Distinguished Mr. Rose", "chapter_number": 40}}
2. "Villains Don't Date Heroes! 68: Emergency Protocol" → {{"story_title": "Villains Don't Date Heroes!", "chapter_number": 68}}
3. "[Zombie Life Survival | 6. Identity]" → {{"story_title": "Zombie Life Survival", "chapter_number": 6}}
4. "The Soul Cog (3/3)" → {{"story_title": "The Soul Cog", "chapter_number": 3}}
5. "A Violent Utopia" → {{"story_title": "A Violent Utopia", "chapter_number": 1}}
6. "Humans don't discriminate even against deathwolders | Part 3" → {{"story_title": "Humans don't discriminate even against deathwolders", "chapter_number": 3}}

Always respond in this exact JSON format:
{{"story_title": "Title here", "chapter_number": NumberHere}}

Now parse this title:
\"{req.title}\"
    """
    
    response = ollama.chat(
        model="mistral:7b-instruct", 
        messages=[{"role": "user", "content": prompt}]
    )
    
    content = response['message']['content']
    try:
        parsed = eval(content)  #llm not always outputting valid json
    except Exception:
        parsed = {"error": "no valid title found"}
    return parsed
