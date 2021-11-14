*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  tommi
    Set Password  tommi123
    Set Password Confirmation  tommi123
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  to
    Set Password  tommi123
    Set Password Confirmation  tommi123
    Submit Register Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kalevi
    Set Password  kalevi1
    Set Password Confirmation  kalevi1
    Submit Register Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  steven
    Set Password  steven123
    Set Password Confirmation  steven321
    Submit Register Credentials
    Register Should Fail With Message  Nonmatching password and password confirmation

Login After Successful Registration
    Set Username  john
    Set Password  john1234
    Set Password Confirmation  john1234
    Submit Register Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  john
    Set Password  john1234
    Submit Login Credentials
    Main Page Should Be Open

Login After Failed Registration
    Set Username  x
    Set Password  hahaha123
    Set Password Confirmation  hahaha123
    Submit Register Credentials
    Register Should Fail With Message  Username too short
    Go To Login Page
    Set Username  x
    Set Password  hahaha123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password
