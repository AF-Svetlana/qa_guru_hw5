import os
from selene import browser, have, by


def test_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Shelby')
    browser.element('#lastName').type('Corgi')
    browser.element('#userEmail').type('corgitest@test.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('9999999999')

    browser.element('#dateOfBirthInput').click()
    browser.element(".react-datepicker__month-select").click().element(by.text('January')).click()
    browser.element(".react-datepicker__year-select").click().element(by.text('2015')).click()
    browser.element('.react-datepicker__day--022').click()

    browser.element('#subjectsInput').type('Biology').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('../files/profile.png'))
    browser.element('#currentAddress').type('Moscow')
    browser.element('#state').click().element(by.text('NCR')).click()
    browser.element('#city').click().element(by.text('Delhi')).click()

    browser.element('#submit').click()

    browser.element('.modal-header').should(have.text("Thanks for submitting the form"))
    browser.element('.table').all('td').even.should(have.exact_texts(
        'Shelby Corgi',
        'corgitest@test.com',
        'Male',
        '9999999999',
        '22 January,2015',
        'Biology',
        'Sports',
        'profile.png',
        'Moscow',
        'NCR Delhi'
    )
    )
