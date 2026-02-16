# AccuKnox-user-management-tests

Assignment For QA Trainee
--------------------------

This repository contains automation scripts for the **OrangeHRM** Admin Module where we can add user, search user,validate user,edit user, delete user ,for Automation script i have used **Playwright with Python** and the **Page Object Model (POM)** design pattern is followed to maintain clean, reusable, and scalable test code..

#Project Setup

1.Clone the Repo

   git clone https://github.com/<your_username>/AccuKnox-user-management-tests.git
   
   cd AccuKnox-user-management-tests
   
2.Create a virtual environment:

   python -m venv venv
   
3.Activate the virtual environment:

   Windows:
   
   venv\Scripts\activate
   
   Linx/Macos:
   
   source venv/bin/activate
   
4.Install dependencies:

   pip install -r requirements.txt
   
   playwright install

5.How to Run the Test Cases

  Run  testCase:
  
   pytest   tests/test_login.py

6.Playwright Version Used

   playwright==1.58.0
   
  Pytest Version Used
  
   pytest-playwright==0.7.2
   
   


