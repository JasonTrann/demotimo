*** Settings ***
Library     BuiltIn
Library     String
Library     Collections
Library     Zoomba.GUILibrary     plugins=Zoomba.Helpers.EdgePlugin
Resource    ../../../Resources/Configuration/Configuration.robot
Resource    ../../../Resources/Data/LoginInformation.robot
Resource    ../../../pom/LoginPage/LoginPage.robot
Resource    ../../../pom/GlobalKeyWords.robot
*** Variables ***

*** Test Cases ***
Test
    Open test Browser   ${Dev-site}     ${Chrome}
    Input user account  ekycmambu10
    Input user password
    CLick Login button
    Input OTP
    Click Submit button OTP
