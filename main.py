import os
from dotenv import load_dotenv
from google import genai


def main():
    #Loads API key
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    #Checks if API key was loaded
    if api_key == None:
        raise RuntimeError("unable to get api key")
    
    #Connects with gemini and prompts it
    client = genai.Client(api_key=api_key)
    content = client.models.generate_content(model="gemini-2.5-flash", contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")

    #Gets token usage
    if content.usage_metadata == None:
        raise RuntimeError("unable to connect to Gemini")
    prompt_token_usage = content.usage_metadata.prompt_token_count
    candidate_token_usage = content.usage_metadata.candidates_token_count

    print("User prompt: Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
    print(f"Prompt tokens: {prompt_token_usage}")
    print(f"Response tokens: {candidate_token_usage}")
    print("Response:")
    print(content.text)

    


if __name__ == "__main__":
    main()
