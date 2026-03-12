SIG: Governance Committee
Date: 2025-10-22
Duration: 64 minutes
Zoom Recording URL: https://zoom.us/rec/share/OiVyi70Hf9yK_ySmEf2N8MgsUQ0HN-UWYIZAjJkH7OUW4JoamUHq-TGabfMZpI_-.jhZ7xAu3pauas1uR
============================================================

## Zoom Recording Transcript

Severin Neumann 00:00:48 Hello?
Austin Parker 00:00:50 Hello?
Pablo Baeyens 00:00:53 Hey.
Dan Gomez Blanco 00:01:07 Hello.
Trask Stalnaker 00:01:14 Hey, fuck.
Alolita Sharma 00:01:27 Hey, everyone. Good morning.
Dan Gomez Blanco 00:01:30 Hello?
Alolita Sharma 00:01:32 Hi, Daniel.
Severin Neumann 00:01:35 Now, no private topics today, apparently.
After we had a run for, like, the last 3 weeks.
Alolita Sharma 00:01:42 Yeah, back to back.
Severin Neumann 00:01:46 10th grade.
Alolita Sharma 00:01:52 Austin, did we, did you see the comments on the… DOC updates for Battelle?
They had a, I think, internal discussion, earlier this week, and they reported an update.
Which I thought was not… not completely… Had… didn't have all the details that… You know, we had discussed.
Live them.
Austin Parker 00:02:18 Where was this?
Alolita Sharma 00:02:20 I'll find the PR, let me…
Austin Parker 00:02:22 Okay.
Alolita Sharma 00:02:22 I'll share.
I just thought that they might be updating you regularly as they, you know, make notes.
Ted Young 00:02:45 Hello, hello.
Severin Neumann 00:02:46 all nom… hello. Have you all nominated people for the Community Awards? We have 38 responses, so… It could need a few more.
Dan Gomez Blanco 00:02:56 When is the, closing date?
Severin Neumann 00:02:58 November 6th, so you still have some time.
Ted Young 00:03:02 Perfect.
Severin Neumann 00:03:03 I will not be annoying November 5th, because I will be on PTO then, but…
Dan Gomez Blanco 00:03:08 Yeah. I don't know if I chose, like, the worst possible three weeks to go on PTO, because I come back and, like, there's so much that's happened, and it's okay.
Ted Young 00:03:15 Yeah, nothing.
Dan Gomez Blanco 00:03:17 Nothing going on here, yeah.
Ted Young 00:03:23 No changes afoot.
Alolita Sharma 00:03:26 Lot of, lot of changes, lot of stuff.
I'm sick.
Ted Young 00:03:41 Let's see…
Severin Neumann 00:03:47 So I think we can get started, right? So… All I put on the agenda is, like, looking back into the donation and project proposals again.
Ted Young 00:04:01 Goddammit.
Severin Neumann 00:04:03 I think the CICD one is… Do we still need, like, people to approve it, or how far are we withstand?
Dan Gomez Blanco 00:04:10 I think we had enough, yeah.
Alolita Sharma 00:04:13 Yeah, that's true.
Severin Neumann 00:04:17 So, technically, we could merge it, or… I mean, there's a few comments still open, so…
Dan Gomez Blanco 00:04:24 I think there is an open comment from me that I'm happy to just fix later. Just related to, like, creating a separate… GitHub project and a separate board for it.
Just close the… phase one. Close. Let's move.
To anyone. Okay. That was the only thing, yeah.
Severin Neumann 00:04:41 Yeah.
Austin Parker 00:04:42 I have a topic after this.
Severin Neumann 00:04:49 Yeah, I think we can try to go through those real quick, but then we can merge this PR, right? So I think there's one… commit suggestion, but beyond that, I think we can… we can merge it, right?
Awesome.
Another one that got active again is the audit logging stick.
I… some folks from SAP, They have been doing some prototyping and, like, Yeah.
I… I'm wondering what to do with this next, right? I mean… It's just something where we say, like, hey, technically it's… Like, within the scope of our project, but they should need more people contributing to it, or is it something where we say, like, hey.
This is maybe something that should stay outside of the project, or what's our emotions around that?
Ted Young 00:05:51 My feeling is if what we're trying to do right now is snow tell, right? Like, if the big effort right now is, like, we want to clean up these SDKs and put a bow on everything for graduation, then, like, audit logging is, like, the perfect example of the kind of thing that would go into the freeze.
where we'd say, like, that's audit logging, great idea, we totally want to do it, but that's features that SDKs are going to have to implement and think about, and so let's pump that to the other side of Snowtel.
Severin Neumann 00:06:23 Hotel, okay, now I get, now I get.
Austin Parker 00:06:25 Yeah, I… I think… We should just… I wish we had a better… I know why we do it the way we do it, but I really… I feel like it kind of kills us that people… Can't go off and… build clean extensions on OTEL.
Ted Young 00:06:53 If they want to go build it as, like, a third-party thing in the hopes of getting, like, OTEL to adopt it later, like, I think that's cool.
Austin Parker 00:07:01 Yeah, but the thing is, is, like, we discourage that with the… like, I feel like we discourage that because of… The whole, like, oh, when people go off and they build stuff in the corner, and they come back and the TC hates it, or whatever.
Ted Young 00:07:14 Yeah, because that's what happens. That's why I don't want us to have, like, a sandbox, right? Because if we promise people something, and then we reject it, then, like, that's.
Severin Neumann 00:07:25 Mmm.
Ted Young 00:07:26 on us. But if we're like, yo, if you guys just want to go build your own audit logging idea on top of OTEL, like, go off and.
Austin Parker 00:07:34 Yeah. I, I feel like…
Severin Neumann 00:07:36 But, but…
Austin Parker 00:07:36 Oh, gone.
Severin Neumann 00:07:38 Yeah, but maybe then, like, it could be, like, a good workflow of how, like, hey, why not spin this off as a CNCF sandbox project, right?
And just to repeat it, like, I think, like, the one thing is, like, as you said, like, hey, people doing their own stuff, and just suddenly we know about it. But what I like about that one, they approached us and said, like, hey, we want to do audit logging on top of OpenTelemetry, and then We looked into, even we looked into their proposal, but then saying, like, hey, this is awesome, we want to have that, but thinking about it.
for a while, actually, this is, like, our… what was the first Kubernetes project that was not part of Kubernetes? That's our moment, to say, like… and I think this… this should be an option for a project proposal, that we say, like, hey, this is really cool what we are doing here.
We think that totally should exist, but maybe the route that you should be taking is not being part of the ever-growing OpenTelemetry project. We support you to spin off your own CNCF thing, right? Maybe that's something we should encourage people doing.
Dan?
Dan Gomez Blanco 00:08:46 Yep, no, I agree with that. And, I also think that from the perspective of the project proposal, and I can't remember exactly now.
If it actually identifies what problems What are the challenges for Hotel to enable that?
So, like, you know, is there anything specific that, you know, is currently basically under the scope of OpenTelemetry?
that, you know, hey, this is a problem for if we wanted to audit logging on top. So maybe, like, there is a split here of, like, hey, on one side, there is the stuff that we can do in OTEL to be able to, you know, empower that.
And the stuff that is, like, you know, not in the scope of hotel. So I think, you know, that's something that we can discuss in the project proposal as well.
Trask Stalnaker 00:09:24 That's what I was gonna raise. For this specific proposal, they can't just go off and build it, because it's very tied to reliable delivery, which is very tied to, like, inside of OpenTelemetry stuff.
That… that's all, but I… I… I support… pushing it. I both support this proposal, I'm interested in this proposal, but I also support that it's not the right time to be you know, trying to spin up a SIG, and… putting TC, resources on it.
Austin Parker 00:10:05 So, I, I wanna… Actually, push back a little bit on what you just said about, like.
it needing to be part of it. I… feel like… if… The design of OTEL is not such that someone cannot re-implement and extend part of the spec and have it cleanly integrate into the rest of OTEL, then we have done fucked up somewhere.
like… I think going and saying, like, hey, yeah, this is a great idea, we don't have the bandwidth to put this in core right… to actually… we don't have the bandwidth to deal with this as, like, a core product feature right now, a core part of OTEL. But the design of OTEL is such that you should be able to go and, like, write Like, re-implement the parts of the SDK that you need to implement to make this work.
Without having to…
Trask Stalnaker 00:11:04 Nobody wants to re-implement SDKs, though.
Austin Parker 00:11:06 I'm able to…
Trask Stalnaker 00:11:07 But…
Ted Young 00:11:08 Just to have…
Austin Parker 00:11:09 Yeah.
Ted Young 00:11:09 Like, I disagree with the idea someone can't implement this on top of OTEL right now. You can make your semantic convention for.
Austin Parker 00:11:16 Oh…
Ted Young 00:11:17 Identifies an audit log, and you can make your own, like, audit exporter that only plucks those things and does reliable delivery instead of.
Austin Parker 00:11:25 I mean, I agree with.
Trask Stalnaker 00:11:26 The reliability goes all the way to the API call, it's not.
Austin Parker 00:11:30 Right.
Trask Stalnaker 00:11:30 It's an X.
Austin Parker 00:11:30 There's…
Trask Stalnaker 00:11:31 concern.
Austin Parker 00:11:32 Right, it is, like, there is… there is other stuff. There would… this would be an audit logging provider, basically.
Ted Young 00:11:38 Right, or it's a totally separate thing like that. Yeah. Completely separate, in which.
Austin Parker 00:11:43 But…
Ted Young 00:11:44 do it.
Austin Parker 00:11:44 But… the design of OTEL should be such that you could write audit logging export, or Audit Logging Provider.
and have that work without having to, like, change protos or do whatever, and I think that we should… be comfortable telling people, like, hey, we expect the design of OTEL that you can go and implement just what you need to make this happen without it also changing core stuff, and for it to be pluggable. And if you go off and work on it and find that that is not the case, okay, great feedback, that's something that we do need to fix.
But we shouldn't just tell people, hey, wait forever until the TC gets unblocked or whatnot.
Ted Young 00:12:26 Yeah.
Yeah, you could just wrap the provider. I feel like there's a million ways to solve this as a separate project.
Alolita Sharma 00:12:36 Yeah, but I, I think, exactly to the separate project point, to Austin's point, you know, I would say it's not that easy anymore to just say that you can go and create another project in CNCF and introduce another project.
Trask Stalnaker 00:12:57 It's hard. That's why people want to do it inside of… they want.
Ted Young 00:13:01 piggyback on our community.
Austin Parker 00:13:03 No, they shouldn't do it in the CNCF. They should just.
Ted Young 00:13:06 You should go do it.
Austin Parker 00:13:08 Yeah.
Ted Young 00:13:09 Right? If I was the CNCF, I would reject this thing as being too small in scope.
Alolita Sharma 00:13:14 Right.
Ted Young 00:13:15 I want to have it as a sandbox, because then we're telling people this mixed message of, go off in a corner, but somehow we're also going to implicitly okay your thing, right? Like, that's the problem with the hotel sandbox, is we…
Alolita Sharma 00:13:29 If what we're telling… Yes, exactly.
Ted Young 00:13:31 We may reject your thing totally when we look at it. We don't want to tell people.
Go put our brand on it and tell users that… to go get stuck on this thing, and then we, like, get stuck supporting it.
Alolita Sharma 00:13:43 But I think… They're doing.
Ted Young 00:13:44 Just go have fun.
Alolita Sharma 00:13:45 just to… you know, have a path forward for folks to go and build or innovate on top of Hotel.
maybe having an, you know, the conversation of having a sandbox kind of project, even outside, you know, CNCF might be something useful to consider. Because, again, I think it's very hard for people to come through the CNCF route. It gets harder as we go along.
But, It's also that we want to encourage folks not to just go away, right, and do something in the wild, and yet have the mentorship coming from the project.
Ted Young 00:14:25 But if what we're saying is we don't have the time to be, right? Like, this is the loop we're in. We're like, let's bring them in, let's make a sandbox, and then, like.
Alolita Sharma 00:14:33 Yeah, yeah, and it doesn't have to be…
Ted Young 00:14:35 C.
Alolita Sharma 00:14:35 Agreed, agreed.
Ted Young 00:14:36 If we're saying we're not gonna do that, we should just be blunt and say, go create a GitHub organization called Hotel Audit Logging.
And just go make your thing there. And… And then, like…
Alolita Sharma 00:14:48 That we could, yeah.
Ted Young 00:14:50 I mean, that thing gets, like, super popular on its own, then, like, hells yeah.
Alolita Sharma 00:14:53 Then they can come back again, then.
Morgan 00:14:55 Yeah, although that'd be… It might have produced incompatible semantic conventions or something, and it's already established, that's the risk.
Alolita Sharma 00:15:03 Exactly.
Ted Young 00:15:03 That's a risk we have with it being in an hotel sandbox, too, I guess is what I'm saying. The difference is, if it's in an hotel sandbox, it's got our name on it, and now it's, like, really confusing.
Alolita Sharma 00:15:12 No, no, but the knee…
Morgan 00:15:14 But we might be able to rein some stuff in, is the difference.
Austin Parker 00:15:17 I wanna just… I wanna throw out an example, or just a.
Morgan 00:15:21 Yeah.
Austin Parker 00:15:21 Or a point, just a point.
Model context protocol.
Pablo Baeyens 00:15:27 Anthropic? Like, let's.
Austin Parker 00:15:29 Yeah, sorry, I just, I want to point out, like, this is not, like, a weird thing in open source.
Alolita Sharma 00:15:33 Yeah.
Austin Parker 00:15:34 Anthropic said, here's model context protocol spec. A bunch of people went out and wrote Go implementations. And then later, they decided, okay, we're gonna go and we're going to, like, make an official upstream SDK. And they didn't just take one of those existing ones, they took ideas from those.
and they pulled it in, and now it's like a core official upstream thing. It doesn't obliviate the work those people did to make their own implementations of it. Like… This is not… this should not be a weird or unusual thing in open source. Like, we should have some confidence in ourselves and say that, hey.
go build it, if you think it's a good idea. If it's a good idea, people will use it, and if it's a really good idea, then we'll figure out how to make it part of Upstream, once you've built it.
Ted Young 00:16:23 Yeah.
Severin?
Severin Neumann 00:16:26 Yeah, I think at the end, just what I hear is, like.
we are not reject… or we would not, like, say no to them because we think it's not a good idea, or should not be part of OpenTelemetry, where we say, like, right now, we already stretched so thin.
And… and we decided to… to laser focus on a few things.
So, here's what we recommend. You do this as a dedicated open source project, and we're happy to work with you closely, right? I mean, if they show up at a SEMCON for SPAC and say, like, hey, here's a change that would help us in our project to be successful.
I think we would be the last people to reject that, right? Except it's like… Contrary to anything we do, but if they say, like, hey, here's some audit, same conf, and we want to have this upstreamed, or whatever, And then later, we can still say, like, hey, what you built here is really cool, let's consume this into our project. So that's what I hear right now.
Alolita Sharma 00:17:25 Yep.
Ted Young 00:17:27 No.
Severin Neumann 00:17:28 URLC.
Juraci Paixão Kröhling 00:17:30 So I have two comments here. First, well, three, I guess. The first one is, I'm sorry that I joined late, and I think I missed the mention to Hotel Sandbox before. But the second thing is.
Sandbox is a sandbox. I don't know how it is in other countries, but here in Germany, when you go to a sandbox, it's written there that the parents take care of their children.
There is no supervision expected by anyone. You just go there, and you are responsible for playing there. It is the same here at Sandbox. I mean, Sandbox is just a neutral place for people to come and collaborate and play together. If the result of that is successful, if there is a community, then we can accept them.
Like, problems that we have.
the problems that we have with Kotlin, or the concerns that we had with Kotlin, could be solved by that. Like, okay, so prove us that you can build a community. And the result of that is we are taking a leap of faith here, trusting that there will be a community. So, the options that we have is either we don't accept.
And we don't move, we don't innovate, and we don't, we don't allow that to happen here within, like, close to us.
Or we accept, and then we end up with, and now I'm not talking about coffee specifically, but then we end up with a lot of half-baked things.
Like, we have a lot of half-baked things in here. A lot. Like, it's a real problem. And if we want things to move.
it's gonna be like that. Like, contribib. Like, contrib is… like, 90% of contribib, any contribib, is half-baked. Like, I… perhaps even more than that.
And people have the expectation that things in Contrib work, and we heard that a couple of weeks ago during the interviews, like, people would expect things in Contrib to have our stamp of approval, and they don't.
And I think… but I think… The third comment that I wanted to make.
I think we should not be even having this conversation right now.
We have so many things right now on our plates. We have to stabilize what we promised to stabilize a couple of years ago.
I don't think we should be talking about audit logging, whatever. I don't think we… Naveen? Kotlin? I mean, sorry for the folks doing Kotlin, but I think even Kotlin might be, like, something that is a distraction for us right now. Like, we just got a report on things that we should be fixing, and as a community, we… At the GC, we have the power to press a stop button and have the community move towards this common goal.
And if we press the stop button in some places of the community, but we leave the doors wide open at other parts of the community, I don't know what is… what kind of message that is. So I think the message should be, we are focused on graduation right now.
That's all that we are thinking about right now. Anything else is a distraction.
And… I'm sorry, Pablo's next, I suppose.
Pablo Baeyens 00:20:29 Yeah, I was going to say, if there's concerns about, moving this to an external project via the CNCF, why don't we ask the CNCF about what they think about this?
We sold… Maybe the TOC, like… Yeah, we want to focus on graduation, How has this worked for Kubernetes?
Wait, what up.
Alolita Sharma 00:20:54 You know, to talk to the… Kubernetes community?
Pablo, because TOC will not be able to provide.
Pablo Baeyens 00:21:01 Talking to the TOC would be the first step, and if the TOC thinks talking to the Kubernetes folks is the right way of doing it, then yep, talking to a Kubernetes folks.
Alolita Sharma 00:21:11 I think… I think, to that point, maybe inviting DIMS, who has been part of the Kubernetes community, may be useful to come and talk with us at the… in the GC, but, Beyond that, I would say it's not the TOC's job to come and tell us what to do.
Morgan 00:21:27 Yeah, I wouldn't… I agree with Alita, also with Austin's comment, like, I wouldn't over-index on the TOC's feedback, like.
Alolita Sharma 00:21:34 Yeah.
Morgan 00:21:35 concerns about OpenSelemetry getting overstretched, at least for myself, like, I don't… my concerns are not influenced by the feedback from the TOC. Like, some of their feedback was on point, a lot of it, I thought, was not.
Alolita Sharma 00:21:45 Yeah.
Morgan 00:21:46 So I would not over-index on their feedback.
Pablo Baeyens 00:21:49 I mean, it's not about over-indexing under feedback, it's more about, like… We want this to be an external project, or at least some of us do, and, like.
the CNCF would be the place for this project to be in, and if we're going to send the people the way, we may as well talk with the CNCF about this.
Austin Parker 00:22:11 I want to just make a really quick point on that topic, though. The CNCF would like… they… They need something before they… Like, you don't go to the CNCF with an idea, you go to the CNCF with a project.
Alolita Sharma 00:22:22 Yeah.
Severin Neumann 00:22:23 It's true, yeah, yeah.
Pablo Baeyens 00:22:25 Sure, I mean, well, then…
Austin Parker 00:22:28 I mean, if you all would like, I can compose a very nice, message to the, people to that issue, and just be like, hey, this is a great idea!
Go work out on over there. But, like.
just telling someone, like, hey, go to the CNCF without an actual…
Morgan 00:22:45 Signature.
Austin Parker 00:22:45 thing is premature. Yep. Yeah.
Ted Young 00:22:48 I will say, if this organization blocks mobile and client development on a whim, or blocks, like, the ability to stand up the OpenTelemetry SDKs as an operator with the injector, I will quit this fucking project and become, like.
Morgan 00:23:05 Yeah, those are both very critical.
Austin Parker 00:23:07 Yeah, I don't want us to over-index on… I'll just say it with my voice. We really… We all read… we were all there, we all read.
Ted Young 00:23:17 The idea that those things need to be stable by the time we graduate, I totally disagree with that, right? Yes. That was… that was the crazy part of their feedback, was that.
Austin Parker 00:23:26 But, but again…
Ted Young 00:23:28 scope.
Austin Parker 00:23:28 We all saw this, we all were there, we all talked to them, we all read the feedback, and we all also saw that a lot of the things that they pointed out were things we were already doing.
Alolita Sharma 00:23:37 Yep.
Austin Parker 00:23:38 like…
Ted Young 00:23:41 Yeah. I would really like to talk about this adopters thing.
The what thing?
Austin Parker 00:23:46 The adopters thing?
Alolita Sharma 00:23:48 Yeah, that's… You have it on the list, Justin.
Ted Young 00:23:54 Yeah.
But I'm glad that we're all in agreement that audit logging is, like, an example of something that's just, like, it's a new project, it's not something our end users are, are, like, clamoring for the way they are.
Morgan 00:24:06 Yeah.
Ted Young 00:24:06 for, like, client stuff, it's… it's, like, very useful. It's, like, clearly in scope as, like, a thing we'd like to do, but it's definitely… like, something that would take resources away from existing stuff, which I would say, is the other thing the mobile and client stuff isn't really doing, right? Like, it's like… it's more like an extension of the project with people who are already involved.
But if we were to try to figure out, like, audit logging and reliable delivery instead of available delivery, that would be like the client SIGs coming back and being like, we want a high-performance mobile protocol. We've already told those people no, because that means like, the TC and everyone has to get involved, but if we want to just build instrumentation… for… for mobile and browser stuff, that… that's not really getting in anybody else's way. So, like, that's okay.
I think that's, like, a reasonable way to kind of, like, shut the gate on new stuff going forwards.
Anyways, Jossi?
Juraci Paixão Kröhling 00:25:09 nothing against Kotlin, or I do agree that client instrumentation is essential, is critical.
at the same time, I'm not… I don't have this opinion because of the TLC comments, or adoption interviews, or anything. I'm making those comments because more than 2 years ago, we were all in Seattle, or most of us were in Seattle, and we came up with a list of things to do.
like, stable instrumentation, performatic instrumentation, like, to have instrumentation and SDKs that have good performance, we are not there. Like, nothing, nothing, like, we're talking about the V1 for the collector.
I mean, nothing that we talked back then happened. So when, Austin says that, you know, we have to walk and chew gum at the same time, I don't know if I get the analogy there, but I think, we haven't done either.
we haven't walked, as good as we could, and we didn't chew the ground as good as we could. I mean, we did poorly, both. And I think… from where I'm standing, we can either keep doing both badly.
Or we can focus on the one thing that we have at hand, like, we have a list of high-priority things right now, and it just so happens that it's a match with what we sent to the CNCF.
And then, we work on that, and then we get it stable. And then we pat ourselves on the back and say, yo, good job, we did what we were supposed to do, like, two years ago. Now let's move on. Now let's get client instrumentation.
If we wait for client instrumentation to be… I mean, if we… I don't know. Again.
Austin Parker 00:26:46 I don't… I don't.
Juraci Paixão Kröhling 00:26:46 Find instrumentation is needed.
Austin Parker 00:26:47 We wait? I think it's…
Ted Young 00:26:50 Hey.
I just think that's… that's an inaccurate assessment of what's blocking us, Jurassi. I'm completely in agreement with you that, like, spinning up more things for, like, the Python maintainers to deal with, and the Ruby maintainers, and, like, everybody who's, like.
maintaining the collector and the SDK, it's like, all of those people need room to just, like, focus on improving the stuff that they already have. But… but, like… you know, the people trying to stand up Android instrumentation aren't… aren't blocking that.
That's… that's… that… but something like audit logging would be like a torpedo in the side of, like, every SIG, you know?
Juraci Paixão Kröhling 00:27:32 I think it is more about the message than the actual implementation, like, the message that we are stopping the road to fix what we… or to do, what we promised to do, I think that's very important. And if Kotlin is the exception to that rule, that's fine.
Like, we can then all convince the community that, you know, Kotlin is so important that it has a… the GC's blessing to bypass the rule. But the rule is, we don't consider anything at all, like, new.
That… I think that's…
Ted Young 00:27:59 I would be in complete agreement with that. There's a couple things we need just to be, like, unblocked with the existing stuff, and I would say Kotlin's kind of the last bit of that that I see on this list here. When I look at the other stuff on this list, it's not… It's, I'm not seeing anything like that.
Severin Neumann 00:28:21 I mean, the Ecosystem Explorer is kind of contributing to that, and it's not, like, a net new thing, it's the evolution of the registry and helping with what we try to do, right? I talked with Jay that, like, adding stability to whatever we build is definitely going to be essential.
And the Elastic PHP stuff is also… an instrumentation, like, an improvement for what PHP is doing today, right? It's a one in, one out.
So it's less about spinning up a new SIG. And this is maybe the comment I wanted to make. I think I totally agree with what Jorasi said about, like, yeah, we need to focus, and we need to make sure that we do the things that we do, but at the end of the day, we're an open source project, so we have to figure out how do we get people in to our community to help with that.
Ted Young 00:29:05 Right? Because if we say, like, yeah, we only do these things that we.
Severin Neumann 00:29:08 do, and we only do it with the people that we have today, we will also not move really fast. So I think it's still a question of, like.
what are the things that help us on that mission, right?
I mean, think about the injector, right? I mean, if it would come today, would we accept it? Probably yes, because it's helping us on… on the whole problem that we have with ease of use and stability. But, yeah.
Austin Parker 00:29:37 Can I just… Just a… to pull a couple things together real quick. One, like… I don't necessarily know if it's helpful to conceptualize, sort of, the problem as, we made these commitments to ourselves and we haven't followed through. Because, you know, some of the feedback… When we were at the collector call on Monday.
A specific thing came up around, like, oh… A maintainer had been trying to, you know, someone had been trying to, improve the memory limit defaults.
For multiple years, and it, you know, kept getting pushed, you know, punted back.
And I have not gone and, like, done a complete, exhaustive investigation of what exactly that entailed. But that… sounds to me like, okay, something in Collector is obviously happening that's distracting from, like, this important work.
I… I really feel like what we… Need to do and say publicly is… To echo a point that Ted has made, we need to publicly state, this is what we think OTEL This is what we are committing to deliver as a project. This is the product that is OpenTelemetry. And this is what that means. And this is what we are going to orient the community around.
And it should then be pretty straightforward for people to figure out, is the work that I am doing aligned with that mission or not?
And if it's not, then… You know, it gets put in the back burner.
Pablo Baeyens 00:31:29 I think that's a good segue into the next topic in the agenda, and maybe…
Austin Parker 00:31:33 So…
Pablo Baeyens 00:31:35 So… I don't know if it's mine… yeah. So, I've gotten a couple people asking, like.
what should they do to help on addressing the TOC recommendations? We've spoken about filing these for OTEPs, we've spoken with the collector.
People… we are kind of the bottleneck on, like, making progress on this, and… I don't know, I want to discuss if there is some way of… getting people involved, starting now. And I have one idea, which would be just something very simple on filing for issues for the different four OTEPs, and opening those issues as, like, a forum for discussion for each of those. Even if it's, like, not fully fleshed out, we have the core idea there, and… Different SIGs can give their feedback on… What do you think about that core idea?
Severin Neumann 00:32:26 Question for clarification, when you say people, what kind of people? Like, existing contributors, maintainers, external people?
Pablo Baeyens 00:32:33 and maintainers. Yeah, a couple of.
Severin Neumann 00:32:36 Because that drives a different conversation versus, like, hey, there's some people at Datadog or Dynatrace or any other.
Pablo Baeyens 00:32:42 Oh, no, no, no, it's like…
Severin Neumann 00:32:44 It's specific maintainers, yeah, okay.
Ted Young 00:32:48 So, so what I'm wondering is, you know, we've said we've got… got 4 possible initiatives, Can we pick one of them?
And be like, this one's the most important, let's kick this one off first and quick and get everybody… Kind of rowing in the direction on just one, rather than trying to hit them with four at the same time.
Alolita Sharma 00:33:11 Yeah, I agree with that approach.
Ted Young 00:33:17 And which one would that be, in your opinion?
Austin Parker 00:33:22 The one thing I will say is that… They are all kind of related, like, they're not… It's not like, oh, we have 4 distinct things, it's like… One of them is updating… you know, it's like, okay, this one… updates and clarifies the stability and maturity stuff. And then the next one says, okay, with that in mind, now here's the new bar for what is considered stable and how that should be presented. And then the next one is, like.
I don't have it pulled up, but… right, like, and then the last one is sort of the release sig, and things like that, and so they are… like, I think there's… I think there's very specific things that we could do, like, that we could say, like, right now, which is, like, hey, if you aren't… already… Putting your docs on the website, then you need to think about how to put your docs on the website.
Including, like, example code, including samples, include… anything that is end-user facing needs to live in the website, and that needs to be canonical. Like, that's something that we could go tell people today.
Ted Young 00:34:37 Docs would be a great place to start, but also you mentioned stability, right? Having a new approach to maybe marking something stable that.
Austin Parker 00:34:46 Yeah.
Ted Young 00:34:46 Stable because of semantic conventions, but then also, like.
Austin Parker 00:34:50 Right, that's the third one, is the CENCOM thing.
Ted Young 00:34:52 rib that's, like, unmaintained and unmaintainable, right? Like, like, picking something like that, like, let's just focus on stability or docks or something, just as a place to get everybody.
Austin Parker 00:35:01 Yeah, I think starting with… I think…
Pablo Baeyens 00:35:04 You ordered them… you ordered them in some way, Austin, when you were talking, so maybe we can start with the first one that you mentioned, the stability guide.
Dan Gomez Blanco 00:35:12 Can I ask the name?
Austin Parker 00:35:13 It's probably the most controversial one.
Dan Gomez Blanco 00:35:16 But I think you mentioned one thing there, though, is, like, that they are interlinked, right? And I think, What if we deconstruct that feedback into, you know, a bit of product thinking, and thinking of the problems that we're trying to solve?
and then prioritize those first. So, like, you know, say, okay, what is the actual… Paying for the end users.
And it would start from that point.
then we say, okay, so how do we solve that pain? And it could be, like, multiple things that, you know, that, you know, that we can… multiple items that we can do for one single, sort of, like, you know… One single problem that end users are finding, basically.
Ted Young 00:35:53 It seemed like another way of breaking the feedback down was there was, like, 3 categories. There's, like.
you know, stability, right? And communicating stability better. There's installation and management, right? Like, we have config files, we have, like, remote management, we've got some injector stuff coming for being able to, like.
allow operators to do it, there's better docks for installing this stuff. There's all the things people need to, like, make installation of hotel suck less than it currently is. That seemed to be, like, the other big area where just lots of feedback was.
And then the third one was basically, like, performance and overhead feedback.
I feel confident saying, like, that goes to, like, the bottom of our list, as far as, like.
Like, we don't need to be working on performance and optimization at the same time as trying to, like.
improve the installation experience or stability. We could… We could say, like.
That's… that… that's gonna come later.
But am I… am I missing something in… in terms of, like.
Those three areas being where we're getting feedback?
Austin Parker 00:37:02 I don't think you're missing things, I think the problem is that… Or the challenge in sort of converting those things into OTEPs, or at least, like, policy guidance, is that they're all very interrelated.
The one… so the exception here is sort of, like, the install… And again, I would point out, like, we are working on all those things, right? Like, the config stuff is, I would say, going pretty well.
Alolita Sharma 00:37:31 Hmm.
Austin Parker 00:37:33 at least in terms of getting it rolled out more broadly. I don't know if anyone has alternative interpretations, but in my mind, at least, it seems like it's going pretty well.
Ted Young 00:37:43 I feel like I don't have eyes on it holistically.
But… But that's… that's an example of an initiative we could get everyone around. It's, like, the config file is, like, a thing we could.
Austin Parker 00:37:55 Yeah.
Ted Young 00:37:56 Don.
Austin Parker 00:37:57 But I… so I think, like, part of… so part of, like, what is… what does it mean to be stable now, or what is the new… what is the new bar? Like, one of the things in the new bar would be, like, oh, to meet this new bar, you've implemented declarative config… 2.0, right? Like…
Ted Young 00:38:16 Another way of framing it is we get dinged for being inconsistent in our implementations.
And the… what maintainers say is they basically implement features that end users are filing issues on, requesting them to do, but we're saying that actually we're picking some subset of features and saying these are kind of a baseline of stuff We actually want this to work everywhere, all the… Right. A config file is an example of… We can't tell everyone to implement everything, but we could say, like, at least this small handful of features we want to make sure are.
Austin Parker 00:38:51 Well, and to Jurassi's point, sorry, sorry for talking over the hands, but to Jurassi's point, like, part of it could also be, like, hey.
we need you to… maybe the perf requirement isn't, like, oh, you have X amount of perf, it's that you publish what the overhead is for your instrumentation.
Right? Like… Because I think it's unreason… it's unreasonable… I think a blanket requirement like, oh, you can't increase, load by more than 5% or whatever is… That's impossible. But what you can do is you can benchmark your shit. And you can say, in this config… the default config, you should expect to see X overhead for installing and using this instrumentation. And that should be part of, like, the bar for your Sable, right, is just those sort of benchmarks.
Juraci Paixão Kröhling 00:39:42 And we are happy with those numbers.
Austin Parker 00:39:45 I… You're willing to back up the number. You're at least willing to say, like, here's the number.
Juraci Paixão Kröhling 00:39:49 I mean, if you're not happy with the numbers, it's not stable. If it is stable, I'm happy with the numbers. No matter what the numbers are. Like, I'm publishing the numbers, I'm happy with the numbers, it's stable. I call it stable.
If I'm not.
Austin Parker 00:40:03 I will point out, different users are going to have extreme… extreme outliers in terms of what is acceptable.
Juraci Paixão Kröhling 00:40:09 That's why, like, that's why. I am a maintainer of that. I'm happy with the number. You as a user, you might not, but that's my bar.
Austin Parker 00:40:17 Yes, you're saying this is this… this is the… this is the number that we hit, and it might be… we might want to improve it, but we're… we are satisfied that this hits the 80th percentile use case, or whatever.
Juraci Paixão Kröhling 00:40:30 you're satisfied, is what I've been looking for, yeah.
Austin Parker 00:40:32 Yeah, like, we're willing to stand behind this number.
Ted Young 00:40:35 Anyway…
Alolita Sharma 00:40:36 Yep, agreed.
Ted Young 00:40:37 room.
Severin Neumann 00:40:38 Yeah.
So from what I hear, I mean, I agree that all those things are interconnected, but from what I hear, I think, like, the… declarative configuration, I mean, we're doing this already, right, is step one. And for me, and this is also, like, maybe my doc's perspective, but, like, if we could get to a point where, like, getting started with any SDK is as simple as it is, for example, with the Node SDK initialization, or with, like.
hey, SDK in it, and here's the config file. If we can get to that, I think we went a long, long way, at least for SDKs. Let's not talk about auto-instrumentation yet, right? So… I would love seeing that, right? I would say, like, this is something where we could go a long, long way.
And then on the back of it, we can say, like, hey, this is now our new definition of stable, but I think that's… that's a… I would prefer starting, really, with just making all that stuff easier, and… what also belongs to that, and I know that I owe, like, running that project, but, like, having that kind of reference implementation in that app.
That showcases, like.
where the problems are, right? That we have something like, okay, this is… I mean, look at how you do Go today, right? I mean, it's like this long laundry list of things that you need to initialize instead of, like, just saying, like, yeah, just start with it, so… if I would start with anything, then it would be, like, the declarative configuration and this whole, like, how do I get even started with my SDK?
And have it consistent across languages.
A blow.
Pablo Baeyens 00:42:23 Oh, okay, yeah, you still have your hand raised, so I didn't know if you had…
Severin Neumann 00:42:26 Yeah, sorry, I forgot to remove it every time, so anyways.
Pablo Baeyens 00:42:31 Alright, so, My point was more on… not on the specific solutions that we want to see, but how do we communicate that to… maintainers, the wider community, and where can they express what they think about this? Like, I don't feel like we discussed that concretely.
Austin Parker 00:42:51 Oh, I was thinking we would open some GitHub discussions in community.
Ted Young 00:42:54 Hmm.
It's almost like I want something that's, like, a meta-OTEP, right? Like, I think, Austin, you've done a good idea of, like, here's, like, there's, like, these are our goals, and then we've decided we're gonna break those goals down into these steps, and these OTEPs relate that steps, but I… I can imagine the community might have feedback even at that level about whether that's The right way to… to break things down, and giving them an opportunity to…
Austin Parker 00:43:20 So, as a suggestion… What if we commit to this week, we go through the language and that stability blog.
We get that where we are all happy with it, and then we publish that, and then we say at the end, we would like to have a public discussion about this in this this GitHub discussion.
and then let people go talk about stuff there while we're working on the OTEPs, because I don't necessarily want to just, like, fire up 4 more or less boilerplate OTEPs Without spending a little bit of time actually, like.
writing them, and not just having fucking AI do it for me.
So, how does… how does that sound as, like, an actionable next step? Because I think if we can do it this week, that's good too, right? Like, if we can get that blog up this week and say, hey, here's the direction, then that is, I think, a good thing to kind of go and show DIMS, and be like… and say, like, hey, look, we listened! Ha!
Not that we weren't listening before, but like… Demonstrating that we're actively working on this.
Ted Young 00:44:30 feedback, but we're not gonna slow our roll and wait for the feedback. We're gonna assume our plan is, like, a good one, and then we'll adjust it.
Austin Parker 00:44:39 Right, we'll adjust it as we go.
Ted Young 00:44:40 As people start taking potshots at it.
Austin Parker 00:44:43 Yeah. So does that sound like something that we are all, like…
Alolita Sharma 00:44:47 Yeah, that's a good idea.
Dan Gomez Blanco 00:44:49 That's good.
Pablo Baeyens 00:44:50 I think…
Ted Young 00:44:50 I'm, like, moving fast, I'm kind of scared.
Pablo Baeyens 00:44:53 like… the draft or something before, with my 10 years, before we publish it on the blog? Like, we don't need to, like, do the whole OTEP thing before we publish this, but just, like.
Austin Parker 00:45:05 share the…
Pablo Baeyens 00:45:06 The community know Duh.
Austin Parker 00:45:08 I mean, we can share the draft.
blog, once it's a PR.
Dan Gomez Blanco 00:45:13 Chair of the PR.
Pablo Baeyens 00:45:14 Sure, that works, but yeah, like, leave at least a bit of time for people.
Austin Parker 00:45:18 What I would… I would like for us to close on this, because we need to talk about the adopter thing, but, can I just have everyone go through the… I will relink it in the GC chat, but can we all just, like, go and make some time?
Today, tomorrow, to go through that, and then Friday, I will get a PR up.
Alolita Sharma 00:45:35 Sounds good.
Pablo Baeyens 00:45:37 Makes sense.
Austin Parker 00:45:37 And then we can let people look at it over the weekend, and then publish it next week.
Alolita Sharma 00:45:40 Yep.
Pablo Baeyens 00:45:42 Yep.
Austin Parker 00:45:42 Alright, great.
And also, if you have any ideas or suggestions or anything, please just, like, for the OTEPs, like, please just leave notes at the bottom of that in the OTEPS section.
That'll help me out a lot.
Anything else on this?
Pablo Baeyens 00:46:10 Nope, you are next.
Austin Parker 00:46:12 So we… Committed to… Giving more adopter info to… gems, and then… I really… Need that?
Like, soon?
Specifically…
Alolita Sharma 00:46:33 What do you need specifically?
Austin Parker 00:46:35 I, I need… I need more adopters. I need, like, names, email, title, I need it sent to me.
Like, and then I will send it, and I will hand it to them, and say, these are the people you should go talk to. The… and… out of… I, I guess also make sure it's not a vendor.
Alolita Sharma 00:46:57 I tend to disagree with their decision about, like, excluding vendors.
Austin Parker 00:47:04 Because… Like, I think that's silly. I think that all of us work at places that have implemented various parts of OTEL and are thus also end users. I think they would get very useful feedback, but… They don't seem to want that, so, okay.
Dan Gomez Blanco 00:47:23 If you can just get me…
Austin Parker 00:47:26 Names, emails, titles, companies.
Dan Gomez Blanco 00:47:29 And that's more than the original list that we had in our internal channel. I think we…
Austin Parker 00:47:33 I want to make sure… I… if they were people that were on that original list, I would, please reach out to them and be like, hey, did anyone contact you? And if they said no.
then I would like them to be on this list. I would especially like for people who were on that list that didn't get reached out to, that match the end user.
Alolita Sharma 00:47:51 So.
Austin Parker 00:47:51 thing.
Alolita Sharma 00:47:52 Austin, I can tell you that, I… we were, from Apple on the end-user list, initially, and… I reached out to Emily, and she said she would reach out if she needed more adopters. Okay, well…
Austin Parker 00:48:06 One of the things we… so that… so, give me the name and email in person, and I will.
Alolita Sharma 00:48:12 Silly.
Austin Parker 00:48:13 Hey, you asked for more adopters? Here's an adopter, right?
Alolita Sharma 00:48:16 Yes.
Austin Parker 00:48:17 I do not have that list, because I did not make the form, Jurassi.
Juraci Paixão Kröhling 00:48:20 No, but I think… I think we had a thread on the GC channel some time ago, where we listed all of the adopters that we would, get in touch with. I don't know if we placed that list elsewhere, or if it's only there. I mean, I can.
Austin Parker 00:48:33 I don't know. If someone can go look, that would be great.
Juraci Paixão Kröhling 00:48:36 I can find that thread, I mean, I have a name here that we would only mention on that context, like…
Austin Parker 00:48:43 Okay, well…
Dan Gomez Blanco 00:48:44 I'll check again. Like I said…
Austin Parker 00:48:46 We don't have to, like, dwell on this too much, but… and also, people that aren't… people that are adopters that were not on that list are also fine. Like I said, they don't have to be, you know… glowing… like, I want people that are, you know… typical AOTEL users, I guess?
Yeah, like, I think the thing that's concerning to me is the feedback of, like, oh, we couldn't find adopters. Like, that doesn't make sense.
Alolita Sharma 00:49:15 I… I have to say that they didn't… they just waited for folks to reach out and, you know, and the link that was being shared was a Calendly link for… books to book time on, the Emily's calendar, for example, or Dimz's calendar.
Austin Parker 00:49:35 Yeah.
Alolita Sharma 00:49:36 It was just that… People don't just… Like a fishing attack already?
Austin Parker 00:49:40 or something… I, I… I don't want to dwell on the process, they run the process their way. I want us to be able to say, you said you had trouble finding adopters, here you go.
Alolita Sharma 00:49:53 Yes. We should be able to provide…
Austin Parker 00:49:56 Adopters.
Alolita Sharma 00:49:58 Agreed.
Austin Parker 00:49:58 So, that's my… that's my ask. I would really love if we could do this, like… So, Austin, should we just add to a doc, or just ping you on DM? You can just, like, if… let's make a Google Doc.
Alolita Sharma 00:50:08 Okay, sounds good.
Juraci Paixão Kröhling 00:50:10 So there's a list of companies, adopters, on the graduation issue, GitHub issue.
Alolita Sharma 00:50:14 Yeah.
Juraci Paixão Kröhling 00:50:15 That contains the list that we… we talked among ourselves.
Austin Parker 00:50:20 Yeah, but we also need, like, email addresses. Like, this shouldn't just be, like, oh, companies, this needs to be.
Juraci Paixão Kröhling 00:50:26 Jesus.
Austin Parker 00:50:27 Specific people that they can email.
Juraci Paixão Kröhling 00:50:30 What, what I, what I…
Dan Gomez Blanco 00:50:31 We didn't say…
Severin Neumann 00:50:32 We have the email addresses on… on the… I think even in the adopters list on the website, right? We can… Hold them from there, some of them, at least.
Dan Gomez Blanco 00:50:40 We, we didn't submit the form for all of these, right? I think that's the… I don't…
Austin Parker 00:50:47 know.
Dan Gomez Blanco 00:50:48 Yeah, so anyway, so let's go back to that list and… yeah.
Makes sense.
Austin Parker 00:50:52 I would like for us to be able to say, here is a list of name, email address, job title, company.
Whatever.
of 20 people, That you can reach out to.
Please go talk to them.
Alolita Sharma 00:51:07 Yep.
Austin Parker 00:51:08 That's… That is my ask, if we can get that within the next… 5 days or so. They're probably not gonna get contacted before KubeCon, I don't know.
But either way, like… What I ask for us is to be able to give them a list, right? A list that meets their criteria.
But yes, Apple, Adobe, JPMC, like, we know the people that are using this stuff. Yep.
Alolita Sharma 00:51:36 I can give names, addresses, emails.
Austin Parker 00:51:39 Yeah.
Anyway… That was my…
Alolita Sharma 00:51:48 And, Austin, I also added the… Comment on the.
Austin Parker 00:51:53 I, I, I saw that.
Alolita Sharma 00:51:54 just that.
Just update on that.
Austin Parker 00:51:57 Yeah, I think that is… that… that reflects the understanding we had based on the conversation, so that's correct.
Okay, cool. Hotel imp… or the… did we already talk about… The OTEP stuff, Ted.
Alolita Sharma 00:52:18 It's snow tapping.
Austin Parker 00:52:19 expand.
Ted Young 00:52:20 Yeah, no, I think we already talked about it. That was my place for us to sort that out.
Alolita Sharma 00:52:29 what's happening? Until unplugged.
Austin Parker 00:52:30 Sponsors?
Alolita Sharma 00:52:30 plugged.
Ted Young 00:52:32 Yeah, Hotel Unplugged, so that's coming along, we need to promote it more. This is just another call for sponsors, so I'll be going around and poking people again, but if your organization was thinking about sponsoring, but hadn't reached out yet.
Please do.
Austin Parker 00:52:51 Did we ever get in touch back with you all?
Ted Young 00:52:55 Don't… I'll double check.
Austin Parker 00:52:57 Double check, I've, I've…
Ted Young 00:52:59 Yep.
Austin Parker 00:53:00 I think we're… we're… I believe we're going to, but…
Ted Young 00:53:03 there were a number of people who were like, were totally cool, and then when I came back, were like, yeah, give me a couple weeks or something, and I can't remember who's who, but I will double check.
Austin Parker 00:53:12 Okay, yeah, it's still…
Ted Young 00:53:13 I'll just double-check and poke you guys again.
Austin Parker 00:53:16 Thanks.
Ted Young 00:53:17 an FYI.
Yeah. Likewise, if you also know of orgs that might be interested to, like, pass a prospectus to, that's great.
I won't be at KubeCon NA, by the way, sadly, so I'm gonna rely on all of y'all to be my hype peeps.
Austin Parker 00:53:37 We'll definitely mention it during the, I think we'll definitely promote it during the, like, maintainer's Track talk and stuff.
Dan Gomez Blanco 00:53:44 Yeah.
Ted Young 00:53:45 It'd be great to have something at the observatory if that thing stood up again.
Like.
Austin Parker 00:53:51 It is, like, we can probably have a slide or something, yeah.
Ted Young 00:53:54 Yeah, like, something we could print out and just tape to the wall.
Austin Parker 00:53:57 Put the QR code for people to… Yeah.
Ted Young 00:54:00 I can help with that.
Austin Parker 00:54:03 Garden.
Ted Young 00:54:04 Shining example, be like Ollie Garden.
Dan Gomez Blanco 00:54:07 I guess one of the comments I got, like, I was talking to someone about that already here at KCD UK, about the auto unplug thing, and they asked if it was a CFB, which there won't be, right, because it is a non-conference.
Austin Parker 00:54:20 No.
Dan Gomez Blanco 00:54:20 To which the response was, like, well, that might make it more difficult. As a maintainer, an hotel might make it more difficult to justify the travel.
Yes.
Ted Young 00:54:30 Is there some kind of special award we can give people that is essentially a participation trophy that we can give to maintainers to be like.
You've won this, like, special community come to… Come to Hotel Unplugged.
As an honored guest award.
That we can give to maintainers so that they can get travel budget approved.
And I'm half joking, but also kind of, like, half serious, because I do wonder if that would actually literally help some people.
If they got it.
Austin Parker 00:55:04 Probably.
Ted Young 00:55:04 Kind of official invite to be there.
Dan Gomez Blanco 00:55:06 I don't know if it is a CFP for… For stem, what is that?
Austin Parker 00:55:11 I don't think so.
Severin Neumann 00:55:12 So, other than, like… No, yeah, something like… but no, yeah, it's difficult, I think. It's different.
Yeah, I think maybe we need to give people something like, hey.
Austin Parker 00:55:22 Fasten is very free, so…
Severin Neumann 00:55:23 Whatever.
Ted Young 00:55:24 I'm totally… I mean, it wouldn't be, like… I don't know that speaker would be the term, but what term… if we wanted to give people, like, some kind of, like, invite, like… As, like, a domain expert.
Austin Parker 00:55:36 Program committee?
Ted Young 00:55:38 maintainer or something, like, basically being like, we want you here because an unconference only works if the maintainers show up. Yeah. Right?
Austin Parker 00:55:47 What about, like, program committee?
Ted Young 00:55:50 Everyone's on the program committee?
Austin Parker 00:55:53 Yeah.
Dan Gomez Blanco 00:55:53 container, or…
Severin Neumann 00:55:54 I mean, we have, like, this is run by the Open Telemetry Governance Committee, so let's turn it into… this event is run by GCTC, and maintainers, and we need at least, I don't know, how many people do we expect for this event? What did you say, Tad?
Ted Young 00:56:09 I mean, I think we have capacity for up to 200, but, like…
Severin Neumann 00:56:13 And, like, in an unconference, there's, like, 10 people in a room, so let's say we need at least 20 to 40 maintainers to help us.
Alolita Sharma 00:56:21 Yeah, just turning.
Severin Neumann 00:56:22 out, and so, like, hey… and then they get jobs, right, from, like, running those sessions to… Preparing something.
Austin Parker 00:56:30 I mean, I think my…
Severin Neumann 00:56:31 Whatever.
Austin Parker 00:56:31 Is we just send a… we just send a maintainer as an invite.
Alolita Sharma 00:56:36 Yeah.
Austin Parker 00:56:36 Like, we just literally have a thing where it's like, hey, is this… as a maintainer.
located in Europe or wherever, we formally are inviting you to be part of the program… the… the program committee for Hotel Unplugged. This is what that means.
If you accept… right? Like… A track organizer would be good, too, or track moderator.
Ted Young 00:56:59 Right? It's just you're speaking at the unconference meeting.
Austin Parker 00:57:04 Like, we're giving… we just… we say, here's your hat, if you would like it, and then they can go and say, hey, someone's offering me a hat, I just have to pay for the train ticket.
Ted Young 00:57:11 Hey, cats!
Wizard caps.
Austin Parker 00:57:14 It works.
Ted Young 00:57:16 We mail you.
Austin Parker 00:57:17 Why is Fostom on a weekend, anyway?
Alolita Sharma 00:57:19 It always is, because everybody locally comes in.
Ted Young 00:57:25 Seoul's airport is hell, don't fly through it, also.
Alolita Sharma 00:57:29 Take the train, take the train.
Severin Neumann 00:57:34 Yeah, but it's German trains.
Austin Parker 00:57:35 Literally.
Severin Neumann 00:57:36 I don't know.
Austin Parker 00:57:36 before.
Alolita Sharma 00:57:37 Trains are easier.
Ted Young 00:57:39 I mean, we… don't leave out of the Brussels airport, I'll tell you that much.
Insane experience, but anyway…
Severin Neumann 00:57:45 They fly to Amsterdam and then go by train, it sounds like.
Dan Gomez Blanco 00:57:49 I'm standing in Brussels.
Austin Parker 00:57:50 I need to pounce off a few minutes early, are we…
Dan Gomez Blanco 00:57:53 just one, there was one topic, I think we already sort of, like, talked about that, Lolita and I, in the thread in the chat. But, yeah, so hotel blueprints, that was something that, you know, one of the things, I guess, that was part of the recommendations from the TOC, but that we were also already talking about.
At least on the end user, sig as well. And, yeah, so… I would like to propose, you know, add a project proposal for this. I think the reason for a project proposal is that we can then try to get end users to, you know, to basically commit to help us with reference architectures and so on.
Alolita Sharma 00:58:26 Yes.
Dan Gomez Blanco 00:58:28 do we think this can be, sort of, like, sponsored by the end-user SIG, or do we think that we need a… I don't think we need a new Sega or anything like that for this, but, like… Happy to.
Alolita Sharma 00:58:38 I think it should be under the end user SIG, because then it gives momentum to the end user SIG also to kind of… Rally around a particular initiative.
Pablo Baeyens 00:58:49 Fantastic.
Alolita Sharma 00:58:50 Yeah.
Pablo Baeyens 00:58:51 Dan, I'm going to send you a link, because somebody from the Developer Experience League said they were working on blog posts that are related to AutoBlueprint, so maybe you want to talk with them.
Dan Gomez Blanco 00:59:01 Oh, okay. Right, yeah, just send them, send them my way, yeah, so I think, you know, my… general… I mean, even though I'll have to put this down in words, but the general idea with that, you know, that this would be a lot more successful if we get end users to help us build these blueprints, right? And then back it… backing it with reference architectures, and, you know, I think that would be… My preferred approach, rather than something that we as… You know.
Alolita Sharma 00:59:28 Yeah, and I think that there's lots of sub-projects within Hotel that reference architectures can be submitted to for. You know, I can definitely contribute a couple, that we have been implemented, You know, within Apple and others, get others also to kind of contribute.
Dan Gomez Blanco 00:59:49 It's good to get a list of a… at least a minimum… for a project, for not… this not to be, like, one of those endless ones, to just basically have a… a set of, like, like, environments, or, like.
Types of, like, deployments, like, you know.
Alolita Sharma 01:00:03 Yeah, deployment patterns are definitely very, you know, useful.
Dan Gomez Blanco 01:00:09 Yep.
Austin Parker 01:00:10 Yeah, I plus one to it being a project, I do have to run real quick, so…
Alolita Sharma 01:00:14 Bye, Austin. Back to you.
Good, good. So, Dan, let me know, and let's work on it.
Dan Gomez Blanco 01:00:20 I'll raise something next week. Yeah, I think this week I'm just still recovering from conferences, but yeah.
Alolita Sharma 01:00:26 Yeah, no worries.
Dan Gomez Blanco 01:00:30 And that's it. Morgan sends some election updates, alright?
Pablo Baeyens 01:00:34 Yeah, which is basically, we have the list of candidates on Helios, we updated the voting… the voters list based on the, form.
And, Morgan sent the first email to voters through Helios. I got mine, so I think.
Alolita Sharma 01:00:56 I got more.
Dan Gomez Blanco 01:00:57 and I know this was mentioned before, for the email to vote, can we… I don't know, that just… have a list of steps. I think the last time was, like, people get confused, because they hit in the vote in Helios, and then it says… You vote, but then you have to validate your vote, and then some people, I think, they don't get to the end, to the final step.
So it's, like, almost like a reminder when we tell people to vote, that, hey, you know, until you see this message, your vote doesn't count, or something like that.
Pablo Baeyens 01:01:24 I think we can do that on the third email, maybe, that we send, the very last one. I'm going to make a note on the draft issue on the project.
Severin Neumann 01:01:32 But are people supposed to vote already? Like, I mean…
Dan Gomez Blanco 01:01:36 Oh, no, no, no.
But… Okay.
Severin Neumann 01:01:37 It was like, when, when it's time for that? Okay, sorry, I misunderstood that.
Alolita Sharma 01:01:41 Yeah.
Severin Neumann 01:01:42 Yeah I need to jump as well. Talk to you. Bye-bye.
Pablo Baeyens 01:01:46 Alright.
Alolita Sharma 01:01:47 Bye, folks. Take care. Bye.
