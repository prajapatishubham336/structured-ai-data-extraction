import os
from typing import List, Optional
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

# Define the desired output structure using Pydantic
class ItemExtraction(BaseModel):
    item_name: str = Field(description="The name of the product or item extracted.")
    category: str = Field(description="The category the item belongs to (e.g., Electronics, Apparel, etc.).")
    price: Optional[float] = Field(description="The price of the item if mentioned, otherwise null.")
    features: List[str] = Field(description="A list of key features or specifications mentioned.")

class ExtractionPipelineOutput(BaseModel):
    items: List[ItemExtraction] = Field(description="List of all items extracted from the text.")
    summary: str = Field(description="A brief one-sentence summary of the extracted text.")

def create_extraction_pipeline():
    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.0,
        groq_api_key=os.environ.get("GROQ_API_KEY")
    )

    structured_llm = llm.with_structured_output(ExtractionPipelineOutput)

    # Prompt Template
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are an expert data extraction assistant. Extract structured information "
            "from the provided text strictly adhering to the requested schema."
        ),
        (
            "human",
            "Extract all product or item information from the following text:\n\n{input_text}"
        )
    ])

    chain = prompt | structured_llm
    return chain

if __name__ == "__main__":
    pipeline = create_extraction_pipeline()

    sample_text = (
        "Yesterday, I bought a Sony WH-1000XM5 wireless noise-canceling headphone for $399.99. "
        "It features 30-hour battery life, multipoint connection, and crystal-clear hands-free calling. "
        "I also picked up a Logitech MX Master 3S wireless mouse priced at $99.99, which has an "
        "8000 DPI optical sensor and quiet clicks."
    )

    print("Running extraction pipeline...")
    
    result = pipeline.invoke({"input_text": sample_text})

    print("\n--- Extracted Structured Output ---")
    print(result)

    print("\n--- JSON String ---")
    print(result.model_dump_json(indent=2))