

```markdown
# Twisted Search

Twisted Search is a web app that redirects your search query to Google with the word "opossum" appended. The app is built using a custom prompt from Google AI Studio and uses Docker to run the code locally.

## Getting Started

### 1. Select the Prompt and Get the Code

1. **Sign In to Google AI Studio:**
   Go to [Google AI Studio](https://aistudio.google.com/) and sign in.

2. **Select the "Twisted Search" Prompt:**
   After signing in, select the **"Twisted Search"** prompt. This will take you to the prompt window where the AI model runs and generates the results.

3. **Get the Code:**
   On the right side of the window, click on the **`<> Get Code`** button. This will provide you with the code for the selected prompt. You can either copy or download the code to use locally.

4. **Get the API Key:**
   In the left corner of the window, click **"Get API Key"** to get your **GEMINI_API_KEY**. This API key enhances the functionality of the Google AI model.

### 2. Setting Up Docker Desktop

1. **Download Docker Desktop:**
   Download Docker Desktop from the official site: [Docker](https://www.docker.com).

2. **Sign In to Docker:**
   Open Docker Desktop and sign in with your Docker account.

3. **Complete the Docker Walkthrough:**
   Docker provides an introductory walkthrough to help you understand how Docker works. This includes examples, such as using the "welcome_to_docker" demo, which shows you how to create a Dockerfile and run a container.

### 3. Instructions to Run Docker Locally

After setting up Docker Desktop, follow these steps to build and run the container for the **Twisted Search** app:

1. **Build the Docker Image:**
   In your terminal, navigate to your project directory and run the following command to build the Docker image:
   ```bash
   docker build -t twisted-search .
   ```
   - `build`: The command to build the Dockerfile.
   - `-t twisted-search`: The tag (name) for the Docker image.
   - `.`: The current directory as the build context.

2. **Run the Docker Container:**
   Once the Docker image is built, run the following command to start the container:
   ```bash
   docker run --name twisted-search -d -p 5002:5000 -e GEMINI_API_KEY="YOUR_API_KEY" twisted-search
   ```
   - `run`: The command to run the built Docker container.
   - `-d`: Runs the container in detached mode (background).
   - `-p 5002:5000`: Maps port 5002 on the host to port 5000 inside the container.
   - `-e GEMINI_API_KEY="YOUR_API_KEY"`: Sets the environment variable for your GEMINI_API_KEY.
   - `twisted-search`: The name of the image to run.

3. **View Docker Images:**
   To check the details of the built Docker image, use the command:
   ```bash
   docker images
   ```

4. **Check Docker Container Status:**
   To view the running Docker containers, use:
   ```bash
   docker ps
   ```

5. **Remove Docker Image:**
   If you want to remove an image by its image ID, use the following command:
   ```bash
   docker rmi <imageid>
   ```

### 4. Running the Web App

After running the Docker container, you should be able to view the **Twisted Search** web app by opening the `code.html` file directly in your browser.

If you're serving the file from Docker, visit the following URL:
```
http://localhost:5002
```
Otherwise, simply open the **`code.html`** file on your local machine.

## Screenshots
![image alt]("C:\Users\bhuvana\Desktop\Screenshots\Screenshot (125).png")
