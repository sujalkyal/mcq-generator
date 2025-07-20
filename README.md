"# MCQ Generator

An intelligent Multiple Choice Question (MCQ) generator powered by OpenAI's GPT models and LangChain. This application automatically creates customized quiz questions from uploaded PDF or text documents with adjustable complexity levels.

## 🚀 Features

- **File Upload Support**: Upload PDF or TXT files as source material
- **Customizable Parameters**: 
  - Number of MCQs (3-20 questions)
  - Subject/Topic specification
  - Complexity level adjustment
- **AI-Powered Generation**: Uses OpenAI GPT models via LangChain for intelligent question creation
- **Automatic Review**: Built-in evaluation system to assess question quality and complexity
- **Interactive Web Interface**: Clean Streamlit-based UI for easy interaction
- **Cost Tracking**: Monitor OpenAI API usage and costs

## 🛠️ Technology Stack

- **Python 3.7+**
- **Streamlit** - Web application framework
- **LangChain** - LLM application development framework
- **OpenAI GPT** - Language model for question generation
- **PyPDF2** - PDF text extraction
- **Pandas** - Data manipulation and display

## 📋 Prerequisites

- Python 3.7 or higher
- OpenAI API key
- Internet connection for API calls

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sujalkyal/mcq-generator.git
   cd mcq-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Install the package (optional)**
   ```bash
   pip install -e .
   ```

## 🚀 Usage

### Running the Streamlit Application

```bash
streamlit run StreamlitAPP.py
```

The application will open in your default web browser at `http://localhost:8501`.

### Using the Web Interface

1. **Upload a file**: Choose a PDF or TXT file containing the source material
2. **Configure parameters**:
   - Set the number of MCQs (3-20)
   - Specify the subject/topic
   - Choose complexity level (e.g., "simple", "intermediate", "advanced")
3. **Generate MCQs**: Click "Create MCQs" to generate questions
4. **Review results**: View the generated questions in a table format along with an AI review

### Example Usage

```python
from src.mcqgenerator.mcq_gen import generate_evaluate_chain
from src.utils import read_file
import json

# Load response template
with open('Response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)

# Generate MCQs
response = generate_evaluate_chain({
    'text': "Your source text here",
    'number': 5,
    'subject': "Python Programming",
    'tone': "intermediate",
    'response_json': json.dumps(RESPONSE_JSON)
})

print("Generated Quiz:", response['quiz'])
print("AI Review:", response['review'])
```

## 📁 Project Structure

```
mcq-generator/
├── README.md
├── requirements.txt
├── setup.py
├── StreamlitAPP.py          # Main Streamlit application
├── Response.json            # MCQ response template
├── experiment/
│   ├── data.txt            # Sample data for testing
│   └── mcqgen.ipynb        # Jupyter notebook for experimentation
└── src/
    ├── __init__.py
    ├── logger.py           # Logging configuration
    ├── utils.py            # Utility functions
    └── mcqgenerator/
        ├── __init__.py
        └── mcq_gen.py      # Core MCQ generation logic
```

## 🔧 Configuration

### Response Format

The application uses a JSON template (`Response.json`) to structure the generated MCQs:

```json
{
    "1": {
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here"
        },
        "correct": "correct answer"
    }
}
```

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key for accessing GPT models

## 🧪 Development

### Running Experiments

Use the Jupyter notebook in the `experiment/` directory:

```bash
jupyter notebook experiment/mcqgen.ipynb
```

### Testing with Sample Data

Sample text data is available in `experiment/data.txt` for testing purposes.

## 📊 Features in Detail

### Intelligent Question Generation
- Uses advanced prompt engineering with LangChain
- Ensures questions are relevant to the source material
- Avoids duplicate questions
- Maintains specified complexity level

### Automatic Quality Review
- AI-powered evaluation of generated questions
- Complexity analysis and feedback
- Suggestions for improvement when needed

### Cost Monitoring
- Real-time tracking of OpenAI API usage
- Token count and cost estimation
- Helps manage API expenses

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Sujal Kyal**
- Email: sujalkyal2704@gmail.com
- GitHub: [@sujalkyal](https://github.com/sujalkyal)
- WebSite: [sujalkyal.dev.in](https://sujaldev-ten.vercel.app/)

## 🙏 Acknowledgments

- OpenAI for providing the GPT API
- LangChain community for the excellent framework
- Streamlit for the intuitive web framework

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the [Issues](https://github.com/sujalkyal/mcq-generator/issues) page
2. Create a new issue if your problem isn't already reported
3. Contact the author via email

## 🔮 Future Enhancements

- Support for more file formats (DOCX, HTML)
- Multiple language support
- Question difficulty scoring
- Export functionality (PDF, Excel)
- Integration with learning management systems
- Batch processing capabilities"