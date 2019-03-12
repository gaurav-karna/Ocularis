![alt text](https://i.ibb.co/TRLvJmt/fin-thumbnail-000.png "Ocularis_Copyright")

# Ocularis

## Let's Imagine with Microsoft

#### A virtual assistant for the visually impaired – a containerized and unified solution to tackle some of the daily challenges faced by millions worldwide who have complete/partial visual impairment. 

1st Place Winner of the Microsoft Discover Azure Hackathon and a regional (Americas) semi-finalist for Microsoft's Imagine Cup. Ocularis is an assistive technology that uses several Azure services to help the visually impaired in their day to day tasks.

## Note:

* Please Use Windows for maximum experience
* Recommended `Python Version - 3.6.4`


## What is Ocularis ?

 A central promise of technology and all its advancements is to bring a better world through solving inherent problems of human society and its individuals. The predominance of smart devices is so obvious that it is now impossible to imagine a world without them around. However, there appears to be a lack of consideration regarding accessibility in contemporary technology, with the industry being heavily biased towards people without impairments of any kind. Nevertheless, things like a smaller market size and weak representation in government and industry are no longer viable justifications for a pervasive tendency towards the 
aforementioned specific catering. Apart from non-technical impediments, there are also some major technical challenges in providing these people with high quality services on par with natural human capabilities. However with the advent of new computing milestones such as machine learning and computer vision, we believe that we are in a unique era of human history such that these challenges have become easier to surmount. One major challenge where we see potential to capitalize on these technologies and make a difference is in the realm of visual impairment. 

Visual Impairment is a decreased ability to see to a degree that causes problems not fixable by usual means, such as glasses [1]. Hence, ordinary tasks become difficult and make them less independent. Simple things such as being aware of their immediate surroundings and recognizing who they are conversing with become exceedingly difficult. We believe we can address these issues using Microsoft Cognitive Services and eventually with Windows IoT core cognitive capabilities, along with a cheap device we call ‘Ocularis’ – meaning ‘eye’ in Latin - that we intend to design and build. Ocularis is an intelligent digital assistant who can understand requests of its user via voice commands and can provide thoughtful responses through her voice. Ocularis tries to find answers to questions by gathering information from its integrated knowledge, the internet, or from the environment that she sees through a high-quality built-in camera. The concept for Ocularis is a simple one, with the aim to make it as seamless as possible to integrate into daily lives. Hence, we want to incorporate the device as a wearable necklace to provide a nice viewpoint for the camera while minimizing impedance with the user’s activity. Essentially, the device is intended to be a third eye for the user and make tasks, simple or complex, much easier to deal with. 

## Why Ocularis ?

Visual Impairment is defined as a visual acuity of worse that 20/40 [1] and low vision is often defined as a visual acuity worse than 20/70 [3]. Unfortunately, there isn’t an exact estimation of the number of the blinds and the visually impaired [13]. According to World Health Organization, in 2018, 217 million people have severe vision impairment and 36 million people are blind [4]. WHO reports that 65 percent of visually impaired, and 82 percent of blind people are over 50 years of age. Unfortunately, this number is increasing because of population growth, ageing problems, and consequences of unhealthy life styles. Reports suggests that this number is expected to rise to more than 550 million by 2050 [5]. 

According to a research published by The Lancet Global Health, 89% of the visually impaired live in low and middle-income countries [6]. However, the population in western countries is still noticeable. As claimed by World Health Organization, in 2010, there were near 26 million visually impaired individuals live in European countries [7]. Other reports state that over 2 million people in UK suffer from sight loss and “In the UK alone, 250 people will start to lose their sight every day” [8,]. Based on a new report published in 2016 by Center for Disease Control and Prevention, nearly 26 million people experience vision loss in the USA [9]. Based on this report, near 11 million of the mentioned population live alone without any partner and less than 6 million of them have a bachelor's degree or higher. Moreover, it states that “Approximately 10.1 million people with vision loss in the U.S. have a family income of less than $35,000, 2.8 million have a family income between $35,000 and $49,999, 3.6 million have a family income between $50,000 and $74,999, 2.3 million have a family income between $75,000 and $99,999 and 4.5 million have a family income of $100,000 or more”. In Canada, the population of the visually impaired is estimated to be around 800,00 and near 5.59 million have an eye disease that could cause sight loss [10,11]. In Australia, it is estimated there are over 575,000 people who are blind or vision impaired. However, despite the fact that blindness and vision impairment affect a significant proportion of Australia’s population, no 
comprehensive data exists on the provision of blindness and low vision services at a national level [15]. In China, another potential market of our product, the number of people who suffer from severe visual impairment is around 17 million and one third of them are blind [12]. 

Therefore, we are confident in saying that the potential market capture for Ocularis is very well-defined in a global context. Unfortunately, reports show that these people deal with serious problems throughout their lives because of the lack of support from society and from loneliness. In the UK, 31% of visually impaired are never or rarely optimistic about the future. Few explanations exist for this unfortunate statistic. Reports estimate that only 17% of people with sight loss receive emotional support and less than a fifth received practical support that helped them get around their home. 35% of people who suffer from vision loss say that they receive frequent or consistent negative feedback from the public [14].

 
## How does Ocularis work ?

![alt text](https://i.ibb.co/jhQb7xf/finalprced-MOD.png "Ocularis_Copyright")

The heart of Ocularis is empowered by a Python application hosted on Windows IoT Core. We have also
developed a UWP version of the application that is available on the repository, however the latter platform is still
under development. This software operates a wearable light-weight device which is supposed to placed as a
necklace around the neck of its user. Ocularis consists of a Camera, Audio I/O Module, Wi-Fi Module, Bluetooth
Module, Cellular Module, a low consumption processor, and RAM. These modules enable the device to interact
with its user via voice and delegate the processing needs to the cloud. The variety of connectivity modules ensure
us that Ocularis is always connected to the internet when available. Having high quality internet connection is
crucial to some functionalities because Ocularis is heavily dependent on Microsoft Azure Cognitive Services such
as Computer Vision and several Bing APIs to bring the incredible features to the customer.
Obviously, internet connection introduces latency and uncertainty to our product. We have taken two measures
to mitigate this problem. First, Ocularis tries to return the answer to its user’s request by going through the Ocularis
Internal Knowledge Base which is sufficient for some basic needs such as asking about time, date, calendar, or
anything that is accessible from user’s phone like messages, emails, and contacts. Secondly, we try to minimize

the number of requests that we need to make to Azure Cognitive Services by using a server that acts as a mediator
between Ocularis and Azure. Without this mediator, we would need several back and forth between Ocularis and
Azure Cognitive Services to be able to serve some requests. However, by putting this Mediator in place, Ocularis
just needs to send one request to the Mediator and then Mediator will be responsible to handle the required
conversation with Azure. Further, we have minimized the number of API calls even more by having pre-loaded
audio files that will consistently be used throughout interacting with Ocularis in a static audio folder.
In addition to Ocularis Internal Knowledge Base, this device has a built-in Internal Image Processor in order to
alarm the user in case of detecting potential danger of falling down, getting out of a sidewalk, or getting close
to an obstacle. This functionality is not supposed to be a replacement to guide dogs but is complementary to
them. It affords a higher level of independence than with previous arrangements. It should be mentioned that
existing Depth and Obstacle Detection approaches do not guarantee 100% accuracy, but we aim to implement
and train the model which provides the most confidence and deterministic behavior. This process needs to be
done by the device and cannot be delegated to the cloud because we need a near real-time alarming system to
increase its reliability. This feature is and will consistently be under development, and will be released in beta
phases to the users with accuracy warnings.

Lastly, to make the conversations between user and Ocularis seem intelligent and pleasant, Ocularis attaches a
context to user requests and provides a response based on this new context and previous contexts that have
changed the state of conversation. In other words, Ocularis does not interpret user’s commands in isolation but
it takes the context of conversation and its state into consideration. As an example, when a user asks a question
like “Who is the current prime minister of Canada?” and Ocularis notifies its user that she has found 5 relevant
pieces of information, Ocularis initiates a state machine (context) to the pair of request and response. So, when
the user asks for further questions such as “give me all your findings”, “give me the first relevant one”, or “repeat
it again please”, Ocularis knows how to respond to the request according to the state of the conversation.
Ocularis State Manager is responsible for transitioning through the possible set of states and even memorizing
the state of previous requests. As an example, a user can ask a question like “who was in front of me?” after
getting the required information about Canada Prime Minister and since device has answered to the question
“who is in front of me?” just before the question about Prime Minister, she can respond back quickly without
sending requests to Azure Cognitive Services. Moreover, Ocularis State Manager helps with navigating Ocularis
internal settings.

## Why is Ocularis better?

Ocularis empowers users with a distinctive set of features that other competitors are nowhere close to.

1. It’s all about the unique user experience that Ocularis delivers. Ocularis is supposed to be like a buddy who is
there to support and guide its users. It is a new platform and isn’t comparable to any other existing
solution. Ocularis is the third eye, as it’s placed as a necklace around its user. All communications with the
device and the user go through a Bluetooth headphone and microphone. Therefore, there is no more
challenge like unlocking the phone, finding the app and opening it up, and getting frustrated when getting
the functionality that you are looking for is not very straightforward. With Ocularis, users can get what they
are looking for just by asking for it.

2. It’s not always the user who initiates a conversation. Ocularis is always conscious and warns if it detects that
the user is approaching an obstacle or when a new notification is raised by the user’s paired phone. Therefore,
the user gets informed of high priority events that are happening around them even when they do not ask for
them.

3. Although Ocularis is a stand-alone device, it can be paired to the user’s phone. So, users can make phone
calls or send messages and emails just by asking Ocularis to do so. Moreover, Ocularis informs them about
receiving calls, messages, and emails. They no longer need to be worried about their phone and its challenging
user interface.

4. Ocularis makes it possible for users to ask for help from their friends without them being around. The Remote
Assistance feature of Ocularis allows trusted friends to connect to the camera and see the world through its
lens. Therefore, they can guide the user remotely.

5. According to our estimations, the cost of Ocularis is a lot lower than a high-end device like iPhone. Currently,
Seeing AI is only available on iPhones which makes the solution less accessible due to the high cost associated.

6. As a unique and unified solution, we provide users with smart sticks. Ocularis sticks have been equipped with
a vibrator and several buttons. The user can use these buttons to send some specific commands to the device.
So, instead of saying loudly “who is this guy in front of me?” they can push a button on their sticks and nobody
gets notified of the interaction between user and Ocularis. Moreover, when Ocularis detects a danger to the
user, it can activate the vibrator in the stick.

