SIG: RPC Sem Conv Stability SIG
Date: 2026-01-15
Duration: 43 minutes
Zoom Recording URL: https://zoom.us/rec/share/XlrBwEKNQ11YNomXZMKdM5qk8XzLWXHi8wvOcyXWNF77omoZ1eSI6yk23Nlep2ZH.so0keWWvjBKHChSq
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:07 Hello, I dress…
**Trask Stalnaker** 00:09 Hey!
**Liudmila Molkova** 00:34 Hard to believe that it's already 15 somewhere else.
Let's see what we have on the project board… I moved some things around earlier.
Hi, Steve.
**Steve Rao** 01:02 Yeah, hello?
**Liudmila Molkova** 01:07 Yeah, we're looking at the project board.
So there are a bunch of things in progress, and I think we should talk about, Activity?
What do we have? Interesting.
**Trask Stalnaker** 01:28 Yeah, we can definitely go through, if we have time, to just go through, spend time in this meeting to go through PR reviews.
**Liudmila Molkova** 01:39 Would you rather start with… some the new, and then there's the Rust type, too. Sure. Okay.
I… created this front, and maybe we can… it's an easy one, so I want to bring it up first.
It came up in the spec call today, on Tuesday.
how it's related to RPC, so what I noticed, that… Or HTTP… metrics.
We use, let's say it's required.
We say it's required for database metrics.
Right, yeah.
For RPC metrics, We say it's recommended.
And… I tend to agree with there is no difference.
But I think we should stay consistent.
And say it's required.
**Trask Stalnaker** 02:51 I agree.
I think the idea with, like.
Was the required metrics would be pretty minimal, generally.
Kind of like required attributes, but I think the, the duration metric.
Without that, what's the… point of, like, of saying you support the metrics. You could still support, so you support some cons for tracing, but you don't support it for metrics.
**Liudmila Molkova** 03:24 Right, yeah, cool, so then, or the RPC… So, I'm going to keep this issue on our board.
Until we fix it, and we can create a separate issue, just… yeah.
**Trask Stalnaker** 04:30 Sounds good.
**Liudmila Molkova** 04:32 crate.
So this was easy.
Let's see… what else do we have?
We started talking about… Canceled.
spans less time.
and… I think the… And collusion there.
So I think the question is, do we… Document anything special on top of Just standard thorough recording.
**Trask Stalnaker** 05:41 Can you, can you write in the notes there what we, Cancellation on the client side is… I forgot we looked it up, but it's… An error, or on the server side, it's… yeah, but it's not on the server side.
**Liudmila Molkova** 06:02 It's currently, and… yeah, it's currently an error.
One client… Not an error on server.
And… we… at least for gRPC.
The things like… Timeouts also appear as cancellations, so we cannot say they are never errors, sometimes they are.
**Trask Stalnaker** 06:33 Right?
**Liudmila Molkova** 06:37 so, what do we say today?
It's generic… Use the context you have if you know about dancer.
Apply your best judgment.
By default, it's an error.
**Trask Stalnaker** 06:58 I think it's… Reasonable, aligns with… other SIMCON.
**Liudmila Molkova** 07:13 Yeah, so I guess we can… we can stop there.
It's not perfect, but Jenny, there is no perfect solution here.
**Trask Stalnaker** 07:23 I think the important thing is that it gives… I mean, we still have the wiggle room to… define later, saying that, like, if you… if the cancellation is for X reason, then… You should treat it as a… Non-error.
I mean, I think that's one of those… it would be one of those examples where… Instrumentations would have to take a major version bump to change the telemetry they made.
But I don't think it would be breaking from semantic convention.
Since it's just… since it's a should.
**Liudmila Molkova** 08:20 Yeah.
Okay, so, Dan, it's a good news, there is nothing we need to do.
So let's just make sure our PC… Spence… And we are referring to recording errors.
And… It has… Everything with a chute.
Okay?
Do we want to close this issue, or.
**Trask Stalnaker** 09:24 I think we just want to unhook it from our PC, maybe?
**Liudmila Molkova** 09:30 Yeah.
**Trask Stalnaker** 09:31 Or was this… was kind of about RPC?
**Liudmila Molkova** 09:36 for example.
**Trask Stalnaker** 09:38 Okay, yeah.
I would just unhook it, or… Post-ability, you know, we wanted to keep the connection.
**Liudmila Molkova** 10:00 Okay, let me just capture that.
**Trask Stalnaker** 10:06 Yeah.
**Liudmila Molkova** 11:38 Okay?
PRC, no.
Not PRC.
**Trask Stalnaker** 11:46 Oh yeah, I'm… Have that typo a bunch lately.
**Liudmila Molkova** 11:53 Yeah, okay.
**Matthew Hensley / Grafana Labs** 11:55 And I think even with that one.
It's good to leave it for now, because… Cancelation can come with errors, also.
So, that's something… JRPC has, so it's completely separate from the status.
In a way. Where you can end up with both in some cases.
No two trucks.
**Liudmila Molkova** 12:20 anchor status.
An error and not an error at the same time.
**Matthew Hensley / Grafana Labs** 12:25 Yes.
**Liudmila Molkova** 12:31 Awesome.
Okay.
So, we… There's nothing to do here.
I think we decided we just keep it open.
So we don't lose track of it, until we stabilize.
**Trask Stalnaker** 12:56 Let me double-check what we said… Okay, only gRPC and Dubbo, great.
So, Steve.
We're leaning on you for double.
**Steve Rao** 13:13 Okay.
**Trask Stalnaker** 13:14 Cheers.
anything… That, Do we have the Dubbo?
Page yet?
**Liudmila Molkova** 13:27 We don't.
**Steve Rao** 13:28 Whoa.
We don't.
**Liudmila Molkova** 13:33 Would you be interested in adding it?
Steve?
**Steve Rao** 13:38 Yeah, okay, yeah, maybe I can, yeah, try to do it with the members from the community recently.
**Liudmila Molkova** 13:49 That would be great, and I think when you do this, you will find At least one issue.
That we are not aware of.
It always happens.
**Steve Rao** 14:01 Okay.
**Liudmila Molkova** 14:08 Cool, so if your other people need help, let us know with the tooling and stuff.
Okay… And… In the last one, we… didn't really talk about is… Exception.
Message.
Not trust, I think it's getting better if we're going to deprecate error message.
**Trask Stalnaker** 14:47 Yeah.
**Liudmila Molkova** 14:53 So let's see, how does it affect RPC?
**Trask Stalnaker** 15:02 I mean, I would argue that it doesn't affect RPC any more or less than HTTP and database.
**Liudmila Molkova** 15:13 Agree.
So what do… for… for HTTP, I think we… we're… Status description.
So, I think the difference for HTTP, we… is this guy.
As I copped in, it's in development.
For databases.
Oh, interesting, so…
**Trask Stalnaker** 15:59 Which is in development.
**Liudmila Molkova** 16:01 Which is in development, yeah.
Spence status, okay.
And what do I see here?
Oh, I mean, wait, we're carefully avoiding…
**Trask Stalnaker** 16:26 Yeah.
**Liudmila Molkova** 16:27 this.
But in practice, RPCX, if you get… an RPC exception from server.
you pretty much know that you shouldn't record it, because you have… you don't know if it contains sensitive details. It could.
**Trask Stalnaker** 16:52 On client spans, if you get it back from the server.
**Liudmila Molkova** 16:56 Actually, on both.
Doesn't matter.
**Trask Stalnaker** 16:59 Yeah.
**Liudmila Molkova** 17:04 And I think the reason… It's… somewhat relevant to HTT… oh, sorry, to RPC.
So specifically in the context of gRPC, people are complaining that Error handling often defaults to sending verbose responses for debugging.
**Trask Stalnaker** 17:42 In production, that's for both utilities.
**Liudmila Molkova** 17:46 Secrets.
And .NET gRPC client, or gRPC Server, even has a special flag that opts in into sending the exceptions back to.
Client.
**Trask Stalnaker** 18:21 I'm torn on that, because on the one hand.
You've explicitly enabled some debug… a debugging setting, and you're sending that over the wire, which is also problematic, potentially, to clients.
But… On the other hand, That's… not.
Necessarily the greatest excuse for… Us to still capture it via telemetry.
Without some kind of opt-in on the telemetry.
Capture.
**Liudmila Molkova** 19:01 You didn't make any conclusion.
For this one, did you?
**Trask Stalnaker** 19:11 Other than I'll, like, report it to the library. They shouldn't… I mean, ideally… be putting… Sensitive data and exception messages, because it's just way too common to dump exception messages into log files.
And… The harm of… Turning that off, you know, would be like, Like, that's… Then you get no logs, can't tell what's going on.
**Liudmila Molkova** 19:47 It's like, if somebody, uses record exception or future set exception.
By default, we would record exception message.
And it's not necessarily intentional, a new login framework, anybody using login framework, usually.
Adds exception, yeah.
**Trask Stalnaker** 20:10 Yeah.
**Liudmila Molkova** 20:12 This pretty much sounds like… Okay, maybe in the world where we allow users to customize exception stack traces, we should also let them customize exception messages.
**Trask Stalnaker** 20:25 Yeah, I mean, there's always… I feel like for the… PII, sensitive data, there's always… collector, processors… it's just a matter of, like, at the SEMCOND level.
We're not… we can't guarantee 100%.
Because there's… people will do weird things, and the… harm of some cons saying, don't capture these things at all.
is bad, is worse than… I think, than…
**Liudmila Molkova** 21:12 So, perhaps what we can do, regardless, actually, of our PC, but in general.
We can modify… the YAML for the exception message, and add a note that it might contain sensitive information.
We have no means to know this is super important, but at the same time, some… people… put secrets in this message, or PIA.
**Trask Stalnaker** 21:47 Yeah, I like that. I think that was kind of… in general, the idea of, like, the PII tagging… of… across all SEMCON would be… Would allow people who are super paranoid to still opt in to that and, you know, get very restricted data, but that's… a choice.
**Liudmila Molkova** 22:12 Yeah, we don't have tagging yet. Actually, nothing stops us from implementing it, but we use some poor version We're heart shape.
We just add a warning in the note, and once we're ready to formalize it, it would be relatively easy to find.
on this.
**Steve Rao** 22:43 attributes that can have information, we can add this.
**Trask Stalnaker** 22:47 Yeah.
I like it.
**Liudmila Molkova** 22:52 Cool.
**Trask Stalnaker** 22:56 And I think that makes sense on exception message, and would not shock anybody.
**Liudmila Molkova** 24:10 Cool.
Should we remove… It, from the RPC board, there is nothing RPC-specific. Would we block RPC stability on this one?
**Trask Stalnaker** 24:26 Num.
I don't think we would.
**Liudmila Molkova** 24:29 Yeah.
Okay… So… We've gone through the to-do items. I… I can actually… Let's see… We can talk about the in-progress stuff now.
So I think we… we're just, keep… keeping this PR open, For the time being? Or do you want to merge it, Trask?
**Trask Stalnaker** 25:23 The migration guide.
Let's merge it.
**Liudmila Molkova** 25:32 Bye.
Majestive, can you take a look, please?
**Steve Rao** 25:39 Okay.
**Trask Stalnaker** 25:40 Yeah, we need, approval.
Yeah, no, no rush on that. That's also… I can continue keeping it up to date there.
But would be good to get another review.
**Liudmila Molkova** 25:55 Yeah, this one is still in draft, there are a couple of things I want us to… Finalize. So, this one, I've got the approvals. We're deprecating the server client request response size.
Oh, Christoph, resolved it.
Awesome. So, as just a general SemConf thing.
We just… the deprecated metrics just disappear.
And maybe if we listed them somewhere as deprecated, it would be more useful.
But yeah, I'm going to hit merge here, because we… Ken?
And it leaves us with DAR.
RPC message events.
So, we shared the proposal to just deprecate them.
And the spec call.
Josh supports it.
And he has some ideas on how to make it useful.
We haven't got any pushback.
So, I have sent a PR. Oh, Trasky already approved it.
**Trask Stalnaker** 27:29 Yep.
**Liudmila Molkova** 27:34 Cool.
So, Matt, Steve, if you can take a look, please do.
**Steve Rao** 27:42 Sure.
**Liudmila Molkova** 27:43 Oh, well… You're pretty much done.
So, with this difference, We have the mapping doc here.
And becomes… Relatively small, we talked about it, right? So there is… more or less… Oh, I didn't create an issue for the URL.
Oops.
**Trask Stalnaker** 28:22 Oh, the scheme.
**Liudmila Molkova** 28:24 The ischemia, ischemia.
**Trask Stalnaker** 28:26 Yeah, yeah, yeah.
**Liudmila Molkova** 28:40 It seems like I… got, Okay, I can take care of this one.
But… Yeah, I removed all the… Staff about SPAN events?
And… Contain additional events that could be recorded.
Oh, that should be recorded as is.
I don't know, I… You can take a look, at this PR. I would appreciate feedback, but it's also okay if we… Keep it open for longer and resolve all the dependencies.
**Trask Stalnaker** 30:16 What dependencies? Just the scheme? Or…
**Liudmila Molkova** 30:23 Yeah, the RPC messages.
**Trask Stalnaker** 30:25 Oh, right, right, the things we're deprecating. Yeah, yeah, yeah, yeah, okay.
**Liudmila Molkova** 30:29 Yeah.
And that's it.
Let's stabilize it tomorrow.
**Trask Stalnaker** 30:47 on it.
**Matthew Hensley / Grafana Labs** 30:54 I may take a quick run-through.
Some of the changes that have been merged, and just make sure they Read okay?
Since they've been done piecemeal, as always, you know, we do them in parts, and like to double-check, found that There's always questions, and… About what was meant, so I've been trying to…
**Trask Stalnaker** 31:15 That would be great.
**Matthew Hensley / Grafana Labs** 31:16 Yep.
**Trask Stalnaker** 31:18 Yeah, feel free to just shoot off random, clarification PRs, or wording PRs, or anything.
**Matthew Hensley / Grafana Labs** 31:29 Yeah, I was just waiting till… It's obvious what would need to be checked out, versus, you know, going through a bunch that we end up scrapping.
**Trask Stalnaker** 31:37 Oh, yeah, yeah. Maybe wait for these, yeah, Lydmilla's two PRs to get merged here, that delete a bunch of stuff.
Which, by the way, I'm a big fan of. Like, I think that… At first, I was kind of hesitant on, like, removing stuff that wasn't, you know, like, why, but, I mean… Until we're ready to do something different.
But I… I'm seeing it now more in the… perspective of de- trying to de-scope the semantic convention repo as a whole.
And… So, yeah.
If it doesn't need to be in here in the semantic convention repo, then let's get rid of it.
**Matthew Hensley / Grafana Labs** 32:28 And keeping it… Very simple to start, and we can always add things, but removing them is… Quite painful. And there's always someone who uses that weird niche thing, and it can never go away because of it.
So, yeah.
**Liudmila Molkova** 32:43 Yeah.
Should we drop this part?
I don't know why it's here.
So I think what is…
**Trask Stalnaker** 33:02 Sound bad at all.
**Matthew Hensley / Grafana Labs** 33:07 Say if we kept it, might need to come up with, like, some examples.
Of where you might do this and not.
**Trask Stalnaker** 33:21 Is this about, like, the nesting?
**Liudmila Molkova** 33:28 Yeah… Particular mode service and added none to the caller.
**Trask Stalnaker** 33:42 Or is this about, like, people using RPC SEMCOM To model their own, sort of, bespoke… HTTP calls that they consider RPC versus using an RPC frame… instrumenting an RPC framework.
**Liudmila Molkova** 34:04 And if we don't understand what it's about, then the readers… We'll have an even harder time.
I think what it says is that you can… about nesting, that you can stamp RPC attributes on the HTTP span.
How would you do this?
**Trask Stalnaker** 34:24 Where…
**Liudmila Molkova** 34:26 you can…
**Trask Stalnaker** 34:28 Oh…
**Liudmila Molkova** 34:29 have RPC as a parent, so the nesting first.
**Trask Stalnaker** 34:44 Do we see anything in database about transporting over HTTP?
Spam.
**Liudmila Molkova** 34:50 No.
Don't think so.
**Trask Stalnaker** 34:55 Yeah, I mean, it… I would… I would… I would be good with removing that, and I mean, there is something interesting there in this, like, of documenting, sort of, this… nesting… stuff where database RPC can use HTTP spans…
**Liudmila Molkova** 35:20 I don't even think it… it's a possibility to merge them together.
Because of the streaming and different durations, and… Stuff like this.
Also, it's pretty common for gRPC Even if it runs on top of HTTP to have… like, different… stack.
not you… not rely on the typical HTTP client, right? So you… in practice, you don't get Both.
**Trask Stalnaker** 36:04 Thank you, but I was trying to remember with GRPC if we… Because gRPC uses Netty.
And we instrument… in Java, we instrument Netdy also, but I… Bing… I don't remember if… No, we would have suppressed… we wouldn't have… Yeah, they made the low level.
**Liudmila Molkova** 36:29 Yeah, so if I remember, they are using the… the LEGO pieces from Nerdy.
That are lower than the instrumentation for each.
**Trask Stalnaker** 36:38 Normal codec, Netty, HTTP codecs, yeah.
Makes sense.
**Liudmila Molkova** 36:46 Steve, would it be the case for, Apache, Dabo, that, you would, use HTTP as a transport under And you would see both the gRPC… sorry, the double and HTTP spins.
**Steve Rao** 37:00 Without the HTV spend. Just, just a double, spend.
Yeah, in gRPC, I, I think, yeah, recently, I have a GRPC demo. I… in Java instrumentation, I don't see any HTTP, spent in gRPC spent.
**Liudmila Molkova** 37:22 They also use Netty for the transport level?
**Steve Rao** 37:28 I, I guess it's natty. I'm not very sure about this one.
**Liudmila Molkova** 37:34 Okay, it's okay.
Anyway, I think we should kill it.
**Matthew Hensley / Grafana Labs** 37:47 I agree. Make my life easier if it's not there, honestly. Because I have a sneaking suspicion that WCF when you use HTTP transports, you're gonna end up With nested spans, and it'll… the order will change depending on which direction.
So on the server, you'll probably have one from ASP.NET, And then from WCF and on the client.
We'll have WCF and the HTTP client.
Stuff.
So…
**Liudmila Molkova** 38:15 Do you expect, like, do you know that people use WCF instrumentation? Do they still care?
**Matthew Hensley / Grafana Labs** 38:23 I'm in… Yeah?
Core WCF?
is… seems to have a lot of momentum behind it, way more than I would have guessed, and… is… Been fully embraced.
**Liudmila Molkova** 38:37 Oh, bye.
**Matthew Hensley / Grafana Labs** 38:38 I've definitely helped users with WCF instrumentation.
And, try to figure out how to make it work with other transports.
**Liudmila Molkova** 38:50 Yeah, so maybe, once we do the RC, or close to RC, I can ping the WCF guy who wanted to be part of this group, but didn't come. Maybe he can at least review what we have.
Okay, so let me create an issue for this one so we don't forget.
**Trask Stalnaker** 39:18 I'm deleting it. It's… it's gone. I sent a PR.
**Liudmila Molkova** 39:21 Yay.
Awesome.
Super productive.
The table of content trust.
**Trask Stalnaker** 39:37 Thank you.
**Liudmila Molkova** 39:43 Cool. Dan, do we have anything else? Should we call it?
**Trask Stalnaker** 39:52 Yeah.
RSC next week?
**Liudmila Molkova** 39:58 Let's try.
So it's.
**Matthew Hensley / Grafana Labs** 40:00 Part of that, do we need to… Do some implementations, like start… working on it, or is it fine to stabilize without anything done? Because I know with databases, we made sure to… Have some pretty reasonable implementations, even though some of them have not shipped yet.
**Liudmila Molkova** 40:20 I think we can do RC, right? And then we will need prototypes. I can't help with Python, I think.
And… Greg?
**Trask Stalnaker** 40:28 Gregor is going to… we just chatted today, is going to work on the Java RPC.
**Liudmila Molkova** 40:37 Nice.
**Steve Rao** 40:41 Yeah, okay, yeah, I'll… I also can do something in Java, PC.
You will.
Java instrumentation.
**Liudmila Molkova** 40:50 Yeah, and it would be great if you could, document how it applies to double.
**Steve Rao** 40:56 Okay.
**Trask Stalnaker** 40:58 Yeah, I think that one.
**Liudmila Molkova** 40:59 the conventions.
**Trask Stalnaker** 41:02 And do you know what we mean by that page, Steve?
The middle will show what we have for… yeah, gRPC… so we have a gRPC one here.
But we want a… a double page.
Yeah, S.
**Steve Rao** 41:22 Okay, I have a question about this point. We also leave some comment attribute in RBC spend, or RBC metrics.
Yeah, if we have some extra… Attributes.
From double, yeah, maybe we need a separate, page to document them.
**Liudmila Molkova** 41:49 I think it should be great to have the page anyway.
Just to provide the… details, right? So… Maybe some of these attributes are not really applicable to you, and it would be great to know. Or maybe there are some Additional… Some additional stuff, for example, we are saying that the certain status codes are errors. Maybe for DABO, it's slightly different than for gRPC.
And it's just informative for people to know, okay, this is what I should expect.
You know that DAW is similar to gRPC, but they don't, and they would appreciate you explicitly mentioning what how… what to expect from double?
This beach is mostly…
**Trask Stalnaker** 42:42 So we would list the stability of it also.
**Liudmila Molkova** 42:46 Yeah.
**Steve Rao** 42:48 Okay. Yeah, I will try to, yeah, send a PR, yeah.
**Liudmila Molkova** 42:54 Yeah, what, this page is pretty much auto-generated, so you… deal with YAML files, you can find where this guy is defined in YAML. You can just copy-paste it and, Modify what, what's, like, the links and, and similar stuff.
**Steve Rao** 43:18 Okay.
**Liudmila Molkova** 43:24 Okay.
Cool. Dan, thank you all.
Arsenal.
**Trask Stalnaker** 43:30 See you next week.
**Matthew Hensley / Grafana Labs** 43:32 doing this week.
**Trask Stalnaker** 43:33 Right.
