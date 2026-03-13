from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

def word_count(text):
    return len(text.split())

model = ChatOpenAI()

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Generate a one line joke about {topic}",
    input_variables=['topic']
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain= RunnableParallel({
    'joke': RunnablePassthrough(),
    'Word Count':RunnableLambda(word_count)
})

# CLEANER METHOD (without using any pre created function)
# parallel_chain= RunnableParallel({
#     'joke': RunnablePassthrough(),
#     'Word Count':RunnableLambda(lambda x:len(x.split()))
# })

chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = chain.invoke({'topic':"Lionel Messi"})

final_result = """{} \nWord Count - {}""".format(result['joke'], result['Word Count']) 

print(final_result)