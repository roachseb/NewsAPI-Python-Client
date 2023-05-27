import pytest
from models.request_model import RequestModel
from services.news_service import get_finance_news

def test_get_finance_news():
    request_model = RequestModel(
        q='finance',
        searchIn='title,content',
        from_param='2023-05-01T00:00:00',
        to='2023-05-27T23:59:59',
        language='en',
        sortBy='popularity',
        pageSize=100,
        page=1
    )

    response_model = get_finance_news(request_model)

    assert response_model.status == 'ok'
    assert isinstance(response_model.totalResults, int)
    assert response_model.totalResults > 0
    assert len(response_model.articles) > 0

