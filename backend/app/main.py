from fastapi import FastAPI

app=FastAPI(
  title="AI Test Management Platform",
  description="Test management & execution platform",
version="0.1.0"
)

@app.get('/')
def root():
    return {
        "message" : "Welcome to the AI Test Management Platform"
    }