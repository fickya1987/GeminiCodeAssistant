### SQL, Python, and JavaScript Assistant

#### Overview
This Streamlit application utilizes Google's Gemini model to convert English text into SQL queries, Python code snippets, and JavaScript code. It serves as a handy tool for developers and data analysts looking to quickly generate code from natural language prompts.

#### Features
- **Multi-Language Support**: Supports conversion to SQL, Python, and JavaScript based on user input.
- **Interactive Interface**: User-friendly interface with text areas for input and buttons for conversion.
- **Database Integration**: Ability to execute generated SQL queries on an SQLite database and display results.

#### Installation
1. Clone the repository:
   ```
   git clone <repository_url>
   cd <repository_name>
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

#### Dependencies
- Streamlit
- pandas
- sqlite3
- google-generativeai
- dotenv

### Screenshots:

![Screenshot 2024-07-03 181616](https://github.com/Tanzila-Ikhlaq/GeminiCodeAssistant/assets/141930681/abcc656e-4bba-4be0-9531-c92baed16d33)

![Screenshot 2024-07-03 183528](https://github.com/Tanzila-Ikhlaq/GeminiCodeAssistant/assets/141930681/33492881-1212-4051-ab5c-cc4d65603168)

![Screenshot 2024-07-03 182456](https://github.com/Tanzila-Ikhlaq/GeminiCodeAssistant/assets/141930681/e9eafcbe-6454-4e72-9377-18f52cdb6b1a)





