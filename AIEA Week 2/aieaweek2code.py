from openai import OpenAI
from pyswip import Prolog

# Initialize OpenAI client with API key
client = OpenAI(api_key="my_actual_api")

def fetch_prolog_code(prompt):
    """
    Uses OpenAI API to generate Prolog code based on the given prompt.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a Prolog expert. Provide only valid Prolog code, no extra explanations."},
            {"role": "user", "content": prompt},
        ],
    )
    
    # Extract the response and clean unnecessary formatting
    code = response.choices[0].message.content.strip()
    return code.replace("```prolog", "").replace("```", "").strip()

def format_prolog_statements(prolog_code):
    """
    Reformats Prolog code to ensure statements are properly grouped and complete.
    """
    statements, temp = [], []
    
    for line in prolog_code.split("\n"):
        line = line.strip()
        if not line or line.startswith("%"):
            continue
        
        temp.append(line)
        
        if line.endswith('.'):
            statements.append(" ".join(temp))
            temp = []
    
    return statements

def execute_prolog_code(prolog_code, query):
    """
    Loads and executes Prolog code, then runs a query against it.
    """
    prolog = Prolog()
    statements = format_prolog_statements(prolog_code)
    
    try:
        for stmt in statements:
            prolog.assertz(stmt.rstrip('.'))  # Load facts and rules
        return list(prolog.query(query))  # Execute the query
    except Exception as error:
        raise Exception(f"Prolog execution failed: {error}")

def run_baseline_test():
    """
    Generates Prolog code for parent-child relationships and a grandparent rule,
    then queries the code.
    """
    prompt = "Define parent-child relationships and a rule for grandparent in Prolog."
    generated_code = fetch_prolog_code(prompt)
    print("Generated Prolog Code:\n", generated_code)
    
    test_query = "grandparent(jane, X)."
    
    try:
        results = execute_prolog_code(generated_code, test_query)
        print("Query Results:", results)
    except Exception as error:
        print(f"Error during Prolog execution: {error}")

if __name__ == "__main__":
    run_baseline_test()