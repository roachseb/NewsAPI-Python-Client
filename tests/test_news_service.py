import os
import pytest
import requests_mock
from newsApi.models.request import EverythingRequestModel, Language, TopHeadlinesRequestModel, SourcesRequestModel
from newsApi.models.response import EverythingResponseModel, TopHeadlinesResponseModel, SourcesResponseModel
from newsApi.service import NewsAPIService  
@pytest.fixture
def news_api_service():
    return NewsAPIService(os.environ.get('NEWS_API_KEY'))

def test_everything(news_api_service):
    request_model = EverythingRequestModel(q="test")
    with requests_mock.Mocker() as m:
        m.get('https://newsapi.org/v2/everything', json={"status": "ok", "totalResults": 10, "articles": []})
        response = news_api_service.everything(request_model)
    assert isinstance(response, EverythingResponseModel)
    assert response.status == 'ok'
    assert response.totalResults == 10

def test_top_headlines(news_api_service):
    request_model = TopHeadlinesRequestModel(q="test")
    with requests_mock.Mocker() as m:
        m.get('https://newsapi.org/v2/top-headlines', json={"status": "ok", "totalResults": 10, "articles": []})
        response = news_api_service.top_headlines(request_model)
    assert isinstance(response, TopHeadlinesResponseModel)
    assert response.status == 'ok'
    assert response.totalResults == 10

def test_sources(news_api_service):
    request_model = SourcesRequestModel(language=Language.EN)
    with requests_mock.Mocker() as m:
        m.get('https://newsapi.org/v2/sources', json={"status": "ok", "sources": []})
        response = news_api_service.sources(request_model)
    assert isinstance(response, SourcesResponseModel)
    assert response.status == 'ok'
