# Canes Automation


A web scraper that automates the web registration for Caniac Club members in order to recieve free box combos and other rewards. The goal is to reduce the time to take to complete the user's registration form.


## Installation


Use the package manager [pip](https://pypi.org/project/pip/) to install the Python library SeleniumBase.

```bash
pip install SeleniumBase
```


## Usage

Once you download the library and execute the code, the web scraper runs an external Chrome application through the listed driver where the script automatically inputs the web address for the registration form. When the script prompts the user for its card number and code from the given Caniac Club member card, the program uses its information to automate the prompted user information within the website.

- Replace "xxxxx" with user's email
    - ``` email = "xxxxx@gmail.com" ```
- Replace "xxxxx" with desired Canes location; the location should be listed in the dropdown of the prompt
    - Replacement should be in the format as shown
        - ``` City - Street Name (Store Number) ``` 
        - List of stores should be seen within the fourth dropdown (Favorite Stores)
- Input card number and code

## Significance

College students have limited time in waiting and filling out an extensive registration form for their free rewards. This is script aims to reduce the time needed for this form allowing for more students to recieve their free box combos.

