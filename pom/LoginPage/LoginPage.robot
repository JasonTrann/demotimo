*** Settings ***
Library     BuiltIn
Library     String
Library     Collections
Library     Zoomba.GUILibrary     plugins=Zoomba.Helpers.EdgePlugin
Resource  ../../Resources/Configuration/Configuration.robot
Resource  ../../Resources/Data/LoginInformation.robot
*** Variables ***
${e_user_name_field}   //input[@name='username']
${e_password_field}     //input[@name='password']
${e_summit_btn}     //button[@type='submit']

*** Keywords ***
Input user account
    [Arguments]  ${user_name}
    wait until page contains element    ${e_user_name_field}      timeout=${timeout}
    input text  ${e_user_name_field}    ${user_name}

Input user password
    wait until page contains element    ${e_password_field}      timeout=${timeout}
    input text  ${e_password_field}    ${password}

CLick Login button
    wait for and click element  ${e_summit_btn}     timeout=${timeout}