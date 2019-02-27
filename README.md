# Pet Adoption Application (Django version WIP)

An application allowing the user to adopt animals (dogs and cats) from an Adoption Center.

Contains the generic class Animal, and the more specific Dog and Cat classes, inheriting from Animal.

Contains an AdoptionCenterFactory which provides:

- a Pool of available animals for adoption;
- an adopt_animal() method allowing the user to adopt an animal of desired breed, age and gender;
- a get_lucky() method which gets a random lucky animal from the Pool for the adopter.

# Application Value
The app can be used by Animal Rescue centers, to match a person willing to adopt a pet with a suitable homeless pet.

# Design Patterns used:
- Pool
- Factory
- Observer (to be implemented, see TODO 3)

# TO DO:
- TO DO: Get the available animals for adoption from a database (e.g. SQLite).
- TO DO 2: Add a mechanism to get input from the user (e.g. filling in a form).
- TO DO 3: The user can subscribe to changes in the Pool so that he/she is contacted whenever a suitable animal is added to the database.
