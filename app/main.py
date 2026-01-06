from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from app.rag import chat

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body>
            <h2>Azure RAG Demo (gpt-4o-mini)</h2>
            <form method="post">
                <textarea name="question" rows="6" cols="60"></textarea><br><br>
                <input type="submit" value="Ask"/>
            </form>
        </body>
    </html>
    """

@app.post("/", response_class=HTMLResponse)
def ask(question: str = Form(...)):
    answer = chat(question, "This is test RAG context.")
    return f"""
    <html>
        <body>
            <p><b>Answer:</b></p>
            <pre>{answer}</pre>
            <a href="/">Ask another</a>
        </body>
    </html>
    """
