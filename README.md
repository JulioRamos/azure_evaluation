# Julio Ramos - Azure Playground
This project is a small Flask web application hosted on Azure. The application includes a guessing game where the user enters a number between 1 and 20 and the app tries to guess it. The app has a maximum of three attempts to guess the user's number.

The running application might be available [here](https://julio-ramos.azurewebsites.net/)

The Flask application contains the following files:

1. app.py - this file contains the Flask application code with two routes:
   - '/': This route is used to display the guessing game page.
   - '/restart': This route is used to restart the game.

2. cv.html - this file is an HTML template used for the guessing game page
   - It includes my personal information, the guessing game, and a restart button.


## Installation
1. Clone the repository using the following command:
```bash
git clone https://github.com/your-username/your-repo.git](https://github.com/JulioRamos/azure_evaluation.git
```

2. Install the required packages using the following command:
```bash
pip install -r requirements.txt
```

3. Run the Flask application using the following command:
```bash
python app.py
```
The application will be available at http://127.0.0.1:5000/.


## Deployment to Azure
To deploy the application to Azure, follow these steps:

1. Create an Azure account and login to the Azure Portal.
2. Create a new Web App in Azure.
3. Set up deployment options for the Web App by connecting it to your GitHub repository.
4. Configure the deployment settings to deploy the master branch automatically.
5. Open the Web App's Configuration settings and add a new application setting with the name WEBSITE_RUN_FROM_PACKAGE and value 1.
6. Save the configuration and wait for the deployment to complete.
7. Once the deployment is complete, navigate to the Web App's URL to view the application.


## Credits
This project was created by Julio Ramos. The Flask framework was used for the web application, and the application is hosted on Azure. The template for the web page was obtained from W3Schools.
