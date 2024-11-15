from bs4 import BeautifulSoup
from typing import Optional


def contains_image(html: str) -> Optional[str]:
    """
    Extracts the source URL of the first image found in the given HTML content.

    This function parses the provided HTML string to locate the first image
    (`<img>`) tag. If an image tag is found, it returns the value of the `src`
    attribute. If no image is found, it returns None.

    :param html: A string containing HTML content to be parsed.
    :type html: str
    :return: The `src` attribute value of the first found image tag, or None if
        no image tag is found.
    :rtype: Optional[str]
    """
    soup = BeautifulSoup(html, "html.parser")
    image = soup.find("img", recursive=True)
    if image:
        return image.get("src")
    return None
