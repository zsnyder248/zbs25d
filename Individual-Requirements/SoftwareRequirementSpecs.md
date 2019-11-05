# Software Requirements Specifications

## Introduction
### Purpose
##### This document is intended to fully specify the requirements and detail the software architecture of the front end web design of Augur. This will describe the behavior of the web page as well as system requirements, design constraints, and inner workings of the page.

### Scope
##### This web page will be used for anyone to view the health of their projects. 


## Software product overview
##### This web page is intended to get information from Augur APIs and display the information on a web page. It will be available to everyone. The web page will display repo groups and repo group information based on the input of the user. Also, the web page will display all information in an organized way.


## System Use
### Actor Survey
#### Employee
##### The employees or software engineers are responsible for including more and more endpoints, so users can see any information they could possibly want.

#### User
##### The user would be the one that views all information by interacting with the interface.


## System Requirements
### Use Cases
#### Use Case Repos
    1. User selects a repo group
    2. The software calls the API based off the repo group selected
    3. The web page displays all repos and repos information that is within that repo group
#### Use Case Contributors
    1. User selects a repo group
    2. The software calls the API based off the repo group selected
    3. The web page displays contributors and their information that have contributed to that repo group

### System functional specification
##### The system is a web application that will use a server. The data will be pulled through the server. There will be a home page to display all repo groups that are apart of Augur. Based on user input, the application will go to a different page to display the relevant data.

### Non-functional requirements
#### Usability
    1. The web page will be user friendly and simple to use
    2. Users can use this web application on any device
#### Reliabilty
    1. The application will always be available
    2. The only bug could come from the API being down
#### Performance
    1. There would be great performance for most of the application
    2. Repsonse time could be slow depending on the amount of data being retrieved by calling the API


## Design Constraints
### Web technology
    1. HTML
    2. CSS
    3. Javascript
### Server backend technology
    1. Ruby on Rails
    2. PHP
### Augur API endpoints
### A web server
    1. Amazon AWS

## Purchased Components
##### A server for the web application. Users can go to the website and use all information. 

## Interfaces
##### The web application interface will be created using HTML, CSS, and Javascript. It will be hosted on a server. The interface will be able to be accessed by any user via the web