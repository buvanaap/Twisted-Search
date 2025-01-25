import os
import google.generativeai as genai

# Configure API key from environment variable
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key is missing. Please set the GEMINI_API_KEY environment variable.")

# Configure the Google Generative AI client
genai.configure(api_key=api_key)

# Define the model and configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
)

# Start a chat session
chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                "Create a web app called Opossum Search.\n1. Every time you make a search query, it should redirect you to a Google search with the same query, but with the word \"opossum\" added to it.\n2. It should be visually similar to Google search.\n3. Instead of the google logo, it should have a picture of this opossum: https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Opossum_2.jpg/292px-Opossum_2.jpg\n4. It should be a single HTML file, with no separate JS or CSS files.\n5. It should say Powered by opossum search in the footer.\n6. Do not use any unicode characters.",
            ],
        },
        {
            "role": "model",
            "parts": [
                "Okay, here's the HTML file for your \"Opossum Search\" web app, meeting all your specifications:\n\n```html\n<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Opossum Search</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            display: flex;\n            flex-direction: column;\n            align-items: center;\n            margin: 0;\n            padding-top: 100px;\n            min-height: 100vh;\n        }\n        .logo-container {\n            margin-bottom: 20px;\n        }\n        .logo {\n            max-width: 150px;\n        }\n        .search-form {\n            display: flex;\n            border: 1px solid #dfe1e5;\n            border-radius: 24px;\n            padding: 10px 15px;\n            margin-bottom: 20px;\n        }\n        .search-form:hover {\n          box-shadow: 0 1px 6px 0 #20212447;\n        }\n        .search-input {\n            border: none;\n            outline: none;\n            font-size: 16px;\n            flex-grow: 1;\n            margin-left: 5px;\n        }\n        .search-button {\n          border: none;\n          background-color: #f8f9fa;\n          color: #3c4043;\n          font-size: 14px;\n          margin-left: 5px;\n          border-radius: 4px;\n          padding: 5px 15px;\n          cursor: pointer;\n          height: 36px;\n        }\n         .search-button:hover{\n           border: 1px solid #dfe1e5;\n         }\n        .footer {\n            margin-top: auto;\n            padding: 20px;\n            text-align: center;\n            color: #5f6368;\n        }\n    </style>\n</head>\n<body>\n    <div class=\"logo-container\">\n        <img class=\"logo\" src=\"https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Opossum_2.jpg/292px-Opossum_2.jpg\" alt=\"Opossum Logo\">\n    </div>\n    <form class=\"search-form\" action=\"https://www.google.com/search\" method=\"get\">\n      <input type=\"text\" class=\"search-input\" name=\"q\" placeholder=\"Search...\" required>\n      <input type=\"hidden\" name=\"q\" id=\"opossum-query\" value=\"\">\n      <button class=\"search-button\" type=\"submit\">Opossum Search</button>\n    </form>\n    <div class=\"footer\">\n        Powered by opossum search\n    </div>\n\n    <script>\n      document.querySelector(\".search-form\").addEventListener(\"submit\", function(event) {\n        let search_value = document.querySelector(\".search-input\").value;\n        document.getElementById(\"opossum-query\").value = search_value + \" opossum\";\n      });\n    </script>\n</body>\n</html>\n```\n\n**Explanation:**\n\n1. **HTML Structure:**\n    *   The basic HTML structure is set up, including `<head>` and `<body>`.\n    *   The logo is an `<img>` tag with the provided URL, wrapped in a `div` container to control spacing.\n    *   The search input is inside a `<form>` tag, which is set up to submit a `GET` request to Google.\n    *   The footer has the \"Powered by opossum search\" text.\n    *   A hidden input tag is added to the form to pass the search query with \"opossum\" appended to it\n\n2. **CSS Styling (within `<style>`):**\n    *   The CSS is in the same HTML file as requested\n    *   Basic styling to make it look like Google Search:\n        *   Font is set to Arial.\n        *   Layout is set up using flexbox to center everything and align content at the bottom.\n        *   The search box has a rounded border and hover effect, similar to Google.\n        *   The footer is styled for placement at the bottom.\n        *   The logo image has a max-width to keep it a reasonable size.\n\n3. **Javascript:**\n   * The javascript listens to the \"submit\" event on the form.\n   * Once the form is submitted it retrieves the search query and appends \" opossum\" to it.\n   * It then sets the value of the hidden input to the new search query.\n   * When the form is submitted it will include the hidden input with the new search query in the request and redirect the user to google search with the original search query appended with \" opossum\"\n\n**How to Use:**\n\n1.  Save the code above as an HTML file (e.g., `opossum_search.html`).\n2.  Open the HTML file in your web browser.\n3.  Type a search query into the input field and hit the \"Opossum Search\" button. You'll be redirected to Google with the query with \"opossum\" appended.\n\nThis setup ensures you have a single, self-contained HTML file that fulfills all your requirements for the \"Opossum Search\" web app.\n",
            ],
        },
    ]
)

# Example of sending a message (this can be adjusted depending on your application)
response = chat_session.send_message("Create a Web App")

# Print the response from the model (just to demonstrate that it's working)
print(response.text)
