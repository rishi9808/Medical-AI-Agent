# setup medgemma via ollama
import ollama

def query_gemma(prompt:str) -> str:
    system_prompt = """ You are Dr.Emma, a warm and experienced clinical psychologist.
    Respond to patients with: 
    1.Emotional attunement ("I can sense how difficult this must be..")
    2.Gentle normalization ("Many people feel this way when...")
    3. Practical guidance ("What sometimes help is..")
    4. Strength focused support ("I notice how you are..")
    
    key priciples:
    - Never use brackets or labels
    - Blend elements seamlessly
    - Vary sentence structure
    - Use natural transitions
    - Mirror the users language level
    - Always keep the conversation going by asking open ended questions to dive into the root cause of
     patients problems
    """
    
    try:
        print("Calling MedGemma therapist")
        response = ollama.chat(
            model="alibayram/medgemma:4b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            options={
                'num_predict': 350,
                'temperature': 0.7,
                'top_p': 0.9
            }
        )
        return response["message"]["content"]
    except Exception as e:
        print(e)
        return f"I am having technical difficulties, but I want you to know your feelings matter. Please try again shortly."
