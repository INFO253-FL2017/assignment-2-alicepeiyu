function validateForm() {
    var x = document.forms["contactus"]["name"].value;
    var y = document.forms["contactus"]["message"].value;
    var z = document.forms["contactus"]["subject"].value;
    if (x == "") {
        alert("name must be filled out");
    return false;
    }
    if (y == "") {
        alert("message must be filled out");
    return false;
    }
    if (z == "") {
        alert("subject must be filled out");
    return false;
    }
    else {
    alert("Your message has been sent");
    return true;
    }
}
