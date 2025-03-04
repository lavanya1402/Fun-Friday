from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # Ensure the root path ("/") is defined
def home():
    return {"message": " This Working. Hello, FastAPI! 🚀 Your app is live!. I am learning something.tes2"}

@app.get("/health")  # Optional health check endpoint
def health_check():
    return {"status": "healthy"}