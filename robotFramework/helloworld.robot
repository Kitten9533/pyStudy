*** Settings ***
*** Variables ***
${var1}          6
@{list1}           a    b    c    ${var1}
&{dict1}          key1=sf   key2=${list1}

*** Test Cases ***
First Case
    Log to console    ${var1}
    Log to console    ${list1}
    Log to console    ${dict1}
    Log to console    ${var1}
    Log to console    ${list1}[0]
    Log to console    ${list1[0]}
    Log to console    ${dict1}['key1']
    Log to console    ${dict1['key1']}
    Log to console    ${dict1.key1}

Second Case
    ${res}    Evaluate    1+2+3
    Log to console    ${res}
    Should Be Equal    ${res}    ${6}

Third Case
    ${res}    Evaluate    'i'*3
    Log to console      ${res}
    Length Should Be    ${res}      3

Fourth Case
    [Documentation]    data-driven case
    [Template]    Calculate "${expression}" and Check Equals "${expected}"
    2+4    ${6}
    9-2    ${7}
    6*4    ${24}

Varargs Case
    Varargs keyword    @{list1}    ${var1}

Kwargs Case
    Kwargs keyword    key1=value1    key2=789

*** Keywords ***
Calculate and Check Equals
    [Arguments]    ${expression}    ${expected}
    ${res}=    Evaluate     ${expression}
    Should Be Equal    ${res}     ${expected}

Calculate "${expression}" and Check Equals "${expected}"
    Calculate and Check Equals      ${expression}       ${expected}

Varargs keyword
    [Arguments]    @{args}
    Log to console    --------
    : FOR    ${item}    IN    @{args}
    \    Log to console    ${item}

Kwargs keyword
    [Arguments]    &{kwargs}
    Log to console    --------
    : FOR    ${item}    IN    @{kwargs.items()}
    \    Log to console    ${item}