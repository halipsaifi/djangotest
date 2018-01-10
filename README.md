# djangotest

A test coding in Django:

with the following:
1. Use Django Form API, see participants addData form
2. Normal forms handling with JQuery, see participants List page
3. base templates, header, footer and common static resources, see static and templates
4. build-in user register, no admin privileges, see register
5. build-in login/authentication existing users (no admin privileges), see Login
6. ROM, participants.models.Participant

branch ec-auth:

7. external authentication: HMS eCommons Authentication, see service and login
8. Django user API, see create new user after ec-authentication

User start with the data collection form, after successful submission, user is redirected to login (or register in master branch). After successful authentication, user is redirected to the list view. On list view page, a dropdown menu is attached to each participant, and changing of the dropdown will save the field alongside the participant data.
