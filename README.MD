# Software Engineer, Portfolio

Portfolio of [Almaz Kunpeissov, Software Engineer](https://akun.dev). Python, Django.

This is Django applications for blogging, portfolio and some e-commerce. 

# To use
* copy the repo
    ```
    git clone https://github.com/akundev/akundotdev.git
    ```



* change `.env` variables:
    ```
    cd akundotdev
    cp .env.example .env
    ```

* install `pipenv` and dependencies, migrate db, collect static files:
    ```
    pip3 install pipenv
    pipenv install
    pipenv run python3 manage.py migrate
    pipenv run python3 manage.py collectstatic
    ```

* start dev server:
    ```
    make run
    ```

* start prod server:
    ```
    make prod
    ```