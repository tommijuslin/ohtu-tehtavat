*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  dolph  lundgren
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  tommi  tommi321
    Output Should Contain  Username already exists

Register With Too Short Username And Valid Password
    Input Credentials  to  tommi123
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input Credentials  steven  seagal1
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  steven  stevenseagal
    Output Should Contain  Password must not contain only letters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Input Credentials  tommi  tommi123
    Input New Command