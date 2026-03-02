SIG: Governance Committee
Date: 2025-12-17
Duration: 93 minutes
============================================================

## Zoom Recording Transcript

Alolita Sharma 00:01:19 Hi, Austin!
Austin Parker 00:01:21 Whoa.
Alolita Sharma 00:01:22 You're looking good! Happy Santa!
Austin Parker 00:01:29 doing, what is it, the…
Alolita Sharma 00:01:34 Are you, are you doing something?
Austin Parker 00:01:36 Yeah, like, I've got a…
Alolita Sharma 00:01:37 Oh, I saw your thing. Yes, yes, yes. Which thing? The one that you're doing online, right? The talk?
Austin Parker 00:01:45 Oh, yeah, I'm doing a kind of hotel… this weekend hotel thing.
Alolita Sharma 00:01:48 Yes. Yeah, okay, okay, very cool. Do you actually post them, Austin?
Austin Parker 00:01:53 Adriana and Reese and them handle all that, I don't…
Alolita Sharma 00:01:57 Okay, okay, very good.
Austin Parker 00:01:58 I don't know where they go.
Alolita Sharma 00:01:59 Hi, Marilla, how are you? I just show up. I see, okay. Oh, by the way, Austin Trask, please do accept your invites. I did send out a, you know.
Austin Parker 00:02:11 What was that?
Yeah.
Alolita Sharma 00:02:13 For the maintainer summit. It will just be… Okay. So that we have a placeholder, and then, you know, we can…
Yeah. Everybody.
So, Trask, I sent it to your Gmail, Austin, I sent it to your Honeycomb.
Austin Parker 00:02:28 Yeah, I see it.
Alolita Sharma 00:02:31 So, again, it's just… Just paperwork in one sense.
Austin Parker 00:02:37 Yeah.
Alolita Sharma 00:02:38 Should be an interesting topic, and also, you know, it's like, we have so many…
and maybe this is a discussion we can have, where, you know, there's some MCP implementations that are being done on top of Hotel, and… but they're not part of the project necessarily, right? Like, Tyler has worked on one, and then, there's another one.
in the community.
Austin Parker 00:03:05 Yeah.
Alolita Sharma 00:03:06 Maybe it's a nice thing to kind of list some of them, vet them out, and then…
List some of them as recommended, or…
Because everybody's trying to build one, but only a few of them will be… Good.
are useful.
So, Marilla, did you, Get set up for KubeCon, you, I think they would like to…
Better book your hotel, if you haven't.
Marylia Gutierrez 00:03:45 No, not… no hotel yet, yeah.
Alolita Sharma 00:03:47 Book it, because you can always cancel it. It's hard to get the right good prices later.
Marylia Gutierrez 00:03:54 Oof.
Austin Parker 00:03:55 Yeah, I booked my hotel this week, I got a…
Alolita Sharma 00:04:01 Yeah, book it. I mean, you can always cancel if something changes, you know, last minute, but it's always harder to get.
Reservations.
Austin Parker 00:04:11 Yeah, I gotta do… I gotta book my flights.
Alolita Sharma 00:04:14 Yeah, flights, yeah, flights are actually…
Relatively reasonable right now, but the non-stops get booked out very fast.
Most folks are probably out today. This one, yeah.
Excellent.
Austin Parker 00:04:48 Yeah…
Marylia Gutierrez 00:05:11 Well, both… Should I see and severing added topics, but…
Alolita Sharma 00:05:16 Yeah.
Austin Parker 00:05:17 Yeah… Alright, I accepted.
Alolita Sharma 00:05:25 Okay, awesome, awesome.
Thank you.
Hi, Jirassi. Hi, Jirassi!
Austin Parker 00:05:35 Getting notes.
Juraci Paixão Kröhling 00:05:37 Hello, hello.
Alolita Sharma 00:05:41 How's the weather in… in… Germany. Kohl's.
Juraci Paixão Kröhling 00:05:47 It's for Brazilian like me, it's really cold.
Alolita Sharma 00:05:50 I know!
Austin Parker 00:05:50 What is cold for you? I was gonna say.
Alolita Sharma 00:05:54 That's.
Juraci Paixão Kröhling 00:05:55 It's a subjective thing. Yeah, it's 2 degrees, it's 2 Celsius right now.
Austin Parker 00:06:01 That's a bug.
Juraci Paixão Kröhling 00:06:01 for you.
Austin Parker 00:06:02 So…
Juraci Paixão Kröhling 00:06:03 Is it…
Alolita Sharma 00:06:04 Freezing? Austin, to you? Here, yeah, it's… there's been snow on the ground since, like, the first week of the month.
Austin Parker 00:06:09 month.
Alolita Sharma 00:06:10 Okay, that's why I moved to California.
Austin Parker 00:06:12 Yeah, post… every year, like, clockwork, it's… go to Rio, like…
Thanksgiving happens, and then it immediately, like, switch flips, and it's like, alright, time for snow, and cold, and ice.
And… You just want to stay inside for 3 months?
Alolita Sharma 00:06:30 Yes, I can understand.
Marylia Gutierrez 00:06:32 Yeah, here was weird, because, like, last year, it took a while for, like, winter to start, only, like, end of December, but this year, it's not winter yet, but it has been, like, minus 12, minus 16, like, Celsius for a couple weeks.
Trask 00:06:48 Wow.
Austin Parker 00:06:49 Yeah, that's…
Marylia Gutierrez 00:06:50 Today is… today is warm, today is minus 2.
But it has been, like, around the minus 10 to something for the past, like, 2 weeks.
Alolita Sharma 00:07:03 It's… it's 62 degrees here at Fahrenheit.
Austin Parker 00:07:07 Yeah, rub it in.
Alolita Sharma 00:07:10 No, no, I'm just reminding you, that's why we pay so much money here to live here.
Austin Parker 00:07:16 I do need… 2… pop out…
Alolita Sharma 00:07:23 All right.
Austin Parker 00:07:23 I'm early, because I'm doing the What's New in Otel thing.
Sure.
Alolita Sharma 00:07:29 Let's run through it. Yeah, let's run through it. We already have agenda items.
Austin Parker 00:07:33 Do we want to talk about, Jurassi, your point, your topic? Because… Yeah.
Juraci Paixão Kröhling 00:07:39 Oh yeah, yeah, I even forgot about that one, yeah. But sure. So, I think we kind of started discussing that during KubeCon.
Austin Parker 00:07:50 Yeah.
Juraci Paixão Kröhling 00:07:52 And, it is actually something that I had in mind for a while now, that we… we have officially a position
for Community Manager that, that, you, you, you took that before even being part of the GC Austin.
I think it was…
by the time that we had the first, leadership summit in San Francisco at the Lightstep offices.
Austin Parker 00:08:16 Yeah.
Juraci Paixão Kröhling 00:08:17 And, and eventually, you became part of the GCC as well, and the roles kind of,
meshed up. Yeah, they, they…
you are one person, right? And,
And I think the… I think the first question is, do we still need a community manager? And the second question is, if we do.
do we want that position to be filled by somebody that is not at the GC? Like…
I could provide my view on that, and then we can…
I don't know, we can discuss on those to ask the questions.
Austin Parker 00:08:56 Here's… here's my take. I think… so let… just to…
reorient on, like, why it exists the way it does is mostly around… We needed a way, like…
the access to various, like, CNCF things required someone that was, like, in the charter as, like, this is the person, right?
To get access to Service Desk, or to be able to do things on behalf of the project.
Now…
I think it's still useful, but what I actually think is… I don't… I think it's too much for one person.
Like…
I think, what I… I think that there's… especially the more we do in terms of, like, our own events, and the more we do in terms of things outside of this, and honestly, the more we try to do things, like, outside
The… the scope of the project, so things like talking, you know, going and talking to other…
orgs. Like, I think a good example of this is when we had, like, Jeremy, you know, Morrell come and talk about, like, the Cloudflare OpenTelemetry stuff. Like, that would actually be really solid for us as a project to kind of go and, like.
talk… someone to go talk to, like, Cloudflare DevRel people, and say, hey, how can we work together? How can we, like…
collaborate, how can we get stuff on the blog, and, you know, because this is all in the service of, like, you know.
Alolita Sharma 00:10:29 Bill?
Austin Parker 00:10:29 up a project community. So I think that fundamentally, though, it's just, like.
That shouldn't necessarily be one person, and my thought is maybe we should think about having, like, 2 or 3 people that are sort of… that work together on this, and…
We can…
figure out, like, exactly how that overlaps with, like, oh, you're attending GC meetings or not, like, maybe that's the part that should kind of, like, go away, but…
take a lot of the stuff that I'm doing in terms of organizing… Contributor GIFs, and da-da-da-da-da, like… And…
Basically, find a couple people that we think are… that would be good at this, that have, you know, that are trusted and respected, have them sort of pair with me for the first half of 2026 or whatever.
and go and sort of, like, introduce them to the people they need to know on the CNCF side, and, like, figure out how we all want to work together, like…
Community management as, like, a group.
And… shore up their charter a little more, and then kind of go from there.
That's kind of where I am right now.
Juraci Paixão Kröhling 00:11:47 Yeah, I…
Originally, I thought that having a one person would be a good idea, but I agree with you. Like, having more people, I think it makes sense.
It could be even some people that are already part of the communication segue. I think the kind of profile kind of overlaps a little bit, but not quite, so it's not entirely the same skill sets, the same goals.
But, I can definitely see it being interesting to some people from the communication sake. Yeah.
But I think one… one… one aspect I would keep there is… Having at least one person
been, Austrian's shadow for at least half, the first half of 2026 to learn, like, what you're doing, and try to
Austin Parker 00:12:42 try to help you offload the things that you don't want to do anymore, or you don't have the, you know, the time to do it anymore, or you're not happy doing it anymore. I mean, that's perfectly possible as well.
Juraci Paixão Kröhling 00:12:54 I don't know if you enjoy doing observatory, but that's something that people can definitely… you could definitely have some help, right?
Austin Parker 00:13:02 Yeah, there's questions, so… or there's hands, so let's do those real quick.
Alolita Sharma 00:13:06 Yeah, so, Jurassi, good, good, point to bring up, because I think that it's,
I think it's very important for the project to actually have a community management
community manager face, because it's a very large… I mean, Hotel is a very large project and has so many diverse communities,
That said, I think that Austin, from what I remember, and, you know, again, thanks for reiterating some of the ideas we had, you know, kind of discussed, even in… when we created this role.
I think the reason why the GC representation was useful was that, you know, then the community's voice is also directly available to the GC, because one of the things that was happening with the
end-user SIG kind of being, or just, you know, the community SIG being kind of detached from the GC was that we were not necessarily…
getting feedback or having some, you know, someone like Austin really filled in that gap to be able to bridge the community interests, as well as CNCF management, if you will, into the GC, right? So, I mean, again, I think that that work is…
required and essential for the GC. Now, what I really like, from the suggestions that both Austin and you made, Jirassi, is that it's not one person's role, right? It's… it's actually perhaps a work group or a…
kind of a SIG, but more folks should participate in it with, you know, strategic focus as well as tactical focus, because one of the things that
You know, happens a lot, and especially because everybody is multitasking,
Is that a lot of the strategic initiatives
You know, don't necessarily connect at the right time with the… with the project.
And that's something that the… Whoever is, in terms of the community manager role.
can help fill.
So I… I mean, I just wanted to reiterate that, because the role, I think, is important, and the connection into the GC is important. But that said, scaling the role is also equally important.
From and participation and… and, programs perspective.
Severin?
Severin Neumann 00:15:45 I don't know, Austin or Yurasi, if you want to respond to that, so…
Austin Parker 00:15:49 My only comment would be, like, I agree, it's probably good to still have that community management function, like, be a part of the GC, but maybe instead of
a weekly part of it, maybe there'd be, like, a monthly sort of cadence, like a quarterly sort of cadence. Especially if we're increasing it to a larger group of people,
Yeah, I think it would just maybe a little more formalism around, sort of like, hey, when are they coming in, and how are we, like, how are we working together? Because I think that ultimately, you know, I think the community side will probably continue to grow over time, even as the GC stays the same size.
Alolita Sharma 00:16:30 Yep. But Severn. Yep.
Severin Neumann 00:16:32 Yeah, I, I, I… I just want to mostly agree to the things that have been said. So.
So my understanding is, like, the community manager role was created back when we had the communications SIG, right, which was kind of doing all of that to some extent, and since Austin was, like, the lead maintainer back then, you were, like, giving that responsibility, and if I look, like, I shared that in the chat, right? Like, what is…
the responsibilities of the community manager, I mean, technically.
A lot of that could be covered by comms.
by contributor experience, by end-user SIG, but…
the thing is, like, how… how can we make sure that they follow with that mandate, and how do they feel empowered to do that? So… so could we pick one person per SIG and say, like, hey, you are now…
the community manager's committee, whatever, I'm excited about calling it that way, but, like, it feels, again, like, one of the situations where people say, like, hey, give me a fancy hat to do this job, versus, like, yeah, just do that job. So, yeah.
Austin Parker 00:17:43 I… So… Yeah, so I do… I would… Just realistically, like.
I get where you're coming from, but also there is a little bit of, like, fancy hatness to it, only in the sense that a lot of it does come down to, sort of, like, relationships.
Alolita Sharma 00:18:02 Yep.
Austin Parker 00:18:03 And relationship building and maintaining those relationships, and so that's one of the reasons that it, like, just…
Like, I think something that would be a good project for sort of, like, the community side of the pro… you know, a good initiative would be, like, okay, how do we kind of programmatize these things more? So when…
the… OBI wants to… Do something, like, to promote their stuff, or like… help…
spread the word, or create a meetup, or… or I don't know, right? But I'm picking a name out of a hat.
Alolita Sharma 00:18:44 you know.
Austin Parker 00:18:45 That… those people should probably have someone to go talk to, or some… like, they, like, hey, these are the people that…
are responsible for these sort of things, and they can kind of, like, go and they can help you. Like, not that they did… not that they have to do everything for you, but, like, they know the people to talk to, they know how to glue your goals into these frameworks, right, and sort of handle that routing. Or to the observatory, you know.
Like, quite frankly, just being able to say, like, okay.
These are the people that have it on their calendar, that know when, you know.
When the artwork is due, and when the, like, schedule needs to be built, and da-da-da-da-da-da-da…
because right now, a lot of that stuff happens, but it is rather ad hoc, and like, you know, I think, you know, just as a…
you know, as a bus factor thing, right? What happens if Morgan and I disappear off the face of the earth, right? Like, what happens and stuff like that? And so that's also why having it kind of, like, federated a little, or spread out into a couple different people, but still saying, like, oh, it's these two or three people that are sort of, like, running this.
I am… I am not also an alien. Anyway, I… I do want to say, because I do have to drop for this other thing, but, like.
I'm totally interested in, like, doing this, and starting this process, so if there's… I have two people I think would be really good for it. I think we could do 3, I think Jurassi, you know, I think that, like, 2 to 3 people is the right number here. If there's…
I'll put the names in the GC chat, but if there's, like, a third person we want to talk to, we can add that, but I think… I don't think there'll be controversial names. And we can discuss this more async over the… over the next month, but…
If people are generally okay with it, then I think we should… Start figuring it out.
Alolita Sharma 00:20:42 Yeah, that's a good suggestion.
Juraci Paixão Kröhling 00:20:45 100% okay with that. I think, to me, the most important aspect of this whole thing is what you mentioned towards the end, like, having somebody
That is responsible.
Austin Parker 00:20:58 for thinking about our, our events, you know, in general.
Alolita Sharma 00:21:02 Yeah.
Austin Parker 00:21:03 Yeah, and definitely a big part of the plan is whoever these people end up being, that there would be sort of a, okay, we're gonna, like.
schedule some time to go through and, like, shadow, and like… you know, maybe it might take 6 months, it might take… it might be a shadowing for the entire year, I don't know, like, this stuff doesn't all happen immediately. But certainly, like, it would be something that…
I think starting in January, you know.
Let's go and start putting this together and figure it out so that
Certainly by the end of 2026, like…
The, they can pick point and run with it on their own.
Did anyone have anything for me before I drop?
Alolita Sharma 00:21:45 Merlia, did you wanna…
Marylia Gutierrez 00:21:46 I was just gonna say, like, because one of the topics of, at least the thing that Savin shared is just, like, tracking reports the end user, like, helped bring back to GC. That is something that I definitely, like, me as the liaison for that thing that I can definitely help out as well.
Austin Parker 00:22:04 Yeah.
Alright, well, happy holidays all, see y'all noon.
Alolita Sharma 00:22:08 I'm biased.
Morgan McLean 00:22:09 holidays.
Alolita Sharma 00:22:09 The other day is. See ya.
Severin Neumann 00:22:12 Yeah, I think we can move on. My only comment would have been that, like, I mean, some of the things are happening already, right? I mean, we have surveys attached to end-user SIG,
We have social media stuff already streamlined, right? I think it's more about communication, but I agree, like, for events, I think that's… that's probably the major thing, but yeah, maybe since Austin left, we can… we can continue on that async.
Alolita Sharma 00:22:38 Yeah, agreed, agreed. And I think that…
It's important enough that, you know, we should absolutely have more folks there.
Supported.
Okay, what's our next topic?
Verasi, we covered yours, and Marilio, did you want to add anything else, in that?
Call out from the feedback link.
Marylia Gutierrez 00:23:12 So yeah, for that one, they were just asking, because the… that project's not, like, officially approved, so they were just wondering any other, like, feedback from GC, and if they can get, like, officially approved. So it's just an ask for people to take a look, to view, see if there is anything controversial there.
Otherwise we can approve that project.
Alolita Sharma 00:23:37 Okay.
maybe we can target, do you want to set a date or something? At least GCs should read through it. I think we had discussed this already when Dan was, pre-election, when Dan was also,
On board. So…
Severin Neumann 00:24:00 Are there any… I don't think, like, there's one comment outstanding for me where they think it can be resolved.
2, 1. So, so probably we can…
Just everybody can read through it, and then… Yeah. …stop or not.
Alolita Sharma 00:24:15 Maybe by… If folks have end of day today, or…
Because.
Morgan McLean 00:24:24 Yeah, I can take a look today.
Alolita Sharma 00:24:25 Yeah, Marion will take a look.
Presque.
We can, we can also, Severin, share this on.
Trask 00:24:35 I have no… I have no electricity, so…
Alolita Sharma 00:24:38 Okay, okay. No worries.
Morgan McLean 00:24:40 Oh, same storm that we got hit with, Trust? Yeah. Yeah.
Trask 00:24:44 Probably.
Morgan McLean 00:24:45 Yeah, last night was quite something.
Alolita Sharma 00:24:48 Yes.
Very severe storms, actually.
Morgan McLean 00:24:51 Yeah, it woke me up.
Alolita Sharma 00:24:53 Yeah.
Marylia Gutierrez 00:24:54 I guess, can people, like, whenever they… you finish looking?
you can… I can create, like, a… just a message on the Slack channel, and people can give, like, a thumbs up, or, like, I have done it, and then we can just go from there.
Alolita Sharma 00:25:07 Sounds good, sounds good.
Thank you, Amrilina. I think, several?
Severin Neumann 00:25:15 Yeah, I think it's a similar question for the MCP proposal.
Alolita Sharma 00:25:20 Yeah.
Severin Neumann 00:25:20 So Pavel asked me today, like, hey, can we…
Can we prove that? I think with this now going into SIG developer experience.
I am at least happy with Ed.
I think the… like, the only thing I asked him is, like, to add a few non-goals to, let's say, make sure that this is not
going into some… some areas that… that it should not address, but beyond that, I think it's… it's in a really good shape.
Yeah. Take a look, and if you're happy with it, approve it so that we get… get maybe both over the finish line.
Alolita Sharma 00:26:00 Okay, and… but, related to this very timely question, Seven, I was wondering if we could actually, from the project,
you know, at least list all the MCP implementations, like one of the comments does list some of them which are, you know, available, but then also perhaps make a recommendation.
Unless, you know, unless the project itself has an MCP implementation, like Powell's, you know, if it…
If that's beneficial…
Severin Neumann 00:26:37 I think they have a list in their proposal. There's, like, 1, 2, 3, 4, 5, 6, or something like that. And I would say that that's, like, one of the first tasks they need to decide is, like, do we start from scratch or not? I think that's not something we should
tell them to do, right? It's more like, hey,
Alolita Sharma 00:26:57 No, no, I mean, what I meant was that, see, there are multiple implementations, because the larger community is actually, you know, having… experimenting, in one sense, right? So, the question is, again, what makes one proposal or one implementation better than others, and what, you know, just because
I mean, Powell is a contributor on Hotel, he's amazing, you know, he's been contributing for a long time. So…
You know, his implementation is probably well thought out, but the question is, again, from an end-user perspective.
Do we make recommendations as the project? Because I have heard this comment from many end users, you know, that, hey, you know, as MCPs get,
get integrated? Is there something that…
is recommended by the project, right? And… or preferred. Trask, you had your hand raised.
Trask 00:27:58 Sorry, it's not on this topic, though, it was back on the last topic, so… Okay, okay. Continue, I'll circle back to me eventually.
Severin Neumann 00:28:06 I mean, the goal of the project is to create an MCP server, which is a reference implementation, so that would be the one that we recommend, right? So, or was it more around, like.
And beyond that, like, for example, if you say, like, an MCP server to query your OpenTelemetry data, that's not something we are going to recommend, like, we are not recommending your observability backend, right? We are not saying.
Alolita Sharma 00:28:33 No, no, not the backend, right? Again, the MCP server implementation with the configuration is what, can be built, you know, by… and there are multiple implementations, as you can see, right? So…
Severin Neumann 00:28:49 Yeah, but that's the goal of the project, right? They figured that out. I don't know.
Alolita Sharma 00:28:54 No, I mean, the question is, do we actually, have that, knowledge or that, you know, discussion within the TC or within a community issue, that what are the, what are the, baselines, you know, requirements?
from a… even from a spec compatibility perspective that an MCP implementation should support.
Trask 00:29:19 apart.
Alolita Sharma 00:29:20 Right? Because you are starting to now introduce third-party layers which are querying data that is generated from
you know, hotel, right? Or collected and then stored somewhere.
So, the… either the storage layer handles that, you know, with the MCP setup, or that you are doing both analysis and store… querying
for specific types of data using OTEL
you know, an OTLP, specifically, for…
a particular implementation. So there are requirements there, where… do we make a recommendation, or do we ask
a particular SIG on the project to actually make recommendations and evaluate. Because this is a new area of, you know, technology that is coming in, right? And it's inevitable that it'll either land into a hotel or a sub… a related project.
just like we started with semantic conventions for AI, genteic AI, and then, you know, we've kind of expanded also into Gen AI and LLMs, and that has worked reasonably well.
Juraci Paixão Kröhling 00:30:38 So, the proposal is quite complete on what it should do, and it has nothing about the query of the data. I mean, we don't do querying. We don't have a query language, we don't have any, anything like that. The proposal focuses on…
a few key features of the existing MCP servers out there. One of them is how to configure an OpenTelemetry collector. The other one is, what are the good things about… how is… how are…
how are the good practices on instrumenting things? Another one is,
So, yeah, there are a few cases there. And they are very on point where open telemetry is relevant. So, instrumentation, pipeline configuration, operator configuration, helping with the semantic conventions, and so on and so forth. So, it's not about querying the data, or…
Alolita Sharma 00:31:32 No, no, I…
Juraci Paixão Kröhling 00:31:33 I'm descend.
Alolita Sharma 00:31:33 I was just using that as an example, and the point here being that my call-out wasn't related necessarily to the donation, right? I'm not…
actually, it's not related at all. It's more that as there are multiple MCP implementations for instrumentation, for example, right, and other functions that can be done through an MCP.
Juraci Paixão Kröhling 00:31:59 No, they're collaborating together.
Alolita Sharma 00:32:02 the recommendation.
Juraci Paixão Kröhling 00:32:03 Yeah, no, they are all correlation there, so there was a mapping at the beginning, so when Pavel made the initial proposal, I left a comment there saying.
Can you list all of the known MCP servers that are in this area, and can we make sure that we collaborate? I think that the authors of two or three of those, they joined. So Adriel Perkins is another contributor to OpenTelemetry. He had another MCP server. He's joining.
A third one was also, is also joining. We were thinking about an MCP server ourselves at Body Garden, so our AI engineer also joined this effort.
So, I think collaboration is happening there.
Alolita Sharma 00:32:41 Yeah, and my point, again, is do we… should we formalize a SIG there, or something of the sort, where, you know, that makes sense, right? Like, because there is a larger community here.
Which is, working around this space.
Juraci Paixão Kröhling 00:32:59 I'd… yeah, I'd recommend taking a look at the proposal and seeing all of the things that were suggested to see what is the current status there.
Alolita Sharma 00:33:07 Yeah, yeah, yeah. I mean, I've looked at the proposal. Again, my point is that from a project perspective, because as an end user, I'm looking for a recommendation, right?
And Prometheus also has similar MCP implementations that are on… that are being done around the project, but not on the project, right? So, again, the…
point is, when somebody goes and searches that what's the recommended MCP implementation for OTEL, or for Prometheus, or for Jaeger, what
you know, what's the recommendation? And that's… that's my point. It's not related to this contribution, necessarily.
So, I mean, I could open up an issue to discuss that, or, you know, it's something that maybe as a community could be discussed, because instrumentation will be affected by the implementation of MCP.
Servers, everybody will use it, you know, in everything.
Severin Neumann 00:34:11 I think if you want to do that, I think the easiest way is, like, read that proposal, and when we accept it, and it moves into DEFX, you can probably work with those people to answer those kinds of questions.
Alolita Sharma 00:34:24 Yeah, that's fine, totally, totally.
Totally cool. I mean, again, I'm just bringing it up from a perspective of, hey, you know, the larger community is looking for that information.
Yeah, sounds good, Severin. I mean, all good. It's just a discussion.
Severin Neumann 00:34:42 Yeah, yeah, that makes sense.
Trask 00:34:48 Back to the question I had, for both of those…
project proposals, do we have already approvals from the SIGs that they're embedded in?
Because I personally wouldn't… even… Approve it until… the SIG has approved it.
Marylia Gutierrez 00:35:25 Are you talking about just the MCP one, or also the one that I brought it up?
Trask 00:35:30 Yeah, both.
Marylia Gutierrez 00:35:31 Both of these. Oh, so yeah, so the one that I brought it up is gonna be… yeah, we already have, because Dan is the one bringing, and who's gonna own is the end user that he's on, so he's gonna be the one leading. He already got people from TC to…
be, like, sponsor. We already got the liaison, me. So it's pretty much, like, all the people that needed to approve already got, like, the… the go-ahead.
Trask 00:35:58 But have they actually approved the PR?
Marylia Gutierrez 00:36:03 That's a… I don't think it… yeah, there's no approval on the actual PR, but yeah, I can… I can bring it up to say, like.
Yeah, the official approval, yeah.
Trask 00:36:13 Can you ask them? Because that's actually, like, one of the main things that I look for and ask people to do. I even ask, usually, the participants.
The people who volunteered to participate, to approve, to actually put their gray checkmark on it.
Marylia Gutierrez 00:36:29 Okay, yeah, I can do that.
Trask 00:36:31 Yeah.
Because then, honestly, for me, it's just a formality for those two, because they're embedded in the SIG.
So, I, I mean, I feel like.
Alolita Sharma 00:36:44 Yeah, agreed, agreed.
Trask 00:36:46 Autonomy at that point, more or less.
Alolita Sharma 00:36:49 Yeah,
Juraci Paixão Kröhling 00:36:51 Yeah, for the MCP, there is one approval by Severin. The GC liaison is Austin, from what I can see here in the proposal.
Alolita Sharma 00:37:00 Hmm.
Juraci Paixão Kröhling 00:37:00 And I know that I… Nico from here from the garden is looking into that this week as well, so his check mark is coming soon.
But yeah, so… but it's coming.
Trask 00:37:14 Cool.
Yeah, I'm happy to… Put a… my green checkmark on there as soon as there's,
more approval… I mean, approvals from the SIGs.
Juraci Paixão Kröhling 00:37:30 And especially for the people who committed to do work on that.
Trask 00:37:33 Yeah, yeah, yeah, yeah, I want to see, not just comment, but like, I feel like having to put your approval on a PR also means that I know that they've actually read the whole thing, and they've…
Juraci Paixão Kröhling 00:37:44 Fair enough.
Trask 00:37:46 Agreeing.
Alolita Sharma 00:37:53 Yeah, that sounds good. Trask, I think we'll all follow the same.
Process.
And we're gonna, I mean, read through these.
Okay, anything else? I think we've completely covered our topics. Morgan?
Morgan McLean 00:38:14 I ain't out of one, yeah.
Yeah, and it's just a… it's a short one. So, there's two relatively new projects in OTEL that I'm… I think there's some…
synergies between, so there's the hotel injector, the purpose of which is to automatically discover customers' applications and apply the appropriate hotel language instrumentation.
And then there's Obi, which uses eBPF, and has several goals, including capturing network telemetry, but also automatically instrumenting applications using eBPF.
The instrumentation parts are somewhat separate, and that's fine, but there's a lot of overlap between their goals around discovery.
And so, I just wanted to give people a heads up. I'm working with some of the maintainers of each to see if there's a way we can not bring both projects together, like, formally, but, like, at least share some of the infrastructure behind the discovery part, so we don't have two different mechanisms.
I think it would be really great. Like, the goal of each is to have a package that you can basically put on a host or apply to a Kubernetes cluster that will automatically instrument everything. I think it would be great as a long-term goal.
to have a binary that you put on a host. It uses one mechanism for discovering things. For applications where OTEL has the appropriate instrumentation, it uses that. For languages where OTEL doesn't have the appropriate instrumentation, it uses the OB capabilities.
That would be neat. Anyway, I'm just chatting about it with the maintainers, just wanted people to know.
Severin Neumann 00:39:39 I'm not a big fan of that, so…
Maybe a related question to that. I mean, we still have the other eBPF project in our…
Morgan McLean 00:39:49 That's right, yeah, I paid little attention to it in the last year.
Severin Neumann 00:39:52 So, and there was a question to that, I think in the general OpenTelemetry channel the other day, like, what's the difference between the two? Yeah. And nobody could really answer that, because someone said, like, yeah, the OpenTelemetry Network is doing networking, and then someone said, like, yeah, but OBI is doing the same thing.
Morgan McLean 00:40:12 Yeah, when OBI was being donated, I had set up some conversations between them and the other SIGs who were looking at or already using eBPF.
And in the case of, like, Go auto-instrumentation, their reaction was like, great, we'll work together with this.
In the case of the network one, their response was like, we're pretty far along, we kind of want to keep doing our own thing. I have not checked in since then, and so I think those awkward questions are probably highlighting an awkward sort of dissonance between the.
Severin Neumann 00:40:42 Yeah, I think even if they say, like, hey, we want to go ahead and do that thing, like, then we need, for example, a page on our website or our…
Morgan McLean 00:40:51 It actually just explains it.
Severin Neumann 00:40:53 That calls set out, right? I mean, for example.
Morgan McLean 00:40:55 I'll dig into that one after. For the injector and OBI, they're both so new, and they're still charting.
Severin Neumann 00:41:01 God.
Morgan McLean 00:41:02 direction, where there's a unique opportunity right now to bring these together, where, like, in six months, they might both say, like, we're too far along, it's too late.
Severin Neumann 00:41:10 Yeah, but I also have the feeling they want to work together, and… Yeah.
Morgan McLean 00:41:15 Yeah, I mean, also, a lot of the maintainers work for me directly, so I can also influence them that way.
projects, but, but.
Marylia Gutierrez 00:41:23 Definitely, like, gaps on both of them that the other can help, like.
Morgan McLean 00:41:26 Yes.
Marylia Gutierrez 00:41:27 API has, like, some issues with, like, some operational system or some languages, like, to collect, maybe that is something that, like, oh, the injector can do those things, and we can.
Morgan McLean 00:41:36 Exactly, because, like…
Marylia Gutierrez 00:41:37 Brian Witters.
Morgan McLean 00:41:38 I'm chatting… I spent a bunch of time with, like, Antoine and Tyler talking about this, and, like, their reaction was the same as my intuition, which is the components within OBI are probably just strictly better at discovering things than what we have in the injector. Like, it's just better. And so…
they're gonna look into it, but it probably makes sense just to use that for the discovery part. But for instrumentation, Marilla, like, it's exactly what you're saying. Like, for languages, for applications written in a language where they're using the frameworks where we have the appropriate OTEL instrumentation, that will provide a better experience than what you're gonna get through eBPF.
Context propagation will work perfectly reliably. In eBPF, it will usually work reliably, unless you're using an async framework, in which case it might not.
And secondly, you can capture spans from various frameworks and things that you're using inside of the app, rather than just requests coming in, requests going out.
But there's also C++, and Go, and Rust, and other languages that we cannot instrument automatically. And there might be cases where someone tries to apply instrumentation and just fails for some reason.
And in those cases, well, the eBPF solution is way better than nothing.
Severin Neumann 00:42:42 And so, you can imagine, like, something where it basically does, like, the best possible option.
Morgan McLean 00:42:46 There's also the whole thing about, like, setting up, and they haven't talked about this as much, but, like, for Splunk's donation for the injector, a big part of it was also the ability to configure collector receivers for third-party apps, like databases and message queues and things like that, when they're discovered.
So they're also, at some point, will want to turn their attention to doing that.
Marylia Gutierrez 00:43:08 You know, just.
Juraci Paixão Kröhling 00:43:08 And we're in goodbye.
Marylia Gutierrez 00:43:09 both of them, and the eye on the OBI become injector, and it is a…
Morgan McLean 00:43:14 There we go.
Marylia Gutierrez 00:43:15 I'm like, what?
Morgan McLean 00:43:16 Whether it's one sig or two sig, I don't really care. The discovery
is where I see the most opportunity to do something right now.
Marylia Gutierrez 00:43:23 Yep.
Juraci Paixão Kröhling 00:43:25 Yeah, Maureen, I'm sure that you… you are, it's in your radar as well, but, I'm sure that the folks from the Operator SIG, they're also going to be interested in being part of this.
Morgan McLean 00:43:34 Yes, yes, yes, I should have mentioned that too. You're absolutely right.
Juraci Paixão Kröhling 00:43:37 Okay.
Morgan McLean 00:43:38 Yeah. Anyways.
Juraci Paixão Kröhling 00:43:40 Yeah, he was killing the right cover.
Morgan McLean 00:43:40 I started with Tyler and Antoine, and then I was going to join the SIGs maybe this week, depends. I might be heading out early for vacation, otherwise early January.
Yeah, I've been saying that a bit, like, I mean, I… that's a phrase I've used for a while, but now I'm becoming, like, every time I hear myself say it, I'm like, I shouldn't say that anymore.
Juraci Paixão Kröhling 00:44:09 Clean.
Alolita Sharma 00:44:10 Yeah, Claude McLean.
It's totally okay. You're absolutely right, Ali.
It's more of an English, thing than… than more so.
But hey, that's all cool. English is an international language.
Although… although I've heard a lot of people use the same phrase in the Valley, so I think it…
Morgan McLean 00:44:43 Well, it's because they're using LLMs more than anyone else, probably.
Alolita Sharma 00:44:48 All good, all good. So, I think, I think, we covered all the topics, but we did not look at our project board, and…
And the in-person meeting, is that… that's just our… for… for reference, I guess.
Did we want to cover the, project board, or should we leave it up for the near…
Morgan McLean 00:45:23 I've got 15 minutes.
Alolita Sharma 00:45:25 Yeah.
We do indeed.
Marylia Gutierrez 00:45:30 One thing that I can also bring up that I've been doing with the six that I liaison is just, like, some of them are doing, like, roadmap this week as well, so they were looking for inputs, so I'm kind of, like, reviewing things with a few of them, and just seeing if we have, you know.
Any, like, suggestions? I was trying to, like, focus on things that would be helpful for graduation, or just stabilizing existing things. So that is basically the guidelines that I've been giving to all the six.
Alolita Sharma 00:46:03 Cool, that's very cool.
And again, Marilla, feel free to share, like, if you need feedback or anything from the larger GC or TC, again, just ping folks on…
Marylia Gutierrez 00:46:17 We're so good, yeah.
Alolita Sharma 00:46:18 Yeah, people are usually very good about
Providing feedback and kind of reading through stuff.
Should we, go through the…
GC projects, I shared the link.
Morgan McLean 00:46:32 Yeah. Right now…
Alolita Sharma 00:46:34 Jen, do you want to share?
Morgan McLean 00:46:36 Yeah.
Alolita Sharma 00:46:37 Okay.
Morgan McLean 00:46:50 We talked about this… Open this one… Open this one…
Alolita Sharma 00:47:00 Yeah, that… I thought we enabled that, didn't we?
Morgan McLean 00:47:03 That's… yeah, the Fossa one, or the Zoom AIs?
Alolita Sharma 00:47:07 zoom in.
Morgan McLean 00:47:10 Let me see…
No AI setting… oh, this is from March.
Da-da-da… We may have, but the last update was in July.
Trask 00:47:27 I think we enabled it on the GC… On this page.
Morgan McLean 00:47:32 Yeah.
Trask 00:47:33 To… as kind of, like… Canary.
Notes, yeah. And at the time, I don't think any of us were impressed with the AI notes. That may, I mean, may have changed, I haven't looked at them.
in a while. Do we still get them? They were getting emailed to us at one point.
Morgan McLean 00:47:53 I haven't seen it in a while. I will say, like, like, my… we don't use Zoom anymore, we're part of Cisco, but my wife does, and she was complaining about the AI summaries pretty recently, that they're still pretty useless in Zoom.
Trask 00:48:09 Yeah, it was really bad the fir- like, when we first turned.
Morgan McLean 00:48:12 Yeah.
Trask 00:48:13 for Le Mans.
Alolita Sharma 00:48:14 So should we drop the idea for now?
Morgan McLean 00:48:19 I can just put a note in here saying, like, well…
Trask 00:48:23 right again.
Morgan McLean 00:48:24 Maybe we want to pull one up, just instead of relying on anecdotes from my spouse.
Marylia Gutierrez 00:48:30 I do want to point out that Dan is the one assigned.
Alolita Sharma 00:48:33 Yeah, Dan had… I mean, originally, I think Dan was good. That's fine.
Morgan McLean 00:48:37 We can fix the… Yeah. Nope, that's not what I wanted to do.
I can't go back.
Oh, this one.
I can put myself for now.
Alright, I will take a look at the AI summaries for the GC meeting, and…
We'll report back if they are quality or not.
Alolita Sharma 00:49:02 Okay.
Morgan McLean 00:49:08 Alright, some of the other ones I opened up, add a triaging document…
So those are steps that we use for triage… This… Was last updated in July…
I don't think we've done this.
Yeah, I don't think we have… We can follow up, Pablo, next meeting.
Because this was assigned to him…
Alright, this was one that came in in June from the TC. I had a document that explains the TC review process.
Alolita Sharma 00:49:49 I think Josh had, Joshuarez had discussed this.
And they had a draft going.
I don't think we ever finalized it.
Morgan McLean 00:50:01 Alright, let's follow up on our next GCTC call.
Alolita Sharma 00:50:04 Okay.
Morgan McLean 00:50:04 Because, yeah, that's… you're echoing what we had posted here in late July.
Alolita Sharma 00:50:08 Yeah.
Morgan McLean 00:50:09 Alright, other ones are faucet scanning… deviations and spec… And EZCLA.
Alright, Fossa…
Trask 00:50:23 is, temp… still temporarily on hold.
Morgan McLean 00:50:28 Okay.
Oh yeah, you were just updating us 3 weeks ago. Okay.
Alolita Sharma 00:50:33 Yeah.
Do you want to just note that, Ryan?
Morgan McLean 00:50:38 Yeah.
It's still the right one? This looks different.
Oh, that's why. There's just one that hasn't loaded.
Alolita Sharma 00:50:47 That's what you're not seeing.
Morgan McLean 00:50:49 Alright, this… is… are we still plan… do this…
Would you say it's blocked, Trask, or is it just on hold, or is it pending some action?
Trask 00:51:04 Just pending resourcing.
Morgan McLean 00:51:10 Save… Stop.
Trask… That's sweet.
Great.
Alright, this one's from Jurassi, assigned to Ted, about how to handle spec deviations.
Discussed this in August… So.
Juraci Paixão Kröhling 00:51:39 He's really old.
Alolita Sharma 00:51:41 Yeah.
Morgan McLean 00:51:43 No, this is this year. The start of it was old, but the latest update was from August.
Okay, really just saying we just need to write this down somewhere. Like, it's already written down, we just need to copy this to a place where we're more satisfied with.
Juraci Paixão Kröhling 00:52:01 Okay, folks, I have one question that just came out to me, not related to triaging. We had a specific topic, the ACLC topic, that I think might have been discussed last week. I just wanted to confirm that it either was discussed, or that we have it lined up.
Morgan McLean 00:52:19 I don't think it was.
I don't think we had any conversations around COC stuff last week.
Juraci Paixão Kröhling 00:52:23 Yeah.
Alolita Sharma 00:52:24 There was no discussion.
Juraci Paixão Kröhling 00:52:26 Should we change them to a private, detroit private link, because I…
Morgan McLean 00:52:31 enough time.
Juraci Paixão Kröhling 00:52:31 I…
Alolita Sharma 00:52:32 Do we have enough time for Tom?
Juraci Paixão Kröhling 00:52:33 I mean, I would like at least to provide what I know in, I don't know, 10 minutes.
Morgan McLean 00:52:39 I cannot generate Zoom links anymore, so someone else…
Juraci Paixão Kröhling 00:52:42 I can send a… I can send a Google Zoom link, sorry, a Google Meet link.
Morgan McLean 00:52:47 If that works for everybody.
Alolita Sharma 00:52:49 That's fine, that's fine.
Juraci Paixão Kröhling 00:52:50 Alright, sorry for the… for being so latex.
Alolita Sharma 00:52:53 No worries, at least you remembered. All good.
Juraci Paixão Kröhling 00:52:57 Alright, see you in a few.
Alolita Sharma 00:52:59 Okay, see ya.
Juraci Paixão Kröhling 00:53:43 So, it should not be taking any notes here. I tried to disable all the assistance.
From this one.
Yeah, so,
we had this, Bogdan topic happening for a while now, and, last week, Bogdan pinged me, and I think he might have pinged Trask as well,
saying that he wants to do now a COC reporting. Like, he… he wants to report somebody, for code of conduct violation, and this is…
why I thought perhaps there was a discussion with him last week, but I'm totally lost on one… the whole Bogdan topic. I was kind of away for a few weeks after KubeCon.
So…
Okay. So,
I will bring up what he said. Perhaps Trask has some information as well. I have the impression that Trask might know a little bit about this as well.
But,
But what I got from him on December 1st… so I was at an off-site that week, so on the week of December 1st, so that's why I didn't join.
And last week, I think I had an event, so that's why I also didn't join last week.
Yeah, so… But, what he shared me back then, so 15 days ago or so.
is that, he wants to report Pablo.
And his messages… his messages were.
Now, I understand who reported me, it was Pablo, has an agenda, bought that guy Douglas.
And he wants to report Pablo, because Bogdan thinks that Pablo intentionally accepted Douglas as an approver.
while Bogdan was on Thanksgiving holidays, so that… because he knew that, Bogdan would block the approval of Douglas as an approver.
Yeah, Douglas is the person with the three exclamation marks.
And,
And then, on the… so yeah, so, and then Bogdan said, on the… in the maintainer channel, I expressed my concerns with that person, Douglas, before, and Pablo said that he did not see it.
But it's not an argument. And then he pays up some discussions there.
And I… I then asked him, like, one thing is not very 100% clear to me, are you looking…
what is your goal? What are you expecting to get out of the report? Like, what is your expectation, right? So, just to understand what kind of problem are we looking at? Are you looking to revert the promotion of Douglas, or anything like that?
And Bogdan mentioned that I'm looking to apply the rules. What that means, I'm not empowered to decide.
And, and he said, basically.
based on US law, this would set a precedent,
And so my… and then I… and then I saw, you know, so it's just GC matter, like, I…
This is not for me. Individually.
Yeah, I mean, this is not… yeah. I mean, basically, what he wants to say is it sets a precedent,
And, he doesn't…
I don't know. I mean, I would love us to follow up on that and see…
What to do, basically.
What's happening?
Oh, yeah.
I can look at that, but I think it was unanimous.
With the… following the rules of the collector.
So, my recollection is the collector has a specific set of rules, meaning maintainers have a specific timeline, or they can reject people, and somebody is accepted as an approver if no maintainers have objections about that person, and if there is a majority of the maintainers approving.
Then you're food.
My understanding is that happened, so the majority of collector maintainers approved. Nobody said anything, but again, that was during Thanksgiving, and that's what Bogdan is saying.
That was on purpose by… by Pablo.
So that Bogdan wouldn't have a blocking vote on that.
Not alone.
Either that, or Contrib, one of those, yeah.
But, yeah.
I need to double-check, but, one thing… so there is a process, a well-documented process for the collector, but the process does state that,
Like, majority of people,
Unless there is a concern from one maintainer. Like, if one maintainer says anything, then…
That… that's a vetto, basically. No veto happened because of Thanksgiving. I'm not even sure that a vetto would have happened.
After one week or so.
But anyway… Yeah, trust.
Yes, yeah.
to complement what Trask said, Pablo also reached out to me, and said, like, with what you… basically what you just shared, that he, during the discussions on the maintainer's channel for the collector.
At some point, he… he told Bogdan, like, I'm not continuing this discussion here, bring it to the GC, because that's, like, I'm…
So, Bogdan…
at a couple of opportunities, he mentioned something like, you are the boss. Like, the GC is the boss, so we do what you tell.
And, the impression is that he sees Pablo in a position of power above what Bogdan has. So that's why Pablo decided to recuse himself also from that discussion, and from…
any GC discussions pertaining to this topic here. So he said, just tell me when you're going to discuss that at the GC, and I can just… I can just skip that one.
But I, yeah, a good point from Trask, I'm gonna document what I know.
I guess the question is then, should we use the existing dock that we have for Doblas as well, or should we start a new one and make a reference between the two docs? I think a new one is deserved in this one, yeah, okay.
Alright.
Yeah, this is my… this is my main concern with this whole situation, that this is not the first time that Pogan is at the center of a discussion. It is, if…
And, I don't know.
I think the pattern is what concerns me here.
So, I don't know, I think we need to have a deeper discussion sometime next year, perhaps.
About Bogdan in general,
Exactly. Well, there are a few that we suspect that left because of logged in, but they would just not say that out loud, yeah.
But cool, so, so I think that's an action item for me. I'm gonna create a new, a new doc share on… on the GC channel.
I'm gonna invite Bogdan as well to a GC call next year, so perhaps the very first one that everybody's available after the…
The break, the, the, the holiday break.
And… and I think now it becomes more…
timely sensitive than it was before, because, I don't know, I think… I have a feeling we have to wrap it up. Like, it's been going on for so long now.
That I think we have to come up with entry.
The end of the story.
So…
That's a complication, because Pablo is the JSON for the collector, if I remember correctly.
So I might… I might step in there, use my collector connections, I still have good ones there, and try to assess what is the healthiness of the collector.
I think Morgan has also very good connections there, so Morgan can also try to do the same.
But I agree that we do have two problems there to deal with. Or three, actually, because we didn't wrap up the previous CLC, as far as I remember, the one with Douglas.
Yeah.
Yeah.
Can you take that action item, Sabrin?
Can you tick?
Can… can you take that action item, Sovereign, to create the channel with the CLC… for the CLC violations without Pablo?
So, we should start with 5 and make everybody paranoid already.
Yeah.
Cool.
All right, so… so I think we have action items for the next one. I'm gonna try to schedule a conversation with Bogdan, so this is my one action item. The second action item is to create this report.
under the admin account, and then share the link on this new channel that Severin is gonna create, so that we have access to that. The other complication is.
Pablo technically would have access to the report as well.
We would have to trust that he would not open the report.
I think…
I don't think… I never saw that. If you could…
If you could show me how to do that, I can gladly do it.
Okay.
Alright.
Okay, cool. In the meantime, I'm just gonna assume that Pablo's not gonna look at that.
And if…
That would be another discussion, I suppose.
Yeah.
Cool, alright.
Sorry, again, for bringing that up so late in the call, but yeah.
No, I see…
So, 14th is GCTC, so that's why I didn't, bring up last week.
So the next… so it's either the 7th or the 21st, 21st.
I'm gonna ask, Paul then.
what is his preference? If we have Quorum, that's fine. If we don't have Quorum, at least we have his side recorded somewhere, like, in our doc, and then we can have a HGC discussion later.
Alright.
Alright.
See ya, folks!
See you next year.
No question, I know.
Tom reconstado.
I know, that's a big catching that's funny.
Pushes to the zones.
Would you have the name?
Welcome back to me.
Quizzes removed from that.
liviev.
et au face.
a ou.
i.
Dab rosa, o sea mundo room.
Siriam trace, Triculumias, plaida.
Hmm.
Nice City usto.
God, get into this.
vous cisitable.
esto.
essay lo que tambien.
Confirm esses.
That'd be one shot.
Asseigno, isso a queen temo estivo de caraja poneso, se queu pela mujo as a mearte.
qui… creation.
No seja is this kind.
Come in.
Okay.
Eu consider modai sante real. Mas. Oh… O escrito, o contte odo.
I think what's from the Rama is, like, a lot of expense metrics, Everything's an event.
auchar.
aqui.
Let's, let's conclude.
eventre.
Deploy to now, blah, blah, blah.
And…
Yeah, key. In conclusion, you know it was a deployed. Turnover touch, immediate drawback, not being used.
a dich.
imagin.
Twice daily. Kia… two bad wings, adoro.
A suker.
de la.
tubao.
Esta correlacionado con consumo sevec.
Entamos dao sao caracional. So selhar o avendis, e la aumenta.
e o vemente crestamo e a causa redar desista correlacao sues. Masuno e a causo do at a causa e verao. Entao essay a causa e verantao, a correlacao e a causo.
Entonces, ta van que a correlation e caso, precise. Depoie.
No folio deploy.
O deploy e cor com corio novo. Esse corio novo e trap, mas qualia… esta controra
Entao, essa es imagando, va a favou se sabe que a conteso nessa verca.
O entsele questa person, promo.
Elkstackles and Peru.
essaversao contemuel.
so que habar.
eu harsh ponto taunto bom, da partaran salmon.
Vo pegar… A…
And I've learned mine is… By the evening.
Make sure you tell me who you are, man.
