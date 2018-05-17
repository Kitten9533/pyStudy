*** Settings ***
Documentation     Example test cases using the keyword-driven testing approach.
Resource        pub.txt
Library           Collections
Library           mylib
Library           yourLib
Library           reqLib
# <span style="color:#FF6666;">Library           Collections</span>

*** Test Cases ***
First Case
    [Documentation]    variable type
    Log to console    ${var1}
    Log to console    ${list1}[0]
    Log to console    ${list1[0]}
    Log to console    ${dict1}['key1']
    Log to console    ${dict1['key1']}
    Log to console    ${dict1.key1}

Second Case
    [Documentation]    Default values with user-keywords
    Calculate and Check Equals
    Calculate and Check Equals    1+5
    Calculate and Check Equals    7-2    ${5}
    Calculate and Check Equals    expression=6+3    expected=${9}

Third Case
    [Documentation]    Varargs with user-keywords
    Varargs keyword    a    f    ${var1}
    Varargs keyword    @{list1}    ${var1}
    Kwargs keyword    key1=value1    key2=789
    Kwargs keyword    &{dict1}
    Kwargs keyword    &{dict1}    mykey=tututu    &{dict1}

Fourth Case
    [Documentation]    data-driven case
    [Template]    Calculate "${expression}" and Check Equals "${expected}"
    2+4    ${6}
    9-2    ${7}
    6*4    ${24}

Fifth Case
    [Documentation]    builtIn library
    ${item}    Get Dictionary Keys    ${dict1}
    Log to console    ${item}

Sixth Case
    [Documentation]    custome keyword
    ${sign}    gen_sign    @{list1}
    Log to console    ${sign}
    ${members}      add_member      Mike
    Log to console      ${members}
    ${members}      add_member      John
    Log to console      ${members}

Seventh Case
    ${members}      add_member      1234
    Log to console      ${members}

Eighth Case
    get    http://httpbin.org/get    action=hadogen
    check status code    200