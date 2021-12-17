*** Settings ***
Library     BuiltIn
Library     String
Library     Collections
Library     Zoomba.GUILibrary     plugins=Zoomba.Helpers.EdgePlugin
Resource  ../../Resources/Configuration/Configuration.robot
*** Variables ***
${e_OTP_field}      //input[@name='otp']
${e_submit_OTP_btn}     //div[@role='dialog']//button[@type='submit']

*** Keywords ***
Input OTP
    wait until page contains element  ${e_OTP_field}    timeout=${timeout}
    input text  ${e_OTP_field}  5555

Click Submit button OTP
    wait for and click element  ${e_submit_OTP_btn}     timeout=${timeout}