# Elements Wellpass Registration Automation

Element Fitness would like you to register for a slot at their gym a day in advance to be able to train if you have a Wellpass. This is annoying and easy to forget. This script is designed to automate that so you can always stick to your routine.

This script works standalone but you dont need to configure a server to run it daily. The Github Actions pipeline is used to run this script serverless.
Just fork this repo and set the secrets/variable. The github actions are configured to run every day at 11 o'clock silently. If something goes wrong than the Error message is passed to you as E-Mail.
But if they dont changes something on their page, than this script should run without a problem.



To set environment secrets/variable in GitHub, follow these steps:

1. Navigate to the GitHub repository where you want to set the environment secrets.
2. Click on the "Settings" tab located in the repository's navigation menu.
3. In the left sidebar, click on "secrets and variables", than on "Actions"
4. Click on the "New repository secret" button.
5. Create a Secret for "ELEMENTS_EMAIL" and "ELEMENTS_PASSWORD" with this names and the value.
6. Go to the Variables Tab and create a Variable for "ELEMENTS_STUDIO_ID" and set your Studio ID with the correct number from the List below 


| key | Value | Type |
| --- | --- | --- |
|ELEMENTS_STUDIO_ID| 62 ( See List below) | variable |
|ELEMENTS_EMAIL | mail@example.com | secert |
|ELEMENTS_PASSWORD | yourElementsPasswot | secret |

| Studio | ID | 
| --- | --- |
| Balanstraße | 65 | 
| Donnersbergerbrücke | 64 | 
| Eschborn | 60 | 
| Eschenheimer Turm | 61 | 
| Henninger Turm | 62 | 
| Paulinenbrücke | 66 | 
| Siemensallee | 63 | 
