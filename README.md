# djangotest
A test coding for UDN in Django:

Dec 18, 2017: New features include login and register pages, access to the list of participants requires authentication. User can register, then login to see the list page. 
I used forms on both pages/views (list view and data collection view), the form on list view only change the dropdown values/status, which is less vulnerable, so I did not use Django Form api. On the data collection page/view, yes, I did it with Django Form with clean_data and validations.
User start with the data collection form, after successful submission, user is redirected to the list view. On list view page, a dropdown menu is attached to each participant, and changing of the dropdown will save the field alongside the participant data.

I used Bootstrap/JQuery javascript library on the List View to make it look good on different devices. I added some simple unit tests following the TDD book. 
