from langchain.agents import tool
from tools import query_gemma

@tool
def ask_mental_health_specialist(query: str) -> str:
    """
    Generate a therapeutic response using the MedGemma model.
    Use this for all general user queries, mental health questions, 
    emotional concerns or to offer empathetic or practical guidance in a
    conversational tone.
    """
    return query_gemma(query)

