# Movie-Recommender-System-using-Machine-Learning

# Why Do We Need Recommender Systems?

We now live in what some call the “era of abundance”. For any given product, there are sometimes thousands of options to choose from. Think of the examples above: streaming videos, social networking, online shopping; the list goes on. Recommender systems help to personalize a platform and help the user find something they like.


The easiest and simplest way to do this is to recommend the most popular items. However, to really enhance the user experience through personalized recommendations, we need dedicated recommender systems.


From a business standpoint, the more relevant products a user finds on the platform, the higher their engagement. This often results in increased revenue for the platform itself. Various sources say that as much as 35–40% of tech giants’ revenue comes from recommendations alone.


Now that we understand the importance of recommender systems, let’s have a look at types of recommendation systems, then build our own with open-sourced data!

# Types of Recommender Systems

Machine learning algorithms in recommender systems typically fit into two categories: content-based systems and collaborative filtering systems. Modern recommender systems combine both approaches.


Let’s have a look at how they work using movie recommendation systems as a base.

![88506recommendation system](https://user-images.githubusercontent.com/106477719/208264787-b91aa99b-7566-4fa3-8db7-49cdc4427b61.png)


# A) Content-Based Movie Recommendation Systems
Content-based methods are based on the similarity of movie attributes. Using this type of recommender system, if a user watches one movie, similar movies are recommended. For example, if a user watches a comedy movie starring Adam Sandler, the system will recommend them movies in the same genre or starring the same actor, or both. With this in mind, the input for building a content-based recommender system is movie attributes.

# B) Collaborative Filtering Movie Recommendation Systems
With collaborative filtering, the system is based on past interactions between users and movies. With this in mind, the input for a collaborative filtering system is made up of past data of user interactions with the movies they watch.

For example, if user A watches M1, M2, and M3, and user B watches M1, M3, M4, we recommend M1 and M3 to a similar user C. You can see how this looks in the figure below for clearer reference.
