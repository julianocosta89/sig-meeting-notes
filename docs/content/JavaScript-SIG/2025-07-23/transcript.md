SIG: JavaScript SIG
Date: 2025-07-23
Duration: 56 minutes
============================================================

## Zoom Recording Transcript

**Jamie Danielson** 00:56 Hello!
**MG Marylia Gutierrez** 00:58 Hello!
**Jamie Danielson** 00:59 Delight meeting so far.
Guess it is middle of summer.
just moving things around before getting started.
Alright, I guess we can get started. I think
one of 2 people listed here.
are currently in the meeting for this topic. I don't know if we want to wait for the other person, or if I'm just not seeing them here.
**Jimmy Thomson** 02:49 Hey? So I think swap! Neil is on the call. I saw him join.
No, he's obviously dropped off again.
**Jamie Danielson** 02:59 Do we wanna wait for him to come back and and go to the next topic and come back to it.
**Jimmy Thomson** 03:05 Yeah, yeah, that. Why not? Thanks.
**Jamie Danielson** 03:07 Okay. Cool. Marilia.
**MG Marylia Gutierrez** 03:10 Yeah. So this one came from, just someone open a an issue today saying, like, Hey, where am we seeing things on the postgres? So I realized it was hard for people know which ones the database are being work on and things like that. So I created this new issue. That lists all the
basically all the plugins that are database related. There was like one rm, I also put it there. Just so people know. So I can show like, okay, Postgres is completed. I'm currently working on the Mysql. And last week I don't remember who it was that asked me.
They was asking if they can work on other ones. So this way is easier for people to see
what is open, and if anyone wants to help out can just put your name here, or, if you don't have permission, just ask me on someone else who has permission to add yourself to the in progress.
**Jamie Danielson** 04:05 Yeah, that sounds great. I guess. Yeah, like, in terms of the permissions thing, right? It should work, I think, as as long as someone adds a comment. Here, then, anyone on Hotel Js. Can assign them to a particular, or just say that they have this one assigned.
**MG Marylia Gutierrez** 04:20 Yeah.
**Jamie Danielson** 04:26 So probably I'm always torn on whether we want to like make things into issues or not
for tracking. But that's also like
extra overhead. I guess we can see as it goes. If it goes pretty quick, then it's probably not necessary.
But thank you for creating that.
**Daniel Dyla (Dynatrace)** 04:45 I think for this case it's fine, like, we don't need separate sub issues for everything, because they're all like completely identical.
As long as people just comment which ones they're working on. I think it's probably good enough.
**Jamie Danielson** 05:01 Nice.
That's great. I'm kind of tempted to
PIN this issue. We haven't really done much. I guess we don't have any pinned issues in Js contrib.
but since that's like one of the top things we're working on, anyway, by pinning it, it kinda shows like that's sort of a top priority.
**Daniel Dyla (Dynatrace)** 05:21 Yeah, go for it. I'm I'm with you.
**Jamie Danielson** 05:25 Nice
**MG Marylia Gutierrez** 05:31 Next up is also me the next one. So yeah, being, I think I mentioned a couple of weeks ago that I started to look at the the cars, if config. So now I'm actually starting to actually work on it. So I put it like the issue, like the plan of my steps, and I just copied them here just
if anyone has any concern. So my idea is pretty much I'm creating like a config provider.
I and I'm putting on the core package, hoping that is a good place to put. So my 1st version is gonna be the config provider is gonna read like environment variable. And then whoever wants to actually read environment variable goes to config provider, not directly to the environment variable. So this way, we know this can like, prepare to have other types of configs, but doesn't change the behavior for current people.
And then basically, I'm creating the
a class that is configuration that is based on this pack for the config file. So this way have the same structure. And it's easier for people to just recognize and hopefully with time. We can find a way to kind of like, generate this part similar. What we do like semantic conventions, we just have whatever is created, there always being generated here, and then I've been talking also with
people that are working this on the Java one. So we're kind of like aligning how to do those things. And then I'm picking one of the packages, I'm thinking, started with the SDK nodes. Because.
I'm getting a few like simple
basically environment variables to test it out more so like as a proof of concept doing this, and once this is replaced with there, then, I create the option to actually refund the file on this config provider
do this whole part of just which actually, I have a question that I just want to use an existing plugin to transform from Yaml to like or Json, or something else. I don't know what is the proper process to like pick, because there are like several that can kind of like do this. So I guess I need to check, for
I don't know permissions like things like that. So.
looking for some guidance on how to pick which one.
And that's kind of the plan. And so once it's working with the SDK like nodes, then I can go over to like all the other repos, and actually get rid of when possible, of environment, variables, and so on.
**Jamie Danielson** 08:01 I think that sounds awesome.
**Daniel Dyla (Dynatrace)** 08:03 Yeah, sounds good. I did the question that I. The 1st question I have is, how did you decide to put it in the core package. Like. Why, why, that package as opposed to
like a new config package, or something like that.
**MG Marylia Gutierrez** 08:18 So, yeah, that was kind of my question. Like, if that is the right place to put. Because I just saw that we had the get environment variable like those functions were on core. So I was like, well, if this is the place to have
config, maybe that is the place to keep. But I'm open to suggestion. If you think should be a completely different one.
Yeah.
**Daniel Dyla (Dynatrace)** 08:41 Yeah. To be completely honest, I think the core package shouldn't exist.
It's kind of just like
the the junk drawer of stuff that we didn't know where else to put it like utility functions. And that kind of thing config is like an important enough component that I think
it likely deserves its own package
especially since it will be used by
like the various SDK packages potentially used by instrumentations. I don't want instrumentations necessarily depending on that core package.
**MG Marylia Gutierrez** 09:18 Okay, yeah, I can do this. And just, you know, like my plan. If you see, like, very basic, I'm gonna try to break them down in very like small set to make it easy to review, so they probably could have now have a lot of to do's like, I'm doing this, because this other thing is coming up so at least to make it very easy for reviewing so.
**Daniel Dyla (Dynatrace)** 09:40 Yeah.
**MG Marylia Gutierrez** 09:40 And yeah, I don't wanna create like, first, st Pr will like
50 files of 100 lines each one. But yeah.
**Daniel Dyla (Dynatrace)** 09:49 Yeah, I think, having it in its own package has other benefits, too, as well, because it'll likely go through some experimental breaking changes. And it's, you know, we can have a a 0 dot whatever version number
and then I have for a long time been considering getting rid of that core package in favor of
like more specific like the the time functions, I think are the most
like crucial in there, and just you know, splitting that into a time package and then splitting the unit conversions into a package and that kind of thing to make it a little bit more
maintainable. I I don't like the core package.
**MG Marylia Gutierrez** 10:39 Yeah. Got a got a plan in place that.
**Daniel Dyla (Dynatrace)** 10:44 In general, the config or the the plan seems okay, though I just would go for a new package. Probably.
**MG Marylia Gutierrez** 10:50 Okay. Yeah. Sounds good.
**Jamie Danielson** 11:00 Awesome. That's exciting.
Okay, so we anything else on those 2, Marilia or anyone else.
**MG Marylia Gutierrez** 11:15 Nothing for me.
**Jamie Danielson** 11:17 Cool thanks for working on those.
Okay, so I think, we have both of you here now for the Es Build support discussion.
**Jimmy Thomson** 11:29 Yeah. So what are you there?
Got it, Biggie? If not, but.
**Daniel Dyla (Dynatrace)** 11:35 Yeah, he is.
**Jimmy Thomson** 11:37 Cool. So it's really just looking for a bit of guidance, really where?
And I said, When I say, we create an edge of working with Microsoft on on a
project for a very big Uk client. And we're we're using open telemetry.
We're bundling our code. But we found that as a result of that bundling we lose the ability to
to an instrument using various packages. An example would be Microsoft's own as your SDK telemetry
instrumentation. Sorry?
so I think that the way forward for us, as far as I can see, is to either
cross our fingers and and hope that at some point the open telemetry community will come up with a
complete solution for working with Es build.
I think the reality is that
that solution, if if it, if if it happens at all, is gonna be in the probably fairly distant future, the the other option. But tell me if I'm wrong. The other option, I think, is to try and build on some of the really good work that I think it was Drew calling had done previously.
to see if we can work with what he's
created so far in order to get that working with with the S build.
Sorry.
It's really just looking for you guys to tell us.
Don't wait for us. Go and look at the good work that Drew's done, and and
and see if we can perhaps help out there as well, or
Perhaps you could pull up your hand. Tell me that in a few months this will all be built into
open to that tree, and happy days.
**Jamie Danielson** 13:45 Right now, I think I've not tried this particular plugin. It is a known thing that, you know.
our instrumentation generally is not supported for bundling, and it's kind of thing, you know we've known about and worked on a little bit here and there. The other Maintainers can correct me if I'm wrong. But it is a lower priority for us. I don't know where it exists in the like.
In the near future. I would be curious to see if that plugin does work. If it's something that can easily be plugged in and and used, I think that's worth
giving a shot, because, if nothing else, one of the things that's always helpful is, you know, getting feedback on something that's working like in production in real world scenarios to be able to. Then look at, you know, what does it take to.
you know? Move this into what we're currently doing?
**Daniel Dyla (Dynatrace)** 14:46 Yeah, I I agree with that. I don't know if, like, lower priority would necessarily be the word that I use, because,
you know, it affects a lot of like
browser. Almost every browser application these days is bundled, and a lot of bundlers share these issues. But the one of the main problems we have is that the browser
like the the SDK and Api were built
node first, st basically from day one like, I'm talking 5 years ago.
And there have been some browser so some work done for browser support.
But it's always been like
whatever to make it work in the browser? Not necessarily like a concerted effort to be like, what does the browser, you know, to to really look at what are the needs of the browser
and the client side. And now there is a working group specifically working on that.
And because that group, I mean, they just started
what they've had 3 meetings, I think. Maybe 2, like they just started I would bring this to them because I don't know what their plans are about this stuff long term. But I would assume that this is a very important part of their strategy, because they're very browser focused, and I think that they will be
assuming bundlers from day one.
**Jimmy Thomson** 16:21 So just just for reference. This is entirely Nodejs. For for us the browser side of things. We're not
tokens.
**Daniel Dyla (Dynatrace)** 16:30 Oh, interesting. Okay, yeah. Sorry. My brain. When I see Bundler stuff it just like jumps to browser.
Okay, well, I guess
all of what I just said is still applicable.
That's why we haven't thought that much about bundlers.
Yes, I know that some people use bundlers with node.
I more than some people. I know that it's a fairly common thing to do, and I know that there are challenges with it.
I guess I had been thinking of this more as a browser specific thing, when it's probably not fair to say that
**Jimmy Thomson** 17:14 Yeah, just the the nature of
So if I
the the cloud functions that have been created today tend to, I think there's a tendency to bundle for those just to keep the the cold starts as low as possible. But but anyway, I'm not. I'm not. I'm not here to try and persuade you to
you know, increase the the importance of this or anything. It's more just to to know whether there is a
a a release coming soon, that that could affect the decisions that we make about, whether we commit resource to, for example, helping out during his project or or another way. And to give you a rough idea, we we're looking at going into production mid next year, and we'd have about a 4 month hardening period before that. So in reality, we we'd want to be implementing this before the end of
that the year. And so if you tell me there's no way nothing's gonna be anything is going to be built into the core for to support. Yes, Bill, by the end of the year. Then that makes it a really easy decision for us to say, well, we okay, we need to focus on picking up and helping with with true with his project, or or some other mechanism.
**Trent Mick** 18:42 Yeah, I don't see it.
I don't speak for everyone, but I think likely having your help is gonna be yours or other people's help is would be required for stuff to happen in core open to entry releases
to get that happen because there's there's no one that I'm aware of.
That's
other than Drew's work, and I'm following what he's been doing lately. That's been involved. Back last year a little bit. I'd had a couple
proof of concept Prs to try to improve the situation a little bit, but I dropped those because that was
just kind of a hackathon thing for me, and I didn't have time to follow up on those. So there are a couple of closed Prs, if you go digging.
Have you guys tried Drew's es build plugin node module.
**Jimmy Thomson** 19:36 That's the one that fairly recent wasn't a few months ago. I think he created that. I haven't tried that yet. No, but I think.
**Trent Mick** 19:43 You know your experience with that, and that certainly that would be a starting point for
what, if anything's needed in core to to do better.
**Jimmy Thomson** 19:51 I think that that would be certainly going to be my
or what I'm gonna suggest as a 1st port of call to to resolve it for us.
because if that works with with minimal effort, then that's great.
But I think we've given us, it's enough for for ourselves and Microsoft to have a chat, and just see
where we want to go forward here, and where we can perhaps support the likes of through all yourselves.
**Trent Mick** 20:22 Okay, yeah. And yeah, there's what's the slack channel, the hotel? Js, dev,
or just hotel Js slack, bringing up
like getting getting involved to some degree, even if it's only to say what your experiences are with current things, whether or not you have the resources to to have people helping out with core would help
**Jimmy Thomson** 20:46 Great.
**Trent Mick** 20:50 When you're talking about your use case. You're talking about
old start time. So I'm guessing function as a service is. Is your use case here?
Yes.
**swapnilnagar** 21:00 Yes.
**Trent Mick** 21:02 Then you said Microsoft, so is this, is this azure functions mostly that you guys are using
on the various providers.
**Jimmy Thomson** 21:09 Sorry talk as he's in the Microsoft Functions team.
**swapnilnagar** 21:13 Yeah, so yeah, Hi, this is faulknil. I'm from the functions team. And yes, you're right, Trent.
that's the that's their use case.
**Trent Mick** 21:22 Okay.
It's not.
**Daniel Dyla (Dynatrace)** 21:26 Yeah, I guess
just to summarize everything I would say, there's no specific reason we haven't done this. It's just that we have limited bandwidth, and it hasn't bubbled to the top.
If you're asking whether we're going to implement something in the next year.
unless somebody puts in a concerted effort. The answer is, no if you're willing to be the person to put in that concerted effort, I don't think that anybody here would want to stop you or block you, or you know there's no reason not to. It. Just hasn't been done. Assuming the changes that you're asking for are, you know, feasible to do. And without, you know, big breaking changes or specification and compliant changes or stuff like that which
at this point, I think, is a fair assumption.
**Jimmy Thomson** 22:13 Great thanks.
**swapnilnagar** 22:16 Can I ask you the question the other way? Like, is there a specific reason why it's been not prioritized? Meaning that is there like considerably more effort to even get involved in this, or
what's the reason for not supporting it?
**Daniel Dyla (Dynatrace)** 22:32 People just haven't asked for it.
**Jamie Danielson** 22:35 We have like, we're trying to figure out. You know, we have limited bandwidth, I guess overall of people involved. And what we have time for. So we've been sort of prioritizing different things depending on
you know what comes up there. That's generally what it is.
**swapnilnagar** 22:51 And if somebody has to go and fix it how
to your best, because you guys know the code base better than anybody else
what you would say like, how much time it will take, or I'm not saying like the the concrete number, but like how much effort you think in your head. It's gonna be.
**Daniel Dyla (Dynatrace)** 23:10 There's no way I can answer that.
**swapnilnagar** 23:12 Okay.
**Daniel Dyla (Dynatrace)** 23:14 I about about the bundlers and and and the changes that would be required to be honest.
**swapnilnagar** 23:21 Hmm, okay.
**Trent Mick** 23:24 I would, I think, as a 1st step I would try Drew's
package first.st See what your experiences are there, and then ask again, and maybe we can like without knowing specifically whether that's sufficient for you or too limited. Then then it's hard to know.
Yeah.
**Daniel Dyla (Dynatrace)** 23:53 I don't see a link from
from this module to like a Github repo, or anything like that. Does anybody know where this is actually the
in development.
**Jamie Danielson** 24:06 I was looking for that, too. It's possible it's not public.
**Daniel Dyla (Dynatrace)** 24:14 Yeah.
found it.
**Jamie Danielson** 24:20 Found it.
**Daniel Dyla (Dynatrace)** 24:21 Yeah, I found it just by Googling. I'll add it to the dock here.
**Jamie Danielson** 24:32 Oh!
**Daniel Dyla (Dynatrace)** 24:34 I'm just asking, because I don't know how much work it, even like
how much he's even done implemented here. And
**Trent Mick** 24:41 He has 2 github handles.
**Jamie Danielson** 24:43 Yeah, I just realized that I'm like, Wait.
good find.
Oh, the Internet.
**Daniel Dyla (Dynatrace)** 24:52 It doesn't seem like it's that much like the Plugin itself doesn't have that much code in it to be completely honest.
So just going purely based on that which is a
a known, horrible way to guess how much work stuff is going to take. But it's the best we've got.
I would say, if somebody really wanted to put effort into this, I
a couple of months seems like it'd be reasonable. I don't know. Like just just kind of guessing based on how much is done here. And this is coming from the outside right? He's he's
purely doing this without making changes to the SDK. If you have the ability to build stuff into the instrumentation, I would assume that
probably it could be done with less work.
But that's just knowing nothing about the bundler or the plugin.
That's a guess. But it's the best guess I've got at the moment. Does that help answer your question?
**swapnilnagar** 26:00 It does.
**Jimmy Thomson** 26:01 Yeah, I did have a look through this this code base and say to you, I thought, Well, there's not too much code here. How hard can it be but
**Jamie Danielson** 26:09 Famous last words.
**Jimmy Thomson** 26:11 Yeah.
**Jamie Danielson** 26:11 Yeah, exactly.
**Jimmy Thomson** 26:13 Okay.
**Jamie Danielson** 26:14 Put that nice. Okay.
**Daniel Dyla (Dynatrace)** 26:17 Because I assume the Plugin.
you know, has to work around all kinds of things that you wouldn't have to work around if you were built in. That's an assumption, but
I think it's likely a good assumption.
So you know.
**Jimmy Thomson** 26:38 Maybe see if we can try and get a hold of True, and see if he's willing to do a bit of a Kt. On what he's done.
**Daniel Dyla (Dynatrace)** 26:51 Somebody made a Pr to add an es build Plugin to contribute like 2 years ago, or last year, or something like that. Was that true?
**Trent Mick** 27:01 That might be true, almost certainly. Drew. Yeah.
**Jamie Danielson** 27:03 Yeah.
**Daniel Dyla (Dynatrace)** 27:05 I wonder what happened to that?
Probably just.
**Jamie Danielson** 27:08 Asked us for feedback, and Trent had a go at.
**Trent Mick** 27:12 I engaged a little bit, and then I dropped it because I didn't have time.
**Daniel Dyla (Dynatrace)** 27:16 Yeah, so it got stale, and he just published on his own, I guess, is most likely what happened.
**Jamie Danielson** 27:21 I think so.
Yeah.
**Daniel Dyla (Dynatrace)** 27:25 Okay.
**Jamie Danielson** 27:26 Yeah, so
oh, here there's a comment. There.
**Daniel Dyla (Dynatrace)** 27:39 Yeah, that was at the start of this year. He said he'd like it to be in this repo, but he's publishing on his own, for now.
so seems like he's still willing to
engage with us. He's not too frustrated by the fact that we ignored him. It's just good.
**Jamie Danielson** 27:56 Might just be being very polite also.
**Daniel Dyla (Dynatrace)** 27:59 Yeah, could be.
**Jamie Danielson** 28:00 I'm sure he's frustrated.
**Daniel Dyla (Dynatrace)** 28:02 I wonder?
If there's some like, maybe an es build plugin?
Yeah, I don't know. I'm not even gonna speculate. I don't know enough about it.
Seems like he'd still be willing to engage, so I'd I'd look for his feedback try out his module and see
if making changes in the SDK is even helpful, or he may say, like, even if you make changes in the SDK, you still have to use a plugin for this or that reason I have no idea.
**swapnilnagar** 28:40 So, so, suggesting we should be connecting with Drew to get more insight on this.
**Daniel Dyla (Dynatrace)** 28:47 I think that's probably a good next step. Yeah.
**Jamie Danielson** 28:50 Yeah, I'm probably trying it out, I guess, too, to see like, get a feel for it.
**swapnilnagar** 29:01 Would you mind just sharing the contact for Drew here on the notes.
**Daniel Dyla (Dynatrace)** 29:07 Don't think that we have his contact.
**swapnilnagar** 29:11 Okay.
**Jamie Danielson** 29:11 You may be able to. I don't know, I guess if.
**Trent Mick** 29:13 I would try it as module, and the repo is linked there, and so you could follow up.
Yes, issues on that. Repo is probably the best way.
**Jamie Danielson** 29:20 Yeah. And then if
yeah. And then, if you're not already in the Cncf slack that tends to be a good way to chat also, like a lot of things, will start like in issues and stuff like that when you're 1st reaching out to folks. But then, you know, you can find people on the Cncf. Slack to chat even post. And like I'd mentioned in here, there's like an hotel. Js Channel and Hotel Js dev channel, etc. So that's a good place to go to.
**Daniel Dyla (Dynatrace)** 29:48 He's on the Cncf slack. I I just posted a link to his user in the chat here.
so maybe that's a good way to get in contact with him. I don't know. He's online right now, so
seems like, maybe he uses the slack.
**Jamie Danielson** 30:06 How's your chance?
**Daniel Dyla (Dynatrace)** 30:08 Now's your chance. Yeah.
**MG Marylia Gutierrez** 30:10 Run, run.
**Daniel Dyla (Dynatrace)** 30:13 He's not too mad at me for posting his user in the chat here.
**Jamie Danielson** 30:16 I know I'm like torn on whether to put that in here or not.
**Daniel Dyla (Dynatrace)** 30:21 I wouldn't put it in the Doc.
**Jamie Danielson** 30:22 No.
**Jimmy Thomson** 30:26 It's fine we'll we'll find him.
**Jamie Danielson** 30:34 Okay.
Anything else on this one before we move on.
**Jimmy Thomson** 30:41 Don't think so. Really appreciate your time. There.
**swapnilnagar** 30:45 Thank you.
**Daniel Dyla (Dynatrace)** 30:47 Thank you.
**Jamie Danielson** 30:50 Svetlana. You are up next.
**Svetlana Brennan** 30:53 Yeah, just a quick Fyi just wanted to update you guys that there's just one issue left in this milestone that doesn't have anyone assigned to it. I could pick it up next week. I'll have some more time at work, but if someone wants it.
you know, wants to take it now, that's fine. I haven't done something like this before, so
I can't promise a specific date when it will be done by. So if this is a very time sensitive thing, then I prefer, if someone else take it, but if no one else will, then I'll give it a shot.
**Jamie Danielson** 31:30 Just wanted to share that.
**Daniel Dyla (Dynatrace)** 31:33 Yeah, I can.
I can probably do this just because I think I have the most
I don't know demons. In my past I've I've been bitten by this more than anybody else, I think. And I have an I have an idea of what to look for, and I think, explaining to somebody else
all of the possible things that can go wrong would take longer than just doing the review.
**Svetlana Brennan** 32:01 Awesome. Thanks. Yeah. I I figured I was like, I don't have much context on this. I mean, I could try it. But it's gonna take a long time.
**Daniel Dyla (Dynatrace)** 32:09 Yeah. Unfortunately, the best way to learn about this is to just do it wrong. Tens of times.
**Svetlana Brennan** 32:17 Oops!
**Jamie Danielson** 32:18 I mean, that's life. Right? So
should I assign you to it?
**Daniel Dyla (Dynatrace)** 32:27 And this, yeah, that's fine.
**Jamie Danielson** 32:33 Okay.
Nice So
awesome.
Okay.
Ready for review. Oh, sorry. Anything else on that one, Svetlana, before I move on.
**Svetlana Brennan** 32:57 Nope, all good.
**Jamie Danielson** 33:02 Close.
Okay.
**David Luna Bistuer** 33:06 Yeah.
**Daniel Dyla (Dynatrace)** 33:06 I guess. Actually, before we move on from that, I would maybe bring up a topic that
is possibly best left for another time, but I'll bring it up now.
The Api version 2 poc that I made. That is a completely different way of writing these Apis.
What are the chances?
And has has anybody looked into that? Has anybody spent time reviewing it and thinking about it?
And is there any appetite to try to apply those to the events. Api.
rather than because right now, if we just continue on the path we're on, we'll do the events Api in the same style as all the other Apis, and then eventually, maybe, we will
make changes to it. But in the interest of avoiding thrash.
should we try to do the event. Api
in, you know, a slightly, in a different way.
I guess the major downside of that would be that the events Api would feel significantly different to use than the other. Like the tracing and metrics. Apis, they would have like a different
an entirely different style.
I don't know. I
I don't know if that's a coherent question or not. Is is that something that people think is a good idea, or is it best left
for? Now?
**Trent Mick** 34:46 You're talking our a Api to poc thing.
**Daniel Dyla (Dynatrace)** 34:49 Yeah.
**Trent Mick** 34:50 So one apologies. I haven't really played with it yet, but
naively, I feel like the maybe naively the logs Api SDK stuff has been sitting there kind of close to
being stable for a long time, and I'm not sure
I'd wanna throw on the thing. Throw on the
let's totally change it. To use this different underpinnings.
**Daniel Dyla (Dynatrace)** 35:18 Yeah.
**Trent Mick** 35:18 Given that. That's still proof concept level right now. But
I don't know. I can understand.
Given the timing that we don't wanna have the churn, but I don't.
**Daniel Dyla (Dynatrace)** 35:30 I mean. I don't know whether the Api 2 dot O stuff will come in any reasonable amount of time, anyway, so.
**Trent Mick** 35:36 Yeah.
**Daniel Dyla (Dynatrace)** 35:36 It's it's potential churn.
Yeah, okay, I guess we won't. We won't go for that. It it's not.
It's not far enough along yet. Okay.
I just thought it was worth mentioning. But we don't have to, really, I think, discuss it in depth at the moment we can move on.
**Trent Mick** 36:03 Okay.
some things. I did wonder. I have been following the the logs. Api stabilization stuff work. But there's been a fair amount of work on
the logs. From hotel spec side, right? So if we're going to be stabilizing something, I wonder if there's more.
**Daniel Dyla (Dynatrace)** 36:21 It. Actually.
So it's made of.
**Trent Mick** 36:23 We're making sure.
**Daniel Dyla (Dynatrace)** 36:25 It kind of horseshoed back around to what we had. But so we
add the logs Api, and then the events. Api was introduced
and like. There were a lot of changes made to it, and there was a lot of back and forth, and it kind of horseshoed back around to what we actually have. We're mostly specification compliant. Now
from having not followed all the spec changes.
**Trent Mick** 36:52 Okay? So yeah, the events. Api was a major one. Another one was on whether.
and maybe this affects the other ones on what the nested attributes are allowed, and the different types of attributes. I don't know what our
current status on support for those changes.
**Daniel Dyla (Dynatrace)** 37:09 Yeah. So the Otep just merged for complex attributes. Which actually, is on all signals.
include but logs was one of the or events was one of the major like drivers for that.
I believe right now we don't support it.
But the specification isn't written there yet. Anyways, the Otep just merged, but I think none of like the follow on spec is is done.
**Trent Mick** 37:44 Okay. Okay.
**Jamie Danielson** 38:14 Okay.
Alright. So now, David.
**David Luna Bistuer** 38:23 Yeah, right? Well.
that's a Pr that I think last week I wasn't here. But you skipped because
because of that. It's great for view, although there is an issue. But I think it's because of the caching of the node modules.
and I will fix, but it's ready for review. So it's ready for your feedback.
Okay, take care.
**Jamie Danielson** 38:45 Is this the thing that lets us run things in docker and stuff.
**David Luna Bistuer** 38:49 Exactly, but for each package, so we have it globally. It was in a previous Pr, and this one is, adding the same scripts in each package, so
you can now compile and run the test with the service on for each package in the
that's the intent. Actually, that just a part of what? That from what we use the upfront. 10, th
so yeah.
okay, so that's it. Just to, you know.
**Trent Mick** 39:24 Oh! Like clear reviews.
**David Luna Bistuer** 39:26 It's ready. Yeah.
**Trent Mick** 39:27 Yeah.
**David Luna Bistuer** 39:28 And then the other 2 is the same. So take your time. It's just that. Now I remember, Jamie, that you did the Pr.
Changing the scripts to to add Esm output to express.
**Jamie Danielson** 39:41 Way back in the day.
**David Luna Bistuer** 39:42 I did something similar within, which is the implementation that we created trend. And I just to test right now, because at that time when you create that pr we didn't appear. Still, we're in typescript 4 dot 4 dot 4.
**Jamie Danielson** 39:57 Yeah.
**David Luna Bistuer** 39:57 And wasn't kind of the the best moment to do it. So now it's
it's a good time, I think. So. I tried this one, and also just to for the sake of having options open. I tried another one with the with another tool, which is, it's called Ts up.
which, under the hoods uses is using yes, built.
which is faster, but at the same time, well, as a as a con, it doesn't do that checking.
So okay, how about look? It's just to, for the sake of having a
you know, resuming the conversation of Esm. And and what's bad should be go.
So that's it. Whoever is interested take your time with the comments here, and we can have this discussion asynchronously.
**Jamie Danielson** 40:43 Have my renewed interest. I created a did I end up creating an issue for the publishing? I guess it's not even the
yeah publishing the.
**David Luna Bistuer** 40:54 I think I think that you have it too. I.
**Jamie Danielson** 40:56 We can like, link them up.
**David Luna Bistuer** 40:58 Yes.
**Daniel Dyla (Dynatrace)** 41:01 One thing that is in the Api to Poc is publishings common Js, and Esm.
With like full standards, compliant publishing.
It's not bundled, but that might be worth looking at. Also.
**David Luna Bistuer** 41:22 Okay, have a look.
**Daniel Dyla (Dynatrace)** 41:25 I did not use Ts up.
Don't know that it matters.
**David Luna Bistuer** 41:32 Yeah, if you, if you're interested, have a look, it's
quite straightforward. So it's using Ts config that you have said in your project.
but have some extra extra options, and
the format is just one of that of them. It comes out of the box. The also. Another thing that happens is also that
it bundles everything. No, it's not bundling, but, you know, puts everything in just one single fact. That's something that for me, it's kind of. So we have. So that those are the differences that we have. I think I put a list of differences
in the Pr for which is using this app?
So yeah, so we can, we can consider. So it's just a.
**Daniel Dyla (Dynatrace)** 42:14 Pushing everything.
**David Luna Bistuer** 42:15 Good. Yeah.
**Daniel Dyla (Dynatrace)** 42:17 Emitting a single file like a single Ts file for the full package. You mean.
**David Luna Bistuer** 42:25 Yeah, but this is quite simple. Just have. You know, we have the only Dts file. And then, just an enum in a, in a, in a separate file for the attributes.
maybe it doesn't work. So maybe in in another file. So something different. I haven't inspect all the options.
But that's 1 thing that no, I don't know for me. I don't know. I'm not sure if it's a good thing or a bad thing
we prefer to have simple format, though, so have a single single Cs file for for each step script, file.
I'll keep looking, and if I find a way of of doing that.
maybe I'll try to update that Pr.
**Daniel Dyla (Dynatrace)** 43:06 Dumping everything out into a single file like one file, for the whole package is definitely a big
like startup time performance enhancement. That was one of the things that man. It's been
probably 2 or 3 years. But
There's somebody did a an analysis of like the the startup performance impact of hotel and actually, literally just going through all of the requires
was an enormous part of of
Of what our impact is like by the share of of startup impact. Time just going through the requires was like 60% of it, or something like that.
And one of the the things that we can do to help that is
publishing in a way that you know, just loading less files. So that may be.
**David Luna Bistuer** 43:59 Those.
**Daniel Dyla (Dynatrace)** 44:00 A a good side benefit.
**Jimmy Thomson** 44:03 So can I add something to that? Just to say that as a part of the work
that we've been doing, Microsoft understanding a lot about how their system works under the hood.
One of the big benefits we found to bundling was that their system internally, when it unzips the zip file that you have to to send up. It's super super quick in the milliseconds, because we just got one file. But if you are bundling up a whole bunch of modules and files it the time to to decompress that it goes up exponentially
sorry.
**David Luna Bistuer** 44:48 All right.
Okay, that's it. From my side.
**Jamie Danielson** 44:51 Nice
copy
cool.
Alright. Gcp resource detector Erin.
**Aaron Abbott** 45:14 Yes, yes, I think this was maybe discussed a few weeks ago. I wasn't here. But yeah, basically. The long and short of it is, we have.
Google has a resource detector we have in a separate repo, but it can't be bundled into the main auto instrumentation.
So this one existing contrib.
And yeah, we would like to kind of consolidate that and have the the thing that Google
kind of maintains or curates either thing in Contrib.
and I guess there's a couple ways forward.
Yeah, do. Do folks have context on this.
**Trent Mick** 45:55 I think so. Yeah.
**Jamie Danielson** 45:56 Yeah.
**Trent Mick** 45:57 Or at least I remember. Yeah.
**Aaron Abbott** 46:00 Okay, yeah, so basically, the options are.
we can contribute like the code we have in our repo. Now that things have sort of stabilized. The reason we had it in a separate repo was mainly for
doing like integration tests against Gcp info, which we obviously can't be doing in the contribute repo
The other kind of option is to pull it in partially as a library, and there's some kind of prior art in different languages for that.
But yeah, at this point I'd be happy to, you know, move all the code in here, so that I think it makes it a little easier for maintainers. But
I know we also are trying to take a stance on putting stuff in contrib versus.
you know, kind of people federating stuff into separate repos. So, yeah.
**Daniel Dyla (Dynatrace)** 46:49 Yeah, I mean, there's so many different sides to this from my perspective. Having things hosted in external repos is is always easier for us. But there's like the discoverability aspect. And then the usability for end users to just like install the auto.
Packages and get everything.
I think what you're referring to from the prior art perspective is like the the other packages you linked to that were essentially just
bundling or like wrapping code that was hosted elsewhere.
And then.
**Aaron Abbott** 47:28 Yeah.
**Daniel Dyla (Dynatrace)** 47:31 Yeah, in in other languages, which
I think one of the problems is that the project as a whole, like all of open telemetry, not open telemetry. Js. Has not really taken
on this issue and and made a policy about it. So we don't really know what to do.
The other part of it is, even if you move all the code into the Hotel Js. Repo, it still depends on the Gcp. Metadata package, which is doing all of the like actual interesting work. Right?
**Aaron Abbott** 48:02 Yeah sort of it. It's basically just like a rest client for the metadata server. So it's
it's doing a little bit. But there's still a fair amount of it's kind of like a dumb wrapper around the Http. Api. To be honest.
**Daniel Dyla (Dynatrace)** 48:16 Yep. So, having given it some thought over the last couple of weeks.
I think I'm coming more in line with being okay with.
you know, it's it's fundamentally not that different than having a dependency like Gcp. Metadata. It's just that the dependency does slightly more
that where I would draw the line is that I wouldn't want to.
Like I would want the version to be pinned
so that we don't like. If if something that we don't control gets published. I don't want the users who depended on a package from our namespace getting a different bundle of code.
**Aaron Abbott** 49:00 Yeah, absolutely.
**Daniel Dyla (Dynatrace)** 49:01 I think that's kind of you know. I I think the the only sort of non-negotiable for me.
**Aaron Abbott** 49:11 Yeah.
**Daniel Dyla (Dynatrace)** 49:12 I don't know. I've I've gone back and forth on this. On the way I feel about this a handful of times in the last couple of weeks. I can't seem to get myself to to settle on a single opinion.
**Aaron Abbott** 49:23 Okay.
yeah, I mean, I I feel likewise like I'm I've kind of changed my mind gone back and forth. But
I I do think, moving the code in here. So just just the Gcp metadata kind of dependency.
I think that would be the best. Just so that, for for example, like this this last move to with SDK 2 and changes to the resource detector. I still haven't updated this other, the one in our Repo to handle that, and stuff like that is pretty mechanical would be well done by maintainers. I think so.
Think that would be my preference at this point. If that's okay, I think it's probably like.
I don't know if I had to guess, like 1,500 lines of actual code.
So nothing crazy. But yeah, is the
**Trent Mick** 50:17 Is the business logic for this stuff, pretty much baked in your opinion, like the different Gcp. Services that this is
creating resource attributes? Or is that pretty much static at this point? Because sometimes there's if like, if there's something new that comes, it's normally it would go through semantic conventions
1st before we're releasing implementation. Or there's like an experimental phase. So I don't know if that gets more difficult for you guys if it's being maintained in the hotel. Js repo.
**Aaron Abbott** 50:49 Yeah, yeah, it's a good question. No, I think
I think it's pretty well baked at this point.
I haven't been changing it much in the last 2 years.
**Trent Mick** 51:00 Okay.
**Daniel Dyla (Dynatrace)** 51:03 I think it.
**Trent Mick** 51:03 And I had the call with him coming into the Hotel Chass control group.
I think, yeah.
**Daniel Dyla (Dynatrace)** 51:09 It doesn't strike me as like something that's gonna add a lot of maintenance burden.
**Aaron Abbott** 51:17 Okay, yeah. I know there was a concern about bundling. Also, did you? Did you have any thoughts on that? Like the Esm plus common Js builds.
**Daniel Dyla (Dynatrace)** 51:28 But.
**Trent Mick** 51:28 Specific to this package.
There.
**Aaron Abbott** 51:34 Yeah. So it was that Gcp metadata dependency. I I think I can dig into whether we support kind of the dual build.
**Trent Mick** 51:45 Okay, yeah, I don't. I'm not aware of a particular one that was specific to Gcp detector for
this. I mean, I can feel like Hotel Js. Is still in early days on the dual build
story. Like so far, the only ones that are emitting both.
or Esm builds are ones that have been
kind of browser targeted, but I know that there's a lot of requests to be doing it for all the packages.
**Aaron Abbott** 52:13 Okay, so that sounds good to me. I think I'll also just dig in. Maybe maybe the Gcp metadata thing we can replace with just raw Http calls. I'll I'll see how much code that adds. But
that might solve all the issues. I think.
**Trent Mick** 52:28 Sorry I showed some excitement there, because I wasn't sure if it was fair to drop in a total side issue here, for, like
the the distro that we have at work for hotel stuff, which is just kind of a light wrapper around, and
put some elastic sugar on it for for my company for our users.
we've actually swapped out the Gcp detector right now, because that the the Gcp. Metadata
dependency, at least the current version was using a version of
Node fetch that made it impossible, or at least something about the code path there made it impossible to not have spans to suppress the spans for those rest.
HP calls so that you'd always get
you'd always get those spans in the user service data. And our workaround was just
bypass and make the HP. Rest. Calls ourselves. So if that's a possibility of dropping that, I think that would. I mean, help my use case. But that's just me.
**Daniel Dyla (Dynatrace)** 53:29 So.
**Aaron Abbott** 53:31 Okay, yeah, I'll I'll.
**Trent Mick** 53:32 So anyway, that sounds good to me. Yeah.
**Aaron Abbott** 53:34 Okay. Great.
**Trent Mick** 53:42 Or Gcp. Metadata. I don't know if that's your own thing being updated. If I think it was using Node fetch because it wanted to use fetch, and that was before Fetch was in all the supported versions of Node Core as well. So yeah.
**Aaron Abbott** 53:53 Yeah, it could also be my fault, because because I haven't updated the
middle repo in a while. But
yeah, I'll definitely take a look.
**Trent Mick** 54:01 Okay? And if you need help on the
the SDK, 2 dot O update for the resource changes, you can reach out. I can help with that, but I'm sure you'll be fine.
**Daniel Dyla (Dynatrace)** 54:13 Shouldn't be too crazy.
**Jamie Danielson** 54:18 And I guess one question I have related to
semantic inventions like, I think we haven't updated
semantic conventions yet in this package. I don't know if we want to do it as like. Try to do it as a fast follow. If we're adding in new
semantic conventions now, or just keep it as is. That might be fine.
**Trent Mick** 54:39 Be done together or separately. I think it's fine. Yeah, you're talking about the the Constance name right to moving to.
**Jamie Danielson** 54:45 Yeah.
**Trent Mick** 54:46 Style. Yeah.
**Jamie Danielson** 54:47 Yeah, moving to the newer style definitely. So like this becomes whatever like adder, underscore, faz, underscore name.
But if it's not stable yet than having the simcom file added in separately to pull in.
I don't know. I don't know if.
**Trent Mick** 55:10 I'm fine. Either way. It can be done as part of this, or separately.
**Jamie Danielson** 55:15 Yeah.
**Trent Mick** 55:17 Aaron, were you gonna be following up on this Pr, or do you think you're gonna be creating a separate Pr.
**Aaron Abbott** 55:23 Well, I'll I'll definitely drop like a comment. Or maybe, Dan, if you want to, just to
capture this discussion. But I'll probably open a separate Pr.
**Trent Mick** 55:32 Okay.
**Aaron Abbott** 55:39 Cool.
Thank you. All appreciate it.
**Trent Mick** 55:42 I can.
**Daniel Dyla (Dynatrace)** 55:43 Thank you.
**Jamie Danielson** 56:03 Alright. So I actually am going to have to run for something. I think we were going to look at
maybe ending this a few minutes early today, but we'll be back next week unless anyone.
**Daniel Dyla (Dynatrace)** 56:21 Yep.
**Jamie Danielson** 56:21 Has anything.
**Daniel Dyla (Dynatrace)** 56:22 That's fine!
**Jamie Danielson** 56:23 Throw it in slack. Yeah.
Okay?
**Daniel Dyla (Dynatrace)** 56:28 3 min isn't really enough to do any triage. Anyway, I'll I'll go through the bugs on my own.
**Jamie Danielson** 56:34 Okay.
**Trent Mick** 56:35 Running, a chimney.
**Daniel Dyla (Dynatrace)** 56:37 Thank you.
**Aaron Abbott** 56:38 Thank you. Everyone.
**Jamie Danielson** 56:39 Thanks, all have a good one.
**Trent Mick** 56:40 So, okay.
