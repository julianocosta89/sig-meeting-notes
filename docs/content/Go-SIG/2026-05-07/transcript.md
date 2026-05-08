SIG: Go SIG
Date: 2026-05-07
Duration: 37 minutes
Zoom Recording URL: https://zoom.us/rec/share/IYF59pj67l9qBkjDBTrg16cil4VeLWAHwYuvbXwipv1YqTGm3fgbSYHKlB43ZCVu.D_Wl0jsyhKGvmzvm
============================================================

## Zoom Recording Transcript

**Pellared** 02:41 Hello?
**Israel Blancas** 02:44 Alright.
**Tyler** 02:46 Hey.
Robert, have you checked the Slack?
Group on who's joining today?
**Pellared** 03:04 There's no message.
**Tyler** 03:06 Okay.
**Pellared** 03:09 No, nothing, no information.
**Tyler** 03:26 Okay.
Oh, I think I see Sam.
**Sam Xie** 03:35 Oh…
**Tyler** 03:36 Hey.
**Pellared** 03:52 Israel, do you have any topics that you want to discuss?
**Tyler** 04:01 Robert, who was that directed to?
**Pellared** 04:03 I'm asking Israel bankers.
**Tyler** 04:06 Oh, okay.
**Pellared** 04:07 He's muted. Maybe AFK.
**Tyler** 04:17 Yeah, maybe, I'm just gonna add a link to the next, release milestone, and then we can probably jump in here in just a second. I might want to move David's… thing down if, nope, David is here. Okay, Yeah, cool. Well, welcome, everyone. We can just… just a second, get started here. If you haven't yet, go ahead and add your name to the attendees list.
If you have agenda items you want to talk about, please go ahead and add them there as well.
And then, yeah, I'll start sharing my screen.
I don't know… Yes. Okay, cool.
One of these years, it'll actually be the year of the Linux desktop, but… Okay.
Awesome. So, start us off.
Welcome, everyone. David, you want to talk about collector resource detectors?
**David Ashpole** 05:28 Yeah, so, this came up that… It's confusing, That the collector's self-observability metrics Have, access to far fewer resource detectors than the collector itself does.
So there's a desire for… the Go SDK… To have, basically.
Just as much resource detection as the resource detection processor does.
And so the idea is, well, why not contribute the resource detectors that are currently in the collector?
into new modules in GoContrib.
Keep, by and large, the same… owners. I'm like… I own the resource detector detection processor in Contrib, in the collector.
But I certainly am not an expert in, like, any of the… you know, WS, or whatever.
platforms, that are supported there. So, there's some other folks who are owners of those various ones. And the idea is, like.
If we contribute them to GoContrib, then the collector can just become a wrapper around the ones in GoContrib.
And then it, you know, its self-observability stuff can be consistent. So, that's the intent. I'm planning to sponsor those, unless there are objections. But if people have concerns about just It's gonna be, like, 20 PRs, probably.
And a lot of new modules and stuff, but overall, it seems like a good thing.
Assuming that these detectors make sense, which I think they Hopefully do.
**Tyler** 07:16 Yeah, that's… that's great. I think… Putting an empty trip, having an order, yeah.
Sorry, go ahead.
**Israel Blancas** 07:22 Oh, sorry, sorry, just because this thing is lagging a bit, sorry. It's not just, like, you know, contributing those ones that are not in country.
But also, you know, maybe there are features that one has and the other not, right? So we can align, and also things that are maybe not part of the semantic conventions, right? And we can, like, be consistent and things like that, because right now, very likely there is some kind of drift between both kind of components, right? For even the ones that are already there.
Oh, sorry, go ahead.
**David Ashpole** 07:54 I see, so they're actually implemented differently as well. So, we may have to make some decisions about Which one to align on.
But I think, hopefully, there's a right answer there.
**Tyler** 08:07 How are they implemented differently?
**David Ashpole** 08:09 Maybe just they collect different attributes in different contexts?
I don't know of any… I don't know the specific examples that we… That drove this.
**Israel Blancas** 08:22 I was checking some days ago, because I had the same idea that… I mean, the thing is that this conversation came because, And pull requests that you've created in the collector.
And… I remember that I started checking, right, because I had the same idea about contributing, I mean, like, trying to talk cry about contributing the thing.
And yeah, I remember there were a couple of things that were looking different, like checking for different resources and things like that, especially in the AWS ones. I don't remember exactly the thing, but in that case, even if you want, I can… I can't create tickets even for that, right, with the small analysis that they did, because they were, like, exposing different things, and also getting the information from different places in some cases.
**David Ashpole** 09:14 Yeah, sure. I think the AWS ones… in GoContrib haven't been looked at very much in the last few years. I think they were added maybe 3 years ago, and back when AWS was really active, and then… Haven't seen very much activity, from what I can recall, but… Yeah, it's good… I think it's good at least to open issues if there are discrepancies between them, and… Yeah, whoever's interested can dig in and… We'll try and get those fixed.
Cool.
That's all for the topic, unless people have concerns or anything.
**Tyler** 09:55 No, it's great. I'm excited. The more support, I think, the better here. These are all… seem relevant.
The only thing is that, I'd say this one needs an owner. I'm happy to have more of a maintainer role in all these, but, like, if it's a company one, I'd like to make sure that we have some sort of representative of that company there.
**David Ashpole** 10:16 Don't know if there's a representative of the company.
Oh.
**Tyler** 10:19 Okay.
**David Ashpole** 10:20 upstream, the upstream collector.
I… I can try and figure out who added it originally. I don't… I think a lot of these were added by folks from Elastic.
I don't have context, but my suspicion was that they already supported these resource detectors in some other form, in some other project or something, and were looking for parity.
But there will be an owner. I'm not sure if it'll be an owner from Dynatrace.
**Tyler** 10:50 Yeah, that's not, I guess, not super critical. Like, our AWS ones are owned by, Alex, can't remember his last name right now, but, like, I mean, I don't think Alex works at, AWS, or he didn't. He worked at Capital One or something like that, so… Yeah, that's not really a problem.
But, yeah, sounds good. Cool.
Cool.
Next up on the release, so… there's two PRs still open here, AdMax… Baggage length limitations. This one is long-standing, this is kind of the blocker on this one.
Sam, where are we at on this?
**Sam Xie** 11:29 I think, I have only 2 or 3 comments need to resolve.
Then after that, it's okay.
**Tyler** 11:39 Okay.
Yeah, it looks like there's, I don't know if this is a duplicate of, some of the co-pilot stuff, but okay, this just needs more review. Or, I'm sorry, iteration.
And update, yep.
And then… Flare Clash, this is just something that I think… This looks ready to merge.
Maybe not. This doesn't look resolved.
**Pellared** 12:11 I think this can be resolved.
**Tyler** 12:14 Okay.
**Pellared** 12:38 I think there were some copilot comments, which were invalid.
After we both…
**Tyler** 12:51 Hmm, yeah.
**Pellared** 12:53 Yes, we can resolve this, we discussed it at least one time.
**Tyler** 12:57 Did this get… fixed?
**Pellared** 13:00 I have no idea, I have not went back to this PR.
**Tyler** 13:05 Yeah, me neither.
**Pellared** 13:06 But I see that it was force-pushed.
So, it is possible that…
**Tyler** 13:22 Okay.
Yeah, okay, it does look… Dated.
What was that file?
Yeah, I don't see it…
**Pellared** 13:55 Okay.
**Tyler** 14:05 I don't see any… That's weird.
**Pellared** 14:14 Clear.
**Tyler** 14:15 not.
This should have regenerated those metrics.
**Pellared** 14:24 Posh.
**Tyler** 14:26 Hmm, I think this might have been solved by not including generated code, which isn't the right solution. Okay, I don't think this is ready, then. I think this still needs some more investigation into this. Okay, so still open PRs on this one, and we can check contribib as well. I don't think there's anything blocking in that one, though.
Yeah, this one has been open for a while. I don't know…
**Pellared** 14:54 Do you think it makes sense to ask, just to separate the PRs, and to have the one for generated as a separate PR?
And…
**Tyler** 15:04 I haven't looked at it. You and David have. Damien and FLC have approved it, so it's kind of up to you if you would like.
**Pellared** 15:11 I mean, I mean, not this one, I mean the previous one.
Guardian version, everything, SamCon.
Just to propose to split up into two PRs.
Because I remember the…
**Tyler** 15:22 No, I'd rather…
**Pellared** 15:23 the reservation.
**Tyler** 15:24 I'd rather be in the same… like, we don't review generated code normally.
No, I think putting it all into one PR makes sense.
Like, definitely shouldn't be updating a template and then not generating the code and committing that in.
**Pellared** 15:41 Yes.
**Tyler** 15:43 Yeah.
Like, if they wanna… Let's remove this generation stuff as well, and then do that in a separate one.
That's fine, but, I mean, I think it should include the generated code here, though.
**Pellared** 15:56 Okay.
**Tyler** 16:00 But yeah, I mean, if you have strong opinions on it, like.
Please go ahead and comment, yeah.
Okay, cool. Alright, so still waiting on, PR work for the next release, so yeah, maybe it's a next week's thing on this one.
**Pellared** 16:18 dot com.
**Tyler** 16:19 Last thing on the agenda, I just wanted to mention that, next week, I… Might be here, I might not, but then the two weeks after, I will be gone for just a vacation. I'm trying to get ready for that vacation beforehand, so I might not be able to make it next Thursday, but we'll see.
But yeah, I'm out for 2 weeks in May. So, yeah, just, nothing… Too dramatic, other than just taking time off.
**David Ashpole** 16:43 Can you share what you're… are you, like, gonna go do something fun, or…
**Tyler** 16:48 I think so. I'm going to Colorado, and I'm gonna go, do some kitchen renovations for, for a house, which I love, that kind of stuff, so I'm pretty excited about it. And then, you know, hiking and fishing in Colorado sounds great in May, so, yeah.
But yeah, like a true vacation. Yeah.
Yeah, so, pretty, pretty excited about that.
But yeah, other than that, I guess, For those two weeks, do we have a volunteer for running these meetings?
**David Ashpole** 17:23 I'm more than happy to run if nobody else wants to.
**Tyler** 17:27 Perfect. I got thumbs up.
From, Robert, I think you're on, David.
**David Ashpole** 17:32 Hmm.
**Tyler** 17:33 Yeah.
**Sam Xie** 17:34 I'm also out next week.
**Tyler** 17:36 Out next week? Okay, cool. Yeah.
Yeah, but I should… I mean, I'm not out of cell phone range, so if you really need me, I'll be around. Probably not checking notifications that often, though.
**David Ashpole** 17:47 You review report requests on your cell phone, right?
**Tyler** 17:51 God, unfortunately, the answer is yes to that, That's usually what gets me into trouble, is then I also respond horribly to some things, and, like, I read them afterwards, like, what was I even trying to say here? Like, but yeah, yes, I do.
So send me the 4,000 line PR while I'm reading it on my phone, please. That'll help.
Maybe also point out that, because I'm taking off time, I'm also thinking about KubeCon proposals. I think it's the end of May as well, right, Robert? Correct me if I'm wrong, but, like, the CFP for the main conference, and then I think the… Observability Day is a little bit after that, but, like, they're coming up, so yeah, for folks that are planning on submitting things, which you should, there's a lot of great… Great work at OTEL. So yeah, I think that if you wanted to come up with a cool idea, worth spending some time thinking about it and getting a talk together.
or talking to other folks around, if you want to do, like, co-presentations and things, I know that a lot of people… I think there's a better acceptance rate for Like, multiple presenters, especially from different companies?
**David Ashpole** 19:02 I would definitely recommend it, yeah.
**Tyler** 19:04 Yeah, so… Yeah, worth, worth, start pinging people and getting drafts together.
Well, cool.
Israel, I see you also added something onto the agenda.
**Israel Blancas** 19:26 Yeah, sorry, I just added it, so if you can take a look, it's… if you can… I mean, I got even approvals for that PR, sorry for pushing for it, but, it's looking a little bit of the working, so then I'm working on the collector.
Yeah, since the release very likely is gonna happen next week, if we can make it happen, I will be more unhappy, and my employer especially. Yeah.
**Tyler** 19:51 It's merged, so yeah, should be, should be all set.
**Israel Blancas** 19:56 Thank you.
**Tyler** 19:56 Well, yeah, thanks, this is what the meeting's for, so, don't feel afraid to keep doing that, so yeah.
Awesome.
Well, yeah, if there's no more topics, we can end the meeting early here.
I'm so happy.
**David Ashpole** 20:13 I'm happy to add a couple topics. They're not, like, high priority, but, I did want to mention, I did look a little bit deeper into… the OpenTelemetry gRPC… Instrumentation?
**Tyler** 20:29 Oh, God.
**David Ashpole** 20:29 There was, like, Robert, I think, mentioned, had some concerns about adding interceptors back in, and so I did do some digging to try and figure out, like.
why did we remove them in the first place? Just to make sure that we weren't… like, if we did need to re-add interceptors, that we weren't going to reintroduce any of the problems that came along with it. And I'm… I think there's… the good news is, I don't think that by attaching some metadata, or, like, sticking metadata in context, that we're gonna introduce any of the performance issues that interceptors had. Like, Interceptors still a few, like, out-of-function call, so they're not free-free.
But it's not nearly as bad as, I think, the things that we were doing before, like wrapping, streams.
And computing… I think at one point we were computing protobuf sizes.
So… Yeah, like… I don't think it'll be as bad as it was before. I think the main ugly bit that comes out of this is that we… our API is going to probably look something like… Give me a bunch of dial options for a client, or give me a bunch of dial options for a server, instead of just, like, a constructor for a stats handler.
I would… I'm… My thinking is that we could keep The current stats handler function public?
If people only want that, they'll miss… some of the, like, one of the semantic convention-based attributes.
And then also offer a function that gives dial options.
Or alternatively, we could deprecate the constructor for the stats handler, and just try and steer people towards having the interceptors.
the main risk.
With the… with not deprecating, is that people just keep using the stats handler, and everybody has non-compliant.
hotel, GRPC metrics. So, I don't know if there are thoughts or… Otherwise, I'm gonna, probably start reviewing this, contributor's PRs and moving towards Having a constructor that has dial option… that just returns dial options.
**Tyler** 22:45 I think what I'd want it to do is maybe we can use some packaging structure here?
Like, can we put the stats handler in, like, a sub-package? Which is… effectively a breaking change, but it, like, still provides that same thing, and it kind of signals that, like, at the top-level package, we sh… we're not recommending using this, but to users, like, I don't want to get rid of it, because I do think you're, like, users that are seeing it, they don't… they don't care about semantic conventions, they like what it's doing, it works, like, I'd rather not… take away just, like, something that works from them. And then… Yeah, like, but putting that in, like, a sub-package and then having it, like, the top level, just, like, these main entry points for, like, these interceptors that you're talking about, like.
ideally, it just sets everything up for you from there, would be… would be, I think, kind of the ideal thing, because it would also signal, like, here's, like, the main entry point we want for this package that's going to give you everything, and then all the other stuff you can… You know, pick as you desire.
And I mean, maybe there's, like, a translation path as well, where you deprecate the top level with, like, an alias, and then you say, like, in the next package, or the next release, you have to go use this other thing from this other package, like, maybe it's not, like.
One time doesn't change.
**Pellared** 24:01 I would rather think of just deprecating this test handle if we are sure that we do not want to support it anymore.
So.
**Tyler** 24:08 The stats handler?
**Pellared** 24:10 Yeah.
**David Ashpole** 24:10 And it's like, the stats handler will still contain 99.9%.
**Tyler** 24:14 Yeah.
**David Ashpole** 24:15 All the logic.
**Tyler** 24:15 I… I would not…
**Pellared** 24:17 Yeah.
**David Ashpole** 24:18 So, we just need… we need one piece of information fetched.
from an interceptor, which will then put it in the context, so that we can get it with our instrumentation. It's a, like, we're just missing this tiny little piece that isn't part of the stats handler API.
**Pellared** 24:36 So we need the both, so we will need the both at the same time?
**David Ashpole** 24:39 That's why the entry point would be, here's… it's… we could do it two ways. We could have a function that returns a bunch of dial options. So you say, like, give me all the client dial options, or give me the server dial options.
And it would return the interceptors and the stats handler.
or… We could have, like, a… A drop-in replacement for… what's the… Like, we could have a dial function.
That just adds our… our arguments, and then… like, we could do it that way, too. And then it would accept the gRPC dial options and just wrap it, right?
**Tyler** 25:24 What about a gRPC connection? Like, an existing gRPC connection?
**David Ashpole** 25:29 Can you stick a stats handler on that?
**Pellared** 25:32 Good morning. I don't think so.
After morning.
Yeah, I'd…
**David Ashpole** 25:39 I think… I think if you wanted to construct your own connection, you would need to first Go get our interceptor and… stats handler before you construct your connection. I don't think you can… like, upgrade a connection. I don't know, actually. You can do with connection as a dial option, right?
**Tyler** 26:01 Yeah, I don't know.
I do remember, like, especially for, like, our export pipeline, we've tried to do, like, these dial option things, and then, like.
I guess it's not as bad because we're handing you back the dial options, but, like, the idea was that, like.
we accepted dial options, and it was just a nightmare compared to just accepting a connection in our exporter, but I think this might be a little different.
**David Ashpole** 26:48 Yeah.
**Tyler** 26:51 Yeah, I guess we don't have to solve it here. We can take a look.
on the issue, but yeah, I do think that, like, Trying to think of… a cohesive… single entry point for people to get all of the telemetry they want is kind of ideal, and then build packaging structure so that it's, like, composable, and if they don't want that, or they want to do it in a different way, or, like, work around it, like, I think it'd be great to provide that as well.
Because, like, like you said, like, it's not… zero resource, to add an interceptor, and so maybe that, for some people, is just, like, I don't… I don't care if I have 100% semantic conventions, if that's the cost, yeah.
**David Ashpole** 27:29 Right, it means that any request, or any… it's not a request, any RPC that's aborted before some point.
Just doesn't get counted.
**Tyler** 27:38 Hmm.
Yeah.
**David Ashpole** 27:41 Or no, it gets counted, it just doesn't have the server address, or the client address. Yeah, the server address.
Or has the wrong one or something, yeah.
**Tyler** 27:53 Which I think maybe some people… in a high-performance situation, or like, that's fine, I don't care. Like, yeah.
I'm thinking of Bogdan.
He's the one that was, like, super heavy on the status handler for that exact reason, but yeah.
**David Ashpole** 28:11 I mean, well, the stats handler had… the previous interceptors had a ton of problems.
**Tyler** 28:16 That too, yeah.
**David Ashpole** 28:17 That weren't just be… because they were interceptors.
**Tyler** 28:22 No, it's our implementation, but yeah, I think that, like.
Yeah. His feedback as well when he added the stats handler stuff, was like, I never want to run these for the overhead.
**David Ashpole** 28:35 Yeah. Yeah.
**Tyler** 28:36 Yeah.
But yeah, I mean, that seems real… Pretty simple.
**David Ashpole** 28:47 Cool.
**Tyler** 28:49 Cool, any other topics, David?
**David Ashpole** 28:56 I don't think there's anything that needs to be… talked about on this call. I did do the follow-ups.
For the exemplar reservoir that we talked about last week, splitting that out into, something in an X package.
**Tyler** 29:10 Oh, yeah.
**David Ashpole** 29:11 There's, like, a string of… PR is blocked on each other, that are blocked on… Some… there's… you know the PR that's, like.
Prevent Reservoir from panicking when size is zero.
**Tyler** 29:26 Yeah.
**David Ashpole** 29:27 But it's been taking forever to review. So that one's blocking a cleanup PR, which is blocking the next one.
**Tyler** 29:33 Okay.
**David Ashpole** 29:36 And I did find a solution, Tyler, to your comment about evaluating a filter multiple times.
**Tyler** 29:43 Oh, really?
**David Ashpole** 29:45 Well, it… I know… I… yeah, well, I did… I did find a solution.
**Tyler** 29:52 In the lazy evaluation way? Yeah.
**David Ashpole** 29:54 Yeah, yeah, well, you… I mean, it essentially requires introducing a new type in the attributes package.
Which… it… Is a set, but a set that has, like, some lazy properties to it.
So you can basically, like, pass a set and a filter, and get a thing back, which is… Which is a… essentially, like, keeps track of the decisions that were originally made.
by the filter.
Yeah, I can present it if that's helpful. People might find it interesting.
But basically, when you originally get… when you first get it… well, let's ignore that path right now.
But you… you can compute the hash.
And then also compute a mask.
Assuming it's less than 64 attributes.
That records all the decisions you made when you computed the hash.
**Tyler** 31:03 Hmm.
**David Ashpole** 31:04 And then later, if you want the… If you want to actually get the full set, you can use those decisions that you made.
To get the exact same set.
That you would have gotten.
And you can also use those to compute the dropped attributes later as well.
**Tyler** 31:24 So I don't under… how does the filter get applied, though?
**David Ashpole** 31:30 So, you can think of, like.
In the initial constructor for this thing, You essentially iterate over you're set.
You apply the filter function, And you record the result of the filter function in this mask.
So this is a 64-bit… integer.
And, like, so say the.
**Tyler** 31:57 Oh, oh, okay, because the result is only a true-false.
**David Ashpole** 32:01 Right, it's a true-false.
**Tyler** 32:02 So, okay, so the map… I see what you're saying, okay.
**David Ashpole** 32:05 You have a bit set that records all the decisions you made.
**Tyler** 32:07 Right, okay.
**David Ashpole** 32:08 And then you're able to apply those when making a new set.
And you're able to apply them when computing the dropped attributes.
So you can kind of cheap.
**Tyler** 32:19 Oh, okay.
**David Ashpole** 32:20 Store the result of the filter.
Instead of having to reapply the filter the second time.
it's new… It's new API surface in the attributes package, which is kind of specific to the Metrics SDK.
it could have been implemented internally in the Metrics SDK, except for the fact that both the Metrics SDK and the exemplar Reservoir Need to be able to, interact with this type.
So it could have been… I suppose it could have been part of the Metrics SDK's public API, but that'd be kind of weird.
**Tyler** 33:02 Well, there's like a… you could do a shared internal, package as well.
**David Ashpole** 33:07 Oh, I think it… Yeah, the idea was that this would be part of… Let's see… That this would actually be something that could be passed.
To the fixed size reservoir.
So that it can also lazily evaluate the dropped attributes.
**Tyler** 33:27 Yeah, but I'm saying, like, If you put… if you put this in, like, internal… SDK metric internal attribute, or something like that, right? Like, it would be accessible to this package and to the,
**David Ashpole** 33:40 I see, I see.
**Tyler** 33:40 geometrics, yeah.
But that's… that's, I think, more… Oh, this is an open PR now. Okay, so maybe that's something I could take a look at, but… Interesting.
Yeah, I mean, honestly, like… In a perfect world, this set would not exist.
In the attribute package, it'd be, something in the metrics package, but…
**David Ashpole** 34:07 Yep.
**Tyler** 34:10 Yeah, okay.
Yeah, the… Yeah, interesting. Okay. I mean, I like the approach, yeah, that's definitely an interesting… do you do a fallback of, like… I mean, obviously, like, the 64… is gonna be a limiter? Like, do you just, like, fall back to, like, a linked list, or not a linked list, like a, like a… He just…
**David Ashpole** 34:37 you just… you just compute a whole set. You just fall back to…
**Tyler** 34:41 Oh, okay.
**David Ashpole** 34:42 We do endorse.
**Tyler** 34:43 Yeah.
Yeah.
**David Ashpole** 34:47 What do we do?
Yeah, yeah, we do… we just literally compute the entire new set. Yeah.
**Tyler** 34:53 Yeah, okay.
So reasonable.
**David Ashpole** 34:56 Slow, but, like, what are you doing?
**Tyler** 34:59 Yeah, 64, whatever, like, that's fine.
Yeah, okay, yeah, actually take a look at that, that looks… that looks cool. I am hesitant about adding new surface area, but… I'm not opposed.
**David Ashpole** 35:15 The only… the only other thing I'll share is I've been working on a new prototype for Bound Instruments that complies with the spec that they merged, and it is going to be significantly more complex than the previous one I'd implemented, just because, the pinning behavior that's now required by the spec In the current PRs.
It's, like, weird to implement, because you have, essentially.
One set of storage that's for unbound attribute calls.
Like, the regular ones, where we hot-swap it.
At collection time, and then you need a different set of storage that's, like, fixed, more like a cumulative metric.
That doesn't get swapped, because you just want to reset each point.
So that… And then you need coordination to make sure that you don't overflow. Yeah.
And, yeah. And you need to make sure all the, like.
Bind with attributes, and the just with attributes.
Work the same way, which is kind of funky.
But I'm working through that now. It's just… it's probably gonna be a lot bigger in terms of, like, surface area and the SDK.
For that reason.
I'll probably… I'll implement it, and I'll give it as feedback to Jack and others, just to see, like.
maybe… Maybe there's other stuff we should do before we try and implement this, so that it isn't so crazy, difficult.
Yeah, I agree.
**Tyler** 36:47 I think that sounds great.
Yeah.
No, it's great. Thanks for taking another stab at it, that's awesome.
**David Ashpole** 36:56 Yep.
Cool. I think that's all the topics that I have that are worth discussing.
**Tyler** 37:03 Cool.
Awesome. Well, if other folks on the call or the recording want to check out those PRs as well, please, please do. I think, more eyes on that work. It's great. It's great work in the metric space, so… Really interesting.
Especially the bound instrument stuff, I think that's gonna be really cool once you get the new PR up.
Okay, any other topics folks want to talk about?
Things that are top of mind?
If not, we can end the meeting early.
Yeah, maybe I'll see y'all next week, otherwise I'll see you in 3 weeks, but yeah, or asynchronous. Till then, bye.
**David Ashpole** 37:43 Bye, everyone.
**Israel Blancas** 37:44 Bye.
