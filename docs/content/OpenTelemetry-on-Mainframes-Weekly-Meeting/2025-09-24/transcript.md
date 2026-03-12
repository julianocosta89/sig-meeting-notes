SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2025-09-24
Duration: 31 minutes
Zoom Recording URL: https://zoom.us/rec/share/OnAZli0fEhNW4dZWgZUlBenusa0fTrBWwnEYuyEYrNZiDCgSyNiDIJBNjRQ1h7AS.V-HUyrfjyxnrw7IR
============================================================

## Zoom Recording Transcript

**Greg Shriver** 01:24 Hello, Antoine.
**Richard Nikula** 01:39 Hey there.
**Greg Shriver** 01:40 Hello, hello?
**Richard Nikula** 01:43 So Rudiger did points this morning he wasn't going to be here.
**Greg Shriver** 01:47 Yeah, and I believe, like.
I think Anand said the same thing.
**Richard Nikula** 01:56 Mmm.
And it appears to be moving.
**Greg Shriver** 02:04 Yeah.
**Richard Nikula** 02:05 Or else he's in an earthquake, when are they in?
**Antoine Toulme** 02:08 I'm just walking around, trying to get coffee. I've been meeting for 2 hours straight, so…
**Greg Shriver** 02:13 Ugh.
**Antoine Toulme** 02:14 I need to walk around a little bit, otherwise I will ossify in place.
One night.
I'm really happy I'm finally managing to actually be on this meeting, because I've been trying to get there, and either miss it, or be having conflicts.
**Greg Shriver** 02:37 Yeah, I understand.
I think we all, have similar challenges.
So, appreciate you being here.
So, this might be a short call today. I don't have… Actually, anything other than, I see… that, david Dye had… Submitted some, Some feedback on the 1741 pull request, which was the original mainframe semantic convention, pull request.
And it looks like there's still… Looks like there's some disharmony with, with… with entities.
And… and that's also, you know, an outstanding item, I think, for all of us, is to… and my… myself included, is to, To better understand the whole… The whole current, project, and current thinking on, on entities.
And how they relate My best estimate, or my best assessment of this is.
It looks like there's, you know, some additional Thought going, surrounding, The creation of semantic conventions.
And… and that… that they all sort of conform to this… this idea of entities, and whether they're identifying attributes or… Descriptive attributes.
And I… I, myself, have not had a chance to really dig through the current guidance on entities yet. I don't know if anybody else on the call has, but I think that's kind of an ongoing action item.
For all of us. I think on the call last week.
I think Rutiga mentioned that, you know, hey, we need to… Kind of internalize this, this whole concept of entities and, and think about it and respond to it, from a mainframe point of view.
So, I am not personally prepared to do that, as I have really no point of view as of yet.
So…
**Antoine Toulme** 05:33 Yeah, I mean, I can talk to what ETTs are supposed to be about, which is that I can talk to the business use case. Why did they come about? Why do we need this one more type of thing? Is that useful?
**Greg Shriver** 05:48 Sure, yeah.
**Antoine Toulme** 05:49 So the problem we've had for a little while is that we've done a really good job of Nailing basic use cases for traces and metrics.
And then logs, right, to make sense.
But what we realized pretty quickly is that we repeat ourselves quite a bit when it comes to all the metric data that we send. We are studying some very rich time series data with dimensions that are the same all the time.
We're also sending the same thing for traces, where we have a lot of information that is repetitive, and it's more descriptive of the environment. So, you could think of this to take something away from mind frames that is more congenial or a specialty of Open Community would be either, let's say, an EC2 instance with all the tags of the EC2 instance and all this information, or it could be a Kubernetes cluster where you want to send all the information you have about a pod that the process is running in, for example.
And the problem we're having is that we now need to be able to send all this information in a way that would allow us to reduce a little bit of traffic of what we send. That would be ideal.
Right, so instead of sending the whole information, you could just send the pod UID, or in the case of a mainframe, it could be the host name, or whatever it is that is identifying a particular context of a metric, or spans, or log, even, being sent.
And the other problem we're having is that we need to start to be able to relate things to each other. Right now, we have a very loose relationship between things. It may make sense for us, for example.
to have some sense of, like, you know, this pod depended on that pod. This service has 3 pods. This HPA set has 5, pods related to it.
And we're not really doing that. So this is very specific to Rendering information in a context that allows people to navigate quickly, so they can do better at reducing, some of the The overarching pain.
reconciling the information with time to query.
My understanding is that for mainframe.
Just being very naive here.
There isn't such a thing as, having some pod-level discussion, or things like that. What might happen is that you might want to have more attributes which are very specific to mainframes that will allow you to perform additional inflammation. So… I would hope that you're not going to be in the thick of things as much as people who have to define You know, how… how do we identify a part… how do we identify a service, and how do we identify your host?
So… I think this makes for a good discussion.
And then I… I think it calls out to the expertise of people working mainframes, such as you, yourself, to Maybe think about, like, some of the concepts that you'd love to shore up.
And associate them with metrics and traces so that they can really become more contextual.
**Greg Shriver** 08:53 Sure.
**Antoine Toulme** 08:55 That's my read of this.
**Greg Shriver** 08:57 That's interesting.
**Antoine Toulme** 08:58 it blends into semantic conventions to some extent. Semantic conventions were just, here are some key-value pairs you should expect on some of the signals that should come in that particular situation.
And so there is this notion of taking the existing semantic conventions and then slightly moving them into a separate object that can be circulated at a different clip, right? So it doesn't have to be sent with every metric data point, so that we can save some of that bandwidth and overhead that we're having to deal with right now.
**Greg Shriver** 09:27 I see.
**Antoine Toulme** 09:29 But that's…
**Greg Shriver** 09:31 So… I'm crowing the lines a bit, I'm not sure if I'm alright.
No, that's… that's very interesting. That's certainly, you know, that perspective certainly helps for me.
from the semantic convention's perspective, my… I mean, and maybe this is a naive assumption, but I thought that, That there were semantic conventions that were resource semantic conventions that cut across all the signals, and then there were other semantic conventions that are, you know, not necessarily, you know, consistent.
Across, across all signals, and that some of the resource semantic conventions were… some of the resource semantic conventions were required.
Is… is this… how is… how are entities related to that, and… and are… And, and is it, can you kind of… can you kind of compare and contrast, like, the… the resource semantic conventions versus, identifying attributes. Are they one and the same, or…
**Antoine Toulme** 10:41 Yeah, I think this, I think what's going to happen is that the resource attributes that will fulfill the identification of a set of metrics will map 11 to the identifying attributes that are in the entities moving forward.
Okay.
I think we're making a really hard bank-left type move, where we're like, okay, we had a very good path where we wanted to stabilize on having a set of common signals, and then some attributes that were going to be common across all, and we did a good job of defining that and all that. And now we're like, oh my god, we made a mistake because we're selling way too much, so can we.
**Greg Shriver** 11:17 Good so much, Jim.
**Antoine Toulme** 11:18 Can we make our way into this? And I think there's a lot of uneasiness about that in general. Like, that might be me.
reading into this too much, but I think the entity's work is kind of showcasing that We… we can… We can simplify a little bit the data model of everything else if we do a good job there.
I don't think… I don't think so many convention is going to change anytime soon, just because entities are just not ready at all, as far as I can understand.
**Greg Shriver** 11:47 Yeah.
**Antoine Toulme** 11:49 Positioning yourself early for entities might make sense to have, well, this type of understanding in the first place, but the other is, even just by itself, this is a signal that has value.
Right? Because imagine you don't send any metrics, traces, you have none of that, but you just send… then you can say, I have 10 mainframes, I have 10 hosts, I have, you know, 10 pods, I have… I have this relationship between them. And that's already useful, because you can populate even a very simple, you know, paste my admin type table or something, and show people, like, here's what I have.
So there's another uneasiness here, which is that, and something that I felt when I joined the pandemic at first, I was not happy.
That we conflated logs and events.
I actually gave feedback to the maintainers at the time and said, this is a huge mistake.
Because these are not the same things. Logs have a very different lifestyle and a different lifecycle than an event. A log is usually going to be seen as a transactional audit capability that needs to be absolutely sent to the backend for legal reasons, and needs to be dealt with in a certain capacity.
It can be parsed for severity, it will have a number of metadata associated with it, and we need to send it to the back so it can be also, like, associated with traces and metrics and whatnot.
But events are a different beast. They're, structured data that have, maybe a, you know, point in time where they're useful, but not 5 minutes after. They, can actually be correlated to multiple things.
And they should be dealt with as if they were rich events that can really carry a lot of meaning. And that's kind of what's happening, is that, The entities are kind of built on top of the log model.
And we're just sticking a JSON in there.
that thing that, that elastic band is being stretched a little bit, then we'll come back and bite. That's just… I'm just… I know how eventually everybody just over-specifies everything, we'll get there.
So… Yeah.
Maybe also, like, give an idea of, like, where the big works are for Overall, in the project, is if you look at the fourth profile. There's the fourth signal profiles. It's trying to go from being very alpha-centric, maybe a bit… to something that is a bit better.
But what happened during that is that they found out that their model was very repetitive, so you could have multiple, multiple times SIM data in one particular profile object.
So they started to over-optimize by having dictionaries that live at the resource level, at the top level of the payload. And those dictionaries are going to be a list, for example, of… all the… A list of all the strings that are in that profile data.
And then the profile itself is just a reference that is line 3 of that dictionary, line 5 of that dictionary, line 10.
**Greg Shriver** 14:56 Oh.
**Antoine Toulme** 14:56 We're having a bit of an issue where we need to kind of be better about being semantically right first before we try to optimize.
So it's… I think this colors the debate just a little bit, because it makes it a bit uneasy. Where do we want to go with entities and profiles, too? Right? That's also a very valid thing. We need to think about that.
And then we have other SIGs that are starting to sprout. One of them is the browser SIG, which I think is getting a little bit of attention, because it's new.
But also, it's showing that we need to pay attention to that. If we don't have a story for browser, then do we really get telemetry? I mean, this is a bit of an issue.
So if you combine all this.
Entities is going to be the one thing that is going to be the slowest in all, because they have to absorb the complexity of all the other initiatives as they go.
Mainframe included, right? You could come up with, hey, we want all this information for mainframe.
And then.
**Greg Shriver** 15:52 Right.
**Antoine Toulme** 15:53 We're like, oh my god, we need to rethink the common… the common ground we have together to make sure we are getting the right requirements for mainframes.
So, I think we are, we're on a path, we need to just be good about it, and the existing semantic conventions with all the resource attributes are great for us, so we can… We can continue to operate, even, as a functional project, but there's just a lot of, uneasiness about making sure we're getting that right in the background.
**Greg Shriver** 16:22 tomorrow.
Wow, that, I mean, that's interesting, and… and thank you, thank you for sharing, for sharing that, that perspective.
**Antoine Toulme** 16:32 Yes.
I don't know everything.
**Greg Shriver** 16:36 Well, no, I get that, but, No, what you've shared, I think, is… Is very helpful, at least for me. And, It does beg a couple questions, though. Like, first, like, we're kind of… I mean, I know we've been working on the mainframe SIG for a while, but we're kind of at the beginning in the mainframe SIG, right?
So, we almost need to know, like.
how do we describe a mainframe, right? How do we describe that, and how do we do… and should we be targeting the semantic conventions as they exist today, and as our customers are using them, and as all the backend observability vendors are using them?
Or, you know, how do we strike that balance between what's there today and what might be there tomorrow in a post-entities world, right? And how do we… how do we get there And, you know, and what are the timelines like? I mean, what, you know, how long before we think that entities will be… will be ready, right?
**Antoine Toulme** 17:48 Yeah, no, I think entities are somewhat ready, actually, on that scale.
**Greg Shriver** 17:52 Okay.
**Antoine Toulme** 17:53 It matters more, like, the adoption of that, and how you emit them from various instrumentations, but that's up to… to us to do. I think what this mainframe SIG should really hone on is the use cases, such as what is a particular user of a mainframe going to care about in terms of what they want to see from an OpenTelemetry implementation, so… You know, we could even just, create some really fictional interface, where you're a customer, and you take feedback, for example, and you just put some comments there, like, I'm a mainframe user, and I want to see how things are going in my mainframe.
Now, drawing on your expertise on mainframes.
What are the 5 things that you do first when someone tells you, go check box, you know, 1 to 3 over there. Like, go for the CPU? Do you go for, like, number of users active on there? This becomes more of a really good discussion about expertise about this. So, would you be able to, think about… User, type of user who's going to use this telemetry.
what job… what job is to be done? You know, it's very simple, like, a line. Like, I am… I'm Bob, I need to see what is causing a process not to start with Intrude, something like that, right? And… and just line them up in some sort of a semantic sense, and then you can start to shop around for how to actually solution that, right? It could be, I think mainframes need to have more metrics, so you could just do a roadmap, it's like, I need to have all those metrics exposed, and they're only exposed in some ways, not mainframes, or… then you can do a research where you map them to the host metrics receiver, which is using GOPSUTL under the hood.
which does very basic Linux-type queries on the OS.
Is that good enough? I don't know, right? And then you would, You would pretty much be able to be coming to a semantic convention meeting and say, here are all the requirements, help me make the mapping to the existing validation, and what the existing means by which a project goes about implementing this functionality, right?
and then hear them out and say, okay, well, there's a gap. You know, we don't have this type of network interface, or we don't have this use case covered properly.
And then we can define what entities are missing for that. I think that's the way the mentoring seek to have a good time.
I know it's complex.
**Greg Shriver** 20:24 Yeah.
Yeah, it is, it is. I mean, just to give you an example, and I don't think… I don't think the mainframe is unique in this, but the customers that we work with, they don't care about the mainframe or Kubernetes, they care about their applications.
So, so they could… I mean, they care that something is running on the mainframe.
But they're more interested in having, you know, visibility into all of that, and what's affecting their, you know, what is causing the slowdown that they're seeing, or the unavailability that they're seeing. Is it related to the mainframe, or is it not related to the mainframe?
I don't think customers, at least the ones that I've worked with, I don't think they go in and say, well, how's my mainframe doing? I mean, unless they have reason to even ask the question, which is, why is my application not submitting payments as fast as it should?
**Antoine Toulme** 21:25 Yeah, what is my queue backed up?
**Greg Shriver** 21:27 Yeah.
**Antoine Toulme** 21:29 But, yeah, this is interesting, because this is the… the… so… That would be a great SME discussion with mainframes, is, like, to understand when… when does mainframes start? When does mainframe stop? Is it just a host discussion? Or are we having a discussion about queues? Are we having a discussion about, you know, transport? Application-level stuff? I am not that person. I don't know how to help you there. But I think if you… if you frame it this way, which is, here are the problems we see, you're going to get pretty far into… into this. And it's entirely possible that, you know, for example, you go and say, well, everything that we care about here is going to be written in some popular language of Java, Python.NET, right?
So therefore, can we find out whether this is specific to mainframe, or is this something that the Java SDK should be able to cover?
And then you can have a mapping discussion with them. It's like, here are my five requirements for Java instruction applications. I want to make sure that if the queue is full, I want to be able to do that. And then the Java folks may come back and say, well, that requires an instrumentation that's specific to this type of software the mainframes will run.
So that we can monitor the Q metrics, example, right?
Or… and that becomes more of a discussion of implementation, where the mainframe SIG is, like, we're getting to sponsor that we want to have an additional set of metrics. So, a good example is, we have a JMX-type integration in Java that allows you to.
**Greg Shriver** 22:56 Great.
**Antoine Toulme** 22:57 demo process, and get metrics out of them.
One of the target systems might be something that is specific to mainframes, but we don't know yet, right? So, you could sponsor that and say, we, mainframe SIG, think this is the important part that we need to do, right?
And because you're, you're so… you saw across multiple dimensions here. You could say, I want the collector to go and do a better job enforcement receiver on mainframes, and give you some use cases. You could go to the Java people. I want you to do better with GMX. You could go to Python folks. I want you to do better in terms of integrations, and see your CPU reporting on mainframes is different on that.
Do a better job there.
So, I don't know, where you want… again, I think, do you have a… Git repository for mainframes?
**Greg Shriver** 23:43 We do, yeah.
**Antoine Toulme** 23:45 Okay, so… It's archived.
**Greg Shriver** 23:49 Oh, wait a minute. Now, so we had a specific repo for the mainframe SIG, and we did archive it.
I think right now, we are trying to fit directly into just issuing pull requests against Oh, jeez, where is that?
**Antoine Toulme** 24:10 multi-conventions?
**Greg Shriver** 24:11 Yeah, I think so.
**Antoine Toulme** 24:13 Okay, that's fine.
But in departments, you don't really have any… Maybe you could… Push some stuff to the spec as well, where you're trying to… Underline the use cases that you want to support for mainframes, right?
**Greg Shriver** 24:28 Yeah.
And we had the beginnings of some of that in some Google Docs.
**Antoine Toulme** 24:33 Perfect. You know, and some, and some Google Sheets where we kind of tried to.
**Greg Shriver** 24:39 You know, blast out some of the, you know, time series metrics and things like that.
Great. And our thought was that we would… that we would take, you know, pieces of that and try and work them in, you know, bit by bit into the existing semantic conventions.
**Antoine Toulme** 25:00 Oh, that's great. Did you try to… One thing that works well for this type of stuff is just opening, peppering the repository with issues, just to have one issue, one line of your sheet.
And this way, kind of help also people come around and be part of the community by helping you out, and… And it helps also with reviews.
Because I just came out hot from a review discussion where We had 15 GitHub issues.
The discussion is no longer… How's maintaining this spreadsheet, how we go about this? More like, okay, you know, GitHub issue, yes, no, yes, no, yes, no, yes, no, right? Very simple.
dedicated to this, you could ask for… That might help you speed up the adoption rate, make sure you get more people involved. These open source projects, the only thing that works is getting more people involved all the time, right? The life or death of an open source initiative is how many people you're able to include into your discussions.
Anyway.
**Greg Shriver** 26:00 Blessing.
**Antoine Toulme** 26:01 Simcov.
**Greg Shriver** 26:03 So you're suggesting that we open up issues?
Yeah. In the semantic convention, and just, you know, kind of state… state our path? Is that… is… is that the recommendation, the guidance?
**Antoine Toulme** 26:15 That's what I tend to do.
**Greg Shriver** 26:18 Okay.
**Antoine Toulme** 26:20 But, you know, I don't expect things to just, they're not really going to take you up for it, but… I find that to be a valid approach to… I'm coming from the Apache Software Foundation, where they had a thing, which is, if it doesn't happen on the mailing list, it didn't really happen.
**Greg Shriver** 26:41 Yeah.
Okay.
Yeah, yeah, no, I understand.
**Antoine Toulme** 26:46 It's not like I have a great, inspiration here, I'm just trying to… to find that if you use this avenue for discussion, the processes are well-horned, and they know what to do. If you apply your own spreadsheet, or you have a Google Doc, or you have some ideas about how to go about this, but it's ever so much removed, one step away from the main way that you engage with community, then it dies on the vine. It's difficult to keep up, and… and then you start to have misalignment over a period of time that's long enough, where you're like, oh, entities? What do we do with that? Like, what's going on with this?
**Greg Shriver** 27:21 Okay.
**Antoine Toulme** 27:22 Otherwise, you know, just looking at the issues, even the same kind of people might feel like they need to bring you along for the entities discussion. They might not right now.
**Greg Shriver** 27:33 Okay. So they're, they're very.
**Antoine Toulme** 27:37 They're very good about it, but yeah.
**Greg Shriver** 27:40 Interesting. Okay.
Okay, well, I appreciate that.
**Antoine Toulme** 27:46 No worries. Another thing which is a bit more like a hammer, mid-nails-type discussion, but… Uppendemetery allows you to create projects in GitHub, and those projects, you can have transitions between them, and you can have, like, label to select which issues show in a project, and those issues can be across multiple GitHub repositories.
So if you would like to track the work of this mainframe SIG in some project, you can. I'm sure you have one, don't you?
That might be present to us here.
Alright, so here's a fun one, right? If you go to the Simity Conventions repository right now, and click on the projects tab, you'll see that there's 1, 2, 3.
8 projects open.
To pick one that is fun and maybe a little flurry, there's a CICD SEMCOM Phase 1 project.
If you click on it, you'll see that there's just a number of things in there, and some of them are not done, some of them are done, some of them are in progress or something.
But you see how this helps people situate themselves and can start to participate in the project, for example?
Because if I care about CICD, and I don't know any better, I'd jump on that project, be like, okay, well, what's to do? Oh, discuss the addition of test suite point ID attributes. Alright, let's click on that, and there's this… You know, discussion about, like, what we're trying to achieve here, how do we go with that, and then we can talk about, like, how to recite people, we… Etc. And this becomes maybe a bit easier on you?
**Greg Shriver** 29:23 Because as someone who's caring about this, it's really difficult to kind of.
**Antoine Toulme** 29:28 Wrangle everybody together.
**Greg Shriver** 29:31 Sure.
Yeah, I do see that.
**Antoine Toulme** 29:37 I have to run. I fully.
**Greg Shriver** 29:39 Yeah.
**Antoine Toulme** 29:40 this tool.
**Greg Shriver** 29:40 Me too, me too, but I, I appreciate, your… your thoughts, and I will do my best to try and summarize them in… Our meeting notes, and when we have a bigger quorum, maybe next week.
I'll try and, if you're not there.
I'll try and articulate your thoughts and your suggestions. And I'll try and get them in some sort of consumable form so that everyone else can see them.
**Antoine Toulme** 30:08 Greg, I think we can get the transcript from the recording.
**Greg Shriver** 30:11 Yeah. Oh. Yeah. Yeah.
**Antoine Toulme** 30:14 That's just… I don't want to do any work. I don't… I really despise, talking for half an hour, then realizing, oh man, we should have.
We should have done this into a written format, but yeah, I agree. If we can continue this discussion next week, some form that can help. I'm only here to help, I don't want to give you work, I did not mean to get you on the sidetrack, but… You keep me talking, I'll just keep talking until the end, so… Sorry.
**Greg Shriver** 30:44 Alright.
So, and did I… did I mention… did I, did I pronounce your name right? It's Antoine?
**Antoine Toulme** 30:50 Yeah, that's right.
**Greg Shriver** 30:51 Okay.
Alright, Antoine, well, nice to meet you, and And, thank you for the discussion.
**Antoine Toulme** 30:58 Have a good one, Greg. Take care.
**Greg Shriver** 31:00 You too. Bye-bye.
**Antoine Toulme** 31:01 Bye.
