# Pet Adoption Application (Django version WIP)

Live version at https://adopt-a-pet.fly.dev/.

An application allowing the user to adopt animals (dogs and cats) from an Adoption Center.

Contains a Pet model (Django) to create a pet instance with attributes species, name, breed, age and gender.

Contains an AdoptionCenterFactory which provides:

- an adopt_animal() method allowing the user to adopt an animal of desired breed, age and gender;
- a get_lucky() method which gets a random lucky animal from the database for the adopter.

# Application Value
The app can be used by Animal Rescue centers, to match a person willing to adopt a pet with a suitable homeless pet.

# Design Patterns used:
- Pool (a database with pets available for adoption)
- Factory
- Observer (to be implemented, see TO DO 2)

# TO DO:
- TO DO 1: Add a mechanism to get input from the user (e.g. filling in a form with desired pet attributes to filter the results).
- TO DO 2: A user can subscribe to get a newsletter about the pets available for adoption (e.g. once weekly).
