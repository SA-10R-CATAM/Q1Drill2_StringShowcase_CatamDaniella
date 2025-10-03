from pyscript import when, display, document

@when("click", "#submit-btn")
def show_message(event):
    name = document.querySelector("#name").value
    age = document.querySelector("#age").value
    school = document.querySelector("#school").value
    schoolidnumber = document.querySelector("#schoolidnumber").value
    
    

    # Clear the output div first
    document.querySelector("#output").innerText = ""

    # Multiline message using input values
    message = f"""`⎚⩊⎚´ Student Profile
    Name ꕤ  : {name}
    Age 𐙚   : {age}
    School : ✿ {school}
    School ID Number ꩜ : {schoolidnumber}
    
   
    ꒰ᐢ. .ᐢ꒱₊˚⊹:
    {name} is currently {age} years old and studies at {school}.
    This information was gathered through input fields and displayed using
    a multiline string in Python via PyScript.
    """

    display(message, target="output")
