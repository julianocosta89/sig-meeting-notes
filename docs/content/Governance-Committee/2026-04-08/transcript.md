SIG: Governance Committee
Date: 2026-04-08
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Trask Stalnaker 00:00:45 Good morning.
Marylia Gutierrez 00:00:48 Pardon.
Austin Parker 00:00:48 Morning.
Ted Young 00:00:50 Hello, hello!
Jack Berg 00:01:02 Is today a joint GCTC meeting? I think that's what the calendar says.
Austin Parker 00:01:05 That's what the calendar says.
Ted Young 00:01:06 It does.
Jack Berg 00:01:09 Alright, I'm in the right place then, I think.
Ted Young 00:01:11 Yeah.
I think the idea was to even have, some guests from the… From the, system packaging SIG.
Tigran Najaryan 00:01:35 Hello, everyone.
Pablo Baeyens 00:01:39 8.
Alolita Sharma 00:01:43 Hi, everyone. Good morning.
Ted Young 00:01:46 Moaning.
Josh Suereth 00:01:47 Morning or afternoon?
Alolita Sharma 00:01:54 Pablo, did you have fun at KubeCon? It was nice to see you.
Pablo Baeyens 00:01:59 Yeah, it was nice. It was very tiring, but it was…
Alolita Sharma 00:02:04 Yes, I think it was. I think… I think there was also a fair bit of flu and stuff going around.
Like, they were…
Ted Young 00:02:13 I had FOMO until I heard about that aspect of it.
Alolita Sharma 00:02:16 Oh, gosh, you didn't miss that. It took out the.
Juraci Paixão Kröhling 00:02:21 Are we talking about false, then?
Alolita Sharma 00:02:24 Do your ass.
Juraci Paixão Kröhling 00:02:27 What if I'm late.
Alolita Sharma 00:02:28 Boston was well, probably worse.
Ted Young 00:02:30 The Boston flu?
Alolita Sharma 00:02:33 the flu, you always…
Austin Parker 00:02:34 Mmm!
I didn't get the flu, but I did have, like, some weird viral thing for a week that was very unpleasant.
Alolita Sharma 00:02:41 Maybe, maybe it was a viral thing, I couldn't, you know, it was just…
Austin Parker 00:02:46 Yeah, I don't know. It wasn't… I tested, it wasn't COVID, it wasn't flu A or B, so it was either a type of flu that didn't get picked up… On the rapid test, or…
Alolita Sharma 00:02:59 It wasn't COVID, for sure.
Marylia Gutierrez 00:03:01 when they.
Austin Parker 00:03:01 You see that?
Marylia Gutierrez 00:03:02 the ticket was all-inclusive, I was not counting that that one includes…
Alolita Sharma 00:03:07 Can he say?
Marylia Gutierrez 00:03:08 But, sure.
Austin Parker 00:03:10 Conrad, it's back!
Alolita Sharma 00:03:13 part of the package. Yeah. Hey, nonetheless, it was very nice to see everybody.
Austin Parker 00:03:20 It was.
Alolita Sharma 00:03:22 We did good, our hotel booth was very popular, and our SIG meetings were also very nice.
Austin Parker 00:03:30 It was…
Ted Young 00:03:30 Yeah.
Austin Parker 00:03:30 The weather was really unpleasant.
Alolita Sharma 00:03:33 Not super pleasant. It was really cold.
Austin Parker 00:03:35 old.
Alolita Sharma 00:03:35 old.
It's like, I should be in Chicago.
Ted Young 00:03:40 I definitely learned that, like, if I can't make KubeCon, it is the best week to take a vacation, because…
Alolita Sharma 00:03:47 Nobody's there.
Austin Parker 00:03:48 Yeah, no, right, nothing's happened, yeah.
Ted Young 00:03:50 Finally go away. Yeah.
Liudmila Molkova 00:03:53 It's actually the best week to work. I mean, you can just work.
Austin Parker 00:03:57 That's true.
Alolita Sharma 00:03:59 Except, Ludwilla, you were there, presenting. Yeah.
Pablo Baeyens 00:04:05 Are we waiting for Antoine, or… We'll just have Michelle?
Alolita Sharma 00:04:12 Is he joining?
Ted Young 00:04:15 Michel, do you know if Antoine's coming? Anthony?
Michele Mancioppi 00:04:21 Let me add, did you add the Mosul to the invite?
Liudmila Molkova 00:04:25 Oh, no, let me ask him.
Sorry.
Alolita Sharma 00:04:47 Marilla Gerasi, did you get the, group photo copies of your nice Brazil… who carried the Brazilian flag? That was so cool.
Juraci Paixão Kröhling 00:04:58 I mean, there's always somebody carrying.
Alolita Sharma 00:05:00 I know! It's so cool.
Juraci Paixão Kröhling 00:05:03 Yeah.
Marylia Gutierrez 00:05:03 And that was, like, just one part of the group. There was, like, many more that were not in that photo.
Alolita Sharma 00:05:10 Wow. You're just a little disinterested.
Juraci Paixão Kröhling 00:05:12 In the photo I don't think I've seen it.
Alolita Sharma 00:05:14 eternally needed.
Marylia Gutierrez 00:05:16 No? Oh, I have… I have a bunch of them, I can send it to you. And then you can pick which one you are blinking or not, that is how…
Alolita Sharma 00:05:28 It was like a soccer match, you know? At the end of the soccer match, everybody gathered up.
Ted Young 00:05:37 Maybe while, Ludmilla's reaching out, I see maybe there's a quick item from Josh Surith down at the bottom.
That looks more like, FYI, but make sure project proposals hit TC inbox.
So…
Josh Suereth 00:05:54 Yeah.
Ted Young 00:05:55 the GC.
Josh Suereth 00:05:57 Pablo made a comment which is, relevant and why it took me so long. I gave up on trying to be clever, and so basically, any time a PR comes in that touches the project directory, it adds a label to put in the TC inbox, the TC puts a label that says, we reviewed it, when we're done.
That's good. This will catch more than project proposals. Because you can put things in the project directory that aren't, but as long as you're okay with us just saying, oh, cool, this isn't for us, we'll mark it reviewed, done, I think this is better than nothing.
That's… that's all it does. Oh, and it updates the thing.
Pablo Baeyens 00:06:29 We're barely find… Yeah, like, I was just trying to reduce noise for you, but, like… If you can limit the noise, then…
Josh Suereth 00:06:37 It'd be… it'd be better if I had figured out how to make it so it's only real project proposals, but I gave up on… on that. I went down a rabbit hole.
Liudmila Molkova 00:06:52 I pinged Anton, he does not, he did not reply yet, but he's online, maybe he will join, a little bit later. I'm sorry for not pinging him earlier.
Michele Mancioppi 00:07:03 Next week.
Tigran Najaryan 00:07:04 him on internal Slack as well, he's not replying, so I don't know.
Pablo Baeyens 00:07:11 Let's get started, I guess.
He'll do it later.
Ted Young 00:07:19 Okay.
So… the packaging SIG proposal, Lyudmila, you've been talking, I think, to Michelle while I'm out. Do you two want to set the stage for the discussion?
Liudmila Molkova 00:07:34 Yeah, I can just, say that we had a conversation at the TC call last week, and we, the conclusion was, at least my interpretation of it, that the Success of the packaging SIG is tight is related to the success of work stream of component definition in the stable by default.up.
And that, this is an important effort if the water comes through. If we are the community to agree to work on this, this is an important work we should fund.
And the key part between them is the definition of what the component is, right? And what was the stability criteria.
We need to work to find, to document and enforce the policy across essentially every SIG. And this is where we need, active involvement from the TC to drive this work through different things to help drive this through different SIGs, and… find the means to enforce the policy, right? So, once it's done, the packaging sync becomes the technical implementation for Linux, right? We could have the same, similar implementation, like, the operator would take the same policy and implement it, right?
Without this effort, packagingSeq would need to do all the work across every SEEK, and it's impossible to do without active involvement from the rest of the community through TC, or some delegation. The TC meeting showed that we want to have guiding, at least, a sponsorship level for this project.
Given this dependency, and I wanted Mikhail to talk more here, because I think we, if he has any additional thoughts, and I think he has a lot. So, Mikel, stage is yours.
Michele Mancioppi 00:09:27 And where should I start? Should I start from why we need it?
Yep.
Yeah. So… I'm going to tap into my commercial experience.
And, I have been… I'm now, co-founder and chief architect of Tarsira, where… We use the injector and effectively, the mechanics package and sync in our Kubernetes operator, which has a spectacular activation rate.
We have industry shattering conversion numbers because of that, of people that start.
Try to use it, and then keep on using their serum.
And… A lot of that is because of the, one-click-to-win mechanic. It's very plug-and-play. You say, you go there and say, hey, monitor me this, and it works. And this is because of the distributions that we prepare.
for JS, for Python, for .NET, for Java.
And we, of course, will achieve more with more distributions that behaved in a way that would feel safe packaging.
The same aspect of making it easier for people to use monitoring starts with them having an easy time.
of, saying what they want monitored. That also worked at Instana.
Instana was a company that, did automatic instrumentations with proprietary technology really right, and I would argue it was literally the best thing that Instana did.
In my experience in 15 years in the industry, I have consistently seen Two different demographics of people.
Meeting or having the task of getting observability data. Those who could, and those who could not.
And the people that could were usually the expert people capable of doing refined settings and figuring out from 5 different medium blog posts, which particular measure settings would work in their case. And that was effectively around the number of people, we're talking low decimal, single digits.
And, most of the people out there, they need the data, they don't know how to get them.
And they desperately need it.
What I say a lot inside the stereo is that an observability tool is a thermometer.
It's the meter for the health.
Of the system that you monitor.
And, none of us need to know how Mercury expands under heat, to tell us that with fever or not in a thermometer. But we're actually asking people adopting OpenTelemetry to know how to build 90% of their thermometer before they get the data they need. And I think we should change that.
Ted Young 00:12:27 Yeah.
this was, brought this up on the… the spec and community call, around how the… there… you… you mentioned these two groups, and I think a concern I have around the… the priority assessment of this project is that the contributors to OpenTelemetry are all people in the one group.
Right? And the end users we really want to build this for, who we know we exist through talking to customers and other things, for those of us who work at vendors, we know that these are big groups.
But they're… and that's the group we want feedback from in terms of whether or not we did it right, and also the group that would really advocate for it. But they're, of course, the person not in the room, generally speaking, unless we actively go out and recruit you know, like, example end users and stuff to come… to come comment on this. So I have a…
Michele Mancioppi 00:13:21 I would argue that there is no amount of outreach that will get in the room people that better know what they're doing in terms of monitoring. And it's the majority out there, and they have every right.
Ted Young 00:13:32 Great.
Michele Mancioppi 00:13:33 To have their systems monitored right.
Ted Young 00:13:36 Right. What I meant was in terms of, like, like, this is a… the… if we just ask our community what is the priority of this, we get a skewed number because of that bimodal distribution.
Morgan McLean 00:13:48 And I wanna… I just wanna echo, what both you were saying, like, it's the same thing at Splunk, where we introduced, you know, some of the components that became the injector two or three years ago, and it radically changed the uptake of open telemetry for us.
Right, because previously people had to go configure the collector. They had to go glue together all of the auto-instrumentation agents that were appropriate for each host. We built this, and now getting data in is rarely a concern of our customers.
It would be… it's essential, I think, that we make… we standardize packaging and use these concepts across the entire project.
Michele Mancioppi 00:14:22 I mean, let's be honest, Dynatrace would not be Dynatrace without the one agent. Instana would not be in Stana without Instana Agent.
And 7 years into OpenTelemetry, I think it's high time we get to that level of prioritization of the first impression.
Morgan McLean 00:14:37 Yep. 100%. Yeah, I'm in very strong agreement.
Ted Young 00:14:45 So, of course, if we didn't feel severely resource constrained, I don't think we would even be having this conversation. It would be a breeze, right? But we are feeling resource constrained in a couple of ways.
I think the primary way, you know, the TC is, you know, trying to review their workloads to figure out, you know, how we put this in, but it's one of those things where it feels like, on that front, to get more involvement, we either need to drop something or finish something.
Which is concerning.
The other groups are the maintainers, right? And then the third group is, you know, getting end users to actually try it.
The thing about those second two groups, I would say, is they're much more likely to interact with this project, if they have something to play with.
And I see some hands up Josh?
Josh Suereth 00:15:47 Yeah, I don't know if I was first. Okay, so I think… yeah, to rephrase what you're saying there, we… I think we need to kind of… expand our planning a little bit, or how we think about OpenTelemetry, the project. One of the things I've been thinking about is, when you look at the efforts we have going on.
Right now, they are kind of low-level concepts of… Sort of. Like, we're gonna focus on configuration, right?
Because we know that we needed consistent configuration across the platform. I think we might need to get, I don't know if you want to call them work streams, if you want to call them something higher than projects, but, like, stable by default's the first one that I think is really critical that we nail.
And, like, Kelly, like, what you're saying resonates with me. We need a distribution of hotel. We need, like, first packaging, like, what's that first experience feel like?
But I feel like this needs to be a effort within OTEL that encompasses a couple SIGs, and we put a couple SIGs within that effort. And that effort has a leader, and that effort is driven.
And that this would be a piece of that effort. Stable by default, I think, there's a set of things that we had in there, but, like, I would put a collector, an operator, and this injector together into, like, a mega-sig, if you will, or a pro… a…
Michele Mancioppi 00:17:09 Projects? Yeah.
Josh Suereth 00:17:10 A what?
Michele Mancioppi 00:17:12 OBI.
Morgan McLean 00:17:13 Yes.
Josh Suereth 00:17:14 OBI as well, yes, OBI…
Morgan McLean 00:17:15 Yes, all three.
Josh Suereth 00:17:16 profiler, but this would be, like, there'd be this project of, like, the OTEL distribution project or something, right? And yeah, the other SIGs would have to participate in this as well. The Java SIG, the AutoAgent, you know, like, they're all somehow involved.
But if we… if we start thinking about prioritization not as every single individual small project against every single individual small project, if we said, cool, we have this mega project, which is open telemetry the distribution.
And within that, we can prioritize projects.
It gives us a little more flexibility in understanding where we're divided and stuff. I got this from looking at… so I'm going off on a little bit of a tangent.
But, like, I think the problem here, is not necessarily whether Injector's valuable, the problem is, what do we stop doing to make sure that it's successful?
That's the question we need to answer, and if we add it, we know that something will not be successful, because we're overloaded.
So, if we add it, we just sacrifice something without making the decision.
We need to make the decision of what we sacrifice, or Injector won't be successful, because we're unwilling to sacrifice anything, right? So that's, I think, what we should focus this discussion on.
Michele Mancioppi 00:18:34 I think Pablo was raising the hand before I did.
Pablo Baeyens 00:18:38 Yeah, so I guess I'll… I'll ask you, Jos, so… My understanding from what Lutbela said was, well, you… you think there is… a need for TC involvement, and so, the TC needs to keep up on doing something else to be able to work on this, I guess is a way of putting it.
is… Is your comment specifically referring to that, or do you think, in general, as a project, like.
We need to give up on something to work on this.
Josh Suereth 00:19:16 I think it's… I think both are true.
Yes.
I would like to get to the point where the TC's interests are aligned with project's interests, and so the TC load is equivalent to project load.
That's one thing we've been trying to do with sponsorship, and so we're trying to correct that. But I also think that we need to be very focused on our efforts here within OpenTelemetry to make sure that we're building things cohesively together. If Injector lives in an island.
we don't get to the point of this OpenTelemetry distribution we want, and that's the thing we want to solve. Like, that's why I'm saying, like, maybe there's a larger effort we need to create around OpenTelemetry, the distribution. Injector's a piece of it.
And so, it's no longer injector against all these things, it's injector as a component of a good goal, right?
Michele Mancioppi 00:20:03 If I may, I actually would like to underline the fact that when you look at the idea of packaging as table by default.
The risk of the project is not injector.
And it's not OBI. And it's not the packaging.
It's the auto-instrumentations, and the languages, and the SDKs, and the experience they give out of the box. That is the risk. So when you go and say, yeah, we need a megaproject, sure, but the six that you have mentioned.
Are not the ones that have to do, the… More refined product decisions, those we have already taken.
That part, a lot of that experience is worked out.
The moment you are given good distress to auto-instrument, for example, the moment Java starts doing meaningful things to the resource detectors without having to jump through 20 hoops, the moment you sort out, for example, some of the kinks in Python, Node.js, auto-instrumentations.
That's a lot of work done, but the 80% of the work for this thing to provide a good experience to the end users is in the language 6.
The easy part, the foreseeable work, the one that I would know how to do from the top of my head, that's the 20% that is in the project proposal, that doesn't worry me the least. What worries me is the fact that we need a more product lens in the language 6 for this to work out.
Ted Young 00:21:36 Igrin?
Tigran Najaryan 00:21:39 I guess which brings to my question, what sort of work do we need within the Language Six? What do we expect the maintainers to do? Is there additional work for them, or do you imagine that you guys, and I see four names in the staffing section of the project proposal, you will be doing all the work.
That is language-specific.
What is the expectation here?
Michele Mancioppi 00:22:02 There are two different types of work. One is enablement work. Like, will we be able to activate a distro? Are we able to package the distro?
Most of that is done. We know how to activate most distros. Of the ones that I believe that we could support, and I haven't looked into it, there is Erlang.
Yep.
That part, not a problem.
What is the kind of work that the language Sikhs need to do?
is actually to align on what is the baseline of experience. For example, I was talking about resource detections. There's an incredible disparity about what an SDK will do out of the box.
to detectors' attributes, and I cannot, I cannot… State enough how important resource attributes are, especially for users that don't know really how to set stuff up better.
I'll give a very concrete example. On Kubernetes, out of the box, you get nothing useful from an SDK. Nothing.
you need to have a collector nearby with a Kubernetes antivirus processor, hoping to all gods, all the new, that the connection, pod association will work, so they don't use any service mesh.
And that is something that breaks all the time, and users get very frustrated for that.
So there is the resource detection to sort out. There is, to some extent, holding to the contract for the injection.
For example, the node SDK changed the parameters it wants to have passed to the node runtime from version 1 to version 2, because of the switch from CGS modules to ECMA modules, or to the new module system, going from required to… to… to import, and import in the middle, and a bunch of different interesting things. That is some work.
But then there is also a matter of the expectations of the instrumentations. For example, you go and automatically inject the open territory of agent.
you have a pretty solid implementation of semantic conventions, a pretty solid coverage of different languages. Most HTTP instrumentations agree, more or less, on how to annotate HTTP spellings, and they more or less generate the same HTTP semantic convention metrics, and then you put you just look at Node.js, which is probably the second most popular SDK that you have in OpenTelemetry, at least in base of adoptions in their setup.
And it's a complete opposite.
the HTTP… even the HTTP semantic conventions are the easiest to get right, and the most commonly right are there.
The Node.js is still, last time I checked, sending the metrics. It was, like, http.request instead of HTP server request, with all the histograms and attributes. I mean, there is a huge chasm there.
Tigran Najaryan 00:24:48 Yeah. What you're describing…
Michele Mancioppi 00:24:51 which libraries are implement… are instrumental or not, because in Java, I will have out-of-the-box experience to trace most database drivers. In Node.js, I don't.
Tigran Najaryan 00:25:02 Yeah. What you're describing, I guess, makes me concerned about the amount of effort that will be needed within the language syncs. That work has to happen to get the consistency you're aiming for, which I agree with you, it is necessary.
Nevertheless, that is work that has to be done, and it's going to be extra load on maintainers, even if you decide that, okay, you will be driving those changes.
So, my concern here would be that this isn't just about having the TC sponsor, this is also about increasing the load on all of OpenTlemetry on the maintainers, so I'm not sure whether We want to do that.
That would be, I guess, my… other concern, in addition to not having the TC sponsor at the moment. And for TC sponsor, I guess my question also would be whether you guys feel that you could live without one. It's also a matter of how… how much you feel that you need that help, or you don't need that help? That would be my other question. Not sure about that. This is the feeling we have as a TC or GC, that a project spans across multiple areas of open telemetry, so naturally we're thinking you need somebody to help you from the TC. I would like to understand whether your feeling is the same here, whether you feel that you don't need it, maybe. I guess you know what to do.
Michele Mancioppi 00:26:26 It depends. To create packages with some distributions, we don't need any help.
We don't need any guidance.
To actually make those distributions worthwhile?
Yeah, we do very much, yeah.
Besides, I would like to point out that I got Tigran in the way that you spoke.
I got somehow a feeling that, I mean, you agree it's important work, you agree that it's gonna take a lot of effort, and that worries you.
My take on that is that if you don't do this work, OpenTentry is not going to be as successful as it could.
For me, it's a no-brainer that you need to do that work.
Tigran Najaryan 00:27:07 I think we all agree here in this room, it's important. It's just a matter of who can do it when, who are the people that we need for it to be successful, to be done properly, like you said.
without, let's say, a sponsor, a TC sponsor, you're saying you can do some things, and you do not necessarily think that those things are good enough.
For your purposes as you aim them to be, right? So… I don't think anybody disagrees here that it is a necessity for us to do. Can we do it now, is the question. Do we have the resources? This is what we're trying to figure out.
I'll lower my hand, I think you're next.
Ted Young 00:27:51 Yeah, so one question I have, you know, a lot of this work is, as you say, around stabilizing the instrumentation packages.
And I do think we need to come up with maybe a fundamentally different approach to managing instrumentation. We've got Weaver coming online, we've got a lot of AI tooling that we didn't have in the past.
I feel like there's maybe some possibility about getting creative around finding a way to lower the load there.
But most importantly, that's work that we have to do regardless of whether or not we have a system installer or Linux or anything. That's… that's required work for OpenTelemetry to be successful at all.
And one thing I wonder about is, like, can we reverse this? Because if… We feel confident that we could build the basics of the system installer, be like, here's the framework, and now we need to decorate it, and things don't get added here until they've gone through that path of getting stabilized and marked as stable and up-to-date.
is this actually, like, a flywheel effect, right? Like, if we have that… we're always looking for a way to take half a loaf in OpenTelemetry. How can we do the work that everyone agrees to, that we have the capacity to do now? And I'm wondering, like, if we build the framework, and then most of the things are missing from it, because they haven't been marked as stable.
Does that actually help us motivate our community to to go in, and deal with those contrib packages. Because we were talking about the SDK maintainers, and they've often said they don't have capacity to really manage all of contribib.
So we need more end users, we need more tooling, we need a better way of managing that in general.
But I have some concerns around, like, blocking all of this work until it's all done. You know, it feels a bit like a catch-22 with that, and I wonder if, like, we could actually use this installer as a motivator to get the rest of the stability work done. I'm curious what you think about that.
Michele Mancioppi 00:29:57 I think that, with the Java, other instrumentations, and, To some extent, tornette.
There is a high enough bar to get a lot of users interested, and set up a comparison that Hopefully, it will be motivating for the communities of the other language Sikhs to meet.
Ted Young 00:30:22 Jack?
Jack Berg 00:30:24 So I have a practical suggestion that I think incorporates some of the ideas I've been hearing from other people. I've thought about this over the past couple of weeks, like, how can we go forward with this?
And, I actually just have a comment that I left on the project proposal that I linked in the chat. And basically, the idea is, like, hey, we're resource constrained now, and partially blocked by this stable by default.
And, but, you know, that is suggesting that we need an elevated sponsorship, TC sponsorship, if we want to engage on this now, but what could we do without an elevated TC sponsorship? And what I propose is we could do packaging for the instrumentations.
So, scope this back from trying to create an open telemetry package, which has to make all sorts of complicated cross-project decisions about what's included, how do components interact with each other, what are the defaults, what sort of gates exist, and scope this back to just saying, like, hey, we are going to publish some of the packages that someday will, you know, compose this larger OpenTelemetry package. We're going to have an OpenTelemetry Java package, an OpenTelemetry Python package, an OpenTelemetry Node package.
And, you know, in the process of publishing those, we… we gain the muscle memory, we gain the experience to learn about publishing, you know, RPM packages and deviant packages, and, and we can do all this without, with just a TC escalating sponsor, because I think, like, the risk is low, and, you know, the natural decision would be to have packages whose versions mirror the components that they bundle up, right? Like, you don't have… you don't create a new versioning scheme for the OpenTelemetry Java package, you just mirror the versioning scheme that already exists for the OpenTelemetry Java agent, and, you know, also with Node, and also with Python. So, the decisions are less, and, you know, by the time we're done with this phase one of the work.
maybe we will be less constrained in other things, and Phase 2 can be bundling these together with, you know, elevated TC sponsorship that, you know, allows us to achieve the higher goals. So, that's my practical suggestion.
Michele Mancioppi 00:32:46 I could even foresee a world… so when you look at both DPM and RPM packages, they have, I think the word is tracks.
So, different levels of stability, the possibility to… to pull in stuff from, for example, I'm very familiar with Ubuntu, main universe, and a bunch of different places from which to pull stuff from. I could see a world in which, we have… I don't want to use the word first-class citizen, but kind of high-quality packages, like, say, Java and .NET, I'll take into at random, with Injector, with OPI, with the collector, and they work very well together, and then if you pull in, if you're a bit more experimental, and you want to go for Python or Ruby, then they will also work, and they will be injected, but it will not be installed by default.
Because they're not there yet.
And that would, would set expectations of the community that, hey, Java, you're gonna have a good time, other stuff, maybe a little less, which is important to set expectations, and also, a way for them to say, hey, I tried the package, the Ruby one existed, but it left wanting, because.
And that is good feedback.
that I feel we don't hear hard enough, because… Since the installation process is so difficult, people that would find the obvious bugs or the things that an expert would not catch, they don't get that far.
Austin Parker 00:34:14 I broadly support the idea of just saying, like.
Hey, we're gonna do this, and we're focusing on stuff that is stable.
based on our existing definitions of stability, I think that also dovetails nicely with the work that's being done at the SUMCOM level and at Weaver to you know, stabilize Semitic conventions.
One thing I do want to point out is just a, you know.
a problem.
We already have a lot of signs of maintainer burnout across language SIGs, especially in all of them that aren't Java, and I actually wouldn't be surprised if we aren't having it in Java, too.
But my only reason I say not Java is because I feel like Java is the healthiest, language sig, just in terms of the amount of people Available to sort of deal with things.
And we are already, and I think, you know, if anyone, you know, people… I have a fairly strong belief that we are going to ask even more of our maintainers over the coming months and years thanks to, advances in LLMs, especially around… cybersecurity topics and vulnerability finding, and OTEL is already a project of significance, due to the people that use it, so we have to be pretty sensitive to the capabilities of, LLM-assisted exploit development and things like that.
So, I'm… I'm already concerned that we are going to… that we are taking a language… bunch of language communities that are already tenuous, and then giving them what they would maybe see as unfunded mandates.
That said… I think if we kind of scope this and say, like, hey, we're focusing on stable stuff, and we're doing, you know, and we're doing everything we can to not put additional work on people, then… I would be super okay with that, and I also feel like it wouldn't necessarily need a ton of TC oversight.
Are we down to… One full-time container in Java Core?
Isn't that way for you?
Jack Berg 00:36:50 That's insane.
Austin Parker 00:36:51 I… I thought we had, like… I would also just, broadly encourage, you know, anyone with the sound of my voice, like, a great way to help this is to… Figure out how to get paid more people to be maintainers on OTEL.
Language SIGs, especially.
Liudmila Molkova 00:37:14 I wanted to say… sorry, I disconnected for a second, maybe, Austin, you already talked about it, but it sounds like what we want is alignment across different… the feature parity across all the languages.
And featured parity across all the instrumentations, and no single TCA, even with whatever escalation level can solve. This is the whole community effort.
So, I was thinking about this. So, this is a good project to… for us to prioritize this feature parity and consistency. We can do a lot with conformance testing, and we are actually pretty much there.
It's the matter of just doing the actual work of plumbing things together.
We can prioritize these efforts, but it would be… it's not one project, it's across all projects. So, assuming packaging starts, and I'm kind of supportive of having it an escalating level, but… I think, one of, active leads on the project, Mikael, Antonio, anybody else who is actively participating in it, would also be part of this pack.
discussions, and the key decisions around the policy, what are we taking, would be made there. It's awesome that Antoine also works on collector, which brings the collector in the picture.
So I think we can make progress, and we can, start doing this, but, maybe we will stuck in some certain areas where we will need maybe dedicated projects, like, I don't know, enforcing semantic conventions compliance.
Ted Young 00:39:04 So, I have a question. I know that, you know, there's some places like Python where, you know, there needs to be some improvement in the installation hooks and whatnot to make it work better, with this kind of installation approach. But it seems like the bulk of the effort relates to the contrib… you know, ecosystem. And we're talking about maintainers, but that's already kind of out of scope of… of maintainers. So, I'm wondering, it's like, this… Am I right in thinking that it's not even just the maintainers, but just this area of open telemetry where we're lacking a comprehensive way of managing it in general?
That feels like where the bulk of the work is, or am I wrong about thinking that the bulk of the work is in the instrumentation packages versus core SDK stuff?
Michele Mancioppi 00:40:01 I believe the bulk of the work is the instrumentation packages, and to a minor extent, the default setup of putting together the country packages. For example, Java, despite being the best one.
is not particularly good at resource detection, not out of the box. And that is something that, with a fatal hands-off mechanism of adding stuff to applications, like the injector, or OBI, for that matter.
It plays counter to the expectations of the user.
Ted Young 00:40:37 Yep.
And when it comes to… and this is a question, you know, for, like, TCGC, right? Like, let's… let's put this… you know, installation approach aside for a second, how are we going to manage updating and maintaining all of this contribib? We know that OpenTelemetry is only as useful as the cleanliness of its data. We need to stabilize and get all that data clean in order to graduate, so… Let's pretend for a moment that the Linux packaging SIG doesn't exist.
We never even thought of this. How are we tackling that problem?
Liudmila Molkova 00:41:20 So we can have a, pipeline.
CI check that's actually pretty much language agnostic, with minimal language involvement, where we validate what specific library needs, and if it, documented, aligned, and whatnot. We can automate it pretty well, and Trask did some awesome job for GenAI, and it's pretty much… Can be done today. We create system of pages, and we, we can flag and fail instrumentations that don't comply.
It's not an overnight fix, but it's also the automatable fix, right? I can… it may be inefficient, there could be bugs, but we could potentially even automate with AI how we, update these instrumentations.
Ted Young 00:42:15 How would you propose scaling that work out? What… would that be a SIG focused on that, or is that… do we need to take a different kind of structure, for managing that? Again, imagine the packaging SIG doesn't exist, like, how would we… how would we structure that work?
Liudmila Molkova 00:42:33 I think this should be structured around semantic conventions, actually, and maybe semantic conventions maintainers can correct me. But we've lately been, focusing on a limited set of, conventions. We don't take new conventions in, and it's a natural step for us to drive the instrumentations, finally, because conventions without instrumentations will learn more and more, doesn't make sense.
Ted Young 00:42:55 Like, you would go, like, let's start with HTTP and tackle all the HTTP everywhere, that kind of approach?
Liudmila Molkova 00:43:01 Yes, so, like, we had the 6 focusing on stabilizing conventions, let's have maybe sub-six now, the same ones with maybe new members.
Enforcing this through the ecosystem.
Michele Mancioppi 00:43:14 If I actually pulled, statistics about, the kind of telemetry, the kind of spans, the kind of annotations that, about 500 customers sent to Dash Zero.
I was surprised by how prevalent HTP is. My guess was around 60%, but the reality is more like 95.
At least of the server spans.
My gut feeling is, the moment we do a good job of HTTP and databases.
That covers a huge amount of mileage, and then RPC and messaging would effectively be the rest of the part that is non-negotiable.
for users to have a good experience out of the box with hotel.
All the rest, even, more… niche technologies, even based on HP, like, let's say, GraphQL.
They, I think it would be fine in a second phase.
Ted Young 00:44:14 Okay.
So that sounds like… I'm curious, like, within the semantic convention, ecosystem, what's the capacity feel like there?
For managing this kind of thing.
Tigran Najaryan 00:44:28 That's not for SEMCOM, though, right? They can set up the tests which discover non-confirmants.
But then the language seeds have to go and fix that, right? Even with, with, I guess, with the proposal to use some sort of AI agents to make the fixes. Maintainers are still supposed to look at that and make sure that they are acceptable to be merged. That's worked for maintainers of language 6.
Ted Young 00:44:55 I meant the setting up of that, you know, the… it feels like if we provided the community with tools to do it, we could potentially find more people to go and do it in the different contrary pose if we made a lot of noise. But we would need to, in my opinion, give people better tools than what we currently have.
Tigran Najaryan 00:45:14 Could we, though? Again, I'm concerned we're creating work for maintainers. We're imagining that we would do this automation and would have some other people somehow fixing these problems. I don't think so. Without maintainers… being heavily involved and prioritizing, at least reviewing and merging those, fixing PRs, it's not gonna go forward.
This is work for maintainers. Even if we say that we will provide some outside contributors who are willing to do the legwork.
Regardless, I think I would feel more comfortable if we say, in the staffing head.
For each of the languages we are assuming that will be packaged.
a maintainer who volunteers to say, okay, I'll take care of the whatever changes, whatever fixes are necessary in my SDK, in my instrumentation, in Java, in Python, whatever, right?
I'm not sure I'm seeing that.
I would want… I would feel more comfortable if I saw that, right? That… that… that willingness… willingness from maintainers to be part of the effort.
Ted Young 00:46:28 I have some thoughts, but I want to let other people talk.
Josh Suereth 00:46:31 Yeah, I want to drop in and kind of respond to what Ted was saying earlier, and I hear what you're saying, Tigrin. I think the key here, the reason that we have concerns is we want maintainers involved in these projects. When it comes to SEMCOMF, this goes to my overall, like.
calling it semantic conventions, I think, is starting to be more and more disingenuous. If we were to talk about consistent instrumentation available in distributions as a project.
Semconf would be a huge participant in that project, but it would involve other maintainers. And that's why I think, you know, to some of the efforts that we're doing, it might make sense to either rebrand or, like, reclassify things, where we have a set of components, like, semantic conventions are a component.
Weaver is a component. Auto-instrumentation is a component, right? Instrumentation contribute is a component, SDK is a component. But when we talk about projects, they're across all of these, and the thing we need to make sure of is we get commitment from the components.
that need to participate in the project, and I'd like our projects to be more… like, product-focused, or outcome-focused, right? So, that it's like, you know, before it was, hey, I have a new component, let me add a new component. Now it should be more, I have this use case, this thing I need to do in O-Tel.
And here are the set of components that need to participate in it. And we coordinate around those fashions. I still think that's true here. And, like, to what Ludmila was saying, you know, in semantic conventions, I think we are, keeping up. I wouldn't say we're healthy, in terms of maintainership.
But we do have, a good bit of people who are involved and active, and we have people who are growing through the ranks that I think is helping. It's just not, you know, is it where I'd like it to be? No.
But this is kind of the focus that that group has had. It's not just on making the labels, we have changed the narrative to be making the instrumentation. So a lot of the people that show up are actually the ones writing the instrumentation now.
And I think that's a good, healthy thing. And that's what we want.
But, you know, a rebranding or a re-advertising could be helpful here.
Liudmila Molkova 00:48:42 Yeah, I wanted to address what Tigran was saying. So, first, we are creating the feedback loop to maintainers, and a lot of them are interested in improving instrumentation. There is a lot of contributions to instrumentations, regardless of us pushing for it.
So if we create a better feedback loop with much easier ways to onboard, it will be easier. What I hear from maintainers as well, that it's hard for them to review PRs, because they don't know if it follows semantic conventions. Guess what? It's automated now, and it makes review process easier. So I think we can create incentive for people. It's a lot of contributions that people can make. It's a trivial contribution, to some extent.
And there is a feedback loop, and I think it's a good job for maintainers to do, to actually address feature gaps and inconsistencies across the project. I would like to… maintainers to spend time on this.
Ted Young 00:49:39 Yeah.
I have two thoughts. One is, I would like maintainers to spend time on this. I wonder if we want to create kind of a new position around, like, contrib… you know, contrib maintainer, right? Like, contrib maintainers today are usually the person who originally wrote the package and submitted it, but people are usually not very attached to these things, and they tend to wander off, and it seems like, especially with tooling.
there could be a way to just more, like, manage instrumentation according to, like, classes of instrumentation, HTTP instrumentation, DB.
And, you know, SDK maintainers have… Long-felt concern about being the person responsible for bottom-lining that stuff. I think if we gave them tools, that would help, but… but I am concerned that that… It fundamentally wouldn't change.
So I wonder if there's, you know, a way to create some additional positions, because I think there might be people who, especially if you had tools, would feel comfortable doing that kind of work.
who might feel less comfortable doing, like, core SDK work. So maybe that's a way to get… to get more help.
I'm curious what people think about that.
Alolita Sharma 00:50:55 Yeah, I agree with.
Carlos Alberto Cortez 00:50:56 You mean, like… But you mean, like, having, like, 2 or 3 people that are not maintainers at all from, like, Java, for example? Like, 3 different people who could be taking care of the Java conflict for people?
Ted Young 00:51:09 In a way, Java's an example, because you have Java Core, and then you have Java instrumentation, right?
SIG with, like, people, like, thinking about that stuff. Yep. To some degree, right? Like, it's a little different in Java, obviously, because everything's so agent-focused, but… but we don't really have anything like that in the other ecosystems. Like, a group.
Alolita Sharma 00:51:29 Billion.
Ted Young 00:51:30 who are thinking about instrumentation in Python, or Ruby, or Node.js.
Alolita Sharma 00:51:35 Yeah, I agree with you, Ted, because the tools, maintainers, or folks who can contribute to doing packaging, doing toolchains, you know, are… don't need to necessarily have, you know, intricate details of the features, From each, library.
Ted Young 00:51:55 Cool. So we have 8 minutes? Sorry, go ahead.
Carlos Alberto Cortez 00:51:59 I was saying it makes sense. Yeah, I just wanted to get that idea clear, so we are just aligned, yeah.
Ted Young 00:52:05 So, we have 8 minutes left. What… let's maybe pivot to next steps here. Like, what… what are our takeaways? What should we… what should we do to… to move this forward in a concrete way?
Tigran?
Tigran Najaryan 00:52:19 I have a proposal here, I guess.
what would make me feel comfortable to move forward with this, right? Setting aside the TC sponsorship.
I would like to see, for every language where we believe there is changes needed, so it's not… ready as these to be packaged.
I would like to see, in the staffing, two people. One is a maintainer who volunteers.
To work on this project.
And a contributor will do the legwork. It shouldn't be on the maintainer to do the work.
the maintainers still need to be able to do the reviews and approvals and all that stuff, but I would like to have a contributor who says, yes, I will go and do all that Work that requires I guess, instrumentations to be aligned with SEMconv, all that stuff, resource detectors, right? And the maintainer, so two people from every language where we require changes. If a language doesn't require changes, if we believe it's totally ready, that's okay, then we don't need.
Extra work there, it's a matter of packaging, that's fine.
If… if we can't find stuffing like that for a language, then I say it's out of scope.
from the project. We don't package it at the moment, right? We're explicit about the languages where we have staffing, we have the resourcing available, then… then we can go ahead with that language.
if we can do that, then the remaining question is that this is sponsorship? I think we'll need to figure out what do we do about that, and even if it's necessary, because then… I guess having that level of support from the maintainers may… may render it unnecessary in my mind, hopefully.
So that's… that's what would make me personally comfortable, so that we don't create Unmanageable amount of work for the rest of maintainers.
Morgan McLean 00:54:14 I will say, Tigran, for the language SIGs, I don't know why that's a prerequisite for this project, like, if the work that we're expecting to do within each language SIG is aligning resource models and things that are not aligned today.
we should be doing that regardless of the packaging sync proposal. That means there are things that are effectively broken today that need to get fixed, even if Antoine and Michelle and others had not come to us.
Tigran Najaryan 00:54:37 I agree with you, Morgan. It's… but there's a lot of things that we need to be doing, right? It's a matter of choosing what do we do and what we can't do.
Morgan McLean 00:54:46 The other thing I would push back on is I don't know if we need to double count. I like your idea of, like, making sure that any language that is in scope for this, we ensure that they have the right staffing for it. I don't know if we need a maintainer and contributor.
But I don't know if we need to debate that here.
Tigran Najaryan 00:55:01 Okay, that's how I'm seeing, because if you don't bring a new contributor, then it's a maintainer.
Morgan McLean 00:55:07 Correct, that's why I say one or the other.
Tigran Najaryan 00:55:09 If you don't bring a maintainer, then the contributor alone can't do the work. The maintainer has to review and merge it. Or an approver, let's say, right? Not a maintainer.
Ted Young 00:55:18 How about this? Let's… let's give it a shot, because I agree with you, Morgan, that, like, if packaging didn't exist, we'd have to be doing it anyway.
Morgan McLean 00:55:25 Yeah.
Ted Young 00:55:26 Seems like a good piece of motivating cheese.
Morgan McLean 00:55:28 It's a good forcing function to do it. Yes, I just want to be clear, I'm not, to your end, I'm not disagreeing with you, it's just more like, like, even if we decided that the packaging SIG is a bad idea, which we're not, I don't think we're saying, but pretend, pretend it was something we didn't agree with for some reason, I would think we would still want to jump on this. Yeah, yeah.
Alolita Sharma 00:55:45 Yeah, absolutely.
Ted Young 00:55:45 But we can see which languages we can find these people for, and then say that's the… those are the things that get added here. We don't want to mess up our existing install paths, but being able to say, as a form of, like, declaring things stable, they've got it added to this, like, you know, integrated system-level installation path.
It's also a good way to flag that to our community.
One last question. We want… we've talked about tooling to help these people. Where would we be building or managing that tooling?
like… How… how…
Tigran Najaryan 00:56:19 I'm hearing Sam Sig is volunteering to do that, that's what I was hearing.
Liudmila Molkova 00:56:24 Yes?
Alolita Sharma 00:56:24 But it's not SEMCOMP. It's another one group.
Ted Young 00:56:30 Let them come true and brace.
Josh Suereth 00:56:32 There's already the same count tooling sig that exists and has been working for years to provide tooling, like, anyway.
Ted Young 00:56:38 But do you feel you have capacity there, Josh? Like, I mean, that's mostly been, like, almost working a level down on, like, Weaver and things like that.
Josh Suereth 00:56:46 Yeah, I know, I don't think… I think we're almost at the point where we could start taking that on, but yeah, we… I don't know, how do you feel, Milla, in terms of staffing? It's, what, 3 of us, really, doing the work?
Trask Stalnaker 00:56:59 Trust community.
Liudmila Molkova 00:57:00 Go first.
Trask Stalnaker 00:57:02 I think we can take what we're doing in Gen AI right now.
And prove that out, and if that is successful, we can replicate that for HTTP and database.
Alolita Sharma 00:57:20 Yeah, I agree with you, Trask, because that can be actually adapted.
Liudmila Molkova 00:57:26 We really need it, and Trask has already done all the work for GenAI, we just need to polish it and make it part of our tail, then it's repeatable.
Alolita Sharma 00:57:33 Yeah.
Ted Young 00:57:35 Nice.
Jurassi, do you wanna play us off?
Juraci Paixão Kröhling 00:57:39 Yeah, I had a comment on what Chiron was talking before, and I think we've found a way to move forward. But I… in any case, I'd like to just make a small comment that Really like to see this one here moving forward, even if in a smaller fashion or a smaller capacity, like, trying out and seeing how it plays out in practice.
Without putting too much requirements on that. Like, let people play with that, let people find solutions, and then if we face problems, then we come back here and we have another discussion. If it's not working out, if it's putting more things on… on the shoulders of maintainers and so on. Like, I have a feeling that, based on our previous discussions, MCP, including Which we are more keen on letting people experiment and do shit. I think that's the term that was officially used this time.
And and let them do shit now, as well, right? So let them play with that, and let them solve issues, and if… If we find maintainers being even more overwhelmed than they are right now, then we come back here, and then we stop it.
But I think I'll better… Have a bias to action here.
Tigran Najaryan 00:59:00 Sure, I'm all for the douchey, I guess, attitude, but… I want to try to prevent the creatureship for others to do.
thing, right?
Juraci Paixão Kröhling 00:59:11 Yeah. If that happens to be the case, then I'm really more than okay in just saying, you know what, stop doing shit. So… Yeah.
But I think we're… we are all in agreement there, I think, right? So… This is not… Not opposing views.
Ted Young 00:59:30 Okay, we have some action items. I'm gonna do my part to help.
you know, organize this, but yeah, GCTC, let's, pay attention to this system packaging project, and also, in the name of transparency, because this is a thing we do, we talk here, but then we forget to update the community.
We need to go back to that project proposal, and give an update there about what we're thinking in some form.
So we can figure that out on Slack offline, but we should do that.
Okay, I have to run.
Alolita Sharma 01:00:04 Awesome, thank you.
Tigran Najaryan 01:00:06 Thank you.
Alolita Sharma 01:00:06 Good.
Michele Mancioppi 01:00:07 Interesting.
Alolita Sharma 01:00:08 Thank you.
Trask Stalnaker 01:00:09 Right.
