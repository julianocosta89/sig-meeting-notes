SIG: Communications SIG
Date: 2026-10-27
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Severin Neumann (Bronto)** 00:09 Hello?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 00:14 Hi, sorry, took me a second to… Undo.
**Severin Neumann (Bronto)** 00:17 No worries.
No worries. Apparently… yeah, my announcement of this meeting, like, I did it in my time zone.
And now I… like, like, US time zone… shift this… or clock changes this weekend. We did it last weekend, so that's why threw it up.
These days.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 00:43 Two weeks.
**Severin Neumann (Bronto)** 00:45 Yeah, let me see, like, can I change the… Oh yeah, time zone is UTC, so I should do… what is it? PST, whatever.
Let me see… I think we meet in.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 00:56 timing.
9 a.m. Pacific time is… yeah.
**Severin Neumann (Bronto)** 01:02 Okay, yeah, now it says 8, so I turned this into 9.
Okay, let me see… This change will go live immediately. Okay, if it's now sending the same message again.
in an hour, then… then we know that I did something wrong.
Okay, yeah, I fixed that.
Looks like it's only the two of us today, but yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 01:29 Actually, it's a good opportunity for me to tell you, I have seen all of your messages about the new, social media workflow. I have not had time to look at any of it, and…
**Severin Neumann (Bronto)** 01:40 No worries. No worries.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 01:41 I just feel like maybe we should get through KubeCon before… at least before I start, because… there's a blog every day, pretty much, until…
**Severin Neumann (Bronto)** 01:51 Yeah, I saw that, like, I mean, I also wanted to review a few of them, but, like, I'm also, like.
I don't know, I'm like, hey, I need to do some community… and we have a lecture this week, right? And I'm not sure if you saw that we had some hiccups.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 02:03 I did see. I did see. Yeah, no, it just… It's… it's dark when I start work here now these two weeks, so it's… I feel like I'm in the twilight Zone, like, everything is just topsy-turvy.
**Severin Neumann (Bronto)** 02:17 Yeah, yeah, yeah, exactly. So I don't know, like… I'm not sure if it was a good idea to put this election, like, two weeks before CubeCon, so it's like a… Big mess, but this is what we do now for A few years, so it kind of works.
But… because then, of course, at KubeCon, like, if the new GC members are there, like, they can… they can already say, like, oh, look at me, I'm a GC member now.
But yeah, it makes things a little bit complicated, and as I said, nobody planned for, like, the election system to have a buck.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 02:52 That's com… but it sounds like Marilia came up with a workaround, right? So…
**Severin Neumann (Bronto)** 02:58 Yeah, so she and I, we chatted yesterday in the evening a lot, and then what I did at some point is that I… gave Claude, like, just… so, the cool thing is, like, our voting system, Helios.
Hey, Vivek, good to have you.
**Vivek Anandaraman** 03:14 Good.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 03:15 Hi, Vivek.
**Vivek Anandaraman** 03:17 Excuse me.
**Severin Neumann (Bronto)** 03:18 We were just talking about the election, and that we… I'm not sure if you saw that, that we had a little bit of a hiccup.
**Vivek Anandaraman** 03:23 Yeah, I saw that.
**Severin Neumann (Bronto)** 03:25 Yeah, so, so, and what I mentioned is that, like, yesterday, the cool thing is that, like, this is a, like, the voting system that we use is also open source.
So I could give it to Claude and say, like, hey, we are seeing this and that issue. My assumption is that it has to do something with people that have elected in the past, but also have a username that has, It has mixed cases, so there has to be some uppercase and lowercase letters.
can you find anything? And then it took, like, a minute or something like that, and it said, like, yeah, there was a fix to help with that, but it was only partial, and now we are, like, in this weird state.
And then, like, Marilia and I, like, looked into it, and then figured out, like, yeah, what we can do is, like, anybody impacted.
can be signed up via, via the Google Mail.
It's not perfect, but yeah, we will… we will get through it. But yeah, a little bit unfortunate.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 04:24 historic voting window, right? So…
**Severin Neumann (Bronto)** 04:27 Excellent.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 04:28 Soon.
**Severin Neumann (Bronto)** 04:29 Yeah, yeah, yeah, yeah. That's the other thing, like, I mean, we have, like, only those 3 days, so it's not really a thing where we can say, like, oh, let's… I also don't want, like, so the person maintaining this piece of software, he came back to us earlier today.
I also don't think it would be good to have this… picks applied today.
So, yeah, LLC.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 04:55 It's interesting that it didn't come up before. I mean, are other projects using it for voting? Like…
**Severin Neumann (Bronto)** 05:01 Singers like… That's like a, how do you say, like, a chain of things that… that…
**Vivek Anandaraman** 05:08 Good question.
**Severin Neumann (Bronto)** 05:09 it got us into this situation. So, so we were pulling data from… DNCF, Git DM, and at some point, they only gave us GitHub handles in lowercase.
Because actually, GitHub is not making any difference there.
But then, I think something in Helios was changed to look for the case.
**Vivek Anandaraman** 05:31 Sweet.
**Severin Neumann (Bronto)** 05:32 Which then led to problems, which we reported, which they fixed earlier this year, like in January or something like that.
And I assume many other people using it don't use GitHub, and they may be more use any other kind of way of doing that. So there's a chain of different things that led to that situation, right? So, I'm not sure about other CNCF projects, I'm not sure what Kubernetes is doing.
But yeah, it was like this kind of combination of things that led to this situation, that we might be… The only ones really impacted by that, so, yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 06:10 Perfect storm.
**Severin Neumann (Bronto)** 06:12 Yeah, it sounds like an observability story at some point that we can tell.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 06:19 Not a blog post, please, though.
**Severin Neumann (Bronto)** 06:22 Yeah, okay, promise. Only on me.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 06:25 I'm tired of looking at blog posts.
**Severin Neumann (Bronto)** 06:30 Yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 06:31 Yeah, right?
So, that being said, I have not had time to look at the work that you've put into automating all of that stuff.
But if you wanted to tell us about it, I wouldn't… I wouldn't oppose that. Or if you want to put it off, we can do that too.
**Severin Neumann (Bronto)** 06:52 No, it's not… it's not, like, super urgent right now.
I mean, just to give you a little bit of a background on that.
we wanted to have, like, social media announcements on GitHub for a long, long time, but Buffer, like, did not open up their API until, like, everybody figured out, with AI, you should do that, so they now opened it up again. And now my idea is to get back to this thing where we can… do things through GitHub.
Because right now, the whole, as you know, like, buffer thing is a little bit Wild West, and we had a few situations where I had to… Mentioned to people, like, hey, we need to change a little bit here and there in the announcements, and that way we could have a proper approval process, and also people get credit for it, right? Through, like, DevStats, which is, like, the upside of it. So right now, every time you put something there, nobody… nobody gets, kind of, it's not counting towards your contributions, that way it would, so, yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 07:58 Nice.
**Severin Neumann (Bronto)** 08:00 Anyways I don't think we need to… to get too much into it, so yeah.
the blog post on the ecosystem pages, that's maybe more something we should be talking about.
Let me maybe share my screen with you real quick, and we maybe… can you see that?
So, meeting… let me open a blog post also.
the issue… Let me resume that. Okay, so we put out this blog post 4 days ago.
We got a little bit of feedback.
So far, like, one person came back and said, like, hey… no, that's not true. I had another person on LinkedIn comment on it, and… They kind of all give the same feedback, that they use the registry, most importantly, to find collector components.
And instrumentation libraries.
And here, I think, OTLP native software.
So most people, like.
**Vivek Anandaraman** 09:11 Meetings.
**Severin Neumann (Bronto)** 09:12 When they complain about something, it's the registry, right? It's not the… it's not really, like, distribution spenders, adopters pages kind of thing. Also, they are also not the ones I'm that much worried about, right? I mean, their registry is the one that makes a lot of work.
So yeah, I would… I would leave it open for another… maybe… I actually wanted to re-promote it this week, that's a good reminder.
Need to find some… some slots in my social media stuff to… to do that.
But yeah.
I think the only thing is we really need to set ourselves a timeline, probably post-CubeCon.
**Vivek Anandaraman** 09:53 Fuck.
**Severin Neumann (Bronto)** 09:53 To decide what we do with the registry and everything, if we really retire it or find a… find a different way to go about it.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 10:06 This might be a stupid question, but… is it worth… the people who've given feedback, is it worth, asking them to give a bit more detail? Like, when they say that they're looking at collector components, like, which part of the metadata they care about? Like, what are they looking for specifically? Or… does that not really matter? Like, do we just need to know that they're looking at collector components?
**Severin Neumann (Bronto)** 10:35 Another thing that, I mean, we could… we could ask more questions, for sure, like, I mean, Because at the end, what we need to know is, At the end, like, is the ecosystem explorer what they're looking for?
Or is there something that the registry exclusively provides?
especially with the things that are not part… so my understanding last time we spoke with Jay around it is, like, the Ecosystem Explorer focuses on… everything that is within the OpenTelemetry project right now, right?
They have plans to do it.
Go outside of that, but this is, like, many, many, many, many months out.
So that means, like, if we really get rid of the registry.
People would not have that one single place where they find all the libraries and all the things.
that natively integrate OpenTelemetry or provide some kind of integration. So I would ask detailed questions in that direction, maybe, especially, right? I mean, the other one is also interesting for… for helping Jay and the team from the… From the ecosystem Explorer to shape whatever they're building.
But my understanding right now is that the Ecosystem Explorer, anyhow, gives you more than the registry ever had, right?
But yeah, I think that's maybe good to poke people a little bit and say, like, hey.
here's the information that we would be curious about. Is there… are there more people using it this and that way? And, like, keep asking those kinds of questions and then collecting some feedback on it.
yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 12:19 Yeah, I think… I think that's fair. I think as we start to narrow down what we're going to do with them. Like, if we do retire the registry, then… for… An indeterminate amount of time Third-party components will not be searchable via any, like, Official OpenTelemetry.
**Severin Neumann (Bronto)** 12:39 Exactly. At least not in an official way, right? I mean, anybody can go to those awesome OpenTelemetry, awesome observability pages, and they're like, hey, this is now… This is now home to those.
Yeah. Yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 12:54 So, I mean, that might be… Specifically, a question worth asking, like, Do you care if… they aren't, like, official. If the… if the third-party components and instrumentations and products are not… included.
**Severin Neumann (Bronto)** 13:12 Hmm.
Yeah, yeah, I think, yeah, maybe we need to be… so because, like, if I go through the list, I mean, the registry… If we kill it entirely.
then yeah, this is mainly the thing that we lose. And maybe for now, some of the languages, because the Ecosystem Explorer ecosystem… no, Explorer… OpenTelemetry.io. I mean, right now, they have only… a subset off.
Of everything, right?
I mean, they want to build out the rest?
I'm not… I'm not sure about their timelines, but right now it's Java and their collector. So… so for some time, we would also lose… All the other languages.
But that's something where I would even be open to say, like, okay, we can wait for that, right?
But for the external libraries, I mean, if this is taking… if this is taking much, much longer, then, yeah, I would… I would not wait for that. Except everybody says, like, oh, but this is so valuable.
For the vendors, I mean, that's the other discussion, right, where we had, like, this thing about, like, hey, should we… So right now, if you… if you… the vendors list is the one where I'm, like, the most open to say, like.
I mean, this list just completely lost its value, right? I mean, it's just a… a list of just, like, names, and I can even spot a few that no longer exist, right? So where we're like, hey, they were acquired, or they gave up their business, or whatever.
So, so I rather would see, like, the thing that Jack suggested about, like, Putting companies here.
That are, like, contributing.
But that would, at the end, be more work than what we have right now, right? So that's the wild thing, because then we have to figure out, like, how do we… how do we track that? Except we outsource that and say, like, hey, this is tracked somewhere in the… in the community repo, and someone like GCTC, whatever, is, like, or some… some other people are looking out for that, and we are just upstream consumers of that.
And just updating that list. And same for the adopters, right? I mean, here, my wish would be to have Mainly the CNCF case studies.
On the other hand, that's not really the page, like, where I miss… Actually, that's the only page I really like. That's the one, like, where I would be really open to say, like, hey, let's… Let's maybe get rid of this components column.
And just… Have, like, those links out to… to any form of… of case study or, or, talks.
And that's it, right? So, I don't know.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 16:03 I mean, there's… there's a bit of overlap here with the reference implementations as well in the docs. Right.
**Severin Neumann (Bronto)** 16:09 Dia.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 16:12 Obviously, if the case studies or talks are, you know, published elsewhere, then we should still have a place that we can link to them, but… Ideally, adopters would be… would be proposing and either writing or asking us to help them write the reference implementations for their own, their own setups. I think that's… that would actually provide value.
Listing.
**Severin Neumann (Bronto)** 16:39 Yeah, exactly. I mean, at the end.
There were two reasons why we had this page, right?
One reason was, very clearly, towards graduation, we needed to give a list of people using OpenTelemetry.
Since we're now post-graduation, and there's other projects leading that way.
that page is not that necessary anymore, and at the end, like, everybody uses OpenTelemetry as… I mean, that sounds a little bit, I say, like, strange, but that's the reality, right? I mean, we are an established project, every, like, like.
The question around, like, who is using that open telemetry thing, It's not that…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 17:21 Yep.
**Severin Neumann (Bronto)** 17:21 relevant anymore.
what… but with that, I don't want to say, like, this is not valuable, and it's not great that people write about OpenTelemetry, so I also don't want to… kind of discredit this, but at the same time, in a sense, Cates is leading the way, right? They don't have… have case studies any longer. What they do is they point back at some point to, to the CNCF case studies, I would need to… I would need to find it where they have it exactly.
But at the end of the day, like, what we would, I think.
want to see, also, is that if you go to through CNCF, I owe… There's somewhere the, There's the case studies.
Does someone know that?
Okay, about… I thought it was a little bit higher up there.
Community… there, there it is, right? Case studies?
And if you now go here for projects.
Then if you type Kubernetes, it's like 107… almost 180.
And with hotel, it's 12, right?
Which is great.
but I would love to see here also, like, A much, much higher number.
So I would actually love to see how we can route people from Being listed here to being listed here, right?
So… but my understanding is also to be listed here, I think you need to use at least two of them.
So… Like, you need to use multiple… multiple projects, which would be totally fine with me, right? So it does not have to be like, hey, this is… because at the end, a big value of hotel comes from being used, not standalone, right? So… And then, at the end, what I would love to see us doing is, like, if people go here into the ecosystem adopters.
That this would then say, like, hey, by the way, here's case studies. And then maybe we have another section that says, like, hey, by the way, here's reference… reference, in integrations and implementations, so… But at the end, this is really the page I'm not… worried as much as the other ones, but because it's the one really, like, I mean, those are the people we care the most about.
But yeah.
Anyways… Let's wait a little bit longer for the feedback, and then we should do some… some thinking on that.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 20:08 Okay, sounds good to me.
**Severin Neumann (Bronto)** 20:11 Okay… This is something… Patrice, I think he shared some… PRs on that, or issues on that recently, right?
Stinky… he's working on that, so I don't think we need to… ARC.
In length about it.
so, yeah, the idea is still, like, to make the SIGs a little bit more independent.
there's not a lot more to be said about, so… Yeah.
Any questions on that part, or, I mean, we are just pushing forward with that?
So…
**Vivek Anandaraman** 21:03 Yeah, I have a different question.
**Severin Neumann (Bronto)** 21:04 Yeah, sure, go ahead.
**Vivek Anandaraman** 21:06 Okay, yeah, I don't know if it belongs to this forum, but I'll just quickly put it anyway. So I'm working on a project where we custom compile the collector contrib.
**Severin Neumann (Bronto)** 21:18 Yep.
**Vivek Anandaraman** 21:19 And sometimes some… for some collectors, we need Kafka receivers, for some, we need ActiveMPs, all these different combinations, right?
And we get vulnerabilities in some of these receivers, and we have to update it, right? So, I'm trying to work on an automated process to have this compiled automatically, and then pushed it into the individual machines, and these are not, like, Docker images.
So I'm just trying to figure out, like, what is the best way, best approach? I mean, do you have, like, a native way to search these, versions?
The receivers… The exporters, All the components, the processors.
Or should I go use the Git API to figure out these portions? I mean, like, what is the best approach, usually?
**Severin Neumann (Bronto)** 22:14 I mean, one place is definitely now the Ecosystem Explorer, right?
**Vivek Anandaraman** 22:19 Yeah.
**Severin Neumann (Bronto)** 22:19 Yeah, like, a list of, like, all the components.
And I think there should also be, like.
Give you… is it, like, they give you, like, details?
about stability, the README, I think they also should give you the version, right? So, the current version.
They tell you a lot. Okay.
Which component is part of which, which thing, and then if you say, like, hey, I have additional filaments here.
I think there's probably also an API somewhere behind that, that you may be.
**Vivek Anandaraman** 22:55 Oh, okay.
**Severin Neumann (Bronto)** 22:56 automatically. The defaults, like, like, there's the, there's this, this is what we talked about a minute ago.
code, OpenTelemetry, let me… Ecosystem Explorer. So there's this… this is the project behind it, right? There's the repository called Ecosystem Explorer.
And they would be the ones that, like, are working on… on building out this thing, and if you say, like, hey, we are… consumers… off.
**Vivek Anandaraman** 23:30 Okay.
**Severin Neumann (Bronto)** 23:31 Or would like to consume the data in this and that form or shape.
**Vivek Anandaraman** 23:35 than…
**Severin Neumann (Bronto)** 23:36 and I would suggest that you… that you go there and raise an issue, or, or a PR with them, and say, like, hey, can you… Wow. Okay.
**Vivek Anandaraman** 23:47 Sure, yeah.
**Severin Neumann (Bronto)** 23:48 Can you, can you, can you, I don't know, add, API to it, or CLI, or whatever, and then make it… make it more accessible.
**Vivek Anandaraman** 23:58 Yeah.
Cool, yeah, that helps. Yeah, right now, doing.
**Severin Neumann (Bronto)** 24:01 Okay.
**Vivek Anandaraman** 24:02 manually, so I'm just trying to figure out, is there an automated way to…
**Severin Neumann (Bronto)** 24:05 So it's definitely somewhere, but they would know better, like, like, like, this is, as I said, the UI, but if you probably already go into the… Into the, let me see, there's probably an API as well.
**Vivek Anandaraman** 24:20 Okay.
**Severin Neumann (Bronto)** 24:21 Yeah, maybe that is something… maybe that's something they should export, that they should expose the, some, some open… open API specification or something like that.
That's definitely something we… we should… we should talk about, yeah.
**Vivek Anandaraman** 24:39 Okay, cool, yeah, I'll do some digging.
**Severin Neumann (Bronto)** 24:42 Okay, cool.
We have this topic here open from Deanna still.
My understanding is, like, this is a collector topic, And I told her to… Go back to… collector maintainers about that.
I mean, Tiffany, you're also, like, a little bit more involved with the collector documentation.
I'm not sure if you had any chance to look into that. If not, it's not, like, something I mean, you have your plate full.
But… but I don't know, so… so it feels like there's some… so… so she was suggesting some… some performance… Testing and doing things on that within the documentation.
And I said, like, hey, that's probably something you should discuss with the… Maintainers.
Yep.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 25:38 I agree with that.
**Severin Neumann (Bronto)** 25:39 For maintainers.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 25:41 She has not been getting much traction, which could mean a variety of things.
I can, I don't know if she has… if… Diana has availability to attend a collector SIG meeting.
**Severin Neumann (Bronto)** 25:55 Yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 25:55 Bring it and just take the temperature and say, you know… The… the whole, like, benchmarking and performance thing is… is a… It's a tricky topic, so…
**Severin Neumann (Bronto)** 26:09 Yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 26:10 I don't know, I don't… I don't know how they feel about it, but I can… I can bring it up in the next Collector meeting and just…
**Severin Neumann (Bronto)** 26:18 Okay.
C. Okay, yeah, they're…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 26:20 Really?
**Severin Neumann (Bronto)** 26:21 That would be great, yeah, yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 26:24 Yep.
**Severin Neumann (Bronto)** 26:25 Okay.
Cool.
Anything else? Any… any topics?
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 26:40 Vivek, there's… one of my colleagues at Grafana has built an open source tool called OTel Checker, and it is.
**Vivek Anandaraman** 26:50 Just the individual.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 26:51 that you can use. I don't know if it'll work for your purposes,
**Vivek Anandaraman** 26:56 Okay.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 26:58 And I don't know… I don't know a lot about it, let's put it that way. I know it exists, and that it's open source, so I'll, I'll put it in the chat here, and you can just take a look.
**Vivek Anandaraman** 27:09 Yeah, that really helps, yeah. Thanks a lot, Tiffany.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 27:13 Yeah.
**Severin Neumann (Bronto)** 27:19 Awesome.
There's nothing left.
I give you back half an hour.
Yeah.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 27:26 Okay, thanks, everyone.
**Severin Neumann (Bronto)** 27:28 And talk to you in two weeks, then we're back to normal time zone differences, so…
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 27:34 Two weeks from now is QCon, right? So I…
**Severin Neumann (Bronto)** 27:37 to cancel.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 27:39 I don't know that it's necessary. I personally won't be here, but…
**Severin Neumann (Bronto)** 27:42 Yeah, normally we cancel during KubeCon. I mean, I'm around, I'm not at KubeCon North America.
But very often, we cancel. But, I mean, we can keep it, and I can jump on the call and see who is coming, and if nobody's showing up, then we just make it a short one.
Yeah. Okay, cool.
**Vivek Anandaraman** 27:57 Okay.
**Severin Neumann (Bronto)** 27:59 Awesome.
**Tiffany Hrabusa (Raintank, Inc. – Grafana Labs)** 27:59 ruin.
**Severin Neumann (Bronto)** 28:00 Thank you, bye-bye.
