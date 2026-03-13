#  LangChain Runnables — Practical Examples (LangChain 1.x)

This repository contains hands-on examples of **LangChain Runnables** using the modern LangChain 1.x API.
The goal of this repo is to understand how chains actually work internally by building them step-by-step using:

* RunnableSequence
* RunnableParallel
* RunnablePassthrough
* RunnableLambda
* RunnableBranch

Instead of using old `langchain.chains`, this project uses the **new Runnable API + LCEL**, which is the recommended way in LangChain 1.x.

This repo is perfect for learning how to build **real LLM pipelines**.

---

## ⚙️ Requirements

Install dependencies:

pip install langchain langchain-core langchain-openai python-dotenv

Create `.env` file:

OPENAI_API_KEY=your_api_key_here

---

## 📁 Files in this repo

This repo contains examples of all major Runnable types.

---

## 🔹 runnablesequence.py

Demonstrates **RunnableSequence**, the most basic building block.

Flow:

topic → joke → explanation → output

Chain:

prompt → model → parser → prompt → model → parser

This shows how multiple steps can be connected in a pipeline.

Used concepts:

* RunnableSequence
* PromptTemplate
* StrOutputParser
* Multi-step chaining

---

## 🔹 runnableparallel.py

Demonstrates **RunnableParallel**, where multiple tasks run at the same time.

Flow:

topic → twitter post + linkedin post

Both prompts run simultaneously and return a dictionary.

Used concepts:

* RunnableParallel
* Multiple prompts
* Parallel execution
* Dictionary output

Example output:

{
twitter: "...",
linkedin: "..."
}

---

## 🔹 runnablepassthrough.py

Demonstrates **RunnablePassthrough**, which forwards the input without changing it.

Flow:

topic → joke → explanation of joke

We keep the joke unchanged while also generating explanation.

Used concepts:

* RunnablePassthrough
* RunnableParallel
* RunnableSequence
* Passing data between steps

This is useful when one output needs to be reused.

---

## 🔹 runnablelambda.py

Demonstrates **RunnableLambda**, which allows custom Python logic inside a chain.

Flow:

topic → joke → word count

We generate a joke and then calculate the number of words using Python.

Used concepts:

* RunnableLambda
* Custom functions inside chains
* Parallel execution
* Data transformation

Example output:

Joke text
Word Count – 9

RunnableLambda is very powerful because it lets you mix LLM + Python logic.

---

## 🔹 runnablebranch.py

Demonstrates **RunnableBranch**, which allows conditional execution.

Flow:

topic → report → check length → summary (if long)

If the report is longer than 300 words → summarize
Otherwise → return original text

Used concepts:

* RunnableBranch
* Conditional logic
* RunnablePassthrough
* RunnableSequence

This is useful when you want LLMs to behave differently based on the result.

Example use cases:

* summarize only if long
* translate only if needed
* classify then route
* validation pipelines

---

##  What you learn from this repo

This repo helps understand:

✔ How LangChain really works internally
✔ How LCEL pipelines are built
✔ How to combine multiple prompts
✔ How to run tasks in parallel
✔ How to add Python logic inside chains
✔ How to create conditional flows
✔ How to reuse outputs between steps

These are the core concepts behind:

* AI agents
* RAG pipelines
* automation workflows
* multi-step LLM apps

---

##  Why Runnables are important

LangChain 1.x is built around Runnables.

Old style:

langchain.chains

New style:

prompt | model | parser

or

RunnableSequence
RunnableParallel
RunnableBranch

Understanding Runnables means you understand modern LangChain.

---

## 📊 Recommended order to read files

1. runnablesequence.py
2. runnableparallel.py
3. runnablepassthrough.py
4. runnablelambda.py
5. runnablebranch.py

Follow this order to understand everything step-by-step.

---

##  Author

Irfan Mohammed

