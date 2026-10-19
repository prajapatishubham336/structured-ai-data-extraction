# structured-ai-data-extraction
A structured AI data extraction pipeline built with Python, LangChain, Groq, and Pydantic to transform unstructured text into schema-validated product information and JSON output.
# 🧩 Structured AI Data Extraction Pipeline

An AI-powered data extraction pipeline built with **Python, LangChain, Groq, and Pydantic**. This project transforms unstructured natural-language text into structured, schema-driven data that can be used by applications, APIs, databases, and data processing workflows.

The pipeline uses a language model with structured-output capabilities to identify product information, extract relevant attributes, and generate a concise summary in a predefined format.

---

## 🚀 Features

- **AI-Powered Information Extraction:** Extract product and item information from natural-language text.
- **Structured Output:** Organize extracted information using predefined Pydantic models.
- **Product Name Extraction:** Identify the names of products mentioned in the input.
- **Category Classification:** Assign categories to extracted items.
- **Price Extraction:** Extract numeric prices when available and support missing values.
- **Feature Extraction:** Collect product specifications and key features.
- **Text Summarization:** Generate a concise summary of the input text.
- **LangChain Pipeline:** Combine prompt templates and a language model into a reusable workflow.
- **JSON Serialization:** Export structured results as formatted JSON.
- **Reusable Design:** Organize extraction logic into a dedicated pipeline function.
- **Environment-Based Configuration:** Load the Groq API key from environment variables.
- **Deterministic Configuration:** Use a model temperature of `0.0` to reduce response variability.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| LangChain Core | Prompt templates and chain composition |
| LangChain Groq | Integration with Groq-hosted language models |
| Groq API | Language model inference |
| Pydantic | Data models, schemas, and output validation |
| python-dotenv | Environment variable management |
| JSON | Structured output serialization |
| Python typing | Type annotations and optional fields |

---

## 🧠 How It Works

The pipeline follows a structured extraction workflow:

1. Define a Pydantic schema describing the expected output.
2. Initialize the Groq language model through LangChain.
3. Configure structured output according to the predefined schema.
4. Create a prompt that instructs the model to extract relevant information.
5. Combine the prompt and model into a LangChain pipeline.
6. Provide the source text to the pipeline.
7. Receive the extracted information as a structured result.
8. Serialize the result into formatted JSON.

### Architecture

**Unstructured Text → Prompt Template → Groq Language Model → Structured Output Processing → Pydantic Schema → Structured Result and JSON**

---

## 📋 Output Schema

The project defines two Pydantic models.

### 1. ItemExtraction

Represents an individual product or item.

| Field | Type | Description |
|---|---|---|
| `item_name` | String | Name of the extracted product or item |
| `category` | String | Category assigned to the item |
| `price` | Optional Float | Numeric price, or null when unavailable |
| `features` | List of Strings | Key features and specifications |

### 2. ExtractionPipelineOutput

Represents the complete extraction result.

| Field | Type | Description |
|---|---|---|
| `items` | List of ItemExtraction | Extracted products and their attributes |
| `summary` | String | A concise summary of the input text |

This schema provides a consistent output structure instead of relying on unstructured, model-generated paragraphs.

---

## 📁 Project Structure

The repository is organized around the main extraction pipeline, dependency configuration, environment settings, and documentation.

- `main.py` — Main structured extraction pipeline.
- `requirements.txt` — Python dependencies.
- `.env` — Private Groq API key; should not be committed.
- `.gitignore` — Specifies files excluded from Git.
- `README.md` — Project documentation.

The filename `main.py` is suggested for the supplied script. If your Python file has a different name, retain the actual filename and adjust the run command accordingly.

---

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or newer recommended.
- A valid Groq API key.
- Internet access for API requests.
- Basic familiarity with Python and JSON.

### 1. Clone the Repository

Clone the GitHub repository to your local machine and navigate to the project directory.

```bash
git clone https://github.com/prajapatishubham336/structured-ai-data-extraction.git
cd structured-ai-data-extraction
```

### 2. Create a Virtual Environment

Create and activate a Python virtual environment to keep project dependencies isolated from other Python applications.

**Windows:** Use the `venv` module and activate the environment through the Windows command prompt or PowerShell.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:** Create the environment using Python and activate it from your terminal.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Install the following Python packages:

- `langchain-core`
- `langchain-groq`
- `pydantic`
- `python-dotenv`

Install them using your project's `requirements.txt` file.

