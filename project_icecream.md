# FILEPATH

"""
Description of the code or function.

Author: [Author Name]
Date: [Date]
Version: [Version Number]
"""

# Your code goes here
# Ice Cream Order App

## Overview

This is a basic iOS app developed in Swift that allows users to order vanilla or chocolate ice cream and checkout using Apple Pay. The app follows the Model-View-Controller (MVC) design pattern and utilizes Apple Pay API for secure and seamless payment processing.

## Requirements

- iOS 13.0 or later
- Xcode 11.0 or later
- Apple Developer Account (for Apple Pay setup)

## Project Setup

1. Open Xcode and create a new project.
2. Choose the "Single View App" template.
3. Provide a name for your app and select Swift as the language.
4. Choose a location to save your project and click "Create".
5. Continue with the default settings on the project configuration screen.

## Project Structure

The project follows the standard MVC design pattern. Here's an overview of the major components:

- `Main.storyboard`: Interface Builder file containing the app's user interface.
- `ViewController.swift`: View controller responsible for handling user interactions and managing UI elements.
- `IceCream.swift`: Model class representing an ice cream order.
- `IceCreamOrderManager.swift`: A singleton class responsible for managing the ice cream order process.
- `PaymentManager.swift`:

