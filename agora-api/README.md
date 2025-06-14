# Agora API

This is the backend API for the Agora project.

## Environmental Variables

The Agora API currently requires the following environmental variable for configuration. These variables can be set directly in your environment or loaded from a `.env` file in the project root directory.

### Required Variables

*   `SQLALCHEMY_DATABASE_URL`: The database connection URL. For example, `sqlite:///./sql_app.db` for a SQLite database.
*   `LLM_CLIENT_DEFAULT_MODEL`: Specifies the default LLM model to use if not explicitly provided in a request. Example: `google-gemini:gemini-2.0-flash`.
*   `LLM_CLIENT_GOOGLE_GEMINI_API_KEY`: Your API key for accessing the Google Gemini LLM. This is required if you are using the `google-gemini` provider.

## Viewing the Documentation

Once the API is running, you can view the interactive API documentation by navigating to the `/docs` endpoint in your web browser. For example, if your API is running locally on port 8000, you would visit `http://localhost:8000/docs`.
