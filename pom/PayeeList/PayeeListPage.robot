*** Settings ***
Library     BuiltIn
Library     String
Library     Collections
Library     Zoomba.GUILibrary     plugins=Zoomba.Helpers.EdgePlugin
Resource  ../../Resources/Configuration/Configuration.robot
*** Variables ***
${e_timo_member_btn}   //button[@id='button-internal']
${e_debit_card_btn}     //button[@id='button-debit-card']

*** Keywords ***
CLick Timo member button
    wait for and click element  ${e_timo_member_btn}    timeout=${timeout}

