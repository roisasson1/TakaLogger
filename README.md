# TakaLogger

I'm working for a start-up company called PARKOMAT Ltd, who specialize in robotic parking devices.
Until now, if there was a fault in one of the sites, only the customer could alert us.

I have created a system which sends a message when a fault appears in one of the sites.

I used Pub/Sub design pattern with RabbitMQ message queue.

The Publish/Subscribe pattern, also known as pub/sub, is an architectural design pattern that provides a framework for exchanging messages between publishers and subscribers. This pattern involves the publisher and the subscriber relying on a message broker that relays messages from the publisher to the subscribers. The host (publisher) publishes messages (events) to a channel that subscribers can then sign up to.
