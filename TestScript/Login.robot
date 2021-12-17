*** Settings ***
Library     BuiltIn
Library     String
Library     Collections
Library     Zoomba.GUILibrary     plugins=Zoomba.Helpers.EdgePlugin
Resource    ../Resources/Configuration/Configuration.robot
Resource    ../Resources/Data/LoginInformation.robot
Resource    ../pom/LoginPage/LoginPage.robot

*** Variables ***

*** Test Cases ***
Test
    Open test Browser   ${Dev-site}     ${Chrome}
    Input user account  pentest005
    Input user password
    CLick Summit button
