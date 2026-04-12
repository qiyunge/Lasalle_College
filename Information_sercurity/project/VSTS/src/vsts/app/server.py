
import uvicorn

def main():
    uvicorn.run(
        "vsts.app.main_web:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )