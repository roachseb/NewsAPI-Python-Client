from models.request_model import RequestModel
from models.response_model import Article, ResponseModel, Source
from services.news_service import get_finance_news


def test_request_and_response_models():
    request_model = RequestModel(
        q='finance',
        from_param='2023-05-01T00:00:00',
        to='2023-05-27T23:59:59',
        sortBy='popularity'
    )

    response_model = get_finance_news(request_model)

    assert isinstance(response_model, ResponseModel)
    assert response_model.status == 'ok'
    assert isinstance(response_model.totalResults, int)
    assert response_model.totalResults > 0
    assert isinstance(response_model.articles, list)
    assert len(response_model.articles) > 0
    for article in response_model.articles:
        assert isinstance(article, Article)
        assert isinstance(article.source, Source)
        assert isinstance(article.title, str)
        assert isinstance(article.url, str)
        assert isinstance(article.publishedAt, str)
