# Land System

The Land System is a web application designed to address land ownership disputes by providing a platform for registering landowners and storing their title deeds securely. Additionally, it generates digital title deeds with QR codes that can be scanned to verify the real landowner, facilitating dispute resolution.

## Features

- **Landowner Registration:** Register landowners and store their information securely in the system.
  
- **Title Deed Management:** Manage title deeds associated with registered landowners, including storage and retrieval.

- **Digital Title Deed Generation:** Generate digital title deeds for registered landowners, each containing a QR code for easy verification.

- **QR Code Verification:** QR codes on digital title deeds can be scanned to verify the authenticity of the landowner, aiding in land dispute resolution.

## Technologies Used

- **Python:** Programming language used for backend development.
  
- **Django:** Python web framework used for developing the web application.
  
- **Flask:** Python micro web framework used for generating digital title deeds.
  
- **MySQL:** Relational database management system used for storing landowner and title deed information.

## Setup Instructions

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/Land_System.git
    ```

2. Install Python dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Set up MySQL database and configure database settings in `settings.py`.

4. Run migrations:
    ```
    python manage.py migrate
    ```

5. Start the Django development server:
    ```
    python manage.py runserver
    ```

6. Access the application at `http://localhost:8000`.

## Contributing

Contributions to the Land System project are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Commit your changes: `git commit -am 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.
## License
