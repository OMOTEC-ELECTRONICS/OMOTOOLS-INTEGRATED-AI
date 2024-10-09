// server_code.h
#ifndef SERVER_CODE_H  
#define SERVER_CODE_H 

// Includes the library
#include <ESP8266WebServer.h> 

const char htmlContent[] = R"====(
<!DOCTYPE html> //declares the document type
<html> // Indicates the beginning of an HTML document
<head> // The title of the web page is set
  <title>Omotools IoT WebViewer</title>
  <style> // CSS styles are defined to control the appearance of the page
    body {
      text-align: center;
      margin: 0;
      font-family: Arial, sans-serif;
    }
    #main-header {
      display: flex;
      align-items: center;
      background-color: #115690;
      color: white;
      padding: 10px;
    }
    #logo {
      align-items: center;
      margin-right: 10px;
      max-height: 50px;
    }

    .controllers {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      margin-top: 20px;
    }

    .controller-box {
      border: 2px solid #99458b;
      padding: 10px;
      margin: 10px;
      width: 500px; /* Adjust the width as needed */
      text-align: center;
    }
    .button {
      background-color: #f47332;
      border: 1px;
      color: white;
      padding: 15px 32px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      margin: 4px 2px;
      cursor: pointer;
      border-radius: 8px;
      width: 100%; /* Make buttons fill the width of the container */
    }
    h2 {
      color: #dc946f; /* Adjust the color as needed */
    }

    table {
      width: 100%;
    }


    table, th, td {
      border: 0px solid #dc946f;
      border-collapse: collapse;
    }
    th, td {
      padding: 15px;
      text-align: center;
    }
  </style>
</head>
<body>
  <div id="main-header">
    <img id="logo" src="https://onmyowntechnology.com/images/omotec_logo.png" alt="Omotools Logo">
    <h1>Omotools IoT WebViewer</h1>
  </div>

  <div class="controllers">
    <div class="controller-box">
      <h2>Motor Controller</h2>
      <button id="togglemotor" class="button" onclick="togglemotor()">Toggle</button>
    </div>

  <script>
  function controlMotor(direction) {
      var xhttp = new XMLHttpRequest();
      xhttp.open("GET", "/motor?direction=" + direction, true);
      xhttp.send();
    }
    var motorState = false; // Variable to track motor state

    function togglemotor() {
      motorState = !motorState; // Toggle the motor state
      var xhttp = new XMLHttpRequest();
      xhttp.open("GET", "/motor?state=" + (motorState ? "on" : "off"), true);
      xhttp.send();
      updateToggleButton();
    }

    function updateToggleButton() {
      var toggleButton = document.getElementById("togglemotor");
      toggleButton.innerHTML = motorState ? "Turn Off" : "Turn On";
      toggleButton.style.backgroundColor = motorState ? "#f47332" : "#4CAF50";
    }
  </script>
</body>
</html>
)====";

void handleRoot();
void handlemotor();



#endif
