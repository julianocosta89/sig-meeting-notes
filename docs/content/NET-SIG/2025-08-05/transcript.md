SIG: .NET SIG
Date: 2025-08-05
Duration: 26 minutes
Zoom Recording URL: https://zoom.us/rec/share/-G6_AmHopGwv9nKrV0ddM2i9FXyZuI06Yx651K0mfP_3cIW2aj7R_xBMEFItpGJh.AmboxaP22mQIJTBx
============================================================

## Zoom Recording Transcript

**Alan West** 00:57 There you go!
**Martin Costello** 01:01 Row.
**Julius Koval** 01:07 Hi.
**Alan West** 01:09 Let's see, share my screen in just a second when we get started. I actually have a hard stop at 1130 today. So just a heads up about that.
Also, I was out a fair amount last week, and this is also a short week for me. So I've been a little bit.
am I?
And slow to respond?
But If there is anything that you need my attention on, please let me know, or you know you can always slack me too.
Martin T. Compliant.
**Martin Costello** 02:14 Yes, so this is mostly just I didn't understand like the overarching plan, so I figured I'd bring it up. So I knew so what to do about it. We had a contributor open a issue about the Ef call provider which distills down to it's using a several versions ago semantic convention. And they're basically going, can we update it? And at least for ef core, it makes sense to do that in step with SQL client, because most people using, or a large number of people using Ef. Core, probably also using SQL. Client. So you wouldn't want 2 different versions of the semantic convention for databases in the same app.
But then I don't know what the general policy is for. How do we deal with semantic conversion updates?
Do we orchestrate everything, or we should do. Just do them per Instrumentation Library. Because then, once I know the answer to that.
then we can come up with a plan for actually tackling this issue, and then Peter linked off to the project boards that you'd set up.
**Alan West** 03:28 Yeah.
So one of your questions was, yeah, how do we?
How do we orchestrate this? So historically, it has been done on a library by library basis.
So the SQL client library does currently support this environment variable that beaters has has cited here.
And I'm guessing that the ef core has not yet implemented. That is that right?
**Martin Costello** 04:09 Honest answer. I don't know what I would imagine. Probably not.
**Alan West** 04:14 Okay, I, yeah, we can just take a quick look.
that's yo, that's totally the wrong repository.
Yeah. So ef core, I mean, I suppose what I could just do is probably just find an example of yeah. So you see, a little bit of history here, like when we stabilized the Http conventions, we introduce the variable and then in the release candidate, we removed the environment variable, and then in the stable release.
Only the new conventions are admitted. So that's kind of the the general flow of these things.
Some while back, I basically began following that same pattern with the SQL client library.
And yeah, well, you, you can see that it's it's being used within within the the SQL client library that we've got some tests that are setting it and and basically based off of what they're set to.
It affects the what's admitted.
This is actually in case you don't weren't aware of this. This is actually dictated by the specification.
So when a body of semantic conventions goes stable, there's these are the.
These are what library or instrumentation authors basically, need to follow.
So this is where this environment variable is described. It's got 3 different values, basically to admit the new conventions or the old conventions, or actually duplicate them, which is kind of interesting.
So this same pattern could be applied to ef core
**Martin Costello** 06:52 Right? Okay? Yeah. I think I think I can go off and read up on this properly offline and work out what to do, but it sounds like a high level.
It's per library. There doesn't need to be any giant coordination effort, but it probably makes sense for any changes to ef core to sort of be in step with the SQL. Client, and then release whatever changes are necessary together.
**Alan West** 07:22 Yeah, I think so.
I think one thing that I've mentioned in the past about the ef core is I the releasing that, as stable might be, have a different story around it than releasing SQL. Client is stable and the only reason.
**Martin Costello** 07:43 Yeah.
**Alan West** 07:43 That is, that there are some some database systems whose conventions are not yet deemed stable. And so, since ef core is an Orm framework.
we might have to figure out a little like dance around that.
**Martin Costello** 08:01 Yeah, I wasn't necessarily thinking of making that stable, but I was just thinking, you know, like, on the same calendar day, there's a new release of both.
That means you can configure them to be emitting similar. The same convention set.
**Alan West** 08:19 Yeah, okay, yep, that makes sense to me.
So yeah, if you yeah, if you want to read up on this, if you have any questions. That's that's cool. One question I actually have to you. Since, maybe you've been thinking about this is.
I definitely definitely see the benefit of the Ifcore instrumentation, because, you know, there are a lot of database drivers in the ecosystem that may not yet be instrumented, maybe never will be instrumented. And so the Ef core instrumentation will be basically the means by which people get instrumentation.
The thing you mentioned, though when you're using both of these.
do you think that there's value in having both? Or would it be better, maybe, to provide some sort of like in the Ef core instrumentation.
if you're using the SQL. Client instrumentation. It seems to me that that would be the most valuable. And like, if you were able to basically toggle SQL. Client off.
or something is a thought that I've had about the Ef core instrumentation.
**Martin Costello** 09:45 I haven't thought about that too much. But 1 1 thing I have noticed, because there was actually a bug I fixed in ef call that I found in the test because of it. So ef call makes it more obvious when you're doing higher level things like database migrations which the sequel client by itself doesn't really know what you're doing at a high level.
**Alan West** 10:09 So it might be.
**Martin Costello** 10:11 The. There's some things the Ef call instrumentation does the yeah, you might want to opt out of like query level stuff.
But there's probably higher level things that are of interest, that you you would still want to do both.
**Alan West** 10:29 Are those things?
Do the do? Do the semantic conventions, or what? I guess? What? What telemetry are we emitting about those higher level things do they? Are they described by the semantic inventions, or are they.
**Martin Costello** 10:44 I guess I'm probably thinking more like the trace level.
**Alan West** 10:49 Rather than any specific resource attributes.
**Martin Costello** 10:53 Like you. Can you cause one of the bugs? I found it was like, What is it? What is going on? And it was sort of like, oh, it cause it's the 1st run of the test. It's doing the database migrate up.
and then it's doing the actual business logic queries, because if you're just thinking in terms of like endpoints, and what the codes doing, it doesn't. You don't think necessarily think about that.
But if it's the 1st request, and there's no database. There's all this extra stuff that's happening.
**Alan West** 11:26 Interested is that we're capturing trace data for for that.
**Martin Costello** 11:32 Yeah, so it it might be the case that cause I think I think me and Matt were actually talking about this separately yesterday, because one of the bug fixes I made so that ef call works nicely with SQL. Client is like there's a bit of code somewhere in the event source thingy that's like it looks at the name of like a parent span or something, and then it goes, oh, sequel is being used to. I'll just return here and not do any more, so that things don't get duplicated too much. Obviously, that isn't a sustainable thing to do for every possible dB, provider.
**Alan West** 12:12 Great.
Yeah, I guess it would be cool to be able to do something automatic like that versus like A, you know, a toggle that people would need to manually clipping it.
**Martin Costello** 12:25 Is it? Think about it a bit more? Because, yeah, you could potentially refactor it to have like that toggle capability. But then make it by default, do it for certain providers, and not others.
**Alan West** 12:40 Yeah, true, like, maybe maybe our recommendation would be, hey, we have SQL client instrumentation. You should use that over ef core. But if you really want to use ef core go ahead and toggle it on, but maybe for another provider.
I kind of what you're saying for another provider that might not have instrumentation. Then it's like default on, or something.
**Martin Costello** 13:01 Yeah.
**Alan West** 13:09 yeah, anyways, things to things to keep on thinking about.
But yeah, I think your 1st step is to basically research, this environment variable. And and you can start applying that to the Ef core stuff.
**Martin Costello** 13:26 Thanks. Yeah, I'll I'll look into that tomorrow, and then I'll put a comment on the issue for the original poster to see which is.
basically, we'll update 2 things roughly in sync. If you wanna start moving things along once the toggle flags in, then go for it.
**Alan West** 13:48 Okay, and separately, but related.
I saw that Steve Gordon had pinged me some issue. I think it was like in the in the.net instrumentation repository he was looking to.
I didn't look at the issue super deeply, but it yeah. I think he was looking at like the possibility of introducing bytecode instrumentation to cover Somenet framework gaps that the SQL. Client library hands and as part of that he was asking about the SQL. Client library, and it's and its timeline for stability. I've I want to get back to it. But I've been struggling to to get the bandwidth. He offered to maybe help. I slacked him, and he hasn't responded yet. But anyways, I'm gonna talk to him and see if it's something that he he wants to get involved in. But that same that same offer applies to anyone anyone that's interested in maybe lending a hand for not just ef core that we're talking about here, but also the SQL. Client.
**Martin Costello** 15:15 Sure that makes sense. I I also I I've met Steve, and he's in my time zone. So it might be to easier to do collaboration.
**Alan West** 15:24 Yeah, that'd be cool. Yeah. I offered. I offered to Steve.
to meet, you know, at a sometime that works better, you know I think like 8 am. Pacific is 4 Pm.
Uk, I think right so.
**Martin Costello** 15:41 Usually. Yeah.
**Alan West** 15:44 Anyways, I'd be happy to to to meet with, if, like you and Steve are are interested in maybe collaborate on that. I'd be happy to just have like kind of an ad hoc meeting at some point with with y'all
**Martin Costello** 16:00 Yeah, sure cause I'm happy to not also get involved with the sequel client stuff in bringing the conventions up. Not just the corporate.
**Alan West** 16:12 Cool?
Yeah. Sounds good.
So yeah, did that that answer all your questions on at least that.
**Martin Costello** 16:27 Yes, thank you.
**Alan West** 16:28 Cool, and Matthew.
**Matthew Hensley / Grafana Labs** 16:34 Just looking for a gut check here. So.
except in some Prs for the redis instrumentation.
learned how it actually is working under the hood where it's converting. Redis commands to activities asynchronously. So after the commands are done and everything. So it's losing any sort of context or scope.
And so activity. Dot current is always null because it's doing it on a background thread, and so on and so forth. So, question being, is it acceptable to set the current activity within that scope as the aspnet and Grpc instrumentation have to do, due to similar limitations, or is that something we should be discouraging in instrumentation.
**Alan West** 17:30 Hmm.
I'm definitely somewhat familiar with the with the goofiness of the redis instrumentation.
the.
So your question is, basically, wherever well, what you're saying, this is this, Pr is making a change to activity current. It's setting it to.
**Matthew Hensley / Grafana Labs** 18:03 Well, that's an alternative to this. Pr, so this Pr is adjusting this new filter enrichment stuff to pass in the correct activity to the callback.
But there's also the possibility of just making it work as expected and kind of hiding the fact. It's doing this asynchronous stuff on a background thread and just it'll work how all the other ones do from the end user standpoint.
**Alan West** 18:32 Okay, I see what you're saying.
I've not looked at the code flow of of the redis instrumentation very closely in a long time.
**Matthew Hensley / Grafana Labs** 18:45 The setting. The activity will always be null here. It's because the conversions happening on a background thread, I mean, at least it should be, it's safe. But in general it's do we want. This is something that should be discouraged and only done when necessary, because there's an easy alternative here.
Another parameter to get the right context? Or could we tied all this from end users? It's just kind of a best practice question more than a specific in this one.
This case.
**Alan West** 19:20 Yeah, it's it. It may very well be safe.
I don't.
No no particular reason. No particular reason comes to my mind that it would be like bad practice.
To fuss around with activity current behind the scenes just so long as we're doing it responsibly, and.
you know, don't create any issues.
**Matthew Hensley / Grafana Labs** 19:54 Okay? Oh, yeah, if there's no.
you know, red flags about doing that. Besides, obviously not having unintended consequences, probably head that way. Just went into get an opinion before I suggested that change, and having to unwind it later.
**Alan West** 20:15 I'm curious, Blanche, do you have any particular thoughts on on that? I mean, this is this is just a dance that we need to do sometimes in in instrumentation.
**Mike "Blanch" Blanchard** 20:25 Yeah, it's been a while since I was in there. I sort of understand the issue.
Have we not released Redis Stable.
**Alan West** 20:36 No, and in fact, the Redis Redis conventions are one of those bodies of conventions that are not stable yet, so we we can't until.
**Mike "Blanch" Blanchard** 20:44 That would be okay to break the Api regarding should we set activity current.
What I would do is I would go look at the other instrumentation like an asp net core, does it set current before it calls filter.
**Matthew Hensley / Grafana Labs** 21:05 So my quick research I did is the aspnet fornet framework.
Messes with the current activity because of context execution.
fun that happens, and the Grpc client instrumentation also does this.
I did not dig in enough yet to see why it needs to. I know why the aspnet needs it, but not this one, but by and large it looks like this is not something commonly done, unless don't have another option.
**Alan West** 21:42 Yeah, the redisc instrumentation is definitely strange. I guess it kind of surprises me that Grpc client is doing it. But there's probably a reason.
**Mike "Blanch" Blanchard** 21:49 It's.
**Alan West** 21:50 I haven't looked at that one either.
**Mike "Blanch" Blanchard** 21:52 This is where range, because the goal of filter is to like, drop the thing.
So if you set current before.
I don't know, you have to allocate a new Async local and execution context. So you're gonna pay some cost just to drop the thing.
But the the goal here with activity. Dot current is to find the parent before the activity is created.
**Matthew Hensley / Grafana Labs** 22:28 I need to it. Look in general, I think currently, it's mostly using the parent one for filtering.
So yeah, this more of a philosophical one as I work through it. Just see if there's any opposition to munging current.
**Alan West** 22:55 If it works, munch away.
**Matthew Hensley / Grafana Labs** 23:03 Alright. Well, it sounds like there's.
**Mike "Blanch" Blanchard** 23:04 My only concern would be the perf impact.
**Alan West** 23:07 Yeah.
**Matthew Hensley / Grafana Labs** 23:09 Oh, there's plenty of perfum packs in this Redis driver. It turns out it likes to chew RAM so.
or sorry this instrumentation for the driver.
It has some pseudo memory, lake starting so.
**Alan West** 23:31 Yeah, I mean. And also, I guess side note, just like, Oh, this is just me getting up on my soapbox again, for no no real fantastic reason, but I really don't like filter. I I wish I wish we had never introduced it in our instrumentation.
I guess this is talking about enrich, I guess. Is it also touching filter?
Yeah, filter is, has always struck me as something that would be well served by processors.
Like a span processor enrich, too. But you know, I guess, enrich or in rich, I've I've always been a little bit more okay with, because often you do want that context.
but I don't know honestly what would be on that context that is of interest to to end users in the context of database stuff. It makes sense to me in the context of of web instrumentation I'm not super familiar with why people would be using enrich in a database setting anyways.
yeah, try it out.
**Matthew Hensley / Grafana Labs** 25:16 Okay? Well, I'm sure I can come up with some contrived use cases for like enrich.
There, yeah, it's stuff people have been asking for, and I think filter having some context, can make sense, but it's also it is inconvenient to have this all over the place, for sure.
Okay, I'm gonna take a look at the Grpc instrumentation some more and figure out why it's having to do similar things and expect that'll give me the hints that I need, since it's a more modern one, and like aspnet that this has to be hacked around.
**Alan West** 26:02 Cool. Okay?
Well, thanks. Y'all. Is there anything else on people's minds going once, going twice alright.
Talk to y'all next week.
**Matthew Hensley / Grafana Labs** 26:22 See you.
