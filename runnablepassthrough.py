from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableSequence
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

parser = StrOutputParser()
model = ChatOpenAI()

prompt1 = PromptTemplate(
    template="Generate a one line joke about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate an explanation about the joke: {joke}",
    input_variables=["joke"]
)

# Joke generator
joke_gen_chain =RunnableSequence(prompt1, model, parser)

# Parallel execution
parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": RunnableSequence(prompt2 , model , parser)
})

# Final chain
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"topic": "Football"})

print(result)