# elements-wellpass-registration


Just fork this repo and set the secrets/variable. The github actions are configured to run every day at 11 o'clock.


To set environment secrets/variable in GitHub, follow these steps:

1. Navigate to the GitHub repository where you want to set the environment secrets.
2. Click on the "Settings" tab located in the repository's navigation menu.
3. In the left sidebar, click on "secrets and variables", than on "Actions"
4. Click on the "New repository secret" button.
5. Create a Secret for "ELEMENTS_EMAIL" and "ELMENTS_PASSWORD" with this names and the value.
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
| Siemensallee | 653 | 
