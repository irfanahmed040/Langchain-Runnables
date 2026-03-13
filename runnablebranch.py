from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableBranch, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

parser = StrOutputParser()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template="Generate a detailed report about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate a summary of the following text\n{text}",
    input_variables=['text']
)

report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>300, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

chain = RunnableSequence(report_gen_chain, branch_chain)

print(chain.invoke({'topic':'Cristiano Ronaldo'}))