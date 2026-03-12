SIG: SIG Injector
Date: 2025-08-11
Duration: 25 minutes
============================================================

## Zoom Recording Transcript

**Antoine Toulme** 04:31 What else would be….
**Satbir Singh** 04:38 Hello?
**Antoine Toulme** 04:39 How you doing?
**Satbir Singh** 04:40 Jon, how are you?
**Antoine Toulme** 04:42 I'm okay.
**Satbir Singh** 04:46 So, you are with Splunk?
**Antoine Toulme** 04:48 Yes.
**Satbir Singh** 04:49 Oh, I'm also with Splunk.
**Antoine Toulme** 04:52 Well, welcome.
**Satbir Singh** 04:54 Yeah.
So, I was part of AppDynamics, but recently AppDynamics was merged with Splunk, right?
**Antoine Toulme** 05:00 Yes.
**Satbir Singh** 05:01 That's all.
**Antoine Toulme** 05:03 Well, it's great to meet you.
This particular discussion here is all about the Open Telemetry Injector project, which we donated about… It was at least 3 months ago.
**Satbir Singh** 05:14 ….
**Antoine Toulme** 05:15 Yeah, there's two… You know, we wanted to have streamed some of the code we depended on that was used by us for autonomous implementation.
**Satbir Singh** 05:23 And to make it easy for people to adopt open telemetry.
**Antoine Toulme** 05:27 So… What it does is that it allows you to Using a Debian RPM package, install a preload.so type hook.
It can intercept creation of processes on your host.
And inject environment variables that point to the Java SDKs, the Node.js SDK, or the… I think Python, not quite yet.
the .NET SDK to, … To inject those agents into the runtime of the processes before they even start.
And then those agents are able to do all sorts of introspection to the code and the runtime to start to inject traces and find metrics that they can export, and start as part of the normal running of a process, so… We've had, really great success with, you know, big cooperations of machines, where they don't have time to find what's running on what. They don't want to, actually, and they would just install this package to, you know, thousands of machines at once, and they would start to report in, and they would start to give us a lot of information about what is actually running on them.
And that was at minimal cost without involving developers.
So this is a really good adoption tool for OpenTeametry. It's critical. There is a part of it that eventually would be somewhat transversal to Docker and communities environments, because the same approach can be taken in a communities environment. We just need to continue to work to make it as… Simple as possible.
That's where we are. What's your interest into this project?
**Satbir Singh** 07:07 Yeah, so actually, I've never contributed to open source projects, so I recently started exploring it, and I added all the meetings into my calendar.
**Antoine Toulme** 07:20 Nice.
**Satbir Singh** 07:21 Today, this is my first meeting, so I just joined this meeting, and trying to see how can I help.
I'm part of customer engineering team, So, I'm just trying to explore how can I contribute to open source, and how can I help, Because I'm not able to understand, like, Where to start, ….
**Antoine Toulme** 07:44 Yep.
**Satbir Singh** 07:45 As a first timer.
**Antoine Toulme** 07:48 So… The OpenTeometry project itself is part of the CNCF, right? So it's a big umbrella of Linux Foundation-type projects. Linux Foundation is known as a type of pay-to-play type projects, where you can sponsor, you can have companies actually participate in making sure that you get the best. It's not… It's not as, open-ended as, let's say, Apache, or it's not as, like, free software, like GPG or, GPL-type software.
… for the CNCF, it's important to have a little bit of a… it's kind of a place where you don't really compete with your competitors, you collaborate with them.
Because you're trying to close a gap in functionality, or you're trying to make a market commoditized? In the case of OpenTeametry, we're trying to make observability a open market, because we realized that people were not adopting.
**Satbir Singh** 08:36 telemetry.
**Antoine Toulme** 08:38 Because they were like, this is too complex, and there's too much vendor lock-in. So, we don't really play hardball with anyone, we're not trying to… computer out anybody, but the sheer size… what happens is the speed at which OpenTelementary innovates and moves forward is also helping other vendors to either adopt it or to kind of be driven away because their vendor lock-in solutions cannot compete with OpenTelementary long-term.
We see a lot of adoption across a lot of customers, specifically in, like, finance sectors and things like this that need this type of functionality around auditing, around having a better view of what's going on.
So, for you to help, in this project, we have many different sub-projects you mentioned, like, you join one particular meeting, but there are many.
**Satbir Singh** 09:27 And….
**Antoine Toulme** 09:28 they kind of reflect on around the different technical artifacts that we're trying to ship, right? So we have one… we have this project for this injector, we have one project for the collector, we have one for the JavaSig, we have one for .NET, one for Node.js, one for Python. They all have a little bit of a different approach to things, because they're made of people who are different, coming from different backgrounds.
And you have a little bit of specialization in the project space, right? So, you wouldn't even go about a feature the same way.
**Satbir Singh** 09:57 ….
**Antoine Toulme** 09:59 the… the way they work is going to be based on your interests, so if you're a Pythonista, for example, then, you know, there's definitely some room for you to go help with Python.
the projects themselves have different levels. So, for each project, you're going to have a population of people who are going to be maintaining the project, and maintaining is just from… the core of that is that their job should be to just merge PRs all day, right? And making sure the domain is not broken, and the figs work, and they're able to kind of help people get their data in.
Then you have approvers. Approvers are here to prove, you know, they actually do the full review of the PR to make sure everything works, and they have… They aspire to become maintainers one day, maybe, but for the most time, they're just trying to make sure that their stuff, whatever changes they value, in terms of maintenance or the features they're trying to land, get in.
And then you have triagers. Triagers are people who have, access to issues, they can review issues, they can make sure that things are working, they can triage PRs, just by adding labels and comments.
And those three measures are key to a project when you scale up, right? Like, the collector project has so many PRs a day, and lots of issues.
**Satbir Singh** 11:16 ….
**Antoine Toulme** 11:17 And then you have contributors who are just members of OpenTeametry, so there's a slight difference between… if you never contributed to OpenTeometry, you're trying to make a PR today.
you'll see that the CI doesn't run, because GitHub has security protections that do not allow first-time users on GitHub to push anything to OpenTeametry without, like, having someone click a button to run the CI for you.
Once you get in and you contribute meaningfully, meaning that you have 5-6 PRs, and you… you can become an open territory member. An OpenTemitary member has the ability to be tagged on issues, you start to have much more of a voice.
**Satbir Singh** 11:56 If you contribute a little bit during the year, you can also vote.
**Antoine Toulme** 12:00 for representatives of the open terminology projects for the CNCF, such as members of the governing committee and members of the technical committee.
So, it starts to pay off a little bit, where you have this sliding scale of involvement, right? You can send a batch, you can become a contributor, you can become a member, then you can become a triager, approver, maintainer.
**Satbir Singh** 12:22 And you can vote for GC, DC people.
**Antoine Toulme** 12:25 So, the more people who do that, the better we are. The type of fixes and the type of changes that you might want to contribute depend a little bit on your skill set and what you like to do, but usually we tag issues that we want help on with the help wanted label.
So, you know, for the collector, for example.
We have this, help wanted tag, let me just put it in the chat for you.
… Right, so we have this type of issues that we try to get people to kind of come and help us with.
… Some of it may seem simple, some of it is not that simple.
But this is a great way to kind of get your toes wet with the project, and if you have any questions, feel free to reach out to me on Slack or WebEx, whatever.
We also… So, besides this, right, so we have these meetings for OpenTeometry. I am, at Splunk, also responsible for making sure we get the collector out. That's kind of my job as a… I'm on the product side now, I used to be engineering manager.
And every Wednesday, 8.30 a.m. Pacific Time, we have office hours, where we try to help Splunkers and Cisco… CiscoNians. If they have any issues, anything they'd like to bring into the OpenTech project, they can you can come talk to us, right? So we kind of have this open-ended session. It's a great way to learn a little bit what's required, what's needed.
So… If you're interested, I can forward you the invite, and, you know, it's completely optional, you don't have to participate if you don't want to, but it's great to know that it's there, and it gives you an anchor point during your week where you know you can come ask questions.
**Satbir Singh** 14:08 Sure, so, yeah, I'm dropping my email in the chat, if you can… Yep. That would be great.
**Antoine Toulme** 14:16 Yes, I'm forwarding you the invite, so, for… It's been working.
Oh, there you go.
And that's all… that's up to you.
**Satbir Singh** 14:40 Yeah, I see that. Thank you.
**Antoine Toulme** 14:43 No worries.
**Satbir Singh** 14:44 So this is, this is, like, internal, Cisco internal meeting that we have, because I… I attended one more meeting, like, couple of weeks back, and I saw a couple of, Splunk guys who were in the meeting. I did not get a chance, because it was a very busy meeting.
But it seems like Splunk is contributing a lot to open source, that's really great, and… I want to see how I can maybe, say, some internal Slack channel or something, I can be part of that group and see.
**Antoine Toulme** 15:16 Let me add you to the right places.
I'll just invite you in here.
You can ask any questions you like, anytime, but… Said VIN.
**Satbir Singh** 15:37 So, I'm part of the Slack, let me… Yeah, I see.
**Antoine Toulme** 15:45 I just studied you to a channel.
**Satbir Singh** 15:50 Hmm.
**Antoine Toulme** 15:51 It's been a bit quiet, but feel free to ask any question here. The only… the other channels more open-ended is the OpenTimity channel.
You can ask questions there.
For what it's worth, we have 11 maintainers at Splunk. We have… something like 71, contributors for Smoke.
We contribute over 50% of the code for Pandemetery.
So we are very much on top of it, and this is important to us.
That's it, you know, we… we brag about those numbers internally to our own self, because I want to make sure that people know how much of a effort we're making and how much it's driving. But we… we don't… we don't want to discourage people from joining, so we… we are… We're roughly at 50%, but then you see also Microsoft being quite there as well. You have all the companies, all the vendors playing along. So, you know, what we would want is to get even more people to show up, not to reduce our… We don't want to reduce what we do, but we would like other people to match up to our energy level and bring more people to help.
**Satbir Singh** 16:57 Yeah, yeah, yeah.
Definitely I'll be interested, because… so I, I'm, just to, … share my… what kind of experience I have. So I had, like… I worked as a Java developer in the past, but, like, for the last close to 10 years, I'm more into customer engineering, where I'm helping customer Resolve AppDynamics issues and helping them implement the product, yeah.
….
**Antoine Toulme** 17:23 Do you work with, … Is it FIRU? Hang on, I gotta forget.
Mate.
Memory's gone.
**Satbir Singh** 17:34 The downside is Crystal is, I think, the….
**Antoine Toulme** 17:39 Typically, the name I'm looking for is in the character, and that's what? Firu.
**Satbir Singh** 17:47 Yes.
**Antoine Toulme** 17:47 And, … I also work quite a bit with… Horseshit Rashput.
**Satbir Singh** 17:54 Yes, yes, I work with those guys.
**Antoine Toulme** 17:57 So, we have an ongoing meeting on a… I'll invite you to that, too. We have a SWAT discussion every other week.
I think it's also worthwhile for you to get in on that. At least know that this happens.
**Satbir Singh** 18:10 ….
**Antoine Toulme** 18:11 So… I'll just put you in.
… This way, if you have any… so if you have any questions related to a pontemetery that, you know, we need to address as part of those ongoing tickets, in terms of maintenance and customer things and all that, you can join that, and it will be helpful to discuss.
**Satbir Singh** 18:35 justice, elderly.
So, Antoine, so you are based in, Bay Area?
Okay, good. Yeah, I'm also in Bayer.
**Antoine Toulme** 18:47 Yeah, I'm in San Jose.
… Okay, well, the… this is the first… I mean, the reason there's just two of us is this is the first meeting for this particular SIG. I've been trying to get it on the agenda, make sure that we start to advertise about it, but… So far, I haven't been very lucky. So, I hope that coming out of August, we'll have more people show up for this meeting, but… For now, it's, it's a little dead. So… Well… Y-yeah. Happens.
**Satbir Singh** 19:27 Yeah, yeah, yes. Yeah, I've been to a couple of meetings, I did not see anyone in those meetings.
**Antoine Toulme** 19:32 Yeah, I mean, it's August, right? It's kind of slow right now.
Like, a lot of people are still out. So I would just, there are meetings which are more, let's say busy, maybe collector meetings, Just today, let's go today, what do you have?
I think, contributor experiencing is not quite lively yet.
… No, no, no, for JavaSig, so since you were a Java developer, the JavaSig on Thursday is always well attended. There's lots of discussion there. I think there's also a lot of, help we could use.
We, we're trying to land, IBM MQ support in Java Contrib, for example.
So we're… we'll be looking to get help on that. Like, there's just a lot of… things to… Get mature, which are not there yet.
True.
**Satbir Singh** 20:31 So, Java, I see it in Thursday, right?
**Antoine Toulme** 20:34 Yeah, at 9am.
**Satbir Singh** 20:36 Thursday at 9am, yes, I see that in my calendar.
**Antoine Toulme** 20:39 I have a… I'm double-booked on that, I have to go to the operating.
**Satbir Singh** 20:44 Yeah, so I'm not able to understand, like, which meetings to attend, because I added a CNCF and open telemetry calendars on my Gmail, but there are so many meetings, I don't know which one to attend and which one to….
**Antoine Toulme** 20:57 Yeah, I mean, it depends on your interest, right? I mean, if you go to a semantic conventions SIG meeting, it's going to be a bit weird, because, you know, the first meeting is… you don't understand what people are talking about.
**Satbir Singh** 21:07 Yeah, yeah, yeah.
**Antoine Toulme** 21:08 It's very arcane. Reading the… on each of those meetings, there's an agenda doc you can read that can give you an idea of what is happening, and people try their best to put agenda items before the meeting so that they can, well, first get a chance to talk, because if you're not listing your item on the agenda, you don't get a slot.
And, maybe gives you a little bit of context of where's it coming from. But you're going to have a hard time piecing out the context coming from the outside for semantic conventions, for example.
For JavaSig, it might be more mundane. It's like, hey, we need help to kind of get the result, we need help with those bugs, we need to do some triaging, we got this annoying report about this issue with that thing.
I think it will come… It will be more relatable for you, because it's less arcane and abstract.
**Satbir Singh** 21:54 There's a lot of meetings that are about specification.
**Antoine Toulme** 21:58 more than an actual implementation. So, for example, at 8 AM on Thursday, there's a Java declarative configuration meeting, and the point is they're trying to make it so that the agents right now can take configuration from environment variables, or CLI arguments, something like this, but they want to take it so that they can do a declarative configuration, which is a file-based configuration.
Now, that file's gonna have to have some sort of a format that people need to agree on. Is it YAML? Is it JSON? Is it something else?
That file needs to be complete, what do we put in that file? How do we make it so it's the same file between, let's say, Java and Python? Where does it become more Java? Where does it become more Python? What can we put in comma and things like that. So they're talking about all those different aspects, and they hash out, like, line by line, what's going to go in there.
might not be that much your cup of tea right now, right? So, if you want to start just fixing issues, I'm so happy to… I can talk to… so, on our end, right, at Splunk, we have a guy called Jason Plum, who's been very involved with Java, who's a maintainer there.
just let me know the Slack channels that you just joined, I can ping him and let him know that you're interested to help, and he will have Java issues for you that you can take a look at, right?
**Satbir Singh** 23:17 Sure, sure. Yeah, that, I'm open to that, yeah, because the thing is, so I'm, … I'm just starting, so, but I think it will be definitely be a great learning experience for me, and I'm willing to spend time, I mean, it will definitely be taking time initially, but I think, I'm just eager to contribute there.
**Antoine Toulme** 23:43 Yeah, no worries. Let me just send a message right now.
**Satbir Singh** 23:52 Yeah, good thing is I got to talk to you today, because I joined a couple of meetings, either there was no one there, or there.
**Antoine Toulme** 23:58 Yeah, that's disrupting me.
**Satbir Singh** 24:00 Yeah, I wondered.
**Antoine Toulme** 24:04 It is what it is, weird.
Just make do with what we have at this point. But yeah, … I offered him to attend.
to Jesse, on Thursday… Would you please… would you have… Any… I have volunteered.
desks.
Feel free to involve him.
Alright, it's up to him.
Okay.
Or I'm gonna call it short, I mean, there's no one showing up, and I don't want to take more, like, I have to… I have to run to my next thing, but yeah, I'll see you around. I've got you on a couple meetings, and, worst case scenario, Jason's gonna have stuff for you. For sure.
**Satbir Singh** 24:57 Sure, sure Thank you.
**Antoine Toulme** 24:59 Thank you for your interest. Have a good one.
**Satbir Singh** 25:01 Careful.
