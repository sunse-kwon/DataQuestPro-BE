# 💡 DataQuestPro

## 🏃‍♂️ Execution

-   [Backend deploy link](http://15.164.56.233:80)
-   [Frontend deploy link](http://15.164.56.233:8000)
-   Test Account 🧪

    ```py
    # For email features, it's recommended to sign up with a real email.
    email: test@dqp.com
    password: test1
    ```

## 📝 Project Purpose and Key Features

-   DataQuestPro is a platform for users to create and participate in surveys. Key features include:
-   User registration, login, and profile management.
-   Survey creation, management, participation, and results viewing.
-   Email verification and notifications.

## 👥 Team Members

-   👨‍💻 Sunse Kwon - User feature development, User API specification, Deployment
-   👨‍💻 Hyunjoong Kim - User feature development, Frontend development
-   👨‍💻 Jooheon Song - Team lead, Notification feature development, Branch strategy planning
-   👨‍💻 Jinwoo Yang - User feature development, Frontend development
-   👨‍💻 Ikjun Choi - Survey feature backend/frontend development, Survey API specification, ERD design


## ⏳ Project Duration

-   August 17, 2023 - September 1, 2023 (approximately 2 weeks)

## 💻 Development Environment

-   **Front-end:**
    ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
    ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
    ![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

-   **Back-end:**
    ![Django REST framework](https://img.shields.io/badge/Django_REST_framework-092E20?style=for-the-badge&logo=django&logoColor=white)
    ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

-   **Deployment:**
    ![Nginx](https://img.shields.io/badge/Nginx-269539?style=for-the-badge&logo=nginx&logoColor=white)
    ![Uswgi](https://img.shields.io/badge/uwsgi-488A99?style=for-the-badge&logo=uwsgi&logoColor=white)
    ![AWS EC2](https://img.shields.io/badge/AWS_EC2-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)

-   **Testing:**
    ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

-   **Library**

    -   Python: 3.10.11
    -   PostgreSQL: 15.4

        ```js
        Django==4.2.4
        django-cors-headers==4.2.0
        django-filter==23.2
        djangorestframework==3.14.0
        djangorestframework-simplejwt==5.2.2
        drf-yasg==1.21.7
        psycopg2-binary==2.9.7
        PyYAML==6.0.1
        uWSGI==2.0.22
        ```

## 📊 ERD

![ERD Image](./README/ERD.png)

## Architecture

![dqp.drawio](./README/dqp.drawio.png)

## 📄 API Documentation

Swagger 📸

![API-1](./README/API-1.png)
![API-2](./README/API-2.png)

## 🎥 Implementations (GIFs)

### 🔑 Authentication

-   Initial Screen

![intro_to_login](./README/gifs/intro_to_login.gif)

-   Sign Up

![user_signup](./README/gifs/user_signup.gif)

-   Login Attempt, Failure

![login_fail](./README/gifs/login_fail.gif)

-   Verify Email

![user_emailcheck](./README/gifs/user_emailcheck.gif)

-   Login

![login](./README/gifs/login.gif)

-   Logout

![logout](./README/gifs/logout.gif)

### 📝 Surveys

-   Browse Surveys by Category

![survey_category](./README/gifs/survey_category.gif)

-   Create Survey

![survey_create](./README/gifs/survey_create.gif)

-   Edit Created Survey

![survey_update](./README/gifs/survey_update.gif)

-   Participate in Survey

![survey_submit](./README/gifs/survey_submit.gif)

-   View Survey Results

![survey_result](./README/gifs/survey_result.gif)

-   Edit Survey Answers

![survey_answer_update](./README/gifs/survey_answer_update.gif)

-   Re-respond to Survey

![survey_update_submit](./README/gifs/survey_update_submit.gif)

-   Delete Created Survey

![survey_delete](./README/gifs/survey_delete.gif)

-   Email Notification on Survey Creation

![survey_create_email](./README/gifs/survey_create_email.gif)

-   Email Notification on Survey Completion

![done_emailcheck](./README/gifs/done_emailcheck_2.gif)

### 👤 Profile

-   View Profile

![profile](./README/gifs/profile.gif)

-   Edit Profile

![profile](./README/gifs/profile-update.gif)

## 🛠️ Issues and Resolutions (Troubleshooting)

### 🚧 Issue #1

-   Issue #1: Frequent Data Modeling Changes

> Problem:
ERD and database design seemed complete, but changes were needed during development.

> Solution:
Held team meetings to write detailed function descriptions and revised the ERD based on these.



### 🚧 Issue #2

-   Issue #2: Inefficient Code Design

> Problem:
Implementing email notifications for survey results within the survey view caused redundancy and inefficiency.

> Solution:
Separated the notification feature using Django Signals to trigger actions on database updates.


### 🚧 Issue #3

-   Issue #3: Deployment Issues

> Problem:
Initial deployment with Gunicorn failed; issues arose when deploying both backend and frontend on the same server.

> Solution:
Separated the backend and frontend on different ports using Nginx server configuration.



### 🚧 Issue #4

-   Issue #4: Token Handling on Logout

> Problem:
Logout process with refresh token blacklisting did not invalidate access tokens.

> Solution:
Cleared tokens from local storage on successful refresh token blacklisting response.



## 🙌 Reflections

-   Sunse Kwon:
   > First experience with GitHub collaboration, handling branch strategies, and merging conflicts was challenging but rewarding.

-   Hyunjoong Kim:

   > Gained confidence and motivation from the team's enthusiasm despite initial uncertainties about the project.

-   Jooheon Song:

   > Previous experience with GitHub helped in managing branches and conflicts; learning and growing with the team was valuable.

-   Jinwoo Yang:

   > team project involved more considerations and frequent meetings, but was rewarding thanks to the team's collaborative spirit.


-   Ikjun Choi:

   > Deciding on the project topic was more comprehensive with the team; enjoyed the collaborative process and learned a lot from handling errors in JS events.



## 👨‍🎓 Future Enhancements

-   Integrate ChatGPT to recommend questions based on the user's survey topic and objectives.
-   Implement statistical visualization (mean, median, min, max) for survey results.
-   Add comment functionality on the survey results page for user interactions.
-   Allow non-registered users to participate via link to increase accessibility.


## 📚 References

> Django Signals: https://docs.djangoproject.com/en/4.2/topics/signals/  
> Django SMTP, sending email: https://docs.djangoproject.com/en/4.2/topics/email/  
> DRF-simpleJWT: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/  
> DRF-yasg: https://drf-yasg.readthedocs.io/en/stable/
