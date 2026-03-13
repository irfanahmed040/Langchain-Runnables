from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

parser = StrOutputParser()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template="generate a small twitter post for {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="generate a small linkedin post for {topic}",
    input_variables=['topic']
)

parallel_chain = RunnableParallel({
    'twitter': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({'topic':'AI'})

print(result)

print("Twitter: " , result['twitter'], "\n")

print("linkedin: ",result['linkedin'])