### 4. Configure the Groq API Key

Create an API key through the [Groq Console](https://console.groq.com/).

Add the key to a `.env` file in the root directory using the environment variable name `GROQ_API_KEY`.

Replace any placeholder with your actual API key.

**Security:** Never commit your real `.env` file or expose your API key in a public repository.

### 5. Run the Pipeline

Run the main Python script from the terminal after activating the virtual environment and installing dependencies.

The program processes the included sample text and prints the structured result along with its JSON representation.

```bash
python main.py
```

---

## 💻 Example Input

The included sample describes two products:

- **Sony WH-1000XM5:** Wireless noise-canceling headphones priced at $399.99, featuring 30-hour battery life, multipoint connectivity, and hands-free calling.
- **Logitech MX Master 3S:** Wireless mouse priced at $99.99, featuring an 8000 DPI optical sensor and quiet clicks.

---

## 📤 Example Structured Output

The expected result contains a collection of extracted products and a summary.

Each product includes its name, category, price, and list of features. The summary briefly describes the products and their key attributes.

For the sample input, the extracted records would represent the Sony WH-1000XM5 and Logitech MX Master 3S, with their respective prices and specifications.

This is an illustrative description of the intended output. Actual categories, wording, and extracted features may vary depending on the model response.

---

## 🔑 Environment Variables

| Variable | Required | Description |
|---|---|---|
| `GROQ_API_KEY` | Yes | API key used to authenticate with Groq |

The model `openai/gpt-oss-120b` is specified directly in the project code. Ensure that the model is available to your Groq account and supports the structured-output configuration used by your installed integration.

---

## 🎯 Use Cases

This project demonstrates techniques that can be applied to:

- Product catalog data extraction.
- E-commerce product information processing.
- Converting natural-language descriptions into structured records.
- Extracting prices and specifications from product descriptions.
- Preparing data for databases and APIs.
- Information extraction from reports and documents.
- Building downstream automation workflows.
- Creating structured outputs for data analysis and AI applications.

These are potential applications of the extraction approach. The supplied example specifically processes product information from text.

---

## ⚠️ Current Limitations

- The example processes a predefined text string rather than reading files or accepting interactive input.
- The schema focuses on product and item information.
- Category assignment is model-generated and may require domain-specific validation.
- Missing prices are represented as nullable values, but no explicit custom business validation is implemented.
- The pipeline does not persist extracted records to a database.
- The current example does not include automated tests or a dedicated user interface.
- Model availability and structured-output support depend on the configured Groq service and installed integration versions.
- Structured output does not guarantee that extracted information is factually correct.

---

## 🚧 Future Enhancements

Possible future improvements include:

- Accept text from PDF, DOCX, CSV, and TXT files.
- Add a Streamlit user interface.
- Support configurable extraction schemas.
- Add batch processing for multiple documents.
- Save results to JSON, CSV, or a database.
- Implement validation rules for prices and product categories.
- Add confidence checks and source-text references.
- Create REST API endpoints with FastAPI.
- Add automated unit and integration tests.
- Support retries, structured logging, and improved error handling.
- Containerize the application using Docker.

These are proposed enhancements and are not included in the current implementation.

---

## 🔒 Security Best Practices

- Keep API credentials in environment variables.
- Exclude `.env` and other secret files from Git.
- Validate extracted information before using it in business-critical systems.
- Treat model-generated data as untrusted until verified.
- Avoid logging sensitive source text or credentials unnecessarily.
- Pin dependency versions for reproducible deployments.

Ensure your `.gitignore` excludes environment files, virtual environments, Python cache files, and other unnecessary local artifacts. An `.env.example` file containing placeholder values can be included to document the required configuration without exposing secrets.

---

## 🤝 Contributing

Contributions, improvements, and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Test the extraction pipeline.
5. Submit a pull request with a clear description.

Please do not include API keys or private data in commits.

---

## 📄 License

No license is currently specified. Add a `LICENSE` file if you intend to define permissions for reuse, modification, and distribution.

---

## 👨‍💻 Author

**Shubham Prajapati**

AI/ML Engineer | Machine Learning | Generative AI

GitHub: [@prajapatishubham336](https://github.com/prajapatishubham336)

---

## ⭐ Support

If you find this project useful for learning about LangChain, Pydantic, structured LLM outputs, and AI-powered data extraction, consider starring the repository on GitHub.

**Turn unstructured text into structured intelligence.**
