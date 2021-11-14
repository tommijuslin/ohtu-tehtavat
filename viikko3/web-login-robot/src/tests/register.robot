*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  tommi
    Set Password  tommi123
    Set Password Confirmation  tommi123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  to
    Set Password  tommi123
    Set Password Confirmation  tommi123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kalevi
    Set Password  kalevi1
    Set Password Confirmation  kalevi1
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  steven
    Set Password  steven123
    Set Password Confirmation  steven321
    Submit Credentials
    Register Should Fail With Message  Nonmatching password and password confirmation

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register
