*** Settings ***
Library           json
Library           requests
Library           RequestsLibrary
Library           collections

*** Test Cases ***
test1
    [Tags]    get
    Create Session    github    https://api.github.com
    ${resp}=    Get Request    github    /users/bulkan
    Should Be Equal As Strings    ${resp.status_code}    200

login
    [Tags]    AZ Login
    Create Session    AZ    http://m.aizhuanshangcheng.com
    &{data}=    Create Dictionary    authCode=1    deviceType=android    location=""    password=12345678    phone=17816866126
    ...    uniqueId=d9f597114a17550b3eb21f13b1ddea1f
    &{headers}=    Create Dictionary    Content-Type=application/json; charset=utf-8
    ${resp}=    Post Request    AZ    /uc/login/in    data=${data}    headers=${headers}
    Should Be Equal As Strings    ${resp.status_code}    200
