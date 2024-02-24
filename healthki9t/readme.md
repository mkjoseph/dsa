Problem Description

Building a mini app that leverages AppleHealth kit. Unsure of the current limitations when working with AppleHealthkit, and looking to build out a small app within a few phases. The first phase is just about capturing apple health data into a firebase db and permissions for a future version. From here, we will determine functionality and the next phase of the project.

User flow

Download and open app
Create account (apple sign-in)
Authentication - Send to firebase
Check for Apple Watch (https://forums.developer.apple.com/forums/thread/6021)
Pass or fail
If pass, collect Apple Watch Version in firebase
If fail, display alert
Create Profile
Capture name (new controller)
Capture username / @handle
Send to firebase
Connect Apple Health Data
Pass or fail
Pass data to firebase (5 specific metrics from Apple Health)
Connect Address Book
Capture and Store in Firebase
This will be used for future use
Connect Push Notifications
Capture and Store in Firebase
This will be used for future use
Controller view - Success message. "Check back soon"
The user must allow all steps in order to complete registration (to arrive at last steps)

To summarize, this app is about creating a user, ensuring they have an apple watch, then passing apple health data to a database.

Once you reach out, I can pass over a wireframe. This is less about perfect design, and more about basic functionality.

Swift
Firebase
Documented code, using GitHub

