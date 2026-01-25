from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt
from langchain_classic.chains import RetrievalQA

class AnimeRecommander:
    def __init__(self, retriever, api_key: str, model_name: str):
        self.llm = ChatGroq(api_key=api_key, model=model_name)
        self.prompt =get_anime_prompt()

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.prompt}
        )

        #new
        # combine_docs_chain = create_stuff_documents_chain(self.llm, self.prompt)
        #
        # self.qa_chain = create_retrieval_chain( retriever=retriever,
        #                                         combine_docs_chain=combine_docs_chain )

    def get_recommendation(self, query: str):
        result = self.qa_chain({"query": query})
        return result['result']