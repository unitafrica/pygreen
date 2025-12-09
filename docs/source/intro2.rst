Python Fundamentals II: functions and classes
================================================================

What is a function?
===================

A **function** is a way to wrap up a piece of code that performs a
specific task. Functions let us:

- **reuse code** without rewriting it  
- make programs **easier to read**  
- structure larger scripts into **logical blocks**

A function usually takes some **inputs** (called *arguments*) and
produces an **output** (returned using the ``return`` keyword).

In everyday language:

    A *function* is a little machine: you give it input → it processes something → it gives you an output.

In programming, functions help us structure code as a **sequence of
meaningful steps**, each **responsible for one specific task**. Each
function does one job well, and the overall program is just the result
of these players working together, step by step.

If you find yourself repeating the same logic (calculations, data
transformations, formatting, checks etc.) it's a sign that the step
should become a function.

Python Built-in Functions
-------------------------

Python already comes with **many pre-defined functions** you can use
right away. They are **loaded automatically** every time you run Python,
so you don’t need to import anything.

Examples: ``print()``, ``len()``, ``type()``, etc.

Official documentation:

- https://docs.python.org/3/library/functions.html

Defining a new Python Function
-------------------------

In Python, we define a function using ``def``. A function has:

1. **Name** → what we call it  
2. **Parameters** → placeholders for the inputs  
3. **Body** → the block of code that does the work  
4. **Return value** → the output (optional)  
5. **Docstring** → description of what the function does (optional)

Image
-----

.. image:: https://drive.google.com/uc?export=view&id=1ufEOIclvmQFVp0Q5DFyYBeEpcwqYt0oF
   :alt: Python function
   :width: 600px
   :align: left

Function Definition vs Function Call
------------------------------------

When working with functions, it’s important to understand the difference
between:

- **Defining a function** → creating it: *“here is what this function does”*
- **Calling a function** → running it: *“now please do that task”*

When we define a function using ``def``, we are simply teaching Python a
new command. Nothing happens yet — Python just stores the function in
memory.

This is also where the **function’s local scope** is created: variables
inside the function exist only while the function runs and disappear
afterwards. This keeps your program clean and avoids name conflicts.

When we **call** the function, Python executes the code inside the body.
Each call runs the function’s logic, possibly with different arguments.

Separating definition and calls gives us:

- **modularity** → define once, use many times  
- **flexibility** → change the function in one place, all calls update automatically

.. code-block:: python

   # Defining your first Python function
   def greetings(name):
       """Print a personalized greeting."""
       print(f"Hello, {name}!")

   # Calling the greetings function
   greetings("Alessandro")
   greetings("Mauro")

Arguments and Parameters
-------------------------

When we call a function, we often need to give it information so it can
do its job. Python uses two key concepts:

- **Parameters** → the names written in the function *definition*
- **Arguments** → the values passed when *calling* the function

    Think of it like filling out a form: the form fields are parameters, the information you write in the fields are arguments.

Python supports **several types of arguments**, each designed to make
functions flexible and easy to use.

1. **Positional Arguments**  
   The *position* determines the meaning. Like filling out a form where
   the first blank must be “animal” and the second must be “name”.

2. **Keyword Arguments**  
   Provided *by name*, so order does not matter.  
   Like writing ``animal = "cat"`` — the computer knows what you mean.

3. **Default Arguments**  
   A parameter can have a *default value*, used when the caller does not
   provide one. It works like a pre-filled value on a form that you can
   change if you want.

4. **Variable-Length Positional Arguments** (``*args``)  
   Allows the function to accept *any number of positional arguments*.
   Inside the function, they become a tuple.

   It’s like saying: “Give me all the items you pass; I’ll pack them
   into a box (a tuple).”

5. **Variable-Length Keyword Arguments** (``**kwargs``)  
   Lets the function accept *any number of keyword arguments*, bundled
   into a dictionary.  
   It’s like letting the user write arbitrary labels and values on a
   form.

Python requires arguments in this order:

    positional → ``*args`` → keyword → default keyword → ``**kwargs``

This keeps things unambiguous and avoids conflicting meanings.

.. code-block:: python

   # Positional arguments: Order matters
   def describe_pet(animal, name):
       print(f"I have a {animal} named {name}.")

   describe_pet("dog", "Rex")   # correct
   describe_pet("Rex", "dog")   # wrong order → wrong meaning

.. code-block:: python

   # Keyword arguments: Order does NOT matter
   describe_pet(animal="cat", name="Luna")
   describe_pet(name="Luna", animal="cat")   # same result

.. code-block:: python

   # Using default values
   def describe_pet(name, animal="dog"):
       # default: animal = "dog"
       print(f"{name} is a {animal}.")

   describe_pet("Buddy")                   # uses default
   describe_pet("Whiskers", "cat")         # override default positionally
   describe_pet("Rocky", animal="hamster") # override using keyword

.. code-block:: python

   # *args: Variable-Length Positional Arguments
   def describe_many_pets(animal, *names):
       """Describe several pets of the same animal type."""
       print(f"You have {len(names)} {animal}(s):")
       for name in names:
           print(f" - {name}")

   describe_many_pets("dog", "Rex", "Buddy", "Snow")
   describe_many_pets("cat", "Luna")

.. code-block:: python

   # **kwargs: Variable-Length Keyword Arguments
   def describe_pet(animal, name, **details):
       """Describe a pet with optional extra info."""
       print(f"{name} is a {animal}.")
       if details:
           print("Additional details:")
           for key, value in details.items():
               print(f" - {key}: {value}")

   describe_pet("dog", "Rex", age=5, color="brown")
   describe_pet("cat", "Luna", vaccinated=True)


