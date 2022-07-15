from typing import Dict, Optional

import feedgenerator


def generate_feed(
    title: str, link: str, param: Dict, description: Optional[str] = None
) -> feedgenerator.Rss201rev2Feed:

    return feedgenerator.Rss201rev2Feed(
        title=title,
        link=link,
        description=(
            description if description else param['twitter']['description']
        ),
        language=param['feed']['language'],
        author_name=param['feed']['author_name'],
        feed_url=param['feed']['feed_url'],
    )
