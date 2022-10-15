from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type = 's-search-result']//a[.//span[@class='a-price']]")
SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
PRODUCT_NAMES = (By.CSS_SELECTOR, "#search .s-result-item")
CURRENT_NAME = (By.CSS_SELECTOR, "#search .s-result-item .a-section.a-spacing-none.a-spacing-top-small.s-title-instructions-style")
PRODUCT_IMAGES = (By.CSS_SELECTOR, "#search .s-result-item .s-product-image-container")
CURRENT_IMAGE = (By.CSS_SELECTOR, "#search .s-result-item .s-product-image-container img.s-image")


@when('Click on the first product')
def click_on_the_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@then('Search results for {expected_result} are shown')
def verify_search_result(context,expected_result):
    actual_result = context.driver.find_element(*SEARCH_RESULT).text
    assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}.'

@then('Verify that every product has a name and image')
def verify_product_name_present(context):

    global name, image
    context.driver.wait.until(EC.presence_of_all_elements_located(PRODUCT_NAMES))
    context.driver.wait.until(EC.presence_of_all_elements_located(PRODUCT_IMAGES))

    names = context.driver.find_elements(*PRODUCT_NAMES)
    images = context.driver.find_elements(*PRODUCT_IMAGES)
    actual_images = []
    actual_names = []

    for image in images[:]:
        image.is_displayed()
        current_image = context.driver.find_element(*CURRENT_IMAGE)
        actual_images += [current_image]
        print(image)

    assert image.is_displayed(), f'Error! Product does not have image {actual_images}.'

    for name in names[:]:
        name.is_displayed()
        current_name = context.driver.find_element(*CURRENT_NAME)
        actual_names += [current_name]
        print(name)

    assert name.is_displayed(), f'Error! Product does not have name {actual_names}.'












