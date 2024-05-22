#### 1. Clone the Repository
First, you need to clone the repository to your local machine. This copies the project files from the remote repository to your computer.

< Put these lines in your terminal: 
git clone https://github.com/yourusername/yourproject.git
cd yourproject
>

## git clone <repository-url>: This command downloads the repository from the specified URL to your local machine.
## cd yourproject: Changes the current directory to the project directory you just cloned.

#### 2. Create and Activate a Virtual Environment
Creating a virtual environment ensures that dependencies are isolated from your global Python environment. This helps prevent conflicts between different projects.

< Put these lines in your terminal: 
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
>

## python -m venv env: This command creates a virtual environment named env in the project directory.
## source env/bin/activate: Activates the virtual environment on macOS/Linux.
## env\Scripts\activate: Activates the virtual environment on Windows.
## Once activated, your terminal prompt should change to indicate that you are now working within the virtual environment.

#### 3. Install Dependencies
Next, you need to install all the required packages and dependencies for the project. These are listed in the requirements.txt file.

< Put these lines in your terminal: 
pip install -r requirements.txt
>

### pip install -r requirements.txt: This command reads the requirements.txt file and installs all the packages listed there into the virtual environment.

#### 4. Apply Migrations and Start the Development Server
Django uses a database to store data. Migrations are used to create or update the database schema. After applying migrations, you can start the Django development server.

< Put these lines in your terminal: 
python manage.py migrate
python manage.py runserver
>

### python manage.py migrate: Applies any pending migrations to the database. This sets up the initial database schema or updates it based on changes in the models.
### python manage.py runserver: Starts the Django development server. You can now access the project in your web browser at http://127.0.0.1:8000/.

#### Summary
1. Clone the repository to get the project files.
2. Create and activate a virtual environment to manage dependencies.
3. Install the required dependencies listed in requirements.txt.
4. Apply database migrations and start the development server to run the project.
