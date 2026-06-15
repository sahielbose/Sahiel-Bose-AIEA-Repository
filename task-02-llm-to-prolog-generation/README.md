# Task 2: LLM to Prolog Code Generation

## Objective

Establish a baseline neuro-symbolic pipeline in which a large language model
writes a logic program and a symbolic engine executes it. This task tests
whether an LLM can be used as the natural-language front end to a formal
reasoner rather than as the reasoner itself.

## What the script does

`generate_prolog.py` runs a four-stage pipeline:

1. **Prompting.** A natural-language instruction (for example, "Define
   parent-child relationships and a rule for grandparent in Prolog") is sent to
   the OpenAI Chat Completions API. A system message constrains the model to
   return only valid Prolog with no surrounding prose.
2. **Cleaning.** The raw completion is stripped of Markdown code fences and
   leading or trailing whitespace so that the text is ready to load.
3. **Parsing.** `format_prolog_statements` walks the generated text line by
   line, skips blank lines and comments, and groups tokens into complete
   clauses, each terminated by a period. This guards against multi-line clauses
   being asserted as fragments.
4. **Execution.** `execute_prolog_code` asserts each clause into a SWI-Prolog
   engine through pyswip and runs a test query, returning the bindings.

The driver `run_baseline_test` ties the stages together: it generates a family
knowledge base, prints it, then queries `grandparent(jane, X)` and reports the
results or any execution error.

## Key ideas

- Separation of concerns between language understanding (the LLM) and sound
  inference (Prolog).
- Defensive post-processing of model output, since generated code cannot be
  trusted to be syntactically clean.
- Error handling around assertion and query execution so that malformed
  generations fail loudly rather than silently.

## Running

```bash
export OPENAI_API_KEY="your-key"
python generate_prolog.py
```

The API key is read from the environment and is never stored in the source.

## Requirements

- Python 3.9 or newer
- `openai`
- `pyswip` and a local SWI-Prolog installation
