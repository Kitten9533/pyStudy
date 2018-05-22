*** Settings ***
Library           json
Library           requests
Library           RequestsLibrary
Library           collections
Library           SeleniumLibrary

*** Test Cases ***
test1
    Create Session    github    https://api.github.com
    ${resp}=    Get Request    github    /users/bulkan
    Should Be Equal As Strings    ${resp.status_code}    200
    Should Be Equal As Strings    1    1
    #Hello
    Log    Hello World    warn

login
    #登录
    Create Session    AZ    http://m.aizhuanshangcheng.com
    &{headers}=    Create Dictionary    Content-Type=application/json; charset=utf-8
    &{data}=    Create Dictionary    authCode=1    deviceType=android    location=""    password=12345678    phone=17816866126
    ...    uniqueId=d9f597114a17550b3eb21f13b1ddea1f
    ${resp}=    Post Request    AZ    /uc/login/in    data=${data}    headers=${headers}
    Should Be Equal As Strings    ${resp.status_code}    200
    Log    ${resp.cookies}
