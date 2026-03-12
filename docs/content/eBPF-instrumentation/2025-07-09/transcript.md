SIG: eBPF instrumentation
Date: 2025-07-09
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/vJ1F2s087cZ4zlZrL8oQp3Fg9Yp8AaskasNWBwMOL-4jFSlqkXaGSR_u2e389FjO.A2ABOU3UkmGMbohF
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:14 Hey!
**Mike Dame** 00:15 Hey, guys.
**Tyler Yahn** 00:16 How's it going.
**Mike Dame** 00:18 Good! How are you?
**Tyler Yahn** 00:20 Doing well, starting up the day.
How about yourself?
**Mike Dame** 00:27 Getting ready for lunch in the middle of the day.
**rafael** 00:31 No, I'm still trying to get by with coffee.
**Tyler Yahn** 00:38 Nice.
Yeah, coffee sounds pretty good at this point.
**rafael** 00:46 Do you guys, you do you grind your own coffee? Or do you by a free ground? Or, Yeah.
**Tyler Yahn** 00:54 Yeah, I'm all about grinding myself. Yeah.
What kind of grinder you have.
**rafael** 01:01 So I got, I'm gonna need some recommendations because I got one. A manual one from from my in laws that I tried today is in the morning just so much work to be spinning the thing. So you got any like auto, one electric one or.
**Tyler Yahn** 01:18 Yeah, yeah, I've had a few I mean, obviously, I've had some think of Barazza before, like an encore 2. And then trying to think like what is the name of the one it's like Ob, Ob, or something like that? That's not ob, that's 1.
Yes.
**rafael** 01:37 That would be too much for the morning.
**Tyler Yahn** 01:41 Yeah, there's another one. There's there's I definitely would recommend putting your money into that like, that's where you're going to get the most benefit, though.
**rafael** 01:50 Look it up.
**Mike Dame** 01:51 I think I have a little like I think it's a cuisinart, you know. Kind of just, I'd say, that's like entry level, probably, you know. But yeah, it's something that you don't wanna go totally cheap on. But as long as it's a brand that you recognize, or one of those, you know. Tyler, I think.
knows a little bit more about it than me, but mine has worked good for me.
**Tyler Yahn** 02:13 Yeah, I've got a fellow o 2. So it's a Gen. 2 of this fellow.
**rafael** 02:18 Alright. I'll look to look it up because I'm done with the manual. I'm done with the mental thing, I was convinced pretty much quickly.
**Tyler Yahn** 02:25 I did that for years. It was It was rough.
Okay, so I'm looking at the agenda. It looks like Nicola has a few items. I'm not seeing Nicola on the call.
**rafael** 02:55 He will join, export him. I can ping him in a minute.
**Tyler Yahn** 02:58 Okay, yeah, I guess.
In the meantime, if you haven't yet added your name to the Attendees list, we can update the list and start adding, There.
**Mike Dame** 03:28 I think Nicola already put contributing guidelines.
**rafael** 03:31 Oh, oh, yeah, see, I need more coffee.
**Tyler Yahn** 03:38 I'm checking slack just to see if he's around.
**rafael** 03:42 Helping him.
**Tyler Yahn** 03:51 Okay. Well.
**Marc** 03:51 Okay. Well.
**Tyler Yahn** 03:56 Probably get started here.
Oh, there's a lot, Mark. I think you're has got a lot of echo.
**rafael** 04:07 Nicola is gonna be 5 min late. By the way.
**Tyler Yahn** 04:10 Okay, then maybe we adjust the agenda accordingly.
Okay, well, then, if that's the case, let's, I'm going to move Nicolas items further down, and we can jump in here.
Awesome.
Okay? So cool. I wanted to start us off by just asking the question about vendoring. I've noticed that we use the like actual vendoring structure of the repository instead of using the Go MoD directive. And it's just more of a question for people that have like come from the bayless space like, why this is done. I'm just wondering if maybe there's an obvious answer.
**rafael** 04:56 I don't know. I mean neutral would know. I mean, like actually committing the vendor directory. Right? Is that what you mean or.
**Tyler Yahn** 05:05 Yeah, yeah, exactly. Yeah. This directory here.
**Mike Dame** 05:10 I wouldn't.
**rafael** 05:11 I mean. Do you know, Mark.
**Tyler Yahn** 05:14 What's that?
**rafael** 05:16 No, I'm asking Mark if he knows, because I mean when when I joined the person was already there, I have no idea why it was done like that.
**Marc** 05:24 Can can you repeat the question.
**Tyler Yahn** 05:26 So I'm wondering why this directory exists, and we don't just use the Go MoD tooling in this project so like you don't need to vendor anything in the in the project, and it should be able to build with.
You can use like.
**Marc** 05:41 I think it's because of the Vpf code. If I'm not mistaken that it cannot be vendor.
**Tyler Yahn** 05:51 There's there's Bpf code in here.
**Marc** 05:54 I don't know why we are using vendor. To begin with.
**rafael** 05:58 Yeah.
**Marc** 05:59 No idea.
**Tyler Yahn** 06:01 Okay.
**Marc** 06:02 Yeah.
**Mike Dame** 06:04 Just guessing on it, I mean, Nicola can probably answer, why, here, that makes a a good reason, or at least an explanation. I've also seen people use vendor, for, like, you know, offline builds.
that could be another reason. I don't know if that was the reason behind here. It's kind of that, you know. Justification is kind of not as popular anymore.
**Tyler Yahn** 06:25 Yeah, cause you can cache your go Mods as well. So okay, I'll maybe open an issue. Then I thought there might be just like a really obvious reason. But if not, it could help reduce the size of the repository. If we can cut that out, so I'll I'll maybe just open an issue to ask the question. And we can, we can go there. Okay, I I just figured there was a really obvious yeah answer. But I guess I guess maybe not. So. Okay.
Awesome. All right. Well, then, I wanted to talk about open Prs. But there's probably way better things to talk about on the agenda. I'd move this just because, Nicholas, I'm gonna move this back down.
but we can go and jump to Nimrod and Mark. What should we put in the SDK name instead of Bela Obi, or the full name.
I guess that's just the whole question right.
**Nimrod Avni** 07:15 I think it really depends, because I think we name a lot of things ob inside the project, especially stuff like the executable and a lot of the of the test of the project. But I don't know.
**Tyler Yahn** 07:31 So I think.
**Nimrod Avni** 07:32 Concrete answer I can change to whatever name we think is good.
**Tyler Yahn** 07:37 What? So by SDK, name, do you mean that we are talking about like scope, instrumentation, attributes.
**Nimrod Avni** 07:42 Yeah, the the resource attribute of telemetry. SDK, name. There's also the self like the self spans and self metrics are in the service name. So I'm guessing you want to change it to match.
Yeah, basically, you know, every time every attribute on like the span or metrics. That, says Beta. I'm guessing we maybe want to change to something general like Ob or open telemetry. Bpf. Instrumentation.
**Tyler Yahn** 08:12 Yeah, I so for, like the like, the resource attribute, I think that having open telemetry Ebpf instrumentation makes a lot of sense like spelling it out for span names. I like I I don't think it's a hard. I don't have a hard preference, but like I just like having Obi there instead, just because it'd be shorter and having shorter names, is a little bit easier to see on a lot of like tracing interfaces. But I, if we wanted to be consistent. I could also see the argument there as well.
**Nimrod Avni** 08:44 I mean, it's not gonna it's gonna be the name of like the not the span name, but like the the service name of.
**Tyler Yahn** 08:51 Oh!
**Nimrod Avni** 08:51 Or self-instrumented spans.
**Tyler Yahn** 08:54 Okay, I see it's just an attribute. It's not the end. The span name.
**Nimrod Avni** 08:57 Yeah. Like for for all the spends produced for other application, it's gonna be on the telemetry SDK language, the telemetry SDK name, and on the self span. It's going to be on like the resource attribute of service name.
So I'm guessing if if the preferences for, like the full, like the full name. I guess we can do it on both.
and they can change like more.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:19 Full name sounds good man, like I. Just so we're going to get trouble with that ob being some German.
I think, like a like department store, or what it is I don't know. Like home improvement store.
**Tyler Yahn** 09:34 Oh, really.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:36 Yeah, apparently it is like, Obi is like ob de if you go look at it like a home depot.
**Marc** 09:43 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:46 But I think we should change the binary to Ob, and prefix the the probes to be with Ob.
So to Bela, the Bela underscore things should go away.
**Nimrod Avni** 10:06 Okay, so I'll I'll change my Pr. And probably push soon.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:11 Nice.
**Tyler Yahn** 10:13 Cool.
Alright.
All right, thanks for that one. That sounds like a good idea.
Nicola. You wanted to talk about the contributing guidelines. I see you're here now. So yeah, I'll hand it over to you.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:25 Yeah, sorry I'm late. This is something that Raphael brought up internally, and he started working on it in my understanding is like, we want to make a contributing guideline. I'll be honest like for us. It was like really difficult to review some of the larger Prs. And it took forever. So we'd like to kind of set the sort of like mode of working to say, Okay, with smaller chunks. I really like what Nimron is doing. He sort of like smaller prs. And then he puts a commit. And in every commit there's like the changes making. And it's easier to follow. So we were like, okay, we like this. And we want to make this, maybe our differ where running things sort of going with that.
**Tyler Yahn** 11:13 What is everyone.
**rafael** 11:15 Sorry. Go ahead. Tyler.
**Tyler Yahn** 11:17 I was just gonna agree, go ahead.
**rafael** 11:18 I was just gonna say, yeah, if you guys having any other like ideas or inputs, otherwise, I was just gonna probably gonna fork, the contributing dot Md. From from one of the hotel products. I was looking on the Go one and as a as a starting point, and then tailor it, and then I was hoping I would probably raise a draft Pr.
and then everyone can comment, and we can adjust to see what works for everyone.
**Tyler Yahn** 11:48 Yeah, I don't know if you need a draft. Pr, I think you just regular pr, sounds fine.
this is, I think, pretty good starting point. There's
**rafael** 11:58 Yeah.
**Tyler Yahn** 12:00 Yeah, I mean, this is kind of helpful how to get things merged. This is where like, the policy comes in.
yeah. There's I'm trying to find it.
there's a 24 h essentially like one workday being open requirement that we have in this repository that we haven't adopted in other repositories. I don't know if we want to just kind of pointing that out. If you're going to copy it from here.
I think that's something that is not common. It's not. It started out as common in hotel. And it's not so common anymore.
but yeah, I think if that seems seems reasonable. We also have in here a bunch of like design choices.
This is essentially where we keep all of our policy decisions on like, Hey, we're gonna do tests this way. Documentation this way, there's a configuration was more the reason why this started. I don't know if I'd copy that is all I'm saying, Yeah, it might be, yeah, okay.
**rafael** 12:57 Yeah, I'll probably like I'll use this as a baseline. But I'll I'll I'll remove anything that that is like a gray area, for now we can edit later, or, you know, work it out and and add extra stuff like what we're discussing now with maybe make it specifically Prs, how how to get it approved quickly or like.
Yeah, it's easier if I open a Pr and then we can take it from there.
**Tyler Yahn** 13:25 Yeah, I mean, and I think this is a good place to put our style guide because we were talking about something like that for like C, or something like that. But I just think I meant, yeah, like you said, I wouldn't start there. Yeah.
**rafael** 13:35 No.
**Marc** 13:36 Raphael. Keep in mind that there's also all the Bpf part. So which is another language. So maybe it was to other section specifically about that testing, or yeah, or how the symbols or all this stuff.
**rafael** 13:57 Sounds good.
**Tyler Yahn** 14:01 Okay? All right.
That's the case. We go on into the agenda. So, Nicola, you want to give some updates on the Go auto usage.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 14:12 Yeah, I just wanted to kind of bring to this team meeting. We had our go auto sig yesterday. So it's on me as an action item, to create a a meta issue to spell it, a process of vendoring one single probe into obi from Goauto the plan is to start by 1st trying to vendor the C part of the Bpf program, and then later on, we progress to try to use the the user space side, and so on until we and going along that way to kind of iron out issues that we may encounter along this process.
Maybe discuss that maybe we start with dB. SQL. Instrumentation for go.
which is one of the simpler probes, and see how it goes from there. Start by making that multiprocess capable in go auto and slowly get to bandwidth. In a way that's pretty much the update. I haven't had time chance yet to make a Meta issue and start working on this, but I will by the end of the week.
**Tyler Yahn** 15:25 Yeah, okay? And maybe just for those that are interested. I was trying to find the other Doc, just the opensometry go auto instrumentation project has the kind of an overview that Nicola had. If you are interested before he gets the issue up. If you wanted to go, find the details and talk a little bit more about it, maybe in like slack or something like that. So yeah, if you haven't taken a look and you're interested, that's the place to to start for. Now, at least.
Okay. Awesome. Yeah. Go ahead.
**Mike Dame** 15:54 Yeah, I just wanted to ask, because I I did miss the Go auto meeting yesterday, but just to draw attention because it's related to this what we talked to last week. I created that issue that you're we're talking about for the this is the the steel thread. Poc, I'm assuming so I just wanted to ask if in that you know issue, did I?
You know, pretty accurately capture what you know people thought of as the approach. It kind of sounds like that's what we're going for here. Is there any other feedback? I saw Nicola? You left some comments on this. But is there anything that I was way off on, or does this kind of seem like the general direction? I I was kind of going, for.
you know, we're we're gonna have an issue for this Poc probe. And then, as I was writing it, I kind of ended up doing a lot of like defining the roles of the repos and stuff which I think are kind of beneficial to tie back to. But I wanna make sure that I wasn't you know, over defining or overstepping anything, and that this all, you know, cohesively makes sense.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:58 No, no, I mean we discussed it a little bit. I think the there's a I mean general consensus. I think all of us want to kind of reuse as much from the code, from the 2 repos that is right. Now, duplicate as you're aware, right? So there's the not just the manager, and and so on. But there's also this duplication around parsing symbols and finding offsets and all sorts of things right?
But the general sort of thing that I had as an opinion there is that there's all these additional kinds of Ebpf concepts that Ob is using at the moment, which there's no adequate support for that in go auto.
and if we did add it there in order for it to be solid and be able to be consumed in ob, we would need to add tests and add functionality in there which may not be ever used in the Go auto project. So I think we left it at that, that we probably need to figure out a way how we're gonna share this. Maybe it's another repo. And the question is, who's then owner of that repo? Who's the Maintainer? How do we ensure that project? Doesn't die? And with her away? And how do we make that happen?
We didn't reach a consensus in any way.
I still don't know what question.
**Mike Dame** 18:22 Yeah, I mean, that's so with this, I was just, you know, trying to keep in mind the part of the whole ob donation there was when I saw the pushback of with the clear definition, of what purpose does each one serve? I think that trying to unify that usage into you know, isolate that usage into the specific repos. The, you know, go auto as the framework and ob as the the tool kind of helps support that and drive the community to the right project. I I saw your comment about adding the extra repo. And I I you know. I'm not sure if that helps. You know that goal. But I do think that maybe there could be something that we end up, you know extending go auto, or, you know, go, auto becomes abstracted into supporting other languages and types of things that you know it, deprecating the the go auto into this new repo, or it evolves in that way. But I, you know, that's kind of getting a little maybe ahead of ourselves here. But yeah. Okay, so I just wanted to gut check that. This was, you know, at least in the right ballpark and draw, you know, bring other people's attention to it that I did, you know. Follow up on that action item and make this issue from last week?
So cool. I'll we can, Nicola, and maybe Tyler, if you guys are around after we could think of about the go auto stuff that I missed yesterday, too. So I'd like to catch up on that without using too much time here.
**Tyler Yahn** 19:45 Yeah, we we. I think we have a little bit. Maybe I can. One of the things that I did want to say that like we did talk about yesterday is that there's like still that what Nicola talked about was that that overlap of the responsibilities between these 2 like having a clear understanding of like what is missing from the the manager versus like the the tracer is, I think, going to be really helpful. And what vice versa as well? What's missing from the the tracer that has is in the manager is going to be helpful in understanding, like the unified like version of whatever is built and helping development that there. So yeah, I think that's why we kind of pointed out that like, this is kind of a good 1st step to understand from like the seaside, but then, like from here, this should help inform the decision of what what is missing between the 2, and then helping you to understand, like what we want to do in the next step. So we really saw this as an iterative approach like this would be the 1st step, and then discussing how that that manager, Evolution, is going to fall out. From this, I think, becomes a little bit clear, and the the probe definition, as well.
**Mike Dame** 20:50 Yeah, I agree. I think starting with the seaside is a good approach. The seaside is good person, because we've kind of that. That whole library side of it has kind of been an afterthought, I think, even last week in my issue I put it as like a bonus issue where it didn't seem like a you know the the main goal. But it is the core of what we're working on. And so I think, yeah. Start with the the sea level stuff. Get that ironed out. And then kind of what you were saying towards the end goal of the probe definition. See what the manager can support, too.
Or whatever you know the unified shared library is. And then whatever can't fall into that manager go level framework, and once we've built up from C to go become something that's necessary for the probe Api. So it's kind of like a like a deductive. Let's see what we can put in, and then we can have our probe Api. We know what needs to be stable and defined there, and I think that that'll help guide us there. So yeah, starting at the low level. I support it.
Good idea.
**Tyler Yahn** 21:54 Yeah. Cool. Awesome.
**Mike Dame** 21:56 Thank you.
**Tyler Yahn** 21:56 Yeah, all right. Yeah. And again, like that, what we just looked at should get transformed into an issue. So we can comment more asynchronously on that one.
All right, next up on the agenda mark. You want to talk about the Docs plan.
**Marc** 22:11 Yeah. I just wonder.
Oh, if yeah, just wondering. Like, if we we have to work on the documentation page anytime soon or like.
or still early for that. And if that's the case, how?
Yeah, I think.
**Nimrod Avni** 22:34 Been an issue regarding like adding documentation.
But I don't think I tagged it.
**Tyler Yahn** 22:41 Oh, okay.
**Nimrod Avni** 22:42 You just search docs, Doc, something not this one.
Yeah. This one.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:51 Yeah.
**Nimrod Avni** 22:53 Like. I looked at it from from a sorry, from an angle of like migrating docs from Bela, because it has, I think probably some of it is not like the most up to date, with, like the changes that we made, but it has, like very good documentation.
So maybe we can I know where we usually put like documentation? Is there like us, like central open telemetry place to add documentation? Or do we just add it to this repository?
**Tyler Yahn** 23:22 There is oops, cardio Oh, okay, that's right. Yeah.
This is the.
**Nimrod Avni** 23:29 What to say.
**Tyler Yahn** 23:30 Yeah, yeah. So we want to put it here.
And so it needs to show up underneath this, think, 0 code installers.
Yeah.
so yeah, right now, this is pointing here. So we probably want to put something for the Eppf Ob stuff here as well. This is where this would be.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:53 So it's not hosted out of the the actual repo it needs to be in a separate repo is that.
**Tyler Yahn** 24:01 it. No, I don't think so anymore. Like at 1 point we did toy with this idea and this kind of pulled from from the repo, but it was easier, for, like the Docs maintainers, to just put it all in into the the main repo That being said like, I think the the best place to to start is maybe there is. I think, a Docs, Sig. We could have somebody. If you want more info, go talk to them about the next steps. I know. Chalen. I think Severn still kind of active. But yeah, I mean the carter. Yeah. So, Philip. He's also like these people are very active in this space for the and they they would be very, I'm sure, willing to help you migrate things and help you format.
**Marc** 24:45 Yeah, and talk to Tiffany. She's also in Grafa. And yeah.
but yeah, I'm also like wondering, because, like.
I, I guess most of the times, like always gonna be used as a receiver in the in the yeah, in the country repo, I guess. So I guess that's where the documentation goes. But I don't know if we also plan to to have a standalone or like, have a different page for the standalone config. And yeah, that's why I.
**Tyler Yahn** 25:22 Yeah, that's.
**Marc** 25:22 Good good question.
**Tyler Yahn** 25:26 Yeah, I mean, so it's going to be. I mean, ideally, it's also a part of the the operator. For the Kubernetes operator. Right? So I think there's like a lot of goals here around.
how it's going to use. It's just a matter of question of like.
you know, how much do we want to document it being used in in each of these ways as we build out that feature, set and build out that functionality? And I I guess that's a good question, because I think if you have it. So there's like 5 different ways for a user to to use this. It's not really ideal, right? Like, it's more confusing than helpful. At that point. And so yeah, I think I think what I would say is that like? Since we already have, like really good documentation, is to copying something or building something off of this that is decent documentation in hotel, and we could evolve with it, you know, like, I think, that maybe as we go to the point where, like, it's going to be used as a collector receiver, or it's going to use in the operator like those documentation at this top level get updated to say, like, Hey, just like.
maybe you know, if you want to run it, standalone. Here you go. Here's like the other docs. But here's like the preferred way to go do this. So yeah, I think moving forward and just trying to to get this so that it's working as a standalone configuration might might make sense in the short term.
**Marc** 26:41 Yeah.
Well, in any case, I can just reach the dogs people and see what's the yeah. The best approach for.
**Tyler Yahn** 26:52 Yeah, I, yeah, there's definitely like page formatting things, especially in like structure in the, in the repo that are for me, a little confusing. But maybe they're not as confusing as I think.
So yeah, I think if you reach out to them they can help you out. And understanding like where to get started. Copying over data is usually something they ask for help on, because they're really good at writing pros and writing, you know, good docs. But like the details are kind of on us. So yeah, that's what they'd be looking for help from. So yeah.
**Marc** 27:26 Yeah. But in, for example, in this case.
serial code, instrumentation of what? Because it's for everything. So
**Tyler Yahn** 27:34 Yeah. Well, exactly. Yeah. That's a great. That's a great question. Like, who do you ask? I think if the docs team asking them how you want to structure this is is a great question for them to understand.
**Marc** 27:45 Yeah, so.
**Tyler Yahn** 27:46 Yeah, we'll do that. Yeah.
Cool.
So yeah, I think I think we have just just more questions for the docs team there. So yeah, if you have any other like, you said, you have contacts on the docs team. So if you have issues, let me know. And we can, we can set something up. But otherwise I think the I've never reached out to the Docs team and them not been extremely helpful. So yeah.
okay, cool Mark, do you also want to talk about the milestone 0 point 1.
**Marc** 28:21 Yeah, I just ask if it's still like.
that's what we want for this milestone. Or do we want to drop or add stuff? Or do we want a milestone at all? Or, Yeah.
**Tyler Yahn** 28:35 I definitely think we should have a milestone. It helps.
I think, helps communicate to the community the broader community that we're. We're, you know our progress and what we're doing. The content of the milestone, I think, is, is definitely a good question.
Yeah, I think we can jump into this a little bit. So right now we've got the config. Codify the config with hotel standards. So this has to do, I think, with yeah, this all has to come back to our migration policy, or I'm sorry our donation proposal was including a lot of these things. I don't think they have to be in the exact initial release. They just need to be included in in our.
**Marc** 29:16 You know our progress in our plan.
**Tyler Yahn** 29:19 So let's see what we need.
So yeah, regular expressions with blobs. Looks like that's got a checkmark. Smart environment, variable substitution. Looks like that's got a checkmark. Rename the name value map pairs by objects also checkmark. So the create Json schema for the refactoring configuration looks like it's still in progress.
**Marc** 29:42 Yeah, that's yeah. Actually, there are these 2 items. And I couldn't find any project. I think, I added a comment in the previous issue pinging you. But I I didn't find I didn't find any projects to. So maybe, since you are the owner of this issue, maybe you can point out what we have to do here, because I couldn't.
I was not very yeah.
**Tyler Yahn** 30:09 Yeah. It's just depending on.
**Marc** 30:17 Door was closed.
Yeah.
**Tyler Yahn** 30:23 Hmm.
Oh, it's a pr, okay, so my idea, or or my understanding of this is that create Json schema?
Okay? So so.
yeah, this could probably get splintered off. I don't think this needs to be in our initial release, because the ultimate goal is that we want to have this project to be able to be configured using the open telemetry declarative configuration, which is something that they're trying to stabilize right now.
And what that means is, it needs to be a part of this instrumentation section of this this project that it's going to be more in the Java size. Yeah, that's a good question. Actually, I imagine that the maybe it's here. So that this this group has actually been working a lot on this to try to integrate, and making sure that, like they are a part of this interpretation section I haven't the slightest where to look in this repository, though, I think, yeah, this, how to map declarative. Yeah, this is probably a good starting point.
Yeah. Okay.
so I I don't know exactly the state of how they're doing it. So I'd have to go and maybe look, look a little further into this. But this is essentially what they're trying to do like. They also have a bunch of these. They use agent properties right? And to map that into some sort of like way that they can allow it, so that when it's passed through declarative configuration it should be able to configure the auto instrumentation.
I'd have to look more into the details of how they're doing it here. But essentially like my understanding of how this is gonna work is you need to. You need to provide some sort of like schema. To say like this is how like our configuration schema should work so we can validate it. And you can pass this into some sort of validator. So things like the go project has something that is is built. It's not done yet. It needs to add this functionality. But this hotel Conf.
it's going to have an Api here where it's going to be able to patch in all of these different values.
Yeah, so essentially like what it's gonna do is it's gonna take in the Json schema, and it's gonna and it's gonna start using it. So if you can't tell by my kind of you know, beating around the bush on this one like, there's not a really great plan yet, and I think if there needs to be some tooling that's going to be built into how this is going to be used. So I don't have. I don't have a great answer for, like the the whole picture of what needs to get done it. Yeah, it probably is going to need to.
you know, coordinate with this project into understanding how this is going to get integrated, which is important, and it's actively being worked on as well. Well.
it's a it's a priority for some people. It's just I don't. How active. I don't. I don't know if I can say that. But So yeah, I think that just needs to get worked on. I think that you could probably split this off into its own issue, though, and we can take this out of this milestone is what I would say.
**Marc** 33:39 Yeah, yeah, okay, okay, okay, let's do that.
And if you would, I will convert the other one in a I mean, maybe it's the same, the same issue. But I'm not sure the this, that the last one, and maybe.
**Tyler Yahn** 33:53 Oh, yeah.
**Marc** 33:54 Yeah.
**Tyler Yahn** 33:56 Yeah, yeah, exactly.
I think that's a good idea. I would convert this as well to another issue.
And then we can just we can pull that out of this issue. This should be done. We can close it, and we can. We can say that that's part of the the milestones closed, and then.
**Marc** 34:08 Yeah, and then, and then, if you can put a bit of information in each one, so.
**Tyler Yahn** 34:13 Yeah, that sounds like a good idea. I I can do that. I'll be looking out for it. We should also of a v 2 milestone.
And so, yeah, whatever issues, let's see.
I think this is a good one. So we can move this to this milestone. And we could just keep track, because this is something we want to keep working on.
Here, why don't we just do this? I can do this as easily as you edits.
Okay, that works.
So did I close that other issue. I don't want to lose it.
Okay, I'll I can add some more issues here, or some more details here, after.
**Marc** 35:13 Add a meeting, cool, cool, cool.
**Tyler Yahn** 35:16 Okay?
And then here, actually, I think that we could close this at this point.
**Marc** 35:25 Yeah.
**Tyler Yahn** 35:50 Okay? And then what else do we have in here?
I'm sure there's documentation on how to exclude services looks like this is blocked. This also is not tagged with documentation.
**Marc** 36:03 Yeah, I mean, we don't have documentation. So I don't know if you wanna have milestone like this in this milestone. We also need to put the having documentation in the milestone, so I don't know if that's part of the milestone.
**Tyler Yahn** 36:18 Yeah, that's a good point. Let's let's do that. Let's add the documentation issue that we have.
**Marc** 36:33 Oh, nice!
**Tyler Yahn** 36:35 Cool, and then let me.
wow.
okay, let's update.
Okay? And then the other one is update telemetry to conform with hotel semantic inventions. This is a good question. I don't know the state of this one, I think. Yeah. Mario might take long for only applicable level metrics or application.
**Marc** 37:21 Worship.
**Tyler Yahn** 37:22 Form it.
Yeah, this is.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 37:24 Yeah, this I can, I think, for application. We're good. I think the the issue is that the network metrics are now have no spec the network flows so.
**Tyler Yahn** 37:38 Oh, then like Huh!
So like.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 37:47 Yeah, so,
**Tyler Yahn** 37:49 Yeah, I'm sorry. I'm like, network.
Hmm, yeah, okay, I thought, there, what used to be like a network specific section. But.
**Marc** 38:00 Oops!
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 38:01 Yeah, no, I think he's working with us.
Spec definition. I think he started on going on those Sig meetings, I believe, to create some sort of like default spec semantic convention about network flows, and then we'll go from there. The application ones should be should be, according to the latest auto specs.
**Tyler Yahn** 38:27 Okay, only application conform to it. Network metrics will be.
yeah, okay. I mean, so this is what you're saying.
Mark.
**Marc** 38:34 A lot of feedback.
Sorry.
**Tyler Yahn** 38:37 I don't know if. Yeah, thanks. So I think what you're saying is that like these don't exist. So only the semantic conventions that exist we comply with is what you're saying.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 38:47 Yeah, yeah. And they'll be undocumented until we or mark this unstable until we actually.
**Tyler Yahn** 38:54 Why, yeah, I think that's that satisfies the conditions of this.
This is asking for hotel semantic conventions. So if the hotel semantic conventions don't exist, then.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 39:02 That's right. Yeah, yeah.
**Tyler Yahn** 39:03 We're we're good.
Okay, yeah.
okay, alright. So I guess if that's the case, then going back here, Mark, it looks like we just have Doc Tasks left at that point right.
**Marc** 40:02 Yeah, sounds good. I will do that.
**Tyler Yahn** 40:05 Okay, are there any other issues that we're missing that we want to include in this 1st release?
I mean, there's a ton of stuff to do. But just like before, like these are things we'd need. I think, before we want to make this release happen.
Yeah, sounds good to me, me, too.
**Marc** 40:31 I don't know if you wanna remove all the references to Bela as part of 0 1.
**Tyler Yahn** 40:39 That would be, I think all public references would be, I think, good. That's a good question. I thought we did that, though. Is that not complete?
**Marc** 40:48 I mean, there's gonna be a few more, I guess.
**Tyler Yahn** 40:56 Yeah, okay, yeah. So definitely, not that. Okay, yeah, I definitely think this should get included. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 41:03 Probably renaming the the some of the you probes and stuff like, I'll explain. Like all of our you probes are prefixed with Bela underscore. So then we can actually, use something like Ebpf top from Netflix to tell you in a environment where you're running, which pros are most expensive. This is how we track performance regressions internally related to releases. So let's say, we've added a new program. This program is very expensive. We kind of look into or to optimize. And then you can kinda you can get these actual metrics about the Evpf program running to see what's low.
But unless they're prefixed. Then they get mixed up with other. Maybe Bpf tools installed. Everybody is installing probes, naming them. Maybe. Similarly, it's kind of hard to tell.
So those that's probably the last bastion of Bewa, naming, renaming.
**Tyler Yahn** 42:06 Okay, so we need to change the probe prefix from Bela to ob.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 42:12 Will be, yeah.
**Tyler Yahn** 42:13 Okay.
**Marc** 42:19 Maybe you can create like, because maybe there are more than this. So maybe you can create like an issue.
**Tyler Yahn** 42:25 Audit, issue.
**Marc** 42:26 Yeah. It's some. Yeah.
**Tyler Yahn** 42:28 Yeah, okay.
okay, yeah. Great suggestions. Okay, any other things we want to include here.
I think that's it. Right?
**Marc** 43:21 Yeah.
**Tyler Yahn** 43:23 Okay. Awesome.
All right, if that's the case.
we have 15 min left, so we can jump through and maybe just talk about open. Prs, I just want to make sure we're making people are unblocked or have some momentum going here. So we yeah, go ahead.
**rafael** 43:44 So sorry, real quickly do we wanna take the opportunity to ask Nicola if he knows about the vendor directory.
**Tyler Yahn** 43:51 I was gonna ask that at the end. But yeah, we could ask now.
**rafael** 43:54 Okay, sorry you did that at the end.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 43:57 Sorry. No, I did. I miss that. I sorry I had to. I had a.
**Tyler Yahn** 44:00 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:01 Like, yeah.
**Tyler Yahn** 44:02 It was. It was I just had like a really quick question that, like I, I was wondering why we have a vendor directory instead of just using the go module tooling here.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:09 Yeah, we can kill it. I don't. I don't feel strongly about that. It was like.
And when Mario and I started this project long ago.
I don't know. Mario thought that. You know things happened in other communities like Nodejs. Packages disappear so vendor ensures that you have a copy of it, and and so on. And so that's why we kind of went with that approach. But it doesn't have to be here.
It's not like for a like functional reason, like like, there's things. Okay.
Now, though. Hi, that's a good question it might be required. But that's a bela thing, not ob thing. So an Ob can go away in Bela. Well, it may actually happen that we need it.
When we vendor the 1st C program from go auto. I'll explain why, because the only way we can make the tooling work.
For without shipping the binaries for the go program for the Ebpf programs is that we have a sub module.
The sub module is where we compile the binaries, and then we copy them into the vendor Directory.
and then they're rendered from there.
but that doesn't have to be checked in. That could be just a build step process, and the Vendor Directory can be in. Get ignore, but we may need it. It's just that it's going to be get ignored and not in the repo.
**Tyler Yahn** 45:45 Oh, I see. Yeah, that makes sense. Yeah.
it makes sense. As long as the go MoD tooling can work with a vendor directory as well.
So if you can do partials which I'm not sure you can.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 45:58 No.
**Tyler Yahn** 45:59 I think I might be a 1 or another, but.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 46:02 I think that's fine. Yeah, I've seen that approach if they just use the vendor directory, but it just don't commit it, because I think at the end of the day just disks disk space.
**Tyler Yahn** 46:12 Yeah, yeah, no. I agree, like we could definitely do it that way.
It's just whether the vendor Directory has to contain all of it, or it can be used to go cache like the go module system like, it's caching. And like, yeah, it's packaging. But anyways, I can take a look I just didn't know, like I was more asking you the question. I don't necessarily.
I'm happy to look into like removing it, but I just wanted to know if people knew like, Hey, don't do that. That's a really bad idea. But this sounds like it may be maybe possible. So we can. We can take a look.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 46:41 No, and I've seen other projects use the Vendor Directory for similar reasons, but then they just don't commit it, and I and I never liked committing it. To be honest, because it just makes certain Prs is impossible to render in good Github ui right, because it's like all the vendor files you've changed. And yeah.
**Tyler Yahn** 46:59 Yeah, that was kind of my question is where it's coming from. Because, like, I, I can't understand some of these. Pr, so yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 47:05 Yeah.
**Tyler Yahn** 47:07 Okay, well, I'll take a look at that. Then it'll be something we can.
Yeah, maybe some processing there.
Okay, so jump into the open Prs add a process minimum age to filter out the short lived processes if needed, like. This is something we talked about last week. If I remember correctly.
it was potentially not.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 47:25 And then.
**Tyler Yahn** 47:26 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 47:27 Yeah, I think it's it's something I need to look into. I I think the author asked for help.
In a sense, I didn't understand why the tests were failing. But yeah, which I totally get difficult to understand without any sort of anyone helping you. So I I think what I'm gonna I it's on my list. I I was on. This happened when I was on vacation. I haven't picked it up after.
**Tyler Yahn** 47:55 No worries.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 47:55 I think the change is okay. I I think the gist of the change is that what they proposed is, there's a lot of noise happen when we discover processes, but they're short lived.
So they wanted to add this sort of like a delay. Well did it live for at least 5 seconds, and then avoids a lot of churn on us like finding a process, pushing it through the pipeline just to find out a couple of seconds later. Oh, it's dead, so there's nothing to instrument.
So they wanted to kind of find a process, make sure, at least, is there for a little 5 seconds, and then then only instrumented.
Oh, helps with sort of like, yeah, load generators. That kind of stuff.
**Tyler Yahn** 48:41 I thought you were saying that this wasn't possible, though, because how do we determine if it's there or not for that period of time. It's not something that, like we hold state on.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 48:51 Yeah. So I think what? So there, there was one issue that we pointed out in the in the review, which I believe he resolved. So the detection that happens on an open port, you can say I want to instrument applications that listen on port 80 80, and then for that the the kind of parsing of the Proc. Files to find what open ports certain processes listen to is very labor, intensive or compute, intensive, I should say and so we don't do that.
Generally we rely on a watcher program. That's an Epf program that notices a new we do that on. Once ob starts we kind of sniff out all running ports or all listen ports on but then we rely on a watcher program that watches for bind, and then it tells us that a new port was bound. Once we do notice the new port being bound, then we go in and parse and find out which process is listening on that.
So that is not possible to do with this approach. But that's already kind of out of the way, I think, he added code to kind of composite for that case. But for all the other cases, we all we we periodically scan anyways, so we scan every like 100 ms for new executables.
**Tyler Yahn** 50:11 Oh, okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:12 So. So when we find a new executable, we check to see what? How long has it been up for, like the typical kind of. If you think uptime on your system, we say uptime for the executable, and we only consider it as a candidate. If it's been up for more than 5 seconds.
**Tyler Yahn** 50:32 Yeah, that seems to make sense. Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:33 Yeah, I think it's a good addition. It will eliminate a lot of noise and unnecessary work. But I think there's probably some subtle bug. There we need.
**Tyler Yahn** 50:44 There always is. Right? Yeah. Yeah.
Oh, okay, all right. Well, then, we'll just yeah. Sounds like it's it's just waiting on more feedback. So that sounds great.
Okay, this update to Kubernetes package to V, 0 3 3.2. Mario had wanted to like double check on this. It's been a little while. I don't know if he just forgot about this at this point.
it does look like I think the tests were failing.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 51:10 And.
**Tyler Yahn** 51:11 I think that might be flaky because it has passed him in the past. If I'm not mistaken.
No, okay. It looks like there's some.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 51:23 Yeah, this looks like a breakage. And some data is not right.
**Tyler Yahn** 51:27 Yeah.
Oh, that's interesting.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 51:30 Yeah.
So maybe it's a. It's a code. Changes required, probably to make this work.
**Tyler Yahn** 51:36 Yeah, okay, alright. So maybe I'll I'll take a look at this. Actually, I can. I can dive into this one.
Okay, my sequel support, prepare statements, refactor event handler.
So this is definitely something for the Mysql ecosystem.
Looks like there's some reviews on this already.
**Mattia Meleleo** 51:56 Yeah, I found other issues, thanks to this test. And I'm working on fixing these other issues first.st But there is nothing blocking this one I should just polish. And yeah, once I fix the this, other issues should be ready.
**Tyler Yahn** 52:13 Okay, cool, alright good to know.
Looks like there's some draft Prs for Gh tasks to generate precompiled integration test images. I'm guessing this is something that's not ready to work. Look at yet, but something from Mario. And then, Raphael, you also have introduced granular service selector export modes. So yeah, we can just wait for wait for those to become non-draft, I guess, unless you guys are, I guess Mario's not on here unless Rafael, you wanted to talk a little bit about something.
**rafael** 52:44 No, I think it's a it's all good. This is just a Pr that I mean, it's in the description. Basically, we we have the the discovery section, where it can specify the attributes you want to use to discover your service in kubernetes, and usually if you say like, I don't know. Kubernetes, namespace, default it will instrument everything there, and if we have, let's say, traces enabled and it will add traces each generate traces for every service. The way we enable traces at the moment is just by specifying hotel exporting point for traces. Either the common one or a specific one for traces that then automatically enable traces. What we're trying to achieve here is to have a little bit more granularity. So we say I want instrument all these services. But this for this particular service inside this namespace, for instance. I don't want traces, or I don't want metrics, or I don't want anything, so it just gives you like a way of from the baseline of instrumenting everything to add more instrumentation or less instrumentation per service, or to be more specific per sections attribute. So then, the service section instrument section that's pretty much what it tries to do.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 54:07 Talked about this.
**Tyler Yahn** 54:08 Wasn't.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 54:09 Meetings. Back yeah.
**Tyler Yahn** 54:10 Yeah, sounds familiar. So, yeah, exactly.
Okay, cool. Well, yeah, we'll keep an eye. And yeah, look forward to reviewing when it's ready.
Okay, last one is this one we talked about, which was a rename at the top of the meeting. So yeah, this looks like I'm guessing. Never mind. You talked about needing to update, but then, otherwise, just reviews right?
**Nimrod Avni** 54:31 I have already updated.
**Tyler Yahn** 54:36 So yeah, it's quick.
Yeah, that's good.
**Nimrod Avni** 54:40 Control.
**Marc** 54:40 It's okay.
Name, I think. Name Rod. I think you have to do close issue.
**Tyler Yahn** 54:47 Because otherwise it's not. Gonna yeah, we can.
Oh, God.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 54:51 Closes or something. Yeah, yeah.
**Nimrod Avni** 54:55 Okay.
**Tyler Yahn** 54:57 Actually, let's do this.
**Marc** 55:00 Yeah, yeah, yeah, thank you. Okay.
**Tyler Yahn** 55:04 Yeah, no worries. Okay, cool. So yeah, just reviews, this looks like it's ready to go.
okay, that is the end of the agenda. I will stop sharing my screen here. Any other things people want to talk about.
It got all weird before we close it out.
Well, if not, we can end it here. Thank you. Everyone for joining. Appreciate your time, appreciate all the hard work that's going on. So yeah, a lot going on a lot to look forward to. So yeah, we'll keep it going.
Yeah, everyone talk to you later. Bye.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 55:41 Bye.
