from sklearn.feature_extraction.text import CountVectorizer

from Word2Vec import spark

vectorizer=CountVectorizer()
# documentDF = spark.createDataFrame([
#     ("With the rapid development of mobile Internet and Internet of Things business, the 5G mobile communication process has been accelerated. This article summarizes the Internet technology under 5G mobile communication, analyses the connotation of Internet of Things, and studies the integration of 5G mobile communications and Internet of Things technology. Through the analysis and discussion of the new possibilities in the Internet of Things era under 5G mobile communication technology, the research shows that the simulation analysis combined with the cell breathing technology and the base station dormancy technology aims to decrease the energy consumption of the base station under the premise of ensuring the communication quality, thereby improving the network energy efficiency. Research shows that in the dense and uniform user distribution scenario, the power consumption has a small decrease due to the increase of power consumption, but the system capacity is significantly improved and the communication quality is improved. It can ensure the user’s fairness and system capacity to achieve, and meet the rate requirements of different users. The analog results verify the accuracy of the theoretical analysis.".split(" "), ),
#     ("5G networks will use novel technological concepts to meet the requirements of broadband access everywhere, high user and device mobility, and connectivity of massive number of devices (e.g., the Internet of Things) in an ultra-reliable and affordable way. Software defined networking and network functions virtualization leveraging the advances in cloud computing such as mobile edge computing are the most sought out technologies to meet these requirements. However, securely using these technologies and providing user privacy in future wireless networks are the new concerns. Therefore, this article provides an overview of the security challenges in clouds, software defined networking, and network functions virtualization, and the challenges of user privacy. Henceforth, this article presents solutions to these challenges and future directions for secure 5G systems.".split(" "), ),
#     ("5G will provide broadband access everywhere, entertain higher user mobility, and enable connectivity of massive number of devices (e.g. Internet of Things (IoT)) in an ultrareliableandaffordableway.Themaintechnologicalenablerssuch as cloud computing, Software Deﬁned Networking (SDN) and Network Function Virtualization (NFV) are maturing towards theirusein5G.However,therearepressingsecuritychallengesin these technologies besides the growing concerns for user privacy. Inthispaper,weprovideanoverviewofthesecuritychallengesin these technologies and the issues of privacy in 5G. Furthermore, we present security solutions to these challenges and future directions for secure 5G systems.".split(" "), ),
#     ("Existing cellular communications and the upcoming 5G mobile network requires meeting high-reliability standards, very low latency, higher capacity, more security, and high-speed user connectivity. Mobile operators are looking for a programmable solution that will allow them to accommodate multiple independent tenants on the same physical infrastructure and 5G networks allow for end-to-end network resource allocation using the concept of Network Slicing (NS). Data-driven decision making will be vital in future communication networks due to the traffic explosion and Artificial Intelligence (AI) will accelerate the 5G network performance. In this paper, we have developed a ‘DeepSlice’ model by implementing Deep Learning (DL) Neural Network to manage network load efficiency and network availability, utilizing in-network deep learning and prediction. We use available network Key Performance Indicators (KPIs) to train our model to analyze incoming traffic and predict the network slice for an unknown device type. Intelligent resource allocation allows us to use the available resources on existing network slices efficiently and offer load balancing. Our proposed DeepSlice model will be able to make smart decisions and select the most appropriate network slice, even in case of a network failure.".split(" "), ),
#     ("The multitude of 5th generation network applications, use cases and services shall have Network Slicing playing a key role in their enablement. Network slicing shall provide end-to-end isolation between the slices. This feature shall provide the ability to customize each of the slices based on the service needs such as bandwidth and latency. The slices maintaining isolation between resource allocation and traffic shall be critically important in protecting the network infrastructure system against Distributed Denial of Service (DDoS) attacks. Systems shall need to adapt to more secured security mechanisms and policies to build a robust 5G network. We are proposing a framework for ‘Secured 5G’ Neural Network creating a robust network slicing architecture. The proposed framework shall enable proactive detection and elimination of threats using deep learning techniques prior to the infestation of the core network. We shall develop a model that enables the threat to be quarantines ensuring end-toend security from device to the core network.".split(" "), )], ["text"])

data_corpus=["guru99 is the best sitefor online tutorials. I love to visit guru99."]
vocabulary=vectorizer.fit(data_corpus)
X= vectorizer.transform(data_corpus)
# vocabulary=vectorizer.fit(documentDF)
# X= vectorizer.transform(documentDF)
print(X.toarray())
print(vocabs())_fulary.get_naeatureme