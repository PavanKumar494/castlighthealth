def accept_alert(browser):
    alt = browser.switch_to_alert()
    alt.accept()


def dismiss_alert(browser):
    alt = browser.switch_to_alert()
    alt.dismiss()


def get_alert_msg(browser):
    alt = browser.switch_to_alert()
    return alt.text
