from concrete_observables import Publisher
from concrete_observer import Subscriber

def main():
    # Create a publisher
    news_publisher = Publisher()

    # Create subscribers
    GorillaNews = Subscriber("Gorilla", news_publisher)
    PandaNews = Subscriber("Panda", news_publisher)

    # Publisher sets new data
    news_publisher.set_data("Breaking News: 1")

    # Another update
    news_publisher.set_data("Update News: 2")

    # Unsubscribe Bob
    PandaNews.unsubscribe()

    # Another update after Bob unsubscribed
    news_publisher.set_data("Final Update: Panda has unsubscribed.")

if __name__ == "__main__":
    main()