Return Values
-------------------------

A function does not need to print its result. More commonly, it computes
a value and gives it back using ``return``. The returned value goes back
to the line that called the function, so it can be:

- stored in a variable  
- passed into another function  
- used in an ``if`` statement or loop

    **Rule of thumb:** use ``print(...)`` for user-facing messages; use ``return ...`` for data the program needs to keep.

In Python, a function can return **any kind of value**. This works
because *everything in Python is an object*: whatever can be stored in a
variable can also be returned from a function.

Below are the most common (and useful) return types:

.. code-block:: python

   # Returning a Single Value
   def dog_to_human_years(age):
       """Return a dog's age converted to human years."""
       return age * 7

   human_age = dog_to_human_years(4)
   print(human_age)  # 28

.. code-block:: python

   # Returning Multiple Values
   def pet_stats(weight, age):
       """Return weight, age, and a simple BMI-like ratio."""
       return weight, age, weight / age

   w, a, ratio = pet_stats(20, 5)
   print(w, a, ratio)

.. code-block:: python

   # Returning a List
   def uppercase_traits(traits):
       """Return a list of traits in uppercase."""
       return [t.upper() for t in traits]

   result = uppercase_traits(["playful", "brown", "energetic"])
   print(result)

.. code-block:: python

   # Returning a Dictionary
   def build_pet(name, animal, age=None):
       """Return a dictionary describing a pet."""
       pet = {"name": name, "animal": animal}
       if age is not None:
           pet["age"] = age
       return pet

   pet = build_pet("Rex", "dog", age=5)
   print(pet)

.. code-block:: python

   # Returning Boolean Values
   def is_senior_pet(age):
       """Return True if age is considered 'senior' for a pet."""
       return age >= 8

   print(is_senior_pet(10))  # True
   print(is_senior_pet(4))   # False

.. code-block:: python

   # Returning Another Function
   def make_feeder(amount):
       """Return a function that feeds a pet by a certain amount (grams)."""
       def feed(food):
           return f"Feed the pet {amount}g of {food}."
       return feed

   small_feeder = make_feeder(50)
   print(small_feeder("kibble"))


Functions and Modules
=====================

Functions help you break your program into small, understandable pieces.
But as your code grows, putting all functions in the same notebook or
file becomes messy. To keep things organized, Python lets you store
functions in separate files called **modules**.

    A module is simply a ``.py`` file containing functions (and variables/classes) you want to reuse.

Using modules allows you to:

- keep your main program clean  
- hide implementation details and focus on high-level logic  
- reuse your functions across multiple scripts  
- share your function library with others  

In practice, a module becomes your own *toolbox*, just like Python’s
built-in modules.

.. code-block:: python

   # -----------------------
   # Small built-in dataset
   # -----------------------
   ANIMALS = {
       "Simba":  {"species": "lion",  "habitat": "savannah", "traits": ["strong", "brave"], "details": {"age": 5}},
       "Po":     {"species": "panda", "habitat": "forest",   "traits": ["cute", "hungry"],  "details": {"bamboo_eaten": 30}},
       "Hedwig": {"species": "owl",   "habitat": "forest",   "traits": ["silent", "nocturnal"]},
       "Kaa":    {"species": "snake", "habitat": "jungle",   "traits": ["stealthy"]},
       "Dory":   {"species": "fish",  "habitat": "ocean",    "traits": ["curious"]},
   }

.. code-block:: python

   # -----------------------
   # Lookup helpers
   # -----------------------
   def exists(name: str) -> bool:
       return name in ANIMALS

   def get_animal(name: str):
       return ANIMALS.get(name)

   def get_species(name: str):
       a = get_animal(name)
       return a.get("species") if a else None

   def get_habitat(name: str):
       a = get_animal(name)
       return a.get("habitat") if a else None

   def get_traits(name: str):
       a = get_animal(name)
       return list(a.get("traits", [])) if a else []

.. code-block:: python

   # -----------------------
   # Tiny knowledge helpers
   # -----------------------
   def diet_by_species(species: str) -> str:
       s = (species or "").lower()
       carnivores = {"lion", "owl", "snake"}
       herbivores = {"panda"}
       omnivores  = {"bear", "dog", "cat", "fish"}
       if s in carnivores:
           return "carnivore"
       if s in herbivores:
           return "herbivore"
       if s in omnivores:
           return "omnivore"
       return "unknown"

   def random_fact_by_species(species: str) -> str:
       s = (species or "").lower()
       facts = {
           "lion":  "Lions live in social groups called prides.",
           "panda": "Pandas can eat bamboo for up to 12 hours a day.",
           "owl":   "Owls can rotate their heads up to 270 degrees.",
           "snake": "Snakes smell with their tongue.",
           "fish":  "Some fish can recognize themselves in a mirror.",
       }
       return facts.get(s, "This species is fascinating—but we need more data!")

.. code-block:: python

   # -----------------------
   # High-level: showcase
   # -----------------------
   def animal_showcase(name: str, show_fact: bool = True):
       """Print a short summary for the given animal name."""
       a = get_animal(name)
       if not a:
           print(f"❌ Animal '{name}' not found in the database.")
           return None

       species = a.get("species", "?")
       habitat = a.get("habitat", "?")
       traits  = ", ".join(a.get("traits", [])) or "—"
       diet    = diet_by_species(species)

       print(f"=== ANIMAL: {name} ===")
       print(f"- Species : {species}")
       print(f"- Habitat : {habitat}")
       print(f"- Traits  : {traits}")
       print(f"- Diet    : {diet}")

       if show_fact:
           print(f"- Fact    : {random_fact_by_species(species)}